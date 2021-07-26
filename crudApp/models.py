from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Crudbase(models.Model):
    name =CharField(max_length=20)
    email =CharField(max_length=30, default="")
    phone = CharField(max_length=10)
    
    def __str__(self):
        return self.name

class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title