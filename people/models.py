from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True )
    last_name = models.CharField(max_length=200)
    st_subject = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.last_name + " " + self.first_name

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True )
    last_name = models.CharField(max_length=200)
    grade = models.CharField(max_length=40)

    def __str__(self):
        return self.last_name + " " + self.first_name
