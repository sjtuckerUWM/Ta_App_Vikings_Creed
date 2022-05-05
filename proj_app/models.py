from django.db import models


# Create your models here.
class Department(models.TextChoices):
    COMP_SCI = 'COMP SCI'
    BIO_SCI = 'BIO SCI'
    CHEM = 'CHEM'
    MATH = 'MATH'
    PHYSICS = 'PHYSICS'
    IND_ENG = 'IND ENG'
    FILM = 'FILM'


class MyUserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    role = models.IntegerField()


class CourseModel(models.Model):
    course_id = models.AutoField(primary_key=True)
    dept_code = models.CharField(max_length=20, choices=Department.choices)
    name = models.CharField(max_length=20)

    assigned_instructor = models.ForeignKey(MyUserModel, on_delete=models.PROTECT, related_name="instructor", null=True)
    assigned_tas = models.ManyToManyField(MyUserModel)


class SectionModel(models.Model):
    section_id = models.AutoField(primary_key=True)

    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    grader = models.BooleanField(default=False)
    assigned_ta = models.ForeignKey(MyUserModel, on_delete=models.PROTECT)
