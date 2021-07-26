from django.contrib import admin
from django.db.models.fields import Field
from crudApp.models import Crudbase, FilesAdmin
# Register your models here.
admin.site.register(Crudbase)
admin.site.register(FilesAdmin)