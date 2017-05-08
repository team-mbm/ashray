from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from cases.serializers import PostalCodeSerializer, CaseSerializer, TypeOfCaseSerializer, LocationSerializer, ContactSerializer
from cases.models import Case, TypeOfCase, Location, Contact, PostalCode


class PostalCodeViewSet(viewsets.ModelViewSet):
    serializer_class = PostalCodeSerializer
    queryset = PostalCode.objects.all()
    permission_classes = [permissions.AllowAny]


class TypeOfCaseViewSet(viewsets.ModelViewSet):
    serializer_class = TypeOfCaseSerializer
    queryset = TypeOfCase.objects.all()
    permission_classes = [permissions.AllowAny]


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [permissions.AllowAny]


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    permission_classes = [permissions.AllowAny]


class CaseViewset(viewsets.ModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()
    permission_classes = [permissions.AllowAny]
    """
    def get_queryset(self):
        if self.request.user.is_staff:
            return Case.objects.all()
        else:
            return Case.objects.all()
    """
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Case.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
