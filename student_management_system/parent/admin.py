from django.contrib import admin

from .models import Parent, Family

admin.site.register([Parent, Family])