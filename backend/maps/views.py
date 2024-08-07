from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Cluster
from .serializers import StudentSerializer, ClusterSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClusterViewSet(viewsets.ModelViewSet):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer

