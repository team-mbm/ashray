from rest_framework import serializers
from cases.models import Case, Contact, Location, TypeOfCase, PostalCode


class PostalCodeSerializer(serializers.HyperlinkedModelSerializer):
    """
    will be used in dropdown list on Frontend part to fill city and state in Location part
    """
    post_office = serializers.SerializerMethodField()

    def get_post_office(self, obj):
        return "postoffice:{0}".format(obj.pin_code)

    class Meta:
        model = PostalCode
        # url field is for showing hyperlink of api and nothing else
        fields = ['url', 'pin_code', 'post_office', 'city', 'state']


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class TypeOfCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeOfCase
        fields = '__all__'


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeOfCaseSerializer()
    contact = ContactSerializer()
    location = LocationSerializer()
    """
    type = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='type_of_case-detail'
    )
    contact = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='contact-detail'
    )
    location = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='location-detail'
    )
    """
    class Meta:
        model = Case
        fields = ('id', 'type', 'contact', 'location', 'case_filer_name', 'name_child', 'desc', 'age_of_child')
