import os

'''
Script to populate Users, and assigned Courses and Laboratories:

THIS MUST BE CALLED AFTER COURSES/LABS ARE POPULATED
'''

def populate():
    
    # Create guest user and profile
    guest = User.objects.create_user('guest', 'guest@guest.com', 'password')
    add_user_profile(guest, 'John', 'Doe', 999999999)
    
    # Assign all courses and their labs
    add_courses_and_labs(guest)
    
    sg = User.objects.get(username='salvatoregiorgi')
    add_user_profile(sg, 'Salvatore', 'Giorgi', 111111111)
    
    # Assign all courses and their labs
    add_courses_and_labs(sg)
    
    fsaleheen = User.objects.create_user('fsaleheen', 'f.saleheen@gmail.com', 'password')
    add_user_profile(fsaleheen, 'Firdous', 'Saleheen', 999999999)
    add_courses_and_labs(fsaleheen)
    
    won = User.objects.create_user('won', 'cwon@temple.edu', 'password')
    add_courses_and_labs(won)

    #######test#####################
    voleksyuk = User.objects.create_user('voleksyuk', 'vira.oleksyuk@temple.edu', 'password')
    add_user_profile(voleksyuk, 'Vira', 'Oleksyuk', 91435609)
    add_courses_and_labs_EE2(voleksyuk)
    ########### test ##################
    ##### ECE 2323 Sec 002 Fall 2014 Students########
    halruhaimani = User.objects.create_user('halruhaimani', 'tue52757@temple.edu', 'password')
    add_user_profile(halruhaimani, 'Hamad' ,'Alruhaimani', 914968783)
    add_courses_and_labs_EE2(halruhaimani)

    kamegan = User.objects.create_user('kamegan', 'tuf27863@temple.edu', 'password')
    add_user_profile(kamegan, 'Koffiedem', 'Amegan', 915120914)
    add_courses_and_labs_EE2(kamegan)

    jcassel = User.objects.create_user('jcassel', 'tue91395@temple.edu', 'password')
    add_user_profile(jcassel, 'Jason', 'Cassel', 915049154)
    add_courses_and_labs_EE2(jcassel)

    jchen = User.objects.create_user('jchen', 'tuf62051@temple.edu', 'passwod')
    add_user_profile(jchen, 'Jayson', 'Chen', 915191504)
    add_courses_and_labs_EE2(jchen)

    mchladek = User.objects.create_user('mchladek', 'tuf59539@temple.edu', 'passwod')
    add_user_profile(mchladek, 'Michael', 'Chladek', 915201683)
    add_courses_and_labs_EE2(mchladek)

    pgarrit = User.objects.create_user('pgarrit', 'tuf81103@temple.edu', 'passwod')
    add_user_profile(pgarrit, 'Pedro', 'Garrit', 915212122)
    add_courses_and_labs_EE2(pgarrit)

    mgeorge = User.objects.create_user('mgeorge', 'tue97790@temple.edu', 'passwod')
    add_user_profile(mgeorge, 'Maya', 'George', 912069999)
    add_courses_and_labs_EE2(mgeorge)

    oigwilo = User.objects.create_user('oigwilo', 'tuf24685@temple.edu', 'passwod')
    add_user_profile(oigwilo, 'Obiora', 'Igwilo', 914879467)
    add_courses_and_labs_EE2(oigwilo)

    njirapattananon = User.objects.create_user('njirapattananon', 'tuf61406@temple.edu', 'passwod')
    add_user_profile(njirapattananon, 'Narongsak', 'Jirapattananon', 915203794)
    add_courses_and_labs_EE2(njirapattananon)

    nkuranaruk = User.objects.create_user('nkuranaruk', 'tue35423@temple.edu', 'passwod')
    add_user_profile(nkuranaruk, 'Nissa', 'Kuranaruk', 910657852)
    add_courses_and_labs_EE2(nkuranaruk)

    ypatel = User.objects.create_user('ypatel', 'tue53802@temple.edu', 'passwod')
    add_user_profile(ypatel, 'Yogesh', 'Patel', 914968508)
    add_courses_and_labs_EE2(ypatel)

    dpittman = User.objects.create_user('dpittman', 'tuf78579@temple.edu', 'passwod')
    add_user_profile(dpittman, 'Devin', 'Pittman', 915240985)
    add_courses_and_labs_EE2(dpittman)

    nroeung = User.objects.create_user('nroeung', 'tue54618@temple.edu', 'passwod')
    add_user_profile(nroeung, 'Nhimvichhay', 'Roeung', 914967703)
    add_courses_and_labs_EE2(nroeung)

    msamarco = User.objects.create_user('msamarco', 'tue77186@temple.edu', 'passwod')
    add_user_profile(msamarco, 'Michael', 'Samarco', 914991638)
    add_courses_and_labs_EE2(msamarco)

    bschumer = User.objects.create_user('bschumer', 'tud51327@temple.edu', 'passwod')
    add_user_profile(bschumer, 'Brad', 'Schumer', 914890566)
    add_courses_and_labs_EE2(bschumer)

    ksou = User.objects.create_user('ksou', 'tud36184@temple.edu', 'passwod')
    add_user_profile(ksou, 'Khuntha', 'Sou', 910232769)
    add_courses_and_labs_EE2(ksou)

    mwilliams = User.objects.create_user('mwilliams', 'tue79528@temple.edu', 'passwod')
    add_user_profile(mwilliams, 'Marcus', 'Williams', 915018904)
    add_courses_and_labs_EE2(mwilliams)

    ryi = User.objects.create_user('ryi', 'tue64554@temple.edu', 'password')
    add_user_profile(ryi, 'Raymond', 'Yi', 914988834)
    add_courses_and_labs_EE2(ryi)
    
    # Print out what we have added to the user.
    for u in User.objects.all():
        for cp in CoursePermission.objects.filter(course=u):
            print "- {0} - {1}".format(str(u), str(cp))

