from gallery.models import GamePic, AdminPic
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['title']}),
        ('Image',               {'fields': ['image']}),
    ]
    list_display = ('title', 'added_date', 'image')
    list_filter = ['added_date']
    
admin.site.register(GamePic, GalleryAdmin)
admin.site.register(AdminPic, GalleryAdmin)

