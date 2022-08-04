from django.db import models


PRIMARY_CLASSES = [
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

TEST_TYPES = [
    ("E", "Exam"),
    ("T1", "Test 1"),
    ("T2", "Test 2")
]



class PrimaryAbstract(models.Model):
    student = models.ForeignKey("student.Student", on_delete=models.PROTECT)

    term = models.CharField(max_length=2, choices=TERMS)
    result_type = models.CharField(max_length=2, choices=TEST_TYPES)

    # Subjects 
    english = models.PositiveIntegerField()
    math = models.PositiveIntegerField()
    agric = models.PositiveIntegerField()
    cca = models.PositiveIntegerField()
    history = models.PositiveIntegerField()
    ss = models.PositiveIntegerField()
    he = models.PositiveIntegerField()
    science = models.PositiveIntegerField()
    computer = models.PositiveIntegerField()
    civic = models.PositiveIntegerField()
    security = models.PositiveIntegerField()
    wr = models.PositiveIntegerField()
    qr = models.PositiveIntegerField()
    phonics = models.PositiveIntegerField()
    writing = models.PositiveIntegerField()
    phe = models.PositiveIntegerField()
    crk = models.PositiveIntegerField()
    yoruba = models.PositiveIntegerField()
    


    class Meta:
        abstract = True


class Primary1(PrimaryAbstract):
    my_class = "Primary 1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Primary 1"
        verbose_name_plural = "Primary 1"
        

class Primary2(PrimaryAbstract):
    my_class = "Primary 2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Primary 2"
        verbose_name_plural = "Primary 2"
        

class Primary3(PrimaryAbstract):
    my_class = "Primary 3"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Primary 3"
        verbose_name_plural = "Primary 3"
        

class Primary4(PrimaryAbstract):
    my_class = "Primary 4"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Primary 4"
        verbose_name_plural = "Primary 4"
        

class Primary5(PrimaryAbstract):
    my_class = "Primary 5"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Primary 5"
        verbose_name_plural = "Primary 5"
        

