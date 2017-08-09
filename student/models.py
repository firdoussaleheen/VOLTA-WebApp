from django.db import models
from django.contrib.auth.models import User

from VLA.models import Course, Laboratory

def get_file_path(instance, filename):
    if not instance.id:
        instance.save()
    lab_name = instance.lab.name.replace(' ', '_')
    return 'users/%s/%s/simulation.png' % (instance.user.username, lab_name)

def get_file_path_processed(instance,filename):
    if not instance.id:
        instance.save()
    lab_name = instance.lab.name.replace(' ', '_')
    return 'users/%s/%s/labeled.png' % (instance.user.username, lab_name)

def get_text_file_processed(instance,filename):
    if not instance.id:
        instance.save()
    lab_name = instance.lab.name.replace(' ', '_')
    return 'users/%s/%s/VLAnetlist.cir' % (instance.user.username, lab_name)

def get_speech_path(instance,filename):
    if not instance.id:
        instance.save()
    return 'users/%s/speech.txt' % (instance.user.username)


### User Classes
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    first_name = models.CharField(max_length=64, help_text="Please enter your first name.", blank=False)
    last_name = models.CharField(max_length=64, help_text="Please enter your last name.", blank=False)
    TUid =  models.PositiveIntegerField(help_text="Please enter your TUid.", blank=False)
    allow_recording = models.BooleanField(default=False)
    allow_recording_answered = models.BooleanField(default=False)
    speech_file = models.FileField(upload_to=get_speech_path,blank=True)
    
    def __unicode__(self):
        return self.user.username
    
# Class for giving students access to a Course
class CoursePermission(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    course_finished = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.course.name
    
# Class for storing completion status and test scores for
# each Laboratory and User
class LabProgress(models.Model):
    user = models.ForeignKey(User)
    lab = models.ForeignKey(Laboratory)
    theory_finished = models.BooleanField(default=False)
    theory_test_finished = models.BooleanField(default=False)
    simulation_finished = models.BooleanField(default=False)
    sim_test_finished = models.BooleanField(default=False)
    hardware_finished = models.BooleanField(default=False)
    results_finished = models.BooleanField(default=False)
    lab_test_finished = models.BooleanField(default=False)
    lab_finished = models.BooleanField(default=False)
    
    theory_views = models.IntegerField(default=0)
    theory_test_views = models.IntegerField(default=0)
    simulation_views = models.IntegerField(default=0)
    sim_test_views = models.IntegerField(default=0)
    hardware_views = models.IntegerField(default=0)
    results_views = models.IntegerField(default=0)
    lab_test_views = models.IntegerField(default=0)
    
    theory_test_score = models.FloatField(blank=True, null=True)
    lab_test_score = models.FloatField(blank=True, null=True)

    netlist = models.TextField(blank=True)
    sim_image = models.FileField(upload_to=get_file_path, blank=True)
    processed_sim_image = models.FileField(upload_to=get_file_path_processed, blank=True)
    standard_netlist = models.TextField(blank=True)#(upload_to=get_text_file_processed,blank=True)
    comparator_output = models.TextField(blank=True)

    def __unicode__(self):
        return self.lab.name

class SimulationQuestionResponse(models.Model):
    labprogress = models.ForeignKey(LabProgress)
    question_number = models.IntegerField(blank=True, null=True)
    student_response = models.IntegerField(blank=True, null=True)







