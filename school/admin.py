from django.contrib import admin
from school.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False


class UserStudentAdmin(BaseUserAdmin):
    inlines = (StudentInline,)

admin.site.unregister(User)
admin.site.register(User, UserStudentAdmin)
