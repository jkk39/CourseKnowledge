from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# this is gonna translate exactly to our database.

class School(models.Model):
	schoolID = models.IntegerField(primary_key = True)
	schoolname = models.CharField(max_length=50)
	address = models.CharField(max_length=50)

	def get_absolute_url(self):
		return reverse('theapp:index')

	# defines what string printout of this table should look like
	def __str__(self):
		return str(self.schoolID).decode("utf-8") + ' - ' + self.schoolname + ' - ' + self.address
		# needed to cast schoolID to unicode since it is an integer.

class Student(models.Model):
	studentID = models.IntegerField(primary_key = True)
	# set school_id when setting the school key
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	GPA = models.FloatField()
	name = models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('theapp:index')

	def __str__(self):
		return str(self.studentID).decode("utf-8")+ ' - ' + self.name + ' - '  + str(self.school_id).decode("utf-8") + ' - ' + str(self.GPA).decode("utf-8")

class Professor(models.Model):
	profID = models.IntegerField(primary_key = True)
	profname = models.CharField(max_length=50)
	dept = models.CharField(max_length=50)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('theapp:index')

	def __str__(self):
		return str(self.profID).decode("utf-8") + ' - ' + self.profname + ' - ' + self.dept + ' - '+ str(self.school_id).decode("utf-8") 


class Course(models.Model):
	courseID = models.IntegerField(primary_key = True)
	prof = models.ForeignKey(Professor, on_delete=models.CASCADE)
	coursename = models.CharField(max_length=50)
	credits = models.IntegerField()

	def get_absolute_url(self):
		return reverse('theapp:index')

	def __str__(self):
		return str(self.courseID).decode("utf-8") + ' - ' + self.coursename + ' - ' + str(self.credits).decode("utf-8") + ' - ' + str(self.prof_id).decode("utf-8")

class EnrollsIn(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	date = models.DateField()
	grade = models.FloatField()

	def get_absolute_url(self):
		return reverse('theapp:index')

	def __str__(self):
		return str(self.student_id).decode("utf-8") + ' - ' + str(self.course_id).decode("utf-8") + ' - ' + str(self.date).decode("utf-8") + ' - ' + str(self.grade).decode("utf-8")

class Friendship(models.Model):
    friend1ID = models.IntegerField()
    friend2ID = models.IntegerField()

    def get_absolute_url(self):
		return reverse('theapp:index')

    def str(self):
        return str(self.friend1ID).decode("utf-8") + ' - ' + str(self.friend2ID).decode("utf-8")