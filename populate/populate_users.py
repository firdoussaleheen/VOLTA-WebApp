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
    add_user_profile(won, 'won', 'won', 999999999)
    add_courses_and_labs(won)

    #######test#####################
    voleksyuk = User.objects.create_user('voleksyuk', 'vira.oleksyuk@temple.edu', 'password')
    add_user_profile(voleksyuk, 'Vira', 'Oleksyuk', 91435609)
    add_courses_and_labs_EE2(voleksyuk)
    
    tuf67721 = User.objects.create_user('tuf67721', 'tuf67721@temple.edu', 'password')
    add_user_profile(tuf67721, 'David B' ,'Arnott', 999999999)
    add_courses_and_labs_EE2(tuf67721)

    tug21208 = User.objects.create_user('tug21208', 'tug21208@temple.edu', 'password')
    add_user_profile(tug21208, 'Sodiq' ,'Bakare-Adebiyi', 999999999)
    add_courses_and_labs_EE2(tug21208)


    tuf46217 = User.objects.create_user('tuf46217', 'tuf46217@temple.edu', 'password')
    add_user_profile(tuf46217, 'Jessica L' ,'Cohen', 999999999)
    add_courses_and_labs_EE2(tuf46217)

    tug25930 = User.objects.create_user('tug25930', 'tug25930@temple.edu', 'password')
    add_user_profile(tug25930, 'Mark' ,'Devlin', 999999999)
    add_courses_and_labs_EE2(tug25930)

    tug19749 = User.objects.create_user('tug19749', 'tug19749@temple.edu', 'password')
    add_user_profile(tug19749, 'Davy' ,'Duong', 999999999)
    add_courses_and_labs_EE2(tug19749)

    tue77920 = User.objects.create_user('tue77920', 'tue77920@temple.edu', 'password')
    add_user_profile(tue77920, 'Eronsele O' ,'Esquirell', 999999999)
    add_courses_and_labs_EE2(tue77920)

    tuf38533 = User.objects.create_user('tuf38533', 'tuf38533@temple.edu', 'password')
    add_user_profile(tuf38533, 'Reed Alexander' ,'PERRY', 999999999)
    add_courses_and_labs_EE2(tuf38533)


    tua52493 = User.objects.create_user('tua52493', 'tua52493@temple.edu', 'password')
    add_user_profile(tua52493, 'DAMIEN N' ,'GORDON', 999999999)
    add_courses_and_labs_EE2(tua52493)


    tuf84649 = User.objects.create_user('tuf84649', 'tuf84649@temple.edu', 'password')
    add_user_profile(tuf84649, 'Nathan Samue' ,'Groblewski', 999999999)
    add_courses_and_labs_EE2(tuf84649)

    tuc73299 = User.objects.create_user('tuc73299', 'tuc73299@temple.edu', 'password')
    add_user_profile(tuc73299, 'BENJAMIN L' ,'GROSS', 999999999)
    add_courses_and_labs_EE2(tuc73299)

    tuf72335 = User.objects.create_user('tuf72335', 'tuf72335@temple.edu', 'password')
    add_user_profile(tuf72335, 'Brandon Joseph' ,'Hacken', 999999999)
    add_courses_and_labs_EE2(tuf72335)

    tue67190 = User.objects.create_user('tue67190', 'tue67190@temple.edu', 'password')
    add_user_profile(tue67190, 'Junzhou' ,'Li', 999999999)
    add_courses_and_labs_EE2(tue67190)


    tuf07535 = User.objects.create_user('tuf07535', 'tuf07535@temple.edu', 'password')
    add_user_profile(tuf07535, 'Nenad' ,'Markovic', 999999999)
    add_courses_and_labs_EE2(tuf07535)


    tuf61549 = User.objects.create_user('tuf61549', 'tuf61549@temple.edu', 'password')
    add_user_profile(tuf61549, 'Sharon U' ,'Obiefuna', 999999999)
    add_courses_and_labs_EE2(tuf61549)


    tuf42280 = User.objects.create_user('tuf42280', 'tue67190@temple.edu', 'password')
    add_user_profile(tuf42280, 'Isaac A' ,'Provenza', 999999999)
    add_courses_and_labs_EE2(tuf42280)


    tud21661 = User.objects.create_user('tud21661', 'tud21661@temple.edu', 'password')
    add_user_profile(tud21661, 'Anthony M' ,'Richards', 999999999)
    add_courses_and_labs_EE2(tud21661)

    tue82652 = User.objects.create_user('tue82652', 'tue82652@temple.edu', 'password')
    add_user_profile(tue82652, 'Kayleigh C' ,'Ross', 999999999)
    add_courses_and_labs_EE2(tue82652)

    tue99793 = User.objects.create_user('tue99793', 'tue99793@temple.edu', 'password')
    add_user_profile(tue99793, 'Nicholas J' ,'Stumpo', 999999999)
    add_courses_and_labs_EE2(tue99793)

    tuf42516 = User.objects.create_user('tuf42516', 'tuf42516@temple.edu', 'password')
    add_user_profile(tuf42516, 'Jonathan W' ,'Szynal', 999999999)
    add_courses_and_labs_EE2(tuf42516)

    tuf77943 = User.objects.create_user('tuf77943', 'tuf77943@temple.edu', 'password')
    add_user_profile(tuf77943, 'Victor' ,'Tang', 999999999)
    add_courses_and_labs_EE2(tuf77943)

    tuf61148 = User.objects.create_user('tuf61148', ' tuf61148@temple.edu', 'password')
    add_user_profile(tuf61148, 'Sophia' ,'Tran', 999999999)
    add_courses_and_labs_EE2(tuf61148)

    tuf73139 = User.objects.create_user('tuf73139', 'tuf73139@temple.edu', 'password')
    add_user_profile(tuf73139, 'z' ,'wang', 999999999)
    add_courses_and_labs_EE2(tuf73139)



    tug27939 = User.objects.create_user('tug27939', 'tug27939@temple.edu', 'password')
    add_user_profile(tug27939, 'Sivan' ,'Zlotnikov', 999999999)
    add_courses_and_labs_EE2(tug27939)
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
