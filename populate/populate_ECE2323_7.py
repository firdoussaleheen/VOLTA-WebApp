import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
-EE Science II Course

LABORATORIES:

'''

    ###
    # EE Science II Lab 7: Impedance Measurement of AC Circuit
    ###
def populate(ee_science_ii):
    impedance_ac = add_lab(course=ee_science_ii, name="Impedance Measurement of AC Circuit",
                                  start_date=timezone.now(), due_date=timezone.now(),
                                  lab_number=7)
    add_lab_objective(lab=impedance_ac,
                      objective="The purpose of this week's lab is to measure impedances of AC circuit. "+
                      "This lab includes a pre-lab.")


    # Impedance Measurement of AC Circuit Theory 
    ci_theory = add_theory(lab=impedance_ac, name="Impedance Measurement of AC Circuit Theory")
    
    add_theory_element(theory=ci_theory, name="ci theory 1", number=1,
                       text_input="Impedance is defined as the ratio of the phasor voltage V to the phasor current I. "+
                       "Since V and I are complex, the impedance Z is complex. Impedance in an ac circuit is analogous to "+
                       "resistance in a dc circuit. In rectangular form, impedance is expressed in terms of resistance (R) "+
                       "and reactance (X) as: \(Z(\\omega)=R+jX(\\omega)\). The magnitude of the impedance can be expressed as: \(|Z|=\\sqrt{R^2+X^2}\). "+
                       "The capacitive reactance is \(X_C=\\frac{1}{j\\omega C}\), and the inductive reactance is \(X_L=j\\omega L\). KVL and KCL are both "+
                       "valid in frequency domain. Therefore, impendences can be combined using the same rules as resistor combinations. "+
                       "This review will help you in performing Pre-Lab and test.",
                       image_input=None, equation_input="", video_input="", element_type='text')

    # Impedance Measurement of AC Circuit theory test
    ci_theory_test = add_theory_test(lab=impedance_ac, name="Impedance Measurement of AC Circuit Theory Test")

                        
    add_theory_test_element(theorytest=ci_theory_test, name="ci theory test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab07/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=ci_theory_test, name="ci theory test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

                        
    add_theory_test_element(theorytest=ci_theory_test, name="ci theory test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab07/fig05.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=ci_theory_test, name="ci theory test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=ci_theory_test, name="ci theory test element 5", number=5,
                      text_input="Note: Figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')

    add_theory_test_question(theorytest=ci_theory_test,
                             question="Consider the circuit in Fig. I. Given, Vm = 10 V and Vo = 5V, what is the magnitude of the impedance?",
                             answer_one="2 \(\\Omega\)", answer_two="4 \(\\Omega\)",
                             answer_three="20 \(\\Omega\)", answer_four="200 \(\\Omega\)",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=ci_theory_test,
                             question="Consider the circuit in Fig. I. Given, Vm = 10 V and Vo = 5V, what is the value of inductive reactance?",
                             answer_one="173.2 \(\\Omega\)", answer_two="17.32 \(\\Omega\)",
                             answer_three="200 \(\\Omega\)", answer_four="20 \(\\Omega\)",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")


    add_theory_test_question(theorytest=ci_theory_test,
                             question="Consider the circuit in Fig. I. Given, Vm = 10 V, Vo = 5V, and reactance  \(X_L\) = 173.2\(\\Omega\), what is the frequency (f) of the input voltage?",
                             answer_one="173.2 kHz", answer_two="27.56 kHz",
                             answer_three="20 kHz", answer_four="5 kHz",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=ci_theory_test,
                             question="Consider the circuit in Fig. II. Given, \(V_{in}(t)=10cos(10000t)\), what is the impedance Z of the circuit?",
                             answer_one="(100+ j0.001) \(\\Omega\)", answer_two="(100- j0.001 \(\\Omega\)",
                             answer_three="(100+ j1000)  \(\\Omega\)", answer_four="(100- j1000)  \(\\Omega\)",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=ci_theory_test,
                             question="Consider the circuit in Fig. II. Given, \(V_{in}(t)=10cos(10000t)\), what is the magnitude of impedance Z of the circuit?",
                             answer_one="900 \(\\Omega\)", answer_two="1005 \(\\Omega\)",
                             answer_three="500 \(\\Omega\)", answer_four="100 \(\\Omega\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")


  
    # Impedance Measurement of AC Circuit Simulation
    ci_simulation = add_simulation(lab=impedance_ac, name="Impedance Measurement of AC Circuit Simulation")

    add_simulation_element(simulation=ci_simulation,
                           name = "Impedance Measurement of AC Circuit simulation 1", number=1,
                           text_input="For each of the two circuits shown in Fig. 1 and 2, find an expression for impedance using Vout, Vin, and resistor value. For Multisim circuit Comparator, you must use step input voltage (1V).(use circuit comparator for the 2 circuit,Vin to be a 1V 100Hz sine wave. Let R=100,C=0.1nF,and L=1mH.)", 
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')

    add_simulation_element(simulation=ci_simulation,
                           name="Impedance Measurement of AC Circuit simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab07/fig01.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=ci_simulation,
                           name="Impedance Measurement of AC Circuit simulation 3", number=3,
                           text_input="Figure 1",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
    add_simulation_element(simulation=ci_simulation,
                           name="Impedance Measurement of AC Circuit simulation 4", number=4,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab07/fig02.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=ci_simulation,
                           name="Impedance Measurement of AC Circuit simulation 5", number=5,
                           text_input="Figure 2",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')



                      

    
    # Impedance Measurement of AC Circuit Hardware
    ci_hardware = add_hardware(lab=impedance_ac, name="Impedance Measurement of AC Circuit Hardware")
    
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 1", number=1,
                         text_input="<h4>Part 1. CIRCUIT 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 2", number=2,
                         text_input="Build the series RL circuit from the pre-lab. Your task is to create a plot with frequency "+
                         "on the x-axis and impedance magnitude on the y-axis. To find the impedance, use the relationship you derive in Pre-lab. "+
                         "Measure the impedance magnitude at the following frequencies to create your plot. These frequencies are log-spaced so be sure "+
                         "to use log-spacing on your x axis. f = 100Hz, 200Hz, 500Hz, 1kHz, 2kHz, 5kHz, 10kHz, 20kHz, 50kHz, 100kHz, 200kHz, 500kHz, 1MHz. "+
                         "Finally answer the following questions:",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 3", number=3,
                         text_input="a. Plot impedance versus frequency using theoretical calculations.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 4", number=4,
                         text_input="b. How is the impedance trend in low and high frequency?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 5", number=5,
                         text_input="c. Plot impedance versus frequency using data from EE board. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 6", number=6,
                         text_input="d. Comment on how well the theoretical values match to the measured data points.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 7", number=7,
                         text_input="<h4>Part 2. CIRCUIT 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 8", number=8,
                         text_input="Repeat the previous section using the RC circuit from the simulation " +
                         "(use the same list of frequencies too). Note that the ceramic capacitor " +
                         "labeled '104' should be 100nF. Answer the following questions:",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 9", number=9,
                         text_input="a. Plot impedance versus frequency using theoretical calculations.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 10", number=10,
                         text_input="b. How is the impedance trend in low and high frequency?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 11", number=11,
                         text_input="c. Plot impedance versus frequency using data from EE board. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 12", number=12,
                         text_input="d. Comment on how well the theoretical values match to the measured data points.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 13", number=13,
                         text_input="<h4>Part 3. CIRCUIT 3</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 14", number=14,
                         text_input="Build the series RLC circuit shown in Fig. 3. Use the same list of frequencies as in circuit 1. Answer the following questions:",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 15", number=15,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab07/fig03.jpg', equation_input="", video_input="", 
                         element_type='image')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 16", number=16,
                         text_input="Figure 3",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 17", number=17,
                         text_input="a. Plot impedance versus frequency using theoretical calculations.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 18", number=18,
                         text_input="b. How is the impedance trend in low and high frequency?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 19", number=19,
                         text_input="c. Plot impedance versus frequency using data from EE board. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=ci_hardware, name="Impedance Measurement of AC Circuit hardware 20", number=20,
                         text_input="d. Comment on how well the theoretical values match to the measured data points.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
   

    # Impedance Measurement of AC Circuit Results
    ci_results = add_results(lab=impedance_ac, name="Impedance Measurement of AC Circuit Results")

    add_results_questions(results=ci_results,
                          question="Write a standard report as specified in the syllabus. "+
                          "Explain your work with the detailed calculations, observations, and analysis. In your report, you must include the answers to the questions in hardware section.",
                          answer_text="",
                          answer_type='text')
     
    add_results_questions(results=ci_results,
                          question="Submit the report to our <a href=\"https://blackboard.temple.edu\">blackboard</a> before the next lab (see syllabus for submission guideline).",
                          answer_text="",
                          answer_type='text')

    # Impedance Measurement of AC Circuit lab test
    ci_lab_test = add_lab_test(lab=impedance_ac, name="Impedance Measurement of AC Circuit lab Test")

                        
    add_lab_test_element(labtest=ci_lab_test, name="ci lab test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab07/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=ci_lab_test, name="ci lab test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

                        
    add_lab_test_element(labtest=ci_lab_test, name="ci lab test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab07/fig05.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=ci_lab_test, name="ci lab test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=ci_lab_test, name="ci lab test element 5", number=5,
                      text_input="Note: Figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')


    add_lab_test_question(labtest=ci_lab_test,
                             question="Consider the circuit in Fig. I. Given, Vm = 10 V and Vo = 5V, what is the magnitude of the impedance?",
                             answer_one="2 \(\\Omega\)", answer_two="200 \(\\Omega\)",
                             answer_three="4 \(\\Omega\)", answer_four="20 \(\\Omega\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=ci_lab_test,
                             question="Consider the circuit in Fig. I. Given, Vm = 10 V and Vo = 5V, what is the value of inductive reactance?",
                             answer_one="17.32 \(\\Omega\)", answer_two="173.2 \(\\Omega\)",
                             answer_three="200 \(\\Omega\)", answer_four="20 \(\\Omega\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")


    add_lab_test_question(labtest=ci_lab_test,
                             question="Consider the circuit in Fig. I. Given, Vm = 10 V, Vo = 5V, and reactance \(X_L\) = 173.2 \(\\Omega\), what is the frequency (f) of the input voltage?",
                             answer_one="27.56 kHz", answer_two="173.2 kHz",
                             answer_three="20 kHz", answer_four="5 kHz",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=ci_lab_test,
                             question="Consider the circuit in Fig. II. Given, \(V_{in}(t)=10cos(10000t)\), what is the impedance Z of the circuit?",
                             answer_one="(100+ j0.001) \(\\Omega\)", answer_two="(100+ j1000) \(\\Omega\)",
                             answer_three="(100- j0.001) \(\\Omega\)", answer_four="(100- j1000)  \(\\Omega\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=ci_lab_test,
                             question="Consider the circuit in Fig. II. Given, \(V_{in}(t)=10cos(10000t)\), what is the magnitude of impedance Z of the circuit?",
                             answer_one="900 \(\\Omega\)", answer_two="500 \(\\Omega\)",
                             answer_three="100 \(\\Omega\)", answer_four="1005 \(\\Omega\)",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")


    # Print out what we have added to the user.
    #for c in Course.objects.all():
    #    for l in Laboratory.objects.filter(course=c):
    #        print "- {0} - {1}".format(str(c), str(l))
            

    # Add labpermissions for new lab for each user 
    for u in User.objects.all():
        add_new_lab_permission(user=u, lab=impedance_ac)
    
def add_lab(course, name, start_date, due_date, lab_number):
    l = Laboratory.objects.get_or_create(course=course, name=name,
                                         start_date=start_date,
                                         due_date=due_date,
                                         lab_number=lab_number)[0]
    return l

def add_lab_objective(lab, objective):
    lo = LabObjective.objects.get_or_create(lab=lab, objective=objective)[0]
    return lo

def add_lab_equipment(lab, equipment):
    le = LabEquipment.objects.get_or_create(lab=lab, equipment=equipment)[0]
    return le

def add_theory(lab, name):
    t = Theory.objects.get_or_create(lab=lab, name=name)[0]
    return t

def add_theory_element(theory, name, number, text_input, image_input,
                       equation_input, element_type, video_input):
    te = TheoryElement.objects.get_or_create(theory=theory, name=name,
                                             number=number,
                                             text_input=text_input,
                                             image_input=image_input,
                                             equation_input=equation_input,
                                             element_type=element_type,
                                             video_input=video_input)[0]
    return te

def add_theory_test(lab, name):
    tt = TheoryTest.objects.get_or_create(lab=lab, name=name)[0]
    return tt

def add_theory_test_element(theorytest, name, number, text_input, image_input,
                         equation_input, element_type, video_input):
    tte = TheoryTestElement.objects.get_or_create(theorytest=theorytest, name=name,
                                               number=number,
                                               text_input=text_input,
                                               image_input=image_input,
                                               equation_input=equation_input,
                                               element_type=element_type,
                                               video_input=video_input)[0]
    return tte

def add_theory_test_question(theorytest, question, answer_one, answer_two,
                             answer_three, answer_four, correct_answer_number,
                             correct_response, incorrect_response):
    ttq = TheoryTestQuestion.objects.get_or_create(theorytest=theorytest,
                                                   question=question,
                                                   answer_one=answer_one,
                                                   answer_two=answer_two,
                                                   answer_three=answer_three,
                                                   answer_four=answer_four,
                                                   correct_answer_number=correct_answer_number,
                                                   correct_response= correct_response,
                                                   incorrect_response=incorrect_response)[0]
    return ttq

def add_simulation(lab, name):
    s = Simulation.objects.get_or_create(lab=lab, name=name)[0]
    return s

def add_simulation_element(simulation, name, number, text_input, image_input,
                           equation_input, element_type, video_input):
    se = SimulationElement.objects.get_or_create(simulation=simulation,
                                                 name=name, number=number,
                                                 text_input=text_input,
                                                 image_input=image_input,
                                                 equation_input=equation_input,
                                                 element_type=element_type,
                                                 video_input=video_input)[0]
    return se

def add_simulation_test(lab, name):
    st = SimulationTest.objects.get_or_create(lab=lab, name=name)[0]
    return st

def add_sim_test_element(simulationtest, name, number, text_input, image_input,
                         equation_input, element_type, video_input):
    ste = SimulationTestElement.objects.get_or_create(simulationtest=simulationtest, name=name,
                                               number=number,
                                               text_input=text_input,
                                               image_input=image_input,
                                               equation_input=equation_input,
                                               element_type=element_type,
                                               video_input=video_input)[0]
    return ste

def add_simulation_test_question(simulationtest, question, answer_one,
                                 answer_two, answer_three, answer_four,
                                 correct_answer_number, correct_response,
                                 incorrect_response):
    stq = SimulationTestQuestion.objects.get_or_create(simulationtest=simulationtest,
                                                       question=question,
                                                       answer_one=answer_one,
                                                       answer_two=answer_two,
                                                       answer_three=answer_three,
                                                       answer_four=answer_four,
                                                       correct_answer_number=correct_answer_number,
                                                       correct_response= correct_response,
                                                       incorrect_response=incorrect_response)[0]
    return stq

def add_hardware(lab, name):
    h = Hardware.objects.get_or_create(lab=lab, name=name)[0]
    return h

def add_hardware_element(hardware, name, number, text_input, image_input,
                         equation_input, element_type, video_input):
    he = HardwareElement.objects.get_or_create(hardware=hardware, name=name,
                                               number=number,
                                               text_input=text_input,
                                               image_input=image_input,
                                               equation_input=equation_input,
                                               element_type=element_type,
                                               video_input=video_input)[0]
    return he

def add_results(lab, name):
    r = Results.objects.get_or_create(lab=lab, name=name)[0]
    return r

def add_results_questions(results, question, answer_text, answer_type):
    rq = ResultsQuestions.objects.get_or_create(results=results, question=question,
                                                answer_text=answer_text,
                                                answer_type=answer_type)[0]
    return rq

def add_lab_test(lab, name):
    lt = LabTest.objects.get_or_create(lab=lab, name=name)[0]
    return lt

def add_lab_test_element(labtest, name, number, text_input, image_input,
                         equation_input, element_type, video_input):
    lte = LabTestElement.objects.get_or_create(labtest=labtest, name=name,
                                               number=number,
                                               text_input=text_input,
                                               image_input=image_input,
                                               equation_input=equation_input,
                                               element_type=element_type,
                                               video_input=video_input)[0]
    return lte

def add_lab_test_question(labtest, question, answer_one,
                                 answer_two, answer_three, answer_four,
                                 correct_answer_number, correct_response,
                                 incorrect_response):
    ltq = LabTestQuestion.objects.get_or_create(labtest=labtest,
                                                       question=question,
                                                       answer_one=answer_one,
                                                       answer_two=answer_two,
                                                       answer_three=answer_three,
                                                       answer_four=answer_four,
                                                       correct_answer_number=correct_answer_number,
                                                       correct_response= correct_response,
                                                       incorrect_response=incorrect_response)[0]
    return ltq

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

def add_new_lab_permission(user, lab):
    labprogress = add_lab_progress(user, lab)
    simulationtest = SimulationTest.objects.filter(lab=lab)
    test_questions = SimulationTestQuestion.objects.filter(simulationtest=simulationtest)
    question_number = 0
    for question in test_questions:
        question_number = question_number + 1
        add_sim_question_response(labprogress, question_number)

# Start execution here!
if __name__ == '__main__':
    print "Starting VLA population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    from VLA.models import *
    from student.models import LabProgress, User, SimulationQuestionResponse
    
    ee_science = Course.objects.filter(name = 'EE Science II')
    for course in ee_science:
        populate(ee_science_ii=course)
