from django.contrib import admin
from project_app.models import User
from project_app.models import Course
from project_app.models import Section

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Section)
