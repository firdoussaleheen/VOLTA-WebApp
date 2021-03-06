import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
-EE Science II Course

LABORATORIES:

'''

    ###
    # EE Science II Lab 8: Bass Booster Implementation using Active Filters
    ###
def populate(ee_science_ii):
    bass_booster = add_lab(course=ee_science_ii, name="Bass Booster Implementation using Active Filters",
                                  start_date=timezone.now(), due_date=timezone.now(),
                                  lab_number=8)
    add_lab_objective(lab=bass_booster,
                      objective="The bass booster is a type of stereo amplifier that amplifies the low frequency audio signal. "+
                      "The purpose of this week's lab is to implement a bass booster using active filters. This lab includes a pre-lab.")


    # Bass Booster Implementation using Active Filters Theory 
    bb_theory = add_theory(lab=bass_booster, name="Bass Booster Implementation using Active Filters Theory")
    
    add_theory_element(theory=bb_theory, name="bb theory 1", number=1,
                       text_input="The stereo amplifier is a filter which isolates specific frequencies "+
                       "(i.e. treble, bass), and then amplifies those signals. A bass booster amplifies the "+
                       "low frequency audio signal. The bass booster circuit can be implemented using active filter.",
                       image_input=None, equation_input="", video_input="", element_type='text')

    add_theory_element(theory=bb_theory, name="bb theory 2", number=2,
                       text_input="An active filter uses active components (i.e. amplifier, Op-Amp). For building a bass booster, "+
                       "the circuit requires to pass the low frequency signal, and amply the signal as well. The booster can be "+
                       "implemented using an inverting Op-Amp amplifier with a parallel RC combination as feedback element. Fig. 1 shows "+
                       "the topology of an inverting Op-Amp amplifier with a parallel RC combination as feedback element. The resistor "+
                       "network in the topology works as amplifier. The RC network acts as a low pass filter.",
                       image_input=None, equation_input="", video_input="", element_type='text')

    add_theory_element(theory=bb_theory, name="bb theory 3", number=3,
                       text_input="",
                       image_input='VLA/courses/EE_Science_II/Lab08/fig01.jpg', equation_input="", video_input="",
                       element_type='image')

    add_theory_element(theory=bb_theory, name="bb theory 4", number=4,
                       text_input="Figure 1",
                       image_input=None, equation_input="", video_input="", 
                       element_type='caption')

    add_theory_element(theory=bb_theory, name="bb theory 5", number=5,
                       text_input="We can express the transfer function of this circuit as follows:",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')

    add_theory_element(theory=bb_theory, name="bb theory 6", number=6,
                       text_input="",
                       image_input=None, equation_input="\\frac{V_{out}}{V_{in}}=-\\frac{Z_2}{Z_1}=-(\\frac{R_2}{R_1})\\frac{1}{1+j\\omega R_2 C_1}", video_input="", 
                       element_type='latex')

    add_theory_element(theory=bb_theory, name="bb theory 7", number=7,
                       text_input="where \(Z_2=R_2||\\frac{1}{j\\omega C_1}\) is the impedance in the feedback. "+
                       "The gain of the filter can be found by taking the magnitude of \(\\frac{V_{out}}{V_{in}}\). The cutoff angular frequency of this filter is "+
                       "\(\\omega_0=\\frac{1}{R_2 C_1}\). This review will help you in performing pre-lab and test.",
                       image_input=None, equation_input="", video_input="", element_type='text')

   

    # Bass Booster Implementation using Active Filters theory test
    bb_theory_test = add_theory_test(lab=bass_booster, name="Bass Booster Implementation using Active Filters Theory Test")

                        
    add_theory_test_element(theorytest=bb_theory_test, name="bb theory test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab08/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=bb_theory_test, name="bb theory test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=bb_theory_test, name="bb theory test element 3", number=3,
                      text_input="Note: Figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')

    add_theory_test_question(theorytest=bb_theory_test,
                             question="Consider the circuit in Fig. I. What is the absolute value of gain when \(\\omega=0\)?",
                             answer_one="1", answer_two="2",
                             answer_three="3", answer_four="4",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")


    add_theory_test_question(theorytest=bb_theory_test,
                             question="Consider the circuit in Fig. I. What is the magnitude of impedance in the feedback part of the circuit when \(\\omega=1000\) rad/s?",
                             answer_one="800 \(\\Omega\)", answer_two="850 \(\\Omega\)",
                             answer_three="400 \(\\Omega\)", answer_four="894 \(\\Omega\)",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")


    add_theory_test_question(theorytest=bb_theory_test,
                             question="Consider the circuit in Fig. I, where \(V_{in}=V_m cos\\omega t\). What type of filter is it?",
                             answer_one="High pass filter", answer_two="Low pass filter",
                             answer_three="Band pass filter", answer_four="Band stop filter",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=bb_theory_test,
                             question="Consider the circuit in Fig. I. What is the cutoff angular frequency \((\omega_0))\ of the circuit?",
                             answer_one="100 rad/s", answer_two="500 rad/s",
                             answer_three="50 rad/s", answer_four="5000 rad/s",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=bb_theory_test,
                             question="Consider that the circuit in Fig. I is used in both stages of a two-stage cascaded amplifier. What will be the absolute value of gain when \(\\omega=0\)?",
                             answer_one="1", answer_two="2",
                             answer_three="3", answer_four="4",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")
   
  
    # Bass Booster Implementation using Active Filters Simulation
    bb_simulation = add_simulation(lab=bass_booster, name="Bass Booster Implementation using Active Filters Simulation")

    add_simulation_element(simulation=bb_simulation,
                           name = "Bass Booster Implementation using Active Filters simulation 1", number=1,
                           text_input="Bring a preliminary circuit design that meets the design requirements shown below:", 
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')

    add_simulation_element(simulation=bb_simulation,
                           name = "Bass Booster Implementation using Active Filters simulation 2", number=2,
                           text_input="For \(f\leq 200\) Hz, the gain should be minimum 4.", 
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')

    add_simulation_element(simulation=bb_simulation,
                           name = "Bass Booster Implementation using Active Filters simulation 3", number=3,
                           text_input="For \(200 < f < 200\) Hz, the gain can be between 4 and 0.5.", 
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')

    add_simulation_element(simulation=bb_simulation,
                           name = "Bass Booster Implementation using Active Filters simulation 3", number=3,
                           text_input="For \(f \geq 700\) Hz, the gain must be maximum 0.5.", 
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')

    add_simulation_element(simulation=bb_simulation,
                           name = "Bass Booster Implementation using Active Filters simulation 4", number=4,
                           text_input="Both amplification and filtering are required to meet the above design "+
                           "criteria. Therefore, an active filter with Op-Amps will be a suitable solution. You may not get "+
                           "the desired high frequency rejection by using one filter. In that case, you need to design two-stage "+
                           "cascade filter. This means you have to design two filters, where the first filter output will be the input "+
                           "for the second filter. You should validate your design by testing it in Multisim using AC frequency sweep. "+
                           "To simulate, you may use u741 Op-Amp. If you need help with Op-Amp amplifier simulation, you can visit "+
                           "<a href=\"https://www.youtube.com/watch?v=vZA47ojNOLs\">Multisim simulation example:Inverting Op-Amp Amplifier</a>. "+
                           "Bring the following to the lab:", 
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')

    add_simulation_element(simulation=bb_simulation,
                           name = "Bass Booster Implementation using Active Filters simulation 5", number=5,
                           text_input="Derive the transfer function \(\\frac{V_{out}}{V_{in}}\)for your design circuit. Also, bring the AC frequency sweep simulation of your design circuit.", 
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')


                    

    
    # Bass Booster Implementation using Active Filters Hardware
    bb_hardware = add_hardware(lab=bass_booster, name="Bass Booster Implementation using Active Filters Hardware")
    
    add_hardware_element(hardware=bb_hardware, name="Bass Booster Implementation using Active Filters hardware 1", number=1,
                         text_input="Implement your design in EE board. For this lab, the part kit contains two dual, Op-Amp ICs -the TCA0372, and the RC4558. "+
                         "This means each IC has two Op-Amps packaged inside. You can find the datasheet for these ICs at: "+
                         "<a href=\"http://www.farnell.com/datasheets/1802317.pdf\"> TCA0372 Datasheet</a> and <a href = \"http://www.farnell.com/datasheets/1803516.pdf\">RC4558 Datasheet</a>. "+
                         "Figs. 2 and 3 show the pin connections for TCA0372 and RC4558.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=bb_hardware, name="Bass Booster Implementation using Active Filters hardware 2", number=2,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab08/fig02.jpg', equation_input="", video_input="", 
                         element_type='image')
    
    add_hardware_element(hardware=bb_hardware, name="Bass Booster Implementation using Active Filters hardware 3", number=3,
                         text_input="Figure 2: TCA0372 pin connection diagram",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')

    add_hardware_element(hardware=bb_hardware, name="Bass Booster Implementation using Active Filters hardware 4", number=4,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab08/fig03.jpg', equation_input="", video_input="", 
                         element_type='image')
    
    add_hardware_element(hardware=bb_hardware, name="Bass Booster Implementation using Active Filters hardware 5", number=5,
                         text_input="Figure 3: RC4558 pin connection diagram",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    
    add_hardware_element(hardware=bb_hardware, name="Bass Booster Implementation using Active Filters hardware 6", number=6,
                         text_input="For the TCA0372, Vcc (pin 2) would be connected to Vp+ and VEE (pin 4) would be connected to Vp-.  For the RC4558, Vcc+ (pin 8) should be connected to Vp+, "+
                         "and Vcc- (pin 4) would be connected to Vp-. Set your Vp+ voltage to +5V, and your Vp- to -5V. Note that your applied input or the output of the amplifier should not be "+
                         "more than the applied voltage in Vcc+ and Vcc-.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=bb_hardware, name="Bass Booster Implementation using Active Filters hardware 7", number=7,
                         text_input="Choose one of the op-amps on the dual op-amp ICs for building your bass booster. Apply 1Vpp sinusoidal input voltage. Observe the frequency response "+
                         "(magnitude of output voltage) of your designed circuit over the range of design frequencies.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=bb_hardware, name="Bass Booster Implementation using Active Filters hardware 8", number=8,
                         text_input="If you design a two-stage cascaded filter, build and test each stage at a time and then connect both stages. "+
                         "Proceeding this way would help debugging the complete circuit easily, if required. "+
                         "Finally, prove that your hardware implementation matches the simulation and meets the design requirements. "+
                         "Your lab kit contains a speaker. Can you hear anything if you connect the output signal to your speaker? Why or why not?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

     

    # Bass Booster Implementation using Active Filters Results
    bb_results = add_results(lab=bass_booster, name="Bass Booster Implementation using Active Filters Results")

    add_results_questions(results=bb_results,
                          question="Write a standard report as specified in the syllabus. "+
                          "Explain your work with the detailed calculations, observations, and analysis. In your report, you must include the answers to the questions in hardware section.",
                          answer_text="",
                          answer_type='text')
     
    add_results_questions(results=bb_results,
                          question="Submit the report to our <a href=\"https://blackboard.temple.edu\">blackboard</a> before the next lab (see syllabus for submission guideline).",
                          answer_text="",
                          answer_type='text')

    # Bass Booster Implementation using Active Filters lab test
    bb_lab_test = add_lab_test(lab=bass_booster, name="Bass Booster Implementation using Active Filters lab Test")

                        
    add_lab_test_element(labtest=bb_lab_test, name="bb lab test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab08/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=bb_lab_test, name="bb lab test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=bb_lab_test, name="bb lab test element 3", number=3,
                      text_input="Note: Figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')


    add_lab_test_question(labtest=bb_lab_test,
                     question="Consider the circuit in Fig. I. What is the absolute value of gain when \(\\omega=0\)?",
                     answer_one="2", answer_two="3",
                     answer_three="1", answer_four="4",
                     correct_answer_number=1,
                     correct_response="",
                     incorrect_response="")

    add_lab_test_question(labtest=bb_lab_test,
                             question="Consider the circuit in Fig. I. What is the magnitude of impedance in the feedback part of the circuit when \(\\omega=1000\) rad/s?",
                             answer_one="850 \(\\Omega\)", answer_two="894 \(\\Omega\)",
                             answer_three="800 \(\\Omega\)", answer_four="850 \(\\Omega\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")


    add_lab_test_question(labtest=bb_lab_test,
                             question="Consider the circuit in Fig. I, where \(V_{in}=V_m cos\\omega t\). What type of filter is it?",
                             answer_one="High pass filter", answer_two="Band pass filter",
                             answer_three="Low pass filter", answer_four="Band stop filter",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=bb_lab_test,
                             question="Consider the circuit in Fig. I. What is the cutoff angular frequency (\(\\omega_0)\) of the circuit?",
                             answer_one="100 rad/s", answer_two="50 rad/s",
                             answer_three="5000 rad/s", answer_four="500 rad/s",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=bb_lab_test,
                             question="Consider that the circuit in Fig. I is used in both stages of a two-stage cascaded amplifier. What will be the absolute value of gain when \(\\omega=0\)?",
                             answer_one="1", answer_two="2",
                             answer_three="3", answer_four="4",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")


    # Print out what we have added to the user.
    #for c in Course.objects.all():
    #    for l in Laboratory.objects.filter(course=c):
    #        print "- {0} - {1}".format(str(c), str(l))
            

    # Add labpermissions for new lab for each user 
    for u in User.objects.all():
        add_new_lab_permission(user=u, lab=bass_booster)
    
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
