from django.db import models


# Create your models here.
class Foto(models.Model):
	fotos =				 models.ImageField(upload_to = 'mias/')
	class Meta:
		verbose_name = ('foto')
		verbose_name_plural = ('fotos')
		def __unicode__(self):
			return self.fotos
