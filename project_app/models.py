from django.db import models


# Create your models here.

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    ROLE_SELECTIONS = [('Supervisor', 0), ('Instructor', 1), ('TA', 2)]


class CourseModel(models.Model):
    course_id = models.AutoField(primary_key=True)
    dept_code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    assigned_instructor = models.ForeignKey(UserModel, on_delete=models.PROTECT , related_name="instuctor")
    assigned_tas = models.ManyToManyField(UserModel)


class SectionModel(models.Model):
    section_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    grader = models.BooleanField(default=False)
    assigned_ta = models.ForeignKey(UserModel, on_delete=models.PROTECT)

