from gallery.models import GamePic, AdminPic
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


admin.site.register(GamePic)
admin.site.register(AdminPic)
