from rest_framework import serializers
from .models import Projects, WorkExperiences

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperiences
        fields = '__all__'