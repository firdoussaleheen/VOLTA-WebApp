from django.db import models

### Help Module classes: VocabDomain and Rulebase

# The following classes are needed for the VocabDomain
class VocabDomain(models.Model):
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name

class VocabTopic(models.Model):
    topic = models.CharField(max_length=128)
    domain = models.ForeignKey(VocabDomain)
    def_useful = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.topic
    
class Node(models.Model):
    topic = models.ForeignKey(VocabTopic)
    word = models.CharField(max_length=128)
    definition = models.CharField(max_length=256)
    views = models.IntegerField(default=0)
    date_added = models.DateTimeField('date added')
    
    def __unicode__(self):
        return self.word
    
class Synonym(models.Model):
    word = models.CharField(max_length=128)
    node = models.ForeignKey(Node)
    
    def __unicode__(self):
        return self.word

# The following classes are for the Rulebase
class Rulebase(models.Model):
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
  
class AnswerTopic(models.Model):
    rulebase = models.ForeignKey(Rulebase)
    TYPE_CHOICES = (
        ('Safety', 'Safety'),
        ('Equipment', 'Equipment'),
        ('VLA', 'VLA'),
        ('Simulation', 'Simulation'),
        ('Hardware', 'Hardware'),
        ('Theory', 'Theory'),
        ('General', 'General'),
    )
    topic = models.CharField(choices=TYPE_CHOICES, max_length=10)
    
    def __unicode__(self):
        return self.topic
  
class AnswerWithQuestion(models.Model):
    rulebase = models.ForeignKey(Rulebase)
    topic = models.ManyToManyField(AnswerTopic)
    question = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    date_added = models.DateTimeField('date added')
    
    def __unicode__(self):
        return self.question
    
class AnswerElement(models.Model):
    answer_with_question = models.ForeignKey(AnswerWithQuestion)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='static/', blank=True)
    equation_input = models.CharField(max_length=128, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('table', 'table'),
        ('video', 'video'),
        ('caption', 'caption'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.answer_with_question.question
    
class AnswerKeyword(models.Model):
    answer_with_question = models.ForeignKey(AnswerWithQuestion)
    node = models.ForeignKey(Node)
    
    def __unicode__(self):
        return self.node.word


    