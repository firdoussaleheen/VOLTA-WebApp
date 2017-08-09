from __future__ import absolute_import
from django.contrib import admin
from tutor.models import *
from VLA.models import *
from student.models import *

class SynonymInline(admin.StackedInline):
    model = Synonym
    extra = 3

class NodeAdmin(admin.ModelAdmin):
    inlines = [SynonymInline]
    list_display = ('word', 'topic', 'views')
    list_filter = ['topic']

class SynonymAdmin(admin.ModelAdmin):
    list_display = ('word', 'node')
    list_filter = ['node']

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('objective', 'lab')
    list_filter = ['lab']
    
class ObjectiveInline(admin.StackedInline):
    model = LabObjective
    extra = 3
    
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'lab')
    list_filter = ['lab']
 
class EquipmentInline(admin.StackedInline):
    model = LabEquipment
    extra = 3

class LabAdmin(admin.ModelAdmin):
    inlines = [ObjectiveInline, EquipmentInline]

class TheoryElementInline(admin.StackedInline):
    model = TheoryElement
    extra = 3

class TheoryAdmin(admin.ModelAdmin):
    inlines = [TheoryElementInline]
    
class TheoryElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'theory')
    list_filter = ['theory']
    
class TheoryTestElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'theorytest')
    list_filter = ['theorytest']
    
class SimulationElementInline(admin.StackedInline):
    model = SimulationElement
    extra = 3

class SimulationAdmin(admin.ModelAdmin):
    inlines = [SimulationElementInline]
    
class SimulationElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'simulation')
    list_filter = ['simulation']
    
class SimulationTestElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'simulationtest')
    list_filter = ['simulationtest']
    
class HardwareElementInline(admin.StackedInline):
    model = HardwareElement
    extra = 4

class HardwareAdmin(admin.ModelAdmin):
    inlines = [HardwareElementInline]

class HardwareElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'hardware')
    list_filter = ['hardware']

class TheoryTestQuestionInline(admin.StackedInline):
    model = TheoryTestQuestion
    extra = 4

class TheoryTestAdmin(admin.ModelAdmin):
    inlines = [TheoryTestQuestionInline]
    
class TheoryTestQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'theorytest', 'correct_answer_number')
    list_filter = ['theorytest']
    
class SimulationQuestionInline(admin.StackedInline):
    model = SimulationTestQuestion
    extra = 4

class SimulationTestAdmin(admin.ModelAdmin):
    inlines = [SimulationQuestionInline]
    
class SimulationTestQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'simulationtest', 'correct_answer_number')
    list_filter = ['simulationtest']
    
class LabQuestionInline(admin.StackedInline):
    model = LabTestQuestion
    extra = 4

class LabTestAdmin(admin.ModelAdmin):
    inlines = [LabQuestionInline]
    list_display = ('lab', 'name')
    list_filter = ['lab']
    
class LabTestElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'labtest')
    list_filter = ['labtest']
    
class LabTestQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'labtest', 'correct_answer_number')
    list_filter = ['labtest']
    
class AnswerKeywordInline(admin.StackedInline):
    model = AnswerKeyword
    extra = 5

class AnswerWithQuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerKeywordInline]
    
class LabProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lab')
    list_filter = ['user', 'lab']
    
class CoursePermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    list_filter = ['user', 'course']
    
class SimulationQuestionResponseAdmin(admin.ModelAdmin):
    list_display = ('labprogress', 'question_number')
    list_filter = ['labprogress']
    
admin.site.register(Course)
admin.site.register(Prereq)
admin.site.register(Laboratory, LabAdmin)
admin.site.register(LabObjective, ObjectiveAdmin)
admin.site.register(LabEquipment, EquipmentAdmin)
admin.site.register(TheoryElement, TheoryElementAdmin)
admin.site.register(Theory, TheoryAdmin)
admin.site.register(TheoryTest, TheoryTestAdmin)
admin.site.register(TheoryTestElement, TheoryTestElementAdmin)
admin.site.register(TheoryTestQuestion, TheoryTestQuestionAdmin)
admin.site.register(SimulationTestQuestion, SimulationTestQuestionAdmin)
admin.site.register(Simulation, SimulationAdmin)
admin.site.register(SimulationElement, SimulationElementAdmin)
admin.site.register(SimulationTest, SimulationTestAdmin)
admin.site.register(SimulationTestElement, SimulationTestElementAdmin)
admin.site.register(Hardware, HardwareAdmin)
admin.site.register(HardwareElement, HardwareElementAdmin)
admin.site.register(Results)
admin.site.register(ResultsQuestions)
admin.site.register(LabTestQuestion, LabTestQuestionAdmin)
admin.site.register(LabTest, LabTestAdmin)
admin.site.register(LabTestElement, LabTestElementAdmin)

admin.site.register(VocabDomain)
admin.site.register(VocabTopic)
admin.site.register(Node,NodeAdmin)
admin.site.register(Synonym, SynonymAdmin)

admin.site.register(Rulebase)
admin.site.register(AnswerWithQuestion, AnswerWithQuestionAdmin)
admin.site.register(AnswerElement)
admin.site.register(AnswerKeyword)
admin.site.register(AnswerTopic)

admin.site.register(UserProfile)
admin.site.register(CoursePermission, CoursePermissionAdmin)
admin.site.register(LabProgress, LabProgressAdmin)
admin.site.register(SimulationQuestionResponse, SimulationQuestionResponseAdmin)
