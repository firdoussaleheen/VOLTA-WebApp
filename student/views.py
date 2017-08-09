from __future__ import absolute_import

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from VLA.models import Course
from student.models import UserProfile, CoursePermission, LabProgress
from tutor.models import Node, AnswerWithQuestion

# Login, register, and profile views
def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If request is a POST, try to pull out relevant information.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'VLA/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    # If request is a POST, try to pull out relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/VLA/')
            else:
                # An inactive account was used - no logging in!
                context_dict = {'disabled_account': True}
                return render(request, 'VLA/login.html', context_dict)
        else:
            # Bad login details were provided. So we can't log the user in.
            context_dict = {'error': True}
            return render(request, 'VLA/login.html', context_dict)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        context_dict = {'error': False, 'disabled_account': False}
        return render(request, 'VLA/login.html', context_dict)

def profile(request, user_name_url):
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
        user_name = user_name_url.replace('_', ' ')
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Check if user is trying to view another user's profile
        # If true, set correct_user=False, else set correct_user=True
        if username != user_name_url:
            context_dict['correct_user'] = False
            return render(request, 'VLA/profile.html', context_dict)
        else:
            context_dict['correct_user'] = True
        
        # Get User object
        try:
            if not User.objects.get(username=user_name):
                return render(request, 'VLA/login.html')
            else:
                this_user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            pass
        
        # Get User Profile
        try: 
            context_dict['user_info'] = UserProfile.objects.get(user=this_user)
        except UserProfile.DoesNotExist:
            context_dict['user_info'] = ''
           
        # Get permissible course and lab information 
        try:
            course_permissions = CoursePermission.objects.filter(user=user)
            for course in course_permissions:
                labs = Laboratory.objects.filter(course=course.course)
                course.labs = []
                for lab in labs:
                    course.labs.append(LabProgress.objects.filter(user=user).get(lab=lab)) 
                course.lab_permissions = []
            context_dict['enrolled_courses'] = course_permissions
        except CoursePermission.DoesNotExist:
            context_dict['enrolled_courses'] = ''
        
        return render(request, 'VLA/profile.html', context_dict)

@login_required
def user_logout(request):
    user = request.user																	#Edited July 22nd, 2015...
    username = request.user.username
    if username == 'guest':
        lab_progress = LabProgress.objects.filter(user=user)
        for lab in lab_progress:
            lab.theory_finished = False
            lab.theory_test_finished = False
            lab.simulation_finished = False
            lab.sim_test_finished = False
            lab.hardware_finished = False
            lab.results_finished = False
            lab.lab_test_finished = False
            lab.lab_finished = False
            lab.save()																			#...end of edits.
    logout(request)
    return HttpResponseRedirect('/VLA')


# Get permissible course list and create URLs
def get_course_list(user):
    permissions = CoursePermission.objects.filter(user=user)
    cour_list = []
    for permission in permissions:
        cour_list.append(permission.course)

    for cour in cour_list:
        cour.url = cour.name.replace(' ', '_')
    return cour_list
