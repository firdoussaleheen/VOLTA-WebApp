import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
-EE Science II Course

LABORATORIES:
-Intro to Multisim using RC Circuit
'''

    ###
    # EE Science II Lab 2: Digilent Board Intro & RC Time Constant
    ###
def populate(ee_science_ii):
    # Find EE Science II Course
    digilent_board_intro = add_lab(course=ee_science_ii, name="Digilent Board Intro using RC Circuit",start_date=timezone.now(),
                                   due_date=timezone.now(),lab_number=2)

    add_lab_objective(lab=digilent_board_intro, objective="The purpose of this week's lab is two-fold. The first goal is to introduce "+
                                "the Digilent Electronics Explorer (EE) board and the second is to give experience in measuring the "+
                                "time constant of an RC circuit.")

    # Digilent EE Board Intro using RC Circuit 
    digilent_board_theory = add_theory(lab=digilent_board_intro, name="RC Circuit Theory Review")
    
    add_theory_element(theory=digilent_board_theory, name="digilent theory 1", number=1,
                       text_input="The previous lab was about introduction to Multisim using RC Circuit. In this lab, we shall learn how to "+
		       "use Digilent EE board for implementing the RC circuit. We shall follow the review of RC circuit theory covered in Lab 1. "+
		       "Also, we shall introduce the formula for charging and discharging current for a series RC circuit. Consider Fig.1 "+
                       "where a series RC circuit is shown with a switch.",
                       image_input=None, equation_input="", video_input="", element_type='text')

    # fig 1 and caption goes here
    add_theory_element(theory=digilent_board_theory,name="digilent theory 2", number=2,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab02/fig01.jpg', equation_input="", video_input="", 
                      element_type='image')

    add_theory_element(theory=digilent_board_theory, name="digilent theory 3", number=3,
                      text_input="Figure 1",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_element(theory=digilent_board_theory, name="digilent theory 4", number=4,
                       text_input="When the switch is in position '1', the capacitor is being charged "+
                       "(assuming zero initial charge). And after that, if the switch is changed to the position '2', the capacitor is being discharged. "+
                       "For position '1' of the switch, the charging current that flows through the resistor experiences an exponential decay. The charging "+
                       "current through the resistor is \(I_r = I_se^{-\\frac{t}{RC}}\), where the initial current is \(I_s=\\frac{V_s}{R}\). For position '2' "+
                       "of switch, the discharging current follows the same formula. However, the direction of the current flow is opposite to the charging current case. "+
                       "This charging and discharging current formula will help you in the lab test.",
                       image_input=None, equation_input="", video_input="", element_type='text')



    # Digilent board Intro using RC circuit theory test
    digilent_board_theory_test = add_theory_test(lab=digilent_board_intro, name="Digilent Board Intro Theory Test")

                        
    add_theory_test_element(theorytest=digilent_board_theory_test, name="digilent theory test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab02/fig03.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=digilent_board_theory_test, name="digilent theory test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=digilent_board_theory_test, name="digilent theory test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab02/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=digilent_board_theory_test, name="digilent theory test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

   
    add_theory_test_question(theorytest=digilent_board_theory_test,
                             question="Refer to Fig. I what would be the initial voltage of the capacitor when the switch is just closed?",
                             answer_one="12V", answer_two="6V",
                             answer_three="4V", answer_four="2V",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=digilent_board_theory_test,
                             question="Refer to the circuit in Fig. I. At t=0.6 ms, what would be the capacitor voltage?",
                             answer_one="9.1V", answer_two="8.1V",
                             answer_three="6.1V", answer_four="8.9V",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=digilent_board_theory_test,
                             question="Refer to the circuit in Fig. II. Given, Vs = 6V, R = 5\(\\Omega\), C = 10 \(\\mu\)F. Suppose, after a long time, if the charging battery is removed and the capacitor "+
                             "is immediately connected across the 5 ohms resistor, what will be the initial value of the discharge current?",
                             answer_one="1.2A", answer_two="0.6A",
                             answer_three="0.3A", answer_four="1.2A",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=digilent_board_theory_test,
                             question="Refer to the circuit in Fig. II. Given, Vs = 6V, R = 5\(\\Omega\), C = 10 \(\\mu\)F. What will be the charging current at the instant t = 50 microseconds? Use the charging current formula.",
                             answer_one="0.368A", answer_two="0.4416A",
                             answer_three="0.6A", answer_four="1.2A",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=digilent_board_theory_test,
                             question="Refer to the circuit in Fig. II. Assume that initial capacitor voltage is zero. When the capacitor in the RC circuit above reaches its maximum voltage, which of the following statements is FALSE? ",
                             answer_one="the voltage across the capacitor is at its maximum", answer_two="the voltage across the resistor is zero",
                             answer_three="the sum of the voltages across the capacitor and resistor is equal to the initial voltage across the resistor", answer_four="the sum of the voltages across the capacitor and resistor is equal to the initial voltage across the capacitor",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")

    # Digilent Board Intro & RC Time Constant Simulation
    digilent_board_simulation = add_simulation(lab=digilent_board_intro, name="Digilent Board Intro Simulation")
    
    add_simulation_element(simulation=digilent_board_simulation,
                           name="digilent intro simulation 1", number=1,
                           text_input="You should use the last simulation circuit in Lab 1 this time. The simulation circuit was an RC circuit with a square pulse input with \(R=1k\\Omega\), \(C=1\\mu F\). Repeat this circuit simulation for "+
                           "\(R=1k\\Omega\), \(C=0.1\\mu F\). Keep the simulation circuits for comparing with hardware results later.(use circuit comparator for the 2 circuits)",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=digilent_board_simulation,
                           name="digilent intro simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab02/fig02.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=digilent_board_simulation,
                           name="digilent intro simulation 3", number=3,
                           text_input="Figure 2",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')

                       

    # Digilent Board Intro & RC Time Constant Hardware
    digilent_board_hardware = add_hardware(lab=digilent_board_intro, name="Digilent Board Intro Hardware")

    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 1", number=1,
                         text_input="In this section, we shall introduce the EE board features step by step. Carefully watch the video tutorial here: <a href=\"https://www.youtube.com/watch?v=rZpEx8R9alw&feature=youtu.be\">Digilent EE Board Tutorial</a>. Finally, you will implement two RC circuits you simulated in Simulation section on the EE board.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 2", number=2,
                         text_input="Now build the circuit in Fig. 3 on your board. Use the AWG module to create an input square wave at 50 Hz. Run both the input "+
                         "and output signals to the oscilloscope (on different channels). You should be able to watch your capacitor charging and discharging. We will "+
                         "be learning in class that this first order circuit is governed by a time constant, \(\\tau=RC\). We will also be learning that the capacitor will "+ 
                         "charge 63% of the way from its initial to its final value in one time constant. Calculate the time constant using your resistor and capacitor "+ 
                         "values. Now, for comparison, measure how much time it takes for your capacitor charges to 63%. You might like to use the 'cursor' feature "+
                         "on your oscilloscope to help you measure exactly. You shall follow the same procedure with a second circuit shown in Fig. 3 but with \(R=1k\\Omega\), \(C=0.1\\mu F\). "+
                         "Go to the Results section for further instructions.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=digilent_board_hardware,
                           name="digilent board hardware 3", number=3,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab02/fig02.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_hardware_element(hardware=digilent_board_hardware,
                           name="digilent board hardware 4", number=4,
                           text_input="Figure 3",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')

    # Digilent board Intro Results
    digilent_board_results = add_results(lab=digilent_board_intro, name="Digilent Board Intro Results")

    add_results_questions(results=digilent_board_results,
                          question="Calculate the time constant using your resistor and capacitor values. Now, for comparison, measure how much time it takes for your capacitor charges to 63%. Ideally, "+
                          "this time should be exactly equal to your RC time constant but more likely than not, there will be some error. What are the sources of error?",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=digilent_board_results,
                          question="For two complete cycles of the square pulse signal, show ONE graph with the pulse input versus time plot, and the voltage across the capacitor versus time plot from EE board.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=digilent_board_results,
                          question="For the second circuit, show ONE graph with the pulse input, simulated capacitor voltage, and hardware capacitor voltage versus time (in other words, x-axis will be time "+
                          "and y-axis will include the pulse input, simulated capacitor voltage, and hardware capacitor voltage). Do the simulated and hardware capacitor voltage match exactly? If not, why?",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=digilent_board_results,
                          question="Show ONE graph with capacitor voltages versus time from both circuits of EE board. Comment on their trends.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=digilent_board_results,
                          question="You must include the answers to the above questions in your report.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=digilent_board_results,
                          question="Write a standard report as specified in the syllabus. "+
                          "Explain your work with the detailed calculations, observations, and analysis.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=digilent_board_results,
                          question="Submit the report to our <a href=\"https://blackboard.temple.edu\">blackboard</a> before the next lab (see syllabus for submission guideline). ",
                          answer_text="",
                          answer_type='text')

    # Digilent board Intro using RC circuit lab test

    digilent_board_lab_test = add_lab_test(lab=digilent_board_intro, name="Digilent Board Intro Lab Test")

                        
    add_lab_test_element(labtest=digilent_board_lab_test, name="digilent lab test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab02/fig03.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=digilent_board_lab_test, name="digilent lab test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=digilent_board_lab_test, name="digilent lab test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab02/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=digilent_board_lab_test, name="digilent lab test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

 
    add_lab_test_question(labtest=digilent_board_lab_test,
                             question="Figure numbers are specific to the test. Refer to Fig. I what would be the initial voltage of the capacitor when the switch is just closed?",
                             answer_one="12V", answer_two="4V",
                             answer_three="6V", answer_four="2V",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=digilent_board_lab_test,
                             question="Refer to the circuit in Fig. I. At t=0.6 ms, what would be the capacitor voltage?",
                             answer_one="8.1V", answer_two="6.1V",
                             answer_three="9.1V", answer_four="8.9V",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=digilent_board_lab_test,
                             question="Refer to the circuit in Fig. II. Given, Vs = 6V, R = 5\(\\Omega\), C = 10 \(\\mu\)F. Suppose, after a long time, if the charging battery is removed and the capacitor "+
                             "is immediately connected across the 5 ohms resistor, what will be the initial value of the discharge current?",
                             answer_one="0A", answer_two="1.2A",
                             answer_three="0.6A", answer_four="0.3A",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=digilent_board_lab_test,
                             question="Refer to the circuit in Fig. II. Given, Vs = 6V, R = 5\(\\Omega\), C = 10 \(\\mu\)F. What will be the charging current at the instant t = 50 microseconds? Use the charging current formula.",
                             answer_one="0.368A", answer_two="0.6A",
                             answer_three="0.4416A", answer_four="1.2A",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=digilent_board_lab_test,
                             question="Refer to the circuit in Fig. II. Assume that initial capacitor voltage is zero. When the capacitor in the RC circuit above reaches its maximum voltage, which of the following statements is FALSE? ",
                             answer_one="the voltage across the capacitor is at its maximum", answer_two="the voltage across the resistor is zero",
                             answer_three="the sum of the voltages across the capacitor and resistor is equal to the initial voltage across the capacitor", answer_four="the sum of the voltages across the capacitor and resistor is equal to the initial voltage across the resistor",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")


    # Print out what we have added to the user.
    #for c in Course.objects.all():
    #    for l in Laboratory.objects.filter(course=c):
    #        print "- {0} - {1}".format(str(c), str(l))
            

    # Add labpermissions for new lab for each user 
    for u in User.objects.all():
        add_new_lab_permission(user=u, lab=digilent_board_intro)
    
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
