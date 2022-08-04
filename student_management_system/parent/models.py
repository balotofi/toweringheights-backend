from django.db import models


class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    sex = models.CharField(
        max_length=1,
        choices=[
            ("M", "Male"),
            ("F", "Female")
        ]
    )



class Family(models.Model):
    father = models.ForeignKey(Parent, on_delete=models.PROTECT, related_name="fathers")
    mother = models.ForeignKey(Parent, on_delete=models.PROTECT, related_name="mothers")
    wards = models.ManyToManyField("student.Student")

    class Meta:
        verbose_name_plural = "Families"

