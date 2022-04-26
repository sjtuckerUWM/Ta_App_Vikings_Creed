from django.contrib import admin
from project_app.models import UserModel
from project_app.models import CourseModel
from project_app.models import SectionModel


# Register your models here.
admin.site.register(UserModel)
admin.site.register(CourseModel)
admin.site.register(SectionModel)
