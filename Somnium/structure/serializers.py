from rest_framework import serializers
from .models import *

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class CollegialBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegialBody
        fields = '__all__'

class AdministrativeBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeBody
        fields = '__all__'
 
class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = '__all__'   

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['userPhoto', 'fullname', 'position', 'director',  'stavka', 'email',]

class DirectorSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    
    class Meta:
        model = Director
        fields = '__all__'
       
class PositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Position
        fields = '__all__'
        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['person', 'date_start', 'date_finish', 'description', 'id']
    
