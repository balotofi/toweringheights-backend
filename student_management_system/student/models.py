from djongo import models


GENERAL_SUBJECTS = [
    ("")
]

CLASSES = [
    ("KG1", "Kindergaten 1"),
    ("KG2", "Kindergaten 2"),
    ("N1", "Nursery 1"),
    ("N2", "Nursery 2"),
    ("P1", "Primary 1"),
    ("P2", "Primary 2"),
    ("P3", "Primary 3"),
    ("P4", "Primary 4"),
    ("P5", "Primary 5"),
]

TERMS = [
    ("1", "First Term"),
    ("2", "Second Term"),
    ("3", "Third Term"),
]



class Class(models.Model):
    pass



class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(max_length=3)
    sex = models.CharField(
        choices=[
            ("M", "Male"),
            ("F", "Female")
        ]
    )
    cur_pos = models.PositiveIntegerField("Position")
    class_ = models.ForeignKey(Class)

    sessions = models.Em

