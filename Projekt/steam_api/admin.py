from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Gamer, Game, Review


# Register your models here.
class GamerInLine(admin.StackedInline):
    model = Gamer
    can_delete = False
    verbose_name_plural = 'Gamers'


class UserAdmin(BaseUserAdmin):
    inlines = (GamerInLine,)


class GameAdmin(admin.ModelAdmin):
    list_display = ["game_name", "gid"]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "gid", "username"]
    list_filter = ["username"]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Review, ReviewAdmin)
