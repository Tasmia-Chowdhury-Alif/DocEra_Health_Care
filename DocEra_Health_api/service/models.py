from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length= 20)
    description = CKEditor5Field(config_name='default')
    image = models.ImageField(upload_to= "service/images/")