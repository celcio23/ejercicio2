from django.db import models

class MisDatos(models.Model):
	nombre = models.CharField(max_length=30)
	skills = models.TextField()
	telefono = models.IntegerField()
	email = models.EmailField()
	imagen = models.ImageField(upload_to='img',null = True, blank= True)
	facebook = models.CharField(max_length=30)
	twitter = models.CharField(max_length=30)
	youtube = models.CharField(max_length=30)
