from django.db import models
from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from .models import Token, Athlete, AuthCode, Activity, Map
import json
import requests

def map_dict(model, dict):
    for k, v in dict.items():
        if hasattr(model, k):
            setattr(model, k, v)

def completeAuth(instance, ):
    auth_url = "https://www.strava.com/oauth/token"

    payload = {
        'client_id': "",
        'client_secret':'',
        'code': instance,
        'grant_type': 'authorization_code',
    }
    try:
        token = requests.post(auth_url, data=payload, verify=False)
        print(token.content)
    except:
        print("Error Connecting to Strava AuthO")
        print(token.content)

    if 'access_token' not in token.json():

        return {'error': 'invalid code sent to strava'}
    access_token = token.json()['access_token']
    refresh_token = token.json()['refresh_token']
    athlete = token.json()['athlete']
    expires_at = token.json()['expires_at']
    expires_in = token.json()['expires_in']
    token_type = token.json()['token_type']


    new_token = Token()
    new_token.access_token = access_token
    new_token.refresh_token = refresh_token
    new_token.expires_at = int(expires_at)
    new_token.expires_in = int(expires_in)
    new_token.token_type = token_type
    new_token.save()

    athlete_id = athlete['id']

    athlete_exist = Athlete.objects.filter(id=athlete_id)

    athlete = ''
    if not athlete_exist:
        new_athlete = Athlete()

        new_athlete.id = athlete_id
        new_token.save()
        new_athlete.refresh_token = new_token

        new_athlete.save()
        athlete = new_athlete
    else:
        athlete_exist[0].refresh_token = new_token
        athlete_exist[0].save()
        athlete = athlete_exist[0]


    activities_url = "https://www.strava.com/api/v3/athlete/activities"

    header = {'Authorization': 'Bearer ' + new_token.access_token}
    param = {'per_page': 200, 'page': 1}
    activities = requests.get(activities_url, headers=header, params=param).json()
    for activity in activities:
        activity_exist = Activity.objects.filter(id=activity['id'])
        date = datetime.datetime.strptime(activity['start_date'],  "%Y-%m-%dT%H:%M:%SZ")

        if not activity_exist and date.year == 2022:
            print(date.year)

            new_activity = Activity()
            map_dict(new_activity, activity)

            new_activity.athlete_id = athlete
            activity_map = activity['map']
            map = Map()
            map_dict(map, activity_map)
            map.save()

            new_activity.map = map
            new_activity.save()
    return {'athlete_id': athlete_id}
