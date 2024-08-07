from rest_framework import serializers
from .models import Student, Cluster

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = '__all__'