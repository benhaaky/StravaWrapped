from rest_framework import serializers

from .models import Token, Athlete, AuthCode, Activity, Map

class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = ('id', 'refresh_token')

class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'polyline', 'resource_state', 'summary_polyline')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    map = MapSerializer()
    class Meta:
        model = Activity
        fields = ('id', 'type', 'name', 'map', 'moving_time', 'elapsed_time', 'athlete_id', 'distance', 'total_elevation_gain', 'kudos_count', 'max_speed', 'average_speed', 'start_date')



class AuthCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthCode
        fields = ('code',)

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('token_type', 'expires_at', 'expires_in', 'refresh_token', 'access_token')
