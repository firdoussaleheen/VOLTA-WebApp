from django.db import models
from tutor.models import AnswerWithQuestion

class Course(models.Model):
    # course info
    name = models.CharField(max_length=128, unique=True)
    crn = models.IntegerField(default=0, blank=True)
    subj = models.CharField(max_length=10)
    course_number = models.IntegerField(default=0)
    section_number = models.IntegerField(default=0, blank=True)
    start_date = models.DateField('Course Start Date', blank=True, null=True)
    end_date = models.DateField('Course End Date', blank=True, null=True)
    lecture_time = models.TimeField('Lecture Time', blank=True, null=True)
    lecture_days = models.CharField(max_length=50, blank=True)
    lecture_location = models.CharField(max_length=50, blank=True)
    lab_time = models.TimeField('Lab Time', blank=True, null=True)
    lab_days = models.CharField(max_length=50, blank=True)
    lab_location = models.CharField(max_length=50, blank=True)
    course_description = models.TextField(max_length=500, blank=True)
    course_overview = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    
    # instructor info
    instructor_name = models.CharField(max_length=50, blank=True)
    instructor_email = models.EmailField(blank=True)
    instructor_office_hours = models.TimeField(blank=True, null=True)
    instructor_office_days = models.CharField(max_length=50, blank=True)
    instructor_office_location = models.CharField(max_length=50, blank=True)
    instructor_phone = models.CharField(max_length=50, blank=True)
    
    # TA info
    TA_name = models.CharField(max_length=50, blank=True)
    TA_email = models.EmailField(blank=True)
    TA_office_hours = models.TimeField(blank=True, null=True)
    TA_office_days = models.CharField(max_length=50, blank=True)
    TA_office_location = models.CharField(max_length=50, blank=True)
    TA_phone = models.CharField(max_length=128, blank=True)
    
    def __unicode__(self):
        return self.name
    
class Prereq(models.Model):
    name = models.CharField(max_length=128, unique=True)
    course = models.ForeignKey(Course)
    topic = models.ManyToManyField(AnswerWithQuestion)
    
    def __unicode__(self):
        return self.name

class Laboratory(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=128, unique=True)
    start_date = models.DateTimeField('Date Assigned', blank=True, null=True)
    due_date = models.DateTimeField('Date Due', blank=True, null=True)
    lab_number = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
    
class LabObjective(models.Model):
    lab = models.ForeignKey(Laboratory)
    objective = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.objective
    
class LabEquipment(models.Model):
    lab = models.ForeignKey(Laboratory)
    equipment = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.equipment


# The following classes are needed for each Laboratory

class Theory(models.Model):
    lab = models.OneToOneField(Laboratory)
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name

class TheoryElement(models.Model):
    theory = models.ForeignKey(Theory)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='VLA/static/VLA/images/', blank=True)
    equation_input = models.CharField(max_length=128, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('video', 'video'),
        ('table', 'table'),
        ('caption', 'caption'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.name
    
class TheoryTest(models.Model):
    lab = models.OneToOneField(Laboratory)
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
    
class TheoryTestElement(models.Model):
    theorytest = models.ForeignKey(TheoryTest)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='VLA/static/VLA/images/', blank=True)
    equation_input = models.CharField(max_length=128, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('video', 'video'),
        ('table', 'table'),
        ('caption', 'caption'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.name
    
class TheoryTestQuestion(models.Model):
    theorytest = models.ForeignKey(TheoryTest)
    question = models.CharField(max_length=128)
    answer_one = models.CharField(max_length=128)
    answer_two = models.CharField(max_length=128)
    answer_three = models.CharField(max_length=128, blank=True)
    answer_four = models.CharField(max_length=128, blank=True)
    correct_answer_number = models.IntegerField(blank=True)
    correct_response = models.CharField(max_length=128, blank=True)
    incorrect_response = models.CharField(max_length=128, blank=True)
    is_answered = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.question
    
class Simulation(models.Model):
    lab = models.OneToOneField(Laboratory)
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name

class SimulationElement(models.Model):
    simulation = models.ForeignKey(Simulation)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='static/', blank=True)
    equation_input = models.CharField(max_length=128, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('video', 'video'),
        ('table', 'table'),
        ('caption', 'caption'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.name
    
class SimulationTest(models.Model):
    lab = models.OneToOneField(Laboratory)
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name

class SimulationTestElement(models.Model):
    simulationtest = models.ForeignKey(SimulationTest)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='VLA/static/VLA/images/', blank=True)
    equation_input = models.CharField(max_length=128, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('video', 'video'),
        ('table', 'table'),
        ('caption', 'caption'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.name

class SimulationTestQuestion(models.Model):
    simulationtest = models.ForeignKey(SimulationTest)
    question = models.CharField(max_length=128)
    answer_one = models.CharField(max_length=128)
    answer_two = models.CharField(max_length=128)
    answer_three = models.CharField(max_length=128, blank=True)
    answer_four = models.CharField(max_length=128, blank=True)
    correct_answer_number = models.IntegerField(blank=True)
    correct_response = models.CharField(max_length=128, blank=True)
    incorrect_response = models.CharField(max_length=128, blank=True)
    is_answered = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.question
    
class Hardware(models.Model):
    lab = models.OneToOneField(Laboratory)
    name = models.CharField(max_length=128, unique=True)
    
    def __unicode__(self):
        return self.name
    
class HardwareElement(models.Model):
    hardware = models.ForeignKey(Hardware)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='static/', blank=True)
    equation_input = models.CharField(max_length=128, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('video', 'video'),
        ('table', 'table'),
        ('caption', 'caption'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.name

class Results(models.Model):
    lab = models.OneToOneField(Laboratory)
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
    
class ResultsQuestions(models.Model):
    results = models.ForeignKey(Results)
    question = models.CharField(max_length=128)
    answer_text = models.TextField(blank=True)
    is_answered = models.BooleanField(default=False)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('table', 'table'),
    )
    answer_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.name
    
class LabTest(models.Model):
    lab = models.OneToOneField(Laboratory)
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name

class LabTestElement(models.Model):
    labtest = models.ForeignKey(LabTest)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='VLA/static/VLA/images/', blank=True)
    equation_input = models.CharField(max_length=128, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('video', 'video'),
        ('table', 'table'),
        ('caption', 'caption'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.name

class LabTestQuestion(models.Model):
    labtest = models.ForeignKey(LabTest)
    question = models.CharField(max_length=128)
    answer_one = models.CharField(max_length=128)
    answer_two = models.CharField(max_length=128)
    answer_three = models.CharField(max_length=128, blank=True)
    answer_four = models.CharField(max_length=128, blank=True)
    correct_answer_number = models.IntegerField(blank=True)
    correct_response = models.CharField(max_length=128, blank=True)
    incorrect_response = models.CharField(max_length=128, blank=True)
    is_answered = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.question
    
