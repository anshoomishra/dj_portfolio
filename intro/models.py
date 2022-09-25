from django.db import models
from .utils import upload_to
from django.db.models.signals import pre_save
# Create your models here.

class AboutMe(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField()
    extra_circular_activities = models.TextField()
    
    
    def __str__(self):
        return self.title + " about "

class Introduction(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    short_intro = models.TextField()
    image = models.ImageField(upload_to=upload_to)
    
    def __str__(self):
        return self.name + " intro"
    
# TODO I am clearing complete table before saving another intro instance since It is intro related stuff so I can have only one intro


def clear_intro_table(sender,instance,*args,**kwargs):
    print(instance)
    data_to_be_deleted = instance.__class__.objects.all()
    for item in data_to_be_deleted:
        item.delete()
    
    
pre_save.connect(clear_intro_table,sender=Introduction)