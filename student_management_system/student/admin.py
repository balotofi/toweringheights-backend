from django.contrib import admin


from .models import Student, Class

admin.site.register([Student, Class])