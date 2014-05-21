from django.contrib import admin
from .models import Project, Photo


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	pass

admin.site.register(Project, ProjectAdmin)

class PhotosAdmin(admin.ModelAdmin):
	pass

admin.site.register(Photo, PhotosAdmin)
