from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "username"]
    list_filter = ["name", "username"]


admin.site.register(User, UserAdmin)