# Add user, user profile, course permission, and lab progress
def add_user():
    u = User.objects.get_or_create(user=user, first_name=first_name,
                                           last_name=last_name, TUid=TUid)[0]
    return u

def add_user_profile(user, first_name, last_name, TUid):
    up = UserProfile.objects.get_or_create(user=user, first_name=first_name,
                                           last_name=last_name, TUid=TUid)[0]
    return up

def add_course_permission(user, course):
    cp = CoursePermission.objects.get_or_create(user=user, course=course,
                                           course_finished=False)[0]
    return cp

def add_lab_progress(user, lab):
    lp = LabProgress.objects.get_or_create(user=user, lab=lab,
                                           theory_finished=False,
                                           theory_test_finished=False,
                                           simulation_finished=False,
                                           sim_test_finished=False,
                                           hardware_finished=False,
                                           results_finished=False,
                                           lab_test_finished=False,
                                           lab_finished=False,
                                           theory_test_score=0,
                                           lab_test_score=0)[0]
    return lp

def add_sim_question_response(labprogress, question_number):
    sqr = SimulationQuestionResponse.objects.get_or_create(labprogress=labprogress, question_number=question_number)
    
    return sqr

# Give permission to guest for all Courses, and all Labs within each course
def add_courses_and_labs(user):
    courses = Course.objects.all()
    for course in courses:
        add_course_permission(user, course)
        labs = Laboratory.objects.filter(course=course)
        for lab in labs:
            labprogress = add_lab_progress(user, lab)
            simulationtest = SimulationTest.objects.filter(lab=lab)
            test_questions = SimulationTestQuestion.objects.filter(simulationtest=simulationtest)
            question_number = 0
            for question in test_questions:
                question_number = question_number + 1
                add_sim_question_response(labprogress, question_number)

#####course permission test for vira###########
def add_courses_and_labs_EE2(user):
    course = Course.objects.filter(name = 'EE Science II')
    for course in course:
        add_course_permission(user, course)
        labs = Laboratory.objects.filter(course=course)
        for lab in labs:
            labprogress = add_lab_progress(user, lab)
            simulationtest = SimulationTest.objects.filter(lab=lab)
            test_questions = SimulationTestQuestion.objects.filter(simulationtest=simulationtest)
            question_number = 0
            for question in test_questions:
                question_number = question_number + 1
                add_sim_question_response(labprogress, question_number)


# Start execution here!
if __name__ == '__main__':
    print "Starting USER population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    from VLA.models import Course, Laboratory, SimulationTest
    from student.models import UserProfile, CoursePermission, LabProgress, User, SimulationQuestionResponse
    populate()
