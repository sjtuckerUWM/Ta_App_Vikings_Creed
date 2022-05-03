from django.contrib import admin
from proj_app.models import SectionModel, CourseModel, MyUserModel
# Register your models here.

admin.site.register(MyUserModel)
admin.site.register(SectionModel)
admin.site.register(CourseModel)