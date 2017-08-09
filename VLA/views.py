# Necessary Imports
from __future__ import absolute_import, division
import re
# Circuit Recognizer Imports
import cv, cv2, sys, math, numpy as np 
sys.path.insert(0, '../')
import circuit_recognizer as CR
# Comparator imports
sys.path.insert(0,'./fix_multisim')
import multisim_translation as trans
from subprocess import call
# Hardware_help Imports
sys.path.insert(0,'./circuit_tracer2')
import vla_3 as HardwareHelp
sys.path.insert(0,'./comparator')
import comparator as cc

# Django-related imports 
import os
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from .models import *
from .forms import UserSimulationImage
from student.models import UserProfile, CoursePermission, LabProgress, SimulationQuestionResponse
from tutor.models import Node, AnswerWithQuestion, AnswerElement


def error404(request):
    return render(request,'VLA/404.html')

def speech_recorder(request):
    return render(request,'VLA/speech_recorder.html')

# Method for speech recognizer data saving
def cgi_script(request):
	if request.method == 'POST':
            searchterm = request.POST['searchbox']
            if not os.path.exists('./VLA/media/users/'+request.user.username+'/'):
                os.makedirs('./VLA/media/users/'+request.user.username+'/')
            f=open('./VLA/media/users/'+request.user.username+'/speech.txt', 'a')
            f.write(searchterm + "\n")
            f.close()
        
	return render(request,'VLA/speech_recorder.html')

def test(request):
    context_dict = {'test' : 0 } 
    context_dict['image_form'] = UserSimulationImage()
    if request.method == 'POST':
        print "POST FOUND" 
        form = UserSimulationImage(request.POST, request.FILES)
        # check if form is valid and image has been selected and is of type PNG

        if 'multisim-upload' in request.POST and form.is_valid(): 
            data = request.FILES['image']
            # Check for valid data
            if str(request.FILES['image']).endswith('.txt') or str(request.FILES['image']).endswith('.cir'):
                net_str = ''
                for line in data.read():
                    net_str += line
                # Call netlist translator on data
                out_str = trans.main(net_str)
		print out_str
                # Save data
                context_dict['out_str'] = out_str
                if 'error1' in out_str:
                  context_dict['error1'] = True

    return render(request, 'VLA/test.html', context_dict)

def hardware_help(request, course_name_url, lab_name_url, hardware_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get course name, lab name, and simulation name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course

        except Course.DoesNotExist:
            pass

        # Get lab, lab sections,
        try:
            labs = get_lab_list(course, user)
            context_dict['labs'] = labs
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab

            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            
            
            #Construct OS path for circuit images
            answers_path = os.getcwd() + '/VLA/static/VLA/courses/' + str(course_name_url) + '/Lab' + str(labs.index(lab)+1).zfill(2) + '/'
           
            #Construct webserver path for circuit images            
            web_answers_path = '/static/VLA/courses/' + str(course_name_url) + '/Lab' + str(labs.index(lab)+1).zfill(2) + '/'

            
            #Create list of tuples with (image name, full image path+"~"+full netlist path)
            answers_circuits = []
            answers_circuits_pic_and_help = []           
            for pic in os.listdir(answers_path):
                if pic.endswith(".png"):
                    answers_circuits.append(pic)
            
            for pic in answers_circuits:
                pic_path = web_answers_path+pic
                help_list = HardwareHelp.translateNetlist(os.getcwd() + '/VLA' + pic_path.replace(".png","_trace.cir"))
                answers_circuits_pic_and_help.append(pic_path+"~"+help_list)
            
            circuit_pics_and_locations = zip(
                         [item for item in answers_circuits],
                         [item for item in answers_circuits_pic_and_help])

            #Create context dict item for that list of tuples
            context_dict["answerkey_circuits"] = circuit_pics_and_locations
            context_dict["default_picture"] = circuit_pics_and_locations[0][1].split("~")[0]
            context_dict["default_help_list"] = circuit_pics_and_locations[0][1].split("~")[1]

        # get help list in context_dict
        except Laboratory.DoesNotExist:
            pass                         
       ## Check for completed netlist from circuit recognizer, return directions on for circuit tracer
       #  **This part has been removed. Instead of checking the student's circuit, hardware help
       #  now just gives help for all circuits in the answers directory
       #
	   #try:
       #        path= context_dict['student_progress'].standard_netlist.path
	   #except Laboratory.DoesNotExist:
	   #    pass
	   #try:
       #        context_dict['student_progress'].hardwarehelp= HardwareHelp.translateNetlist(fname=path)
	   #except Laboratory.DoesNotExist:
	   #    pass

        # Update number of views if link was clicked
        if request.method == 'GET':
            context_dict['student_progress'].simulation_views = context_dict['student_progress'].simulation_views + 1
            context_dict['student_progress'].save()

    return render(request, 'VLA/hardware_help.html', context_dict)

def index(request):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Display course list in sidebar
        cour_list = get_course_list(user)
        context_dict = {'cour_list': cour_list}
	
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        profile = UserProfile.objects.get(user=user)
        context_dict['allow_recordings'] = profile.allow_recording_answered

        # If request is a POST, try to pull out relevant information
        # Set is_completed to True
        if request.method == 'POST':
	    # TEMPORARY SOLUTION SO I DON'T HAVE TO KEEP GOING TO ADMIN PANEL
	    return render(request, 'VLA/speech_recorder.html', context_dict)
            profile.allow_recording_answered = True
            if 'yes' in request.POST:
                profile.allow_recording = True
            profile.save()

            context_dict['allow_recordings'] = True
	    return render(request,'VLA/speech_recorder.html', context_dict)
        return render(request, 'VLA/index.html', context_dict)

# View used to display About information on VLA
def about(request):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        context_dict = {'logged_in': False}
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Display course list in sidebar
        cour_list = get_course_list(user)
        context_dict = {'cour_list': cour_list}

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        context_dict['logged_in'] = True
    return render(request, 'VLA/about.html', context_dict)

# View used to present Course with all course, instructor, TA info
def course(request, course_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get course name and set course url
        course_name = course_name_url.replace('_', ' ')
        context_dict = {'course_name': course_name, 'course_name_url': course_name_url}

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get all course information for selected course
        try:
            course = Course.objects.get(name=course_name)
            context_dict['course'] = course

        except Course.DoesNotExist:
            pass

        # Get prereq information for selected course
        try:
            prereq = Prereq.objects.get(course = course)
            context_dict['prereq_name_url'] = prereq.name.replace(' ','_')
            context_dict['prereq'] = prereq
        except Prereq.DoesNotExist:
            pass

        # Display all course related labs in the sidebar
        try:
            context_dict['labs'] = get_lab_list(course, user)
        except Laboratory.DoesNotExist:
            pass

        return render(request, 'VLA/course.html', context_dict)


# View used to present Prereqs for a given course
def prereq(request, course_name_url, prereq_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get course name and prereq name and set course url
        course_name = course_name_url.replace('_', ' ')
        prereq_name = prereq_name_url.replace('_', ' ')
        context_dict = {'course_name': course_name, 'course_name_url': course_name_url,
                        'prereq_name': prereq_name, 'prereq_name_url': prereq_name_url}

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get all course information for selected course
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get all prereq information for selected course
        # prereq info consists of AnswerWithQuestion object with associated AnswerElement
        try:
            prereq = Prereq.objects.get(course = course)
            context_dict['prereq'] = prereq
            prereq_topics = prereq.topic.all()
            for topic in prereq_topics:
                topic.answer = AnswerElement.objects.filter(answer_with_question=topic)
            context_dict['prereq_topics']= prereq_topics

        except Prereq.DoesNotExist:
            pass

        # Display all course related labs in the sidebar
        try:
            context_dict['labs'] = get_lab_list(course, user)
        except Laboratory.DoesNotExist:
            pass

        return render(request, 'VLA/prereq.html', context_dict)


# View used to present Laboratory and Objectives for a given Course
def lab(request, course_name_url, lab_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get lab and course name
        lab_name = lab_name_url.replace('_', ' ')
        course_name = course_name_url.replace('_', ' ')

        # Set searched flags to false and get complete question and definition lists
        context_dict = {'lab_name': lab_name}
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get selected course
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get selected lab and extract objectives
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict['objectives'] = LabObjective.objects.filter(lab=lab)
            context_dict['equipment'] = LabEquipment.objects.filter(lab=lab)
            labs = get_lab_list(course, user)
            context_dict['labs'] = labs
#	    print 'this is lab number '+ str(labs.index(lab))
#	    if int(labs.index(lab))<7:
#		context_dict['student_progress'].lab_number = True
#		print 'true'
#	    else:
#	        context_dict['student_progress'].lab_number = False
#		print 'Flase'
            # Display lab sections in sidebar
            context_dict = get_sections(context_dict, lab)

        except Laboratory.DoesNotExist:
            pass

        return render(request, 'VLA/lab.html', context_dict)


# Lab section views: theory, theorytest, simulation, hardward, etc.

# View used for presenting Theory section of a given Laboratory/Course
# Information is presented in the form of text, images, equations, videos, or tables
def theory(request, course_name_url, lab_name_url, theory_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get course name and lab name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get Course and set course URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get Laboratory, lab sections, and theory elements
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            context_dict['theory_elements'] = TheoryElement.objects.filter(theory=context_dict['theory'])

            # Update number of views if link was clicked
            if request.method == 'GET':
                context_dict['student_progress'].theory_views = context_dict['student_progress'].theory_views + 1
                context_dict['student_progress'].save()
        except Laboratory.DoesNotExist:
            pass

        # If request is a POST, try to pull out relevant information
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['student_progress'].theory_finished = True
            context_dict['student_progress'].save()
        return render(request, 'VLA/theory.html', context_dict)

# View used for giving test on theory
# Questions are multiple choice, with at least two choices needed
def theorytest(request, course_name_url, lab_name_url, theorytest_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get course name and lab name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}

        # Set to true before test is taken, in order to surpress error message
        # If all questions are not answered will be set to false
        context_dict['questions_filled'] = True

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get course and construct course URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get lab, lab sections, and theory test questions
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            theorytest_questions = TheoryTestQuestion.objects.filter(theorytest=context_dict['theorytest'])
            context_dict['theorytest_questions'] = theorytest_questions
            context_dict['theorytest_elements'] = TheoryTestElement.objects.filter(theorytest=context_dict['theorytest'])

            # Update number of views if link was clicked
            if request.method == 'GET':
                context_dict['student_progress'].theory_test_views = context_dict['student_progress'].theory_test_views + 1
                context_dict['student_progress'].save()
        except Laboratory.DoesNotExist:
            pass

        # If request is a POST, try to pull out relevant information.
        # Checks to see if each question is answered
        # if not return questions_filled=False and send to theorytest.html
        # Assigns each answer to question.given_answer
        if request.method == 'POST':
            num_of_questions = 0
            num_of_correct = 0
            for question in theorytest_questions:
                num_of_questions = num_of_questions + 1
                name = 'choice' + str(num_of_questions)
                if name in request.POST:
                    question.given_answer = int(request.POST[name])
                    question.is_answered = True
                    question.save()
                else:
                    context_dict['questions_filled'] = False
                    context_dict['test_complete'] = False
                    return render(request, 'VLA/theorytest.html', context_dict)
                if question.given_answer == question.correct_answer_number:
                    num_of_correct = num_of_correct + 1

            # Calculate test score
            context_dict['student_progress'].theory_test_score = num_of_correct/num_of_questions*100

            # Set just_finished and is_completed to True and save
            context_dict['just_finished'] = True
            context_dict['theorytest_questions'] = theorytest_questions
            context_dict['student_progress'].theory_test_finished = True
            context_dict['student_progress'].save()
        else:
            context_dict['just_finished'] = False

        return render(request, 'VLA/theorytest.html', context_dict)

# View for displaying directions for circuit simulation
# Information is presented in the form of text, images, equations, videos, or tables
# Simulation results will be recorded in the form of an image uploaded by the User
def simulation(request, course_name_url, lab_name_url, simulation_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get course name, lab name, and simulation name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass



      # Get lab, lab sections,
        try:
            labs = get_lab_list(course, user)
            context_dict['labs'] = labs
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            context_dict['simulation_elements'] = SimulationElement.objects.filter(simulation=context_dict['simulation'])   
	##   For lab1 to lab7, CC shows. Lab 8 to lab 11, CC is hidden.       
	    if int(labs.index(lab))<7:
		context_dict['student_progress'].lab_number = True
	    else:
	        context_dict['student_progress'].lab_number = False
            # Update number of views if link was clicked
            if request.method == 'GET':
                context_dict['student_progress'].simulation_views = context_dict['student_progress'].simulation_views + 1
                context_dict['student_progress'].save()
        except Laboratory.DoesNotExist:
            pass

        # Send form to view
        context_dict['image_form'] = UserSimulationImage()

        # Error message is used to tell user they haven't selected an image to upload
        context_dict['error_message'] = False

        ## If request is a POST, try to pull out relevant information.
        ## Set is_completed to True
        if request.method == 'POST':
            # IDEA: SAVE AS DATA.READ IN DB OR AS INMEM IMG INSTEAD OF A LOCATION. THEN PERFORM OPERATIONS ON THE DATA
            # GENIUS
            context_dict['student_progress'].simulation_finished = True
            context_dict['student_progress'].save()
            print "POST FOUND" 
            form = UserSimulationImage(request.POST, request.FILES)
            # check if form is valid and image has been selected and is of type PNG
            if 'multisim-upload' in request.POST and form.is_valid(): 
                data = request.FILES['image']
                # Check for valid data
                if str(request.FILES['image']).endswith('.txt') or str(request.FILES['image']).endswith('.cir'):
                    net_str = ''
	    
                    for line in data.read():
                        net_str += line
                    out_str=trans.main(net_str)
		    try:
		        context_dict['labs'] = get_lab_list(course, user)
		    except Laboratory.DoesNotExist:
		         pass
# labs solution numbers#
		    number_solution=[3,1,1,2,1,1,2]
    		    answers_path = os.getcwd() + '/VLA/static/VLA/courses/' + str(course_name_url) + '/Lab' + str(labs.index(lab)+1).zfill(2) + '/'
		    for i in range (number_solution[int(labs.index(lab))]):			
				    f=open(answers_path+"netlist_"+str(i)+".cir",'r')
				    ans_str=f.read()
				    ans_str=trans.main(ans_str)				    
				    result=cc.main(out_str,ans_str)
				    if result== 'equal':
		                       break


		    context_dict['student_progress'].save()
                    # Save data
                    context_dict['student_progress'].standard_netlist = net_str
                    context_dict['student_progress'].volta_netlist = out_str
                    context_dict['student_progress'].ans_netlist = ans_str
                    context_dict['student_progress'].lab_number = labs.index(lab)+1
                    context_dict['student_progress'].simulation_finished = True
                    context_dict['student_progress'].save()

		    context_dict['student_progress'].result= result
		    context_dict['student_progress'].save()	

                else:
                    context_dict['error_message'] = True
                    context_dict['student_progress'].save()
                    return render(request, 'VLA/simulation.html', context_dict)
                   
            elif form.is_valid() and request.FILES['image']:
                data = request.FILES['image']
                context_dict['student_progress'].sim_image= request.FILES['image']                
                # Run image processing on uploaded images and return processed image
                path = default_storage.save('tmp/sim_img.png', ContentFile(data.read()))
                tmp_file = os.path.join(settings.MEDIA_ROOT, path)                
                path_to_processed_img = "users/" + username + "/" + lab_name.replace(' ', '_') + "/" + "nodes.png"
                path_to_netlist = "users/" + username + "/" + lab_name.replace(' ', '_') + "/" + "VLAnetlist.cir"
                context_dict['student_progress'].netlist = CR.circuit_recognizer((tmp_file), "/media/" + path_to_processed_img)
                context_dict['student_progress'].simulation_finished = True
                context_dict['student_progress'].processed_sim_image = path_to_processed_img
                context_dict['student_progress'].standard_netlist = path_to_netlist
                context_dict['student_progress'].save()
                path = default_storage.delete('tmp/sim_img.png')
            else:
                pass
                # User did not select an image
                #context_dict['error_message'] = True
        return render(request, 'VLA/simulation.html', context_dict)

# View used for giving test on simulation
# Questions are multiple choice, with at least two choices needed
def simulationtest(request, course_name_url, lab_name_url, simulationtest_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get lab name, course name, an simulation test name
        lab_name = lab_name_url.replace('_', ' ')
        course_name = course_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}

        # Set to true before test is taken, in order to surpress error message
        # If all questions are not answered will be set to false
        context_dict['questions_filled'] = True

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get lab, lab sections, and simulation test questions
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            simulationtest_questions = SimulationTestQuestion.objects.filter(simulationtest=context_dict['simulationtest'])
            num_of_questions = 0
            for question in simulationtest_questions:
                num_of_questions = num_of_questions + 1
                question.given_answer = SimulationQuestionResponse.objects.filter(labprogress=context_dict['student_progress']).get(question_number=num_of_questions)
            context_dict['simulationtest_questions'] = simulationtest_questions
            context_dict['simulationtest_elements'] = SimulationTestElement.objects.filter(simulationtest=context_dict['simulationtest'])

            # Update number of views if link was clicked
            if request.method == 'GET':
                context_dict['student_progress'].sim_test_views = context_dict['student_progress'].sim_test_views + 1
                context_dict['student_progress'].save()
        except Laboratory.DoesNotExist:
            pass

        # If request is a POST, try to pull out relevant information.
        # Checks to see if each question is answered
        # if not return questions_filled=False and send to theorytest.html
        # Assigns each answer to question.given_answer
        if request.method == 'POST':
            num_of_questions = 0
            num_of_correct = 0
            for question in simulationtest_questions:
                num_of_questions = num_of_questions + 1
                name = 'choice' + str(num_of_questions)
                if name in request.POST:
                    question.given_answer = SimulationQuestionResponse.objects.filter(labprogress=context_dict['student_progress']).get(question_number=num_of_questions)
                    question.given_answer.student_response = int(request.POST[name])
                    question.given_answer.save()
                    question.is_answered = True
                    question.save()
                    if question.given_answer.student_response == question.correct_answer_number:
                        num_of_correct = num_of_correct + 1
                else:
                    question.given_answer = SimulationQuestionResponse.objects.filter(labprogress=context_dict['student_progress']).get(question_number=num_of_questions)
                    if question.given_answer.student_response:
                        question.given_answer.save()
                        question.is_answered = True
                        question.save()
                        if question.given_answer.student_response == question.correct_answer_number:
                            num_of_correct = num_of_correct + 1
                    else:
                        question.is_answered = False
                        question.save()
                        context_dict['questions_filled'] = False
                    #context_dict['test_complete'] = False
                    #return render(request, 'VLA/simulationtest.html', context_dict)


            if num_of_correct == num_of_questions:
                context_dict['student_progress'].sim_test_finished = True

            # Set just_finished and is_completed to True and save
            context_dict['simulationtest_questions'] = simulationtest_questions
            context_dict['student_progress'].save()

        return render(request, 'VLA/simulationtest.html', context_dict)

# View for displaying directions for hardware experiment
# Information is presented in the form of text, images, equations, videos, or tables
def hardware(request, course_name_url, lab_name_url, hardware_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get course name and lab name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get lab, lab sections, and hardware elements
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            context_dict['hardware_elements'] = HardwareElement.objects.filter(hardware=context_dict['hardware'])

            # Update number of views if link was clicked
            if request.method == 'GET':
                context_dict['student_progress'].hardware_views = context_dict['student_progress'].hardware_views + 1
                context_dict['student_progress'].save()
        except Laboratory.DoesNotExist:
            pass

        # If request is a POST, try to pull out relevant information.
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['student_progress'].hardware_finished = True
            context_dict['student_progress'].save()
        return render(request, 'VLA/hardware.html', context_dict)

# NEEDS TO BE FINISHED
# View for displaying forms for user to input hardware results
# The information entered by the user will added to a generated Word document
def results(request, course_name_url, lab_name_url, results_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get course name and lab name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get lab, lab sections, and hardware elements
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            results_questions = ResultsQuestions.objects.filter(results=context_dict['results'])
            context_dict['results_questions'] = results_questions

            # Update number of views if link was clicked
            if request.method == 'GET':
                context_dict['student_progress'].results_views = context_dict['student_progress'].results_views + 1
                context_dict['student_progress'].save()
        except Laboratory.DoesNotExist:
            pass

        # If request is a POST, try to pull out relevant information.
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['student_progress'].results_finished = True
            context_dict['student_progress'].save()
        return render(request, 'VLA/results.html', context_dict)

# View used for giving test on simulation
# Questions are multiple choice, with at least two choices needed
def labtest(request, course_name_url, lab_name_url, labtest_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username

        # Get lab name, course name, an simulation test name
        lab_name = lab_name_url.replace('_', ' ')
        course_name = course_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}

        # Set to true before test is taken, in order to surpress error message
        # If all questions are not answered will be set to false
        context_dict['questions_filled'] = True

        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get lab, lab sections, and simulation test questions
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            labtest_questions = LabTestQuestion.objects.filter(labtest=context_dict['labtest'])
            context_dict['labtest_questions'] = labtest_questions
            context_dict['labtest_elements'] = LabTestElement.objects.filter(labtest=context_dict['labtest'])

            # Update number of views if link was clicked
            if request.method == 'GET':
                context_dict['student_progress'].lab_test_views = context_dict['student_progress'].lab_test_views + 1
                context_dict['student_progress'].save()
        except Laboratory.DoesNotExist:
            pass

        # If request is a POST, try to pull out relevant information.
        # Checks to see if each question is answered
        # if not return questions_filled=False and send to theorytest.html
        # Assigns each answer to question.given_answer
        if request.method == 'POST':
            num_of_questions = 0
            num_of_correct = 0
            for question in labtest_questions:
                num_of_questions = num_of_questions + 1
                name = 'choice' + str(num_of_questions)
                if name in request.POST:
                    question.given_answer = int(request.POST[name])
                    question.is_answered = True
                    question.save()
                else:
                    context_dict['questions_filled'] = False
                    context_dict['test_complete'] = False
                    return render(request, 'VLA/labtest.html', context_dict)
                if question.given_answer == question.correct_answer_number:
                    num_of_correct = num_of_correct + 1

            # Calculate test score
            context_dict['student_progress'].lab_test_score = num_of_correct/num_of_questions*100

            # Set just_finished and is_completed to True and save
            context_dict['just_finished'] = True
            context_dict['labtest_questions'] = labtest_questions
            context_dict['student_progress'].lab_test_finished = True
            context_dict['student_progress'].save()

        return render(request, 'VLA/labtest.html', context_dict)


# Get permissible course list and create URLs
def get_course_list(user):
    permissions = CoursePermission.objects.filter(user=user)
    cour_list = []
    for permission in permissions:
        cour_list.append(permission.course)

    for cour in cour_list:
        cour.url = cour.name.replace(' ', '_')
    return cour_list

# Get complete lab list for a given course and create URLs
def get_lab_list(course, user):
    lab_list = []
    permissions = LabProgress.objects.filter(user=user)
    for permission in permissions:
        if permission.lab.course == course:
            lab_list.append(permission.lab)

    for lab in lab_list:
        lab.url = lab.name.replace(' ', '_')

    return lab_list

# Get complete section list for a given lab and create URLs
def get_sections(context_dict, lab):
    try:
        theory = Theory.objects.filter(lab=lab).get(lab=lab)
        theory.url = theory.name.replace(' ', '_')
        context_dict['theory'] = theory
    except Theory.DoesNotExist:
        pass
    try:
        theorytest = TheoryTest.objects.filter(lab=lab).get(lab=lab)
        theorytest.url = theorytest.name.replace(' ', '_')
        context_dict['theorytest'] = theorytest
    except TheoryTest.DoesNotExist:
        pass
    try:
        simulation = Simulation.objects.filter(lab=lab).get(lab=lab)
        simulation.url = simulation.name.replace(' ', '_')
        context_dict['simulation'] = simulation
    except Simulation.DoesNotExist:
        pass
    try:
        simulationtest = SimulationTest.objects.filter(lab=lab).get(lab=lab)
        simulationtest.url = simulationtest.name.replace(' ', '_')
        context_dict['simulationtest'] = simulationtest
    except SimulationTest.DoesNotExist:
        pass
    try:
        hardware = Hardware.objects.filter(lab=lab).get(lab=lab)
        hardware.url = hardware.name.replace(' ', '_')
        context_dict['hardware'] = hardware
    except Hardware.DoesNotExist:
        pass
    try:
        results = Results.objects.filter(lab=lab).get(lab=lab)
        results.url = results.name.replace(' ', '_')
        context_dict['results'] = results
    except Results.DoesNotExist:
        pass
    try:
        labtest = LabTest.objects.filter(lab=lab).get(lab=lab)
        labtest.url = labtest.name.replace(' ', '_')
        context_dict['labtest'] = labtest
    except LabTest.DoesNotExist:
        pass

    return context_dict



# NOT WORKING
# Incomplete method used for extracting text elements from elements
# and replacing all keywords with mouseover definitions and links
def replace_with_definitions(elements):
    # get all useful definitions
    topic_list = VocabTopic.objects.filter(def_useful=False)
    def_list = Node.objects.all().exclude(topic__in=topic_list)

    # split text into list of words
    for element in elements:
        if element.element_type == 'text':
            words = element.text_input.split()
            for definition in def_list:
                if definition.word in words:
                    words = [w.replace(definition.word, definition.word) for w in words]
                #words = [word.replace(word, 'aaa')]
        # join words
        joined_words = '--'.join(words)
        element.text_input = joined_words

    return elements

###
#def GenerateDocument(request):
#
#    document = Document()
#    docx_title="TEST_DOCUMENT.docx"
#    # ---- Cover Letter ----
#    document.add_picture((r'%s/static/images/my-header.png' % (settings.PROJECT_PATH)), width=Inches(4))
#    document.add_paragraph()
#    document.add_paragraph("%s" % date.today().strftime('%B %d, %Y'))
#
#    document.add_paragraph('Dear Sir or Madam:')
#    document.add_paragraph('We are pleased to help you with your widgets.')
#    document.add_paragraph('Please feel free to contact me for any additional information.')
#    document.add_paragraph('I look forward to assisting you in this project.')
#
#    document.add_paragraph()
#    document.add_paragraph('Best regards,')
#    document.add_paragraph('Acme Specialist 1]')
#    document.add_page_break()
#
#    # Prepare document for download
#    # -----------------------------
#    f = StringIO()
#    document.save(f)
#    length = f.tell()
#    f.seek(0)
#    response = HttpResponse(
#        f.getvalue(),
#        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
#    )
#    response['Content-Disposition'] = 'attachment; filename=' + docx_title
#    response['Content-Length'] = length
#    return response




