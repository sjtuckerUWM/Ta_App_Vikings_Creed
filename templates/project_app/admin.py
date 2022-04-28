from django.contrib import admin
from templates.project_app.models import UserModel
from templates.project_app.models import CourseModel
from templates.project_app.models import SectionModel


# Register your models here.
admin.site.register(UserModel)
admin.site.register(CourseModel)
admin.site.register(SectionModel)
