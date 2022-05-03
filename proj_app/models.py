from django.db import models


# Create your models here.

class MyUserModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    role = models.IntegerField()


class CourseModel(models.Model):

    dept_code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    assigned_instructor = models.ForeignKey(MyUserModel, on_delete=models.PROTECT , related_name="instructor")
    assigned_tas = models.ManyToManyField(MyUserModel)

    course_id = models.AutoField(primary_key=True)
    dept_code = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=20)

    assigned_instructor = models.ForeignKey(MyUserModel, on_delete=models.PROTECT, related_name="instructor", null=True)
    assigned_tas = models.ManyToManyField(MyUserModel, null=True)

class SectionModel(models.Model):

    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    grader = models.BooleanField(default=False)
    assigned_ta = models.ForeignKey(MyUserModel, on_delete=models.PROTECT)
