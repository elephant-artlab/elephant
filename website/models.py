import os

from django.db import models
from django.db.models.signals import pre_delete



class Project(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	description = models.TextField(blank=True, null=True)
	url = models.URLField(blank=True, null=True)
	image = models.ImageField(upload_to="uploads/", blank=True, null=True)
	image_name = models.CharField(max_length=16, null=True, blank=True)
	image_description = models.CharField(max_length=19, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	#Displays objects "name" in the admin instead of "Project object"
	def __unicode__(self):
		return unicode(self.name)

def clean_photos(sender, instance, **kwargs):
	if instance.image:
		if os.path.isfile(instance.image.path):
			os.remove(instance.image.path)

	photos = Photo.objects.filter(project__id=instance.id)
	for photo in photos:
		if os.path.isfile(photo.image.path):
			os.remove(photo.image.path)
		

pre_delete.connect(clean_photos, sender=Project)


class Photo(models.Model):
	project = models.ForeignKey(Project)
	image = models.ImageField(upload_to="uploads/", blank=True, null=True)

	#Displays objects "image" in the admin instead of "Photo object"
	def __unicode__(self):
		display_name = str(self.project) + " - " + str(self.image)
		return unicode(display_name)