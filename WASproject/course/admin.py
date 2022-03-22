from django.contrib import admin
from .models import Courses


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'startDate')


admin.site.register(Courses, CoursesAdmin)
