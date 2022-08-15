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


class KG1(models.Model):
    student = models.ForeignKey("student.Student", on_delete=models.PROTECT)

    term = models.CharField(max_length=2, choices=TERMS)
    result_type = models.CharField(max_length=2, choices=TEST_TYPES)

    #subjects
    english = models.FloatField("English Language")
    math = models.FloatField("Mathematics")
    art = models.FloatField("Creative Art")
    social_studies = models.FloatField("Social Studies")
    health_education = models.FloatField("Health Education")
    science = models.FloatField("Science")
    writing = models.FloatField("Handwriting")
    music_rhymes = models.FloatField("Music/Rhymes")

    class Meta:
        verbose_name = "Kindergartan 1"
        verbose_name_plural = "Kindergartan 1"

class KG2(models.Model):
    student = models.ForeignKey("student.Student", on_delete=models.PROTECT)

    term = models.CharField(max_length=2, choices=TERMS)
    result_type = models.CharField(max_length=2, choices=TEST_TYPES)
    #subjects
    english = models.FloatField("English Language")
    math = models.FloatField("Mathematics")
    art = models.FloatField("Creative Art")
    social_studies = models.FloatField("Social Studies")
    health_education = models.FloatField("Health Education")
    science = models.FloatField("Science")
    writing = models.FloatField("Handwriting")
    music_rhymes = models.FloatField("Music/Rhymes")
    phonics = models.FloatField("Phonics")
    computer = models.FloatField("Computer Studies")
    crk = models.FloatField("Religious Education")

    class Meta:
        verbose_name = "Kindergartan 2"
        verbose_name_plural = "Kindergartan 2"



class NUR1(models.Model):
    student = models.ForeignKey("student.Student", on_delete=models.PROTECT)

    term = models.CharField(max_length=2, choices=TERMS)
    result_type = models.CharField(max_length=2, choices=TEST_TYPES)

    #subjects

    english = models.FloatField("English Language")
    math = models.FloatField("Mathematics")
    art = models.FloatField("Creative Art")
    social_studies = models.FloatField("Social Studies")
    health_education = models.FloatField("Health Education")
    science = models.FloatField("Science")
    writing = models.FloatField("Handwriting")
    music_rhymes = models.FloatField("Music/Rhymes")
    phonics = models.FloatField("Phonics")
    computer = models.FloatField("Computer Studies")
    crk = models.FloatField("Religious Education")
    qr = models.FloatField("Quantitative Reasoning")
    vr = models.FloatField("Verbal Reasoning")

    class Meta:
        verbose_name = "Nursery 1"
        verbose_name_plural = "Nursery 1"



class NUR2(models.Model):
    student = models.ForeignKey("student.Student", on_delete=models.PROTECT)

    term = models.CharField(max_length=2, choices=TERMS)
    result_type = models.CharField(max_length=2, choices=TEST_TYPES)

    #subjects
    english = models.FloatField("English Language")
    math = models.FloatField("Mathematics")
    art = models.FloatField("Creative Art")
    social_studies = models.FloatField("Social Studies")
    p_health_education = models.FloatField("P.H.E")
    civic = models.FloatField("Civic Education")
    sec_edu = models.FloatField("Security Education")
    science = models.FloatField("Science")
    writing = models.FloatField("Handwriting")
    phonics = models.FloatField("Phonics")
    computer = models.FloatField("Computer Studies")
    crk = models.FloatField("C.R.K")
    qr = models.FloatField("Quantitative Reasoning")
    vr = models.FloatField("Verbal Reasoning")

    class Meta:
        verbose_name = "Nursery 2"
        verbose_name_plural = "Nursery 2"



class PrimaryAbstract(models.Model):
    student = models.ForeignKey("student.Student", on_delete=models.PROTECT)

    term = models.CharField(max_length=2, choices=TERMS)
    result_type = models.CharField(max_length=2, choices=TEST_TYPES)

    # Subjects 

    english = models.FloatField("English Language")
    math = models.FloatField("Mathematics")
    art = models.FloatField("Creative Art")
    social_studies = models.FloatField("Social Studies")
    p_health_education = models.FloatField("P.H.E")
    civic = models.FloatField("Civic Education")
    sec_edu = models.FloatField("Security Education")
    science = models.FloatField("Science")
    writing = models.FloatField("Handwriting")
    phonics = models.FloatField("Phonics")
    computer = models.FloatField("Computer Studies")
    crk = models.FloatField("C.R.K")
    qr = models.FloatField("Quantitative Reasoning")
    vr = models.FloatField("Verbal Reasoning")
    agric = models.FloatField("Agriculture")
    history = models.FloatField("History")
    yoruba = models.FloatField("Yoruba")
    


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
        

