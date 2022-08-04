from django.contrib import admin

from .models import Primary1, Primary2, Primary3, Primary4, Primary5

admin.site.register([
    Primary1,
    Primary2, 
    Primary3, 
    Primary4, 
    Primary5
])