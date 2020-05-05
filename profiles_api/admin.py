from django.contrib import admin
from profiles_api import models   #our model

# Register your models here.
admin.site.register(models.UserProfile)
