from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models


class Album(models.Model):
	artists = models.CharField(max_length=100)
	album_title = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=500)
	
	def __unicode__(self):
		return smart_unicode(self.artists + '-' + self.album_title)




class Songs(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=150)
	is_favorite = models.BooleanField(default=False)



	def __unicode__(self): 
		return smart_unicode(self.song_title)

