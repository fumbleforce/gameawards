from runs.models import Run, Developer, Game, Upload
from django.contrib import admin

admin.site.register(Game)
admin.site.register(Run)
admin.site.register(Developer)




class RunsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['title']}),
        ('Content',               {'fields': ['version', 'game', 'uploaded_file']}),
    ]
    list_display = ('title','version', 'game', 'uploaded_file')
    
admin.site.register(Upload, RunsAdmin)
