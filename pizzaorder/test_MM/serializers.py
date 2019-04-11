from rest_framework import serializers
from pizzaorder.test_MM.models import  Person, PersonCase,Case
class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('name',)


class PersonCasetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonCase
        fields = ('person', 'case', 'role')

    def create(self, validated_data):
        case_data =  self.validated_data.pop('case')
        person = Person.objects.create(**validated_data)


class CaseSerializer(serializers.ModelSerializer):

    personcase = PersonSerializer(many=True, read_only=True)
    case_to_person = PersonSerializer(many=True)

    class Meta:
        model = Case
        fields = ('summary', 'litigants', 'case_to_person')