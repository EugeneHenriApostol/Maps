from django.db import models

#Student Model with necessary information
class Student(models.Model):
    year_level = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    age = models.IntegerField()
    strand = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255)
    previous_school = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10)
    demographic_data = models.JSONField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

#Clustering Model for Student Clusters    
class Cluster(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    student_ids = models.JSONField()

    def __str__(self):
        return self.name


