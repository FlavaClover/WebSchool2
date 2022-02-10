from django.contrib import admin
from school.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False


class UserStudentAdmin(BaseUserAdmin):
    inlines = (StudentInline,)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'surname', 'name', 'patronymic', 'age')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.unregister(User)
admin.site.register(Student, StudentAdmin)
admin.site.register(User, UserStudentAdmin)
