import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
-EE Science II Course

LABORATORIES:
-
'''

    ###
    # EE Science II Lab 5: Frequency Response of a Second Order Filter
    ###
def populate(ee_science_ii):
    second_filters_freq = add_lab(course=ee_science_ii, name="Frequency Response of a Second Order Filter",
                                  start_date=timezone.now(), due_date=timezone.now(),
                                  lab_number=5)
    add_lab_objective(lab=second_filters_freq,
                      objective="The purpose of this week's lab is to build a second order filter and "+
                      "analyze its frequency response. We shall only explore the amplitude response of the filter for a range of frequencies. "+
                      "This lab includes pre-lab of simulating filters. You are expected to simulate the circuit before coming to the lab.")


    # Frequency Response of a Second Order Filter Theory 
    fsof_theory = add_theory(lab=second_filters_freq, name="Frequency Response of a Second Order Filter Theory")
    

    add_theory_element(theory=fsof_theory, name="fsof theory 1", number=1,
                       text_input="",
                       image_input="VLA/courses/EE_Science_II/Lab05/fig01.jpg", equation_input="", video_input="", element_type='image')

    add_theory_element(theory=fsof_theory, name="fsof theory 2", number=2,
                       text_input="Figure 1: A series RLC Circuit",
                       image_input=None, equation_input="", video_input="", element_type='caption')   

    add_theory_element(theory=fsof_theory, name="fsof theory 3", number=3,
                      text_input="Consider the series RLC circuit in Fig. 1 where a sine input Vin(t) is applied. The output voltage Vout(t)  is measured across the capacitor. "+
                      "The output voltage can be written as: "+
                       "\(V_{out}=(\\frac{\\frac{1}{j\\omega C}}{R+\\frac{1}{j\\omega C}+j\\omega L})V_{in}=( \\frac{\\frac{1}{j\\omega C}}{R+j(\\frac{1}{j\\omega C}-\\omega L)})V_{in}\)",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')


    add_theory_element(theory=fsof_theory, name="fsof theory 4", number=4,
                       text_input=" At resonance, we have \(\\frac{1}{\\omega C}-\\omega L=0\)  which gives \(\\omega_R=\\frac{1}{\\sqrt{LC}}\) , where \(\\omega_{R}\)  is called resonant frequency. "+
                       "RLC circuits are resonant circuits, as the energy in the system resonates between the inductor "+
                       "and capacitor. At resonant frequency, the voltage across the resistor becomes maximum. A series RLC circuit can be used as a filter. The cutoff frequency for the series RLC filter given "+
                       "here can be calculated using \({{f}_{c}}=\\frac{1}{2\pi \\sqrt{LC}}\). This review will help you take the test and write the lab report.",
                       image_input=None, equation_input="", video_input="", element_type='text')



    # Frequency Response of a Second Order Filter theory test
    fsof_theory_test = add_theory_test(lab=second_filters_freq, name="Frequency Response of a Second Order Filter Theory Test")

                        
    add_theory_test_element(theorytest=fsof_theory_test, name="fsof theory test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab05/fig01.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=fsof_theory_test, name="fsof theory test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=fsof_theory_test, name="fsof theory test element 3", number=3,
                      text_input="Note: figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="",
                      element_type='text')


   
    add_theory_test_question(theorytest=fsof_theory_test,
                             question="Consider the series RLC circuit in Fig. I. A sinusoidal input voltage is applied. Given, L=4mH and C =1nF. What is the resonant angular frequency? ",
                             answer_one="1M rad/s", answer_two="0.5M rad/s",
                             answer_three="2M rad/s", answer_four="4M rad/s",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=fsof_theory_test,
                             question="Refer to the series RLC circuit in Fig. I. Given, \(V_{in}(t)=50cos(\\omega t + 30^0)\), R=25 \(\\Omega\) , C=50\(\\mu\) F, and L=20mH. What is the impedance of the circuit at f=60Hz?",
                             answer_one="50+j45.51\(\\Omega\)", answer_two="50-j45.51\(\\Omega\)",
                             answer_three="25-j45.51\(\\Omega\)", answer_four="25+j45.51\(\\Omega\)",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=fsof_theory_test,
                             question="Refer to the series RLC circuit in Fig. I. Given, \(V_{in}(t)=50cos(\\omega t + 30^0)\), R=25 \(\\Omega\) , C=50\(\\mu\) F, and L=20mH. What is the current amplitude at f=60Hz?",
                             answer_one="0.96 A", answer_two="0.48 A",
                             answer_three="0.24 A", answer_four="1.2 A",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=fsof_theory_test,
                             question="Refer to the series RLC circuit in Fig. I. Given, \(V_{in}(t)=50cos(\\omega t + 30^0)\), R=25 \(\\Omega\) , C=50\(\\mu\) F, and L=20mH. For what frequency, this filter will allow the input signal to pass?",
                             answer_one="<200 Hz", answer_two="<159.2 Hz",
                             answer_three=">159.2 Hz", answer_four=">259.2 Hz",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=fsof_theory_test,
                             question="Refer to the series RLC circuit in Fig. I. Given, \(V_{in}(t)=50cos(\\omega t + 30^0)\), R=25 \(\\Omega\) , C=50\(\\mu\) F, and L=20mH. At resonant frequency, which will be true for the current through the resistor?",
                             answer_one="The current will be minimum", answer_two="The current will be maximum",
                             answer_three="The current will not change", answer_four="The current will flow in opposite direction compared to other frequency",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    # Frequency Response of a Second Order Filter Simulation
    fsof_simulation = add_simulation(lab=second_filters_freq, name="Frequency Response of a Second Order Filter Simulation")
    
    add_simulation_element(simulation=fsof_simulation,
                           name="fsof intro simulation 1", number=1,
                           text_input="Using a circuit simulator (for example, Multisim), build the circuit in Fig. 2. Allow Vin to be a 1V 2kHz sine wave. Let R=1500, C=4.7nF, and L=1mH. "+
                           "Run your simulation (5ms should be enough) and determine the amplitude of the output cosine. Repeat this process for the following frequencies: f=2k, 5k, 10k, 20k, "+
                           "30k, 40k, 50k, 60k, 70k, 80k, 90k, 100k, 200k, 300kHz. Make a plot with frequency on the x-axis and the Vout amplitude on the y-axis using Matlab/Octave/Excel. "+
                           "What type (e.g. low pass, high pass, band pass, etc.) of filter is this? In the beginning of the lab, you must submit: Vout amplitude versus frequency plot.(use circuit comparator for circuit with 2k Hz)",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=fsof_simulation,
                           name="fsof intro simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab05/fig01.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=fsof_simulation,
                           name="fsof intro simulation 3", number=3,
                           text_input="Figure 2",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
    
                      

    # Frequency Response of a Second Order Filter Hardware
    fsof_hardware = add_hardware(lab=second_filters_freq, name="Frequency Response of a Second Order Filter Hardware")

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 1", number=1,
                         text_input="<h4>Part 1. FILTER 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 2", number=2,
                         text_input="Using your Digilent EE board, build the circuit from the pre-lab (see Fig. 3). Generate a 1V 1kHz sine input, "+
                         "apply it as Vin, and measure the amplitude of Vout. Do this measurement for all of the frequencies in the pre-lab : 2k, 5k, 10k, 20k, 30k, 40k, "+
                         "50k, 60k, 70k, 80k, 90k, 100k, 200k, 300kHz. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 3", number=3,
                         text_input="<h4>Part 1. Questions:</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 4", number=4,
                         text_input="a. Create a plot of Vout versus f and superimpose it on the pre-lab plot.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 5", number=5,
                         text_input="b. How well do they agree?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 6", number=6,
                         text_input="c. Compare the voltage in the resonant frequency from Pre-lab and Digilent EE board.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware,
                           name="fsof intro simulation 7", number=7,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab05/fig01.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_hardware_element(hardware=fsof_hardware,
                           name="fsof intro hardware 8", number=8,
                           text_input="Figure 3",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')


    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 9", number=9,
                         text_input="<h4>Part 2. FILTER 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="first order filters hardware 10", number=10,
                         text_input="Design and build a first order RC low-pass filter with the same cutoff frequency as the filter 1 circuit. "+
                         "Measure the Vout at all the same frequencies as with Filter 1 and superimpose the frequency plot with that of Filter 1.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 11", number=11,
                         text_input="<h4>Part 2. Questions:</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 12", number=12,
                         text_input="a. Create a plot of Vout versus f for filter 1 and superimpose it on filter 2 response.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 13", number=13,
                         text_input="b. How are the two filters similar? ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 14", number=14,
                         text_input="c. How are they different? ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 15", number=15,
                         text_input="d. Which is the better filter? In what way is it better?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 16", number=16,
                         text_input="<h4>Part 3. FILTER 3</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="first order filters hardware 17", number=17,
                         text_input="Repeat the steps for Filter 1 but using R=100\(\\Omega\) .",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 18", number=18,
                         text_input="<h4>Part 3. Questions:</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 19", number=19,
                         text_input="a. Create a plot of Vout versus f for filter 1 and superimpose it on filter 2 response.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fsof_hardware, name="fsof board hardware 20", number=20,
                         text_input="b. How does the filter response for this filter differ from that of filter 1?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    

    # Frequency Response of a Second Order Filter Results
    fsof_results = add_results(lab=second_filters_freq, name="Frequency Response of a Second Order Filter Results")

    add_results_questions(results=fsof_results,
                          question="Write a standard report as specified in the syllabus. "+
                          "Explain your work with the detailed calculations, observations, and analysis.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=fsof_results,
                          question="In your report, you must include the answers to the questions. The questions were in Hardware section of this lab manual.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=fsof_results,
                          question="Submit the report to our <a href=\"https://blackboard.temple.edu\">blackboard</a> before the next lab (see syllabus for submission guideline).",
                          answer_text="",
                          answer_type='text')

    # Frequency Response of a Second Order Filter lab test
    fsof_lab_test = add_lab_test(lab=second_filters_freq, name="Frequency Response of a Second Order Filter Lab Test")

                        
    add_lab_test_element(labtest=fsof_lab_test, name="fsof lab test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab05/fig01.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=fsof_lab_test, name="fsof lab test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=fsof_lab_test, name="fsof lab test element 3", number=3,
                      text_input="Note: figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="",
                      element_type='text')


   
    add_lab_test_question(labtest=fsof_lab_test,
                             question="Consider the series RLC circuit in Fig. I. A sinusoidal input voltage is applied. Given, L=4mH and C =1nF. What is the resonant angular frequency? ",
                             answer_one="2M rad/s", answer_two="1M rad/s",
                             answer_three="0.5M rad/s", answer_four="4M rad/s",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=fsof_lab_test,
                             question="Refer to the series RLC circuit in Fig. I. Given, \(V_{in}(t)=50cos(\\omega t + 30^0)\), R=25 \(\\Omega\) , C=50\(\\mu\) F, and L=20mH. What is the impedance of the circuit at f=60Hz?",
                             answer_one="50+j45.51\(\\Omega\)", answer_two="25-j45.51\(\\Omega\)",
                             answer_three="50+j45.51\(\\Omega\)", answer_four="25+j45.51\(\\Omega\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=fsof_lab_test,
                             question="Refer to the series RLC circuit in Fig. I. Given, \(V_{in}(t)=50cos(\\omega t + 30^0)\), R=25 \(\\Omega\) , C=50\(\\mu\) F, and L=20mH. What is the current amplitude at f=60Hz?",
                             answer_one="0.24 A", answer_two="0.96 A",
                             answer_three="0.48 A", answer_four="1.2 A",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=fsof_lab_test,
                             question="Refer to the series RLC circuit in Fig. I. Given, \(V_{in}(t)=50cos(\\omega t + 30^0)\), R=25 \(\\Omega\) , C=50\(\\mu\) F, and L=20mH. For what frequency, this filter will allow the input signal to pass?",
                             answer_one="<200 Hz", answer_two=">159.2 Hz",
                             answer_three="<159.2 Hz", answer_four=">259.2 Hz",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=fsof_lab_test,
                             question="Refer to the series RLC circuit in Fig. I. Given, \(V_{in}(t)=50cos(\\omega t + 30^0)\), R=25 \(\\Omega\) , C=50\(\\mu\) F, and L=20mH. At resonant frequency, which will be true for the current through the resistor?",
                             answer_one="The current will be maximum", answer_two="The current will be mminimum",
                             answer_three="The current will not change", answer_four="The current will flow in opposite direction compared to other frequency",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")


    # Print out what we have added to the user.
    #for c in Course.objects.all():
    #    for l in Laboratory.objects.filter(course=c):
    #        print "- {0} - {1}".format(str(c), str(l))
            

    # Add labpermissions for new lab for each user 
    for u in User.objects.all():
        add_new_lab_permission(user=u, lab=second_filters_freq)
    
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
