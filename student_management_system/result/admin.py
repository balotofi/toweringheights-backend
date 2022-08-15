from django.contrib import admin

from .models import KG1, Primary1, Primary2, Primary3, Primary4, Primary5, \
    KG1, KG2, NUR1, NUR2

admin.site.register([
    Primary1,
    Primary2, 
    Primary3, 
    Primary4, 
    Primary5,
    KG1,
    KG2,
    NUR1,
    NUR2
])