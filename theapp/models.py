from __future__ import unicode_literals

from django.db import models

# this is gonna translate exactly to our database.

class School(models.Model):
	schoolID = models.IntegerField(primary_key = True)
	schoolname = models.CharField(max_length=50)
	address = models.CharField(max_length=50)

class Student(models.Model):
	studentID = models.IntegerField(primary_key = True)
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	GPA = models.FloatField()
	name = models.CharField(max_length=100)

class Professor(models.Model):
	profID = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=50)
	dept = models.CharField(max_length=50)

class Course(models.Model):
	courseID = models.IntegerField(primary_key = True)
	prof = models.ForeignKey(Professor, on_delete=models.CASCADE)
	coursename = models.CharField(max_length=50)
	credits = models.IntegerField()

class EnrollsIn(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	date = models.DateField()
	grade = models.FloatField()

# Will need to add frienship class later on for advanced functions