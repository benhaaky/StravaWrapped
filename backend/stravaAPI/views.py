from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .new_user import *
from .serializers import AthleteSerializer, AuthCodeSerializer, TokenSerializer, MapSerializer, ActivitySerializer
from .models import Token, Athlete, AuthCode, Activity, Map


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all().order_by('id')
    serializer_class = AthleteSerializer

class AuthCodeViewSet(viewsets.ModelViewSet):
    serializer_class = AuthCodeSerializer

    def get_queryset(self):
        return AuthCode.objects.all().order_by('code')

    def create(self, request, *args, **kwargs):
        print(request)
        new_code = AuthCode()

        new_code.code = request.data['code']
        new_code.save()
        serializer = AuthCodeSerializer(new_code)
        response = completeAuth(new_code.code)

        return Response(response)


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all().order_by('refresh_token')
    serializer_class = TokenSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        if self.request.query_params.get('athlete_id'):
            athlete_id = self.request.query_params.get('athlete_id')
            results = Activity.objects.filter(athlete_id=athlete_id)

            return results
        else:
            Activity.objects.all().order_by('id')

    # def get_activity(self, request, *args, **kwargs):
    #     print(request.data)
    #     print("args: ", args)
    #     print("kwargs: ", kwargs)
    #     Activity.objects.filter(athlete_id=request.data)
    #     return Response(route)


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all().order_by('id')
    serializer_class = MapSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all().order_by('refresh_token')
    serializer_class = TokenSerializer
