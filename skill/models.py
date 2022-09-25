from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return "skill " + self.name
class SkillSet(models.Model):
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    skill_title = models.CharField(max_length=100)
    proficiency = models.FloatField()
    relevant_experience = models.IntegerField()
    image = models.ImageField(upload_to="media/",null=True,blank=True)
    def __str__(self):
        return self.skill_title
    