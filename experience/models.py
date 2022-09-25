from django.db import models
from skill.models import Skill
from django.db.models.signals import post_save, pre_save


# Create your models here.


class CompanyQueryset(models.QuerySet):
    def featured(self):
        return self.filter(featured=True)
    
    def all_projects(self):
        return self.project_set.all()


class CampanyModelManager(models.Manager):
    def get_queryset(self):
        return CompanyQueryset(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset()




class Company(models.Model):
    name = models.CharField(max_length=100)
    duration_spent = models.CharField(max_length=20, null=True, blank=True)
    joining_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    # responsibility = models.ForeignKey(Responsibility, on_delete=models.CASCADE, related_name="responsibilities",blank=True,null=True)
    
    class Meta:
        ordering = ['-joining_date']
    
    @property
    def duration(self):
        return self.duration_spent
    
    def __str__(self):
        return self.name

class Responsibility(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="responsibilities",blank=True,null=True)
    def __str__(self):
        return self.title
class ProjectQuerySet(models.QuerySet):
    def active(self):
        return


class ProjectManager(models.Manager):
    
    def get_queryset(self):
        return ProjectQuerySet(self.models, using=self._db)
    
    def all(self):
        return self.get


class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    technologies = models.ManyToManyField(Skill, related_name="skills", null=True, blank=True)
    
    class Meta:
        verbose_name = 'Project'
    
    def __str__(self):
        return self.name


def company_duration_update_receiver(instance, sender, *args, **kwargs):
    if not instance:
        return
    if not instance.joining_date:
        raise ValueError("joining date must be there")
    if instance.end_date:
        instance.duration_spent = (instance.end_date - instance.joining_date) // 365
    else:
        instance.duration_spent = "currently working"


pre_save.connect(company_duration_update_receiver, sender=Company)
