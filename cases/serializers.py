from rest_framework import serializers
from cases.models import  Case, Contact, Location, TypeOfCase

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
class TypeOfCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfCase
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    type = TypeOfCaseSerializer()
    location = LocationSerializer()
    contact = ContactSerializer()
    class Meta:
        model = Case
        fields = ('type', 'location', 'contact', 'case_filer_name', 'desc', 'name_child', 'age_of_child')
