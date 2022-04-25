from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=9)
    ROLE_SELECTIONS = [('Supervisor', 0), ('Instructor', 1), ('TA', 2)]


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    dept_code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    assigned_instructor = models.ForeignKey(User.user_id, on_delete=models.PROTECT)
    assigned_tas = models.ManyToManyField(User.user_id)


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course.course_id, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    grader = models.BooleanField(default=False)
    assigned_ta = models.ForeignKey(User.user_id, on_delete=models.PROTECT)

