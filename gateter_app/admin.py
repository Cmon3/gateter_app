from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile, Maullido

# Register or unregister your models here.
admin.site.unregister(Group)
admin.site.register(Profile)
admin.site.register(Maullido)
