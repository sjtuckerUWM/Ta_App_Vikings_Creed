from django.db import models


# Model for Department name
class Department(models.TextChoices):
    COMP_SCI = 'COMP SCI'
    BIO_SCI = 'BIO SCI'
    CHEM = 'CHEM'
    MATH = 'MATH'
    PHYSICS = 'PHYSICS'
    IND_ENG = 'IND ENG'
    FILM = 'FILM'

# Model for users
class MyUserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    role = models.IntegerField()

# Model for course
class CourseModel(models.Model):
    course_id = models.AutoField(primary_key=True)
    dept_code = models.CharField(max_length=20, choices=Department.choices)
    name = models.CharField(max_length=50)

    assigned_instructor = models.ForeignKey(MyUserModel, on_delete=models.SET_NULL, related_name="instructor", null=True)
    assigned_tas = models.ManyToManyField(MyUserModel, related_name="tas")

# Model for Section
class SectionModel(models.Model):
    section_id = models.AutoField(primary_key=True)

    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    grader = models.BooleanField(default=False)
    assigned_ta = models.ForeignKey(MyUserModel, null=True, on_delete=models.SET_NULL)
