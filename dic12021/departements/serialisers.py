from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from departements.models import EtudiantModel

from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class EtudiantSerializer(serializers.ModelSerializer):

    class Meta:
        model = EtudiantModel
        fields = "__all__"


class ViewListEtudiant(generics.ListAPIView):
    queryset = EtudiantModel.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    #two methodes for authentication (using Token or using session)
