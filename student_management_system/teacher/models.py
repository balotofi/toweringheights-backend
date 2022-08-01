from djongo import models

from student.models import CLASSES


SPECIAL_SUBJECTS = [
    ("IRS", "Islamic Religious Studies"),
    ("Phonics", "Phonics"),
    ("Music", "Music"),
    ("French", "French")
]

class ClassTeacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sex = models.CharField(
        max_length=2,
        choices=[
            ("M", "Male"),
            ("F", "Female")
        ]
    )
    my_class = models.CharField("Class", max_length=5, choices=CLASSES)  #TODO: Add validation to make sure multiple teachers can't exist for the same class.
    has_left =  models.BooleanField(default=False)

    
class SubjectTeacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=10, choices=SPECIAL_SUBJECTS)
    has_left = models.BooleanField(default=False)