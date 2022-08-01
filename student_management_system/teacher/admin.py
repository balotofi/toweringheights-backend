from django.contrib import admin


from .models import ClassTeacher, SubjectTeacher

admin.site.register([ClassTeacher, SubjectTeacher])