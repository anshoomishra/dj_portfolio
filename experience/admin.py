from django.contrib import admin
from .models import Company,Project,Responsibility
# Register your models here.

admin.site.register(Company)
admin.site.register(Responsibility)
admin.site.register(Project)