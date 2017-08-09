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
    # EE Science II Lab 3: Introduction to First Order Filters
    ###
def populate(ee_science_ii):
    first_order_filters = add_lab(course=ee_science_ii, name="Introduction to First Order Filters",
                                  start_date=timezone.now(), due_date=timezone.now(),
                                  lab_number=3)
    add_lab_objective(lab=first_order_filters,
                      objective="The purpose of this week's lab is to build and test your first high pass or low pass filter. Filters are circuits that allow certain frequencies "+
                      "to pass through while blocking others. Here you will be building two circuits "+
                      "and determining what types of filters they are and what ranges of frequencies they allow to pass. "+
                      "This lab includes pre-lab consisting simulation of filters. You are expected to simulate before coming to the lab.")


    # Introduction to First Order Filters Theory 
    fof_theory = add_theory(lab=first_order_filters, name="Introduction to First Order Filters Theory")
    
    add_theory_element(theory=fof_theory, name="fof theory 1", number=1,
                       text_input="In this section, we shall review the concepts of sinusoid functions, phasors, "+
                       "and a brief description about filters. The most common alternating waveform in AC circuit is the sinusoidal waveform. "+
                       "The sinusoidal waveform can be expressed mathematically by:\(x(t)=X_M sin(\\omega t+\\theta)\), where where, x(t) could "+
                       "represent either v(t) or i(t). \(X_M\) is the amplitude or peak value, \(\\omega\)  is angular frequency, \(\\theta)\)  is the phase angle. "+
                       "The angular frequency can be expressed as: \(\\omega=2\pi f= \\frac{2\pi}{T}\) , where f is the frequency and T is period.",
                       image_input=None, equation_input="", video_input="", element_type='text')

  
    add_theory_element(theory=fof_theory,name="fof theory 2", number=2,
                      text_input="However, working with sinuosoid functions can be tedious. To overcome this, we use phasors. A phasor essentially "+
                      "represents a waveform as a single complex number, assuming the frequency is known. By using phasor, we convert the trigonometric part "+
                      "of the problem into an algebraic one. To establish the idea of phasor, we use Euler's identity which relates time-varying sinusoidal functions "+
                      "and complex numbers. The Euler's identity is: \(e^{j\\omega t}=cos \\omega t + j sin\\omega t\), where \(j=\\sqrt{-1}\).",
                      image_input='', equation_input="", video_input="", 
                      element_type='text')

    add_theory_element(theory=fof_theory, name="fof theory 3", number=3,
                      text_input="Now that we get some introductory idea about sinusoids and phasors, let us have a brief discussion about electronic filters. "+
                      "Consider the RC circuit in Fig. 1. An RC circuit can be used as a filter. Depending on where we apply the sinusoid input and where we capture the output signal, a series "+
                      "combination of capacitor and resistor can act as low pass filter or high pass filter. The low pass filter attenuates the output signal at "+
                      "higher frequency than cutoff frequency, and the high pass filter attenuates the output signal at lower frequency than cutoff frequency. ",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')

    add_theory_element(theory=fof_theory, name="fof theory 4", number=4,
                       text_input="",
                       image_input="VLA/courses/EE_Science_II/Lab03/fig04.jpg", equation_input="", video_input="", element_type='image')

    add_theory_element(theory=fof_theory, name="fof theory 5", number=5,
                       text_input="Figure 1",
                       image_input=None, equation_input="", video_input="", element_type='caption')

    add_theory_element(theory=fof_theory, name="fof theory 6", number=6,
                       text_input="The cutoff frequency can be calculated using \(f_c=\\frac{1}{2\pi RC}\)"+
                       "We can see for a series RC circuit the cutoff frequency is inversely proportional to time constant \(\\tau \) of the circuit. "+
                       "This review will help you take the test and write the lab report.",
                       image_input=None, equation_input="", video_input="", element_type='text')



    # Introduction to First Order Filters theory test
    fof_theory_test = add_theory_test(lab=first_order_filters, name="Introduction to First Order Filters Theory Test")

                        
    add_theory_test_element(theorytest=fof_theory_test, name="fof theory test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab03/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=fof_theory_test, name="fof theory test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=fof_theory_test, name="fof theory test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab03/fig05.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=fof_theory_test, name="fof theory test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

   
    add_theory_test_question(theorytest=fof_theory_test,
                             question="Given that the voltage  \(v(t)=120cos(314t+\\frac{3\pi}{4})\), what is the period (in millisecond) and phase angle (in degree)?",
                             answer_one="50 ms, 45 degree", answer_two="20 ms, 45 degree",
                             answer_three="20 ms, 135 degree", answer_four="2 ms, 135 degree",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=fof_theory_test,
                             question="Suppose, there are two branch currents in a network as: \(i_1(t)=2sin(377t+45^0)\) and \(i_2(t)=0.5cos(377t+10^0)\). "+
                             "What is the phase angle (in degree) by which \(i_1(t)\) leads \(i_2(t)\)?",
                             answer_one="45", answer_two="55",
                             answer_three="-55", answer_four="35",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=fof_theory_test,
                             question="Figure numbers are specific to this test. Refer to the circuit in Fig. I, suppose that the time constant \(\\tau\)  "+
                             "is 1/3.14 ms. What would be the cutoff frequency for this filter circuit?",
                             answer_one="5 kHz", answer_two="0.5 MHz",
                             answer_three="5 MHz", answer_four="0.5 kHz",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=fof_theory_test,
                             question="For the circuit in Fig. I, suppose that the time constant \(\\tau\) is 1/3.14 ms. Which frequency will this circuit block?",
                             answer_one="<0.5 kHz", answer_two=">0.5 kHz",
                             answer_three="<0.1 kHz", answer_four="0.1 to 0.4 kHz",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=fof_theory_test,
                             question="Refer to the circuit in Fig. II, suppose that the time constant \(\\tau\)  is 1/3.14 ms. What would be the cutoff frequency for this filter circuit?",
                             answer_one="<0.5 kHz", answer_two=">0.5kHz",
                             answer_three=">0.8 kHz", answer_four=">0.1 kHz",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")

    # Introduction to First Order Filters Simulation
    fof_simulation = add_simulation(lab=first_order_filters, name="Introduction to First Order Filters Simulation")
    
    add_simulation_element(simulation=fof_simulation,
                           name="fof intro simulation 1", number=1,
                           text_input="Using a circuit similator, build the following circuit. Allow the input to be a 1V sine wave " +
                           "and the output to be the voltage across the capacitor. This is exactly the same circuit that " +
                           "you worked with in Lab 2 except we are using a sine wave for input instead of a square wave. " +
                           "With the sine wave frequency equal to 10Hz, determine the peak voltage of the output sine wave. " +
                           "Then, keeping the input amplitude at 1V, repeat this measurement for the following frequencies: " +
                           "10Hz, 20Hz, 50Hz, 100Hz, 200Hz, 500Hz, 1kHz, 2kHz. <b> Finally make a plot of the amplitude of the " +
                           "output signal versus frequency using Matlab/Excel/Octave. Bring this plot with you to lab. What kind of filter have you built?(use circuit comparator for  this circuit with 10Hz)</b>",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=fof_simulation,
                           name="fof intro simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab03/fig02.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=fof_simulation,
                           name="fof intro simulation 3", number=3,
                           text_input="Figure 2",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
  
                      

    # Introduction to First Order Filters Hardware
    fof_hardware = add_hardware(lab=first_order_filters, name="Introduction to First Order Filters Hardware")

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 1", number=1,
                         text_input="<h4>Part 1. FILTER 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 2", number=2,
                         text_input="In this section you will repeat the steps of the simualtion on your Digilent board. Build the circuit in Fig. 3. Using a sine " +
                         "wave input, measure the peak voltage of the output sine wave and create a plot of peak amplitude versus " +
                         "frequency (use the same frequencies as the simulation).",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 3", number=3,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab03/fig02.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 4", number=4,
                         text_input="Figure 3",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 5", number=5,
                         text_input="<h4>Part 1. Questions:</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 6", number=6,
                         text_input="a. Overlay this plot with the pre-lab plot. Do they agree?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 7", number=7,
                         text_input="b. If not, how far off are they? Why? ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 8", number=8,
                         text_input="c. What kind of filter have you built?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 9", number=9,
                         text_input="d. What are the voltage at cutoff frequency from simulation and hardware?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 10", number=10,
                         text_input="<h4>Part 2. FILTER 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 11", number=11,
                         text_input="Repeat the steps of the previous section with the circuit shown Fig. 4. The output voltage is the " +
                         "voltage across the resistor. In this case, use the following range of frequencies: 100Hz, 200Hz, 500Hz, 1kHz, " +
                         "2kHz, 5kHz, 10kHz, 20kHz.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 12", number=12,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab03/fig03.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 13", number=13,
                         text_input="Figure 4",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 14", number=14,
                         text_input="<h4>Part 2. Questions:</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 15", number=15,
                         text_input="a. What kind of filter have you built? ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 16", number=16,
                         text_input="b. Overlay the plot for peak amplitude versus frequency from simulation and hardware. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 17", number=17,
                         text_input="c. Do they agree? If not, how far off are they? Why? ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=fof_hardware, name="fof board hardware 18", number=18,
                         text_input="d. What are the voltages at cutoff frequency from simulation and hardware?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    

    # Introduction to First Order Filters Results
    fof_results = add_results(lab=first_order_filters, name="Introduction to First Order Filters Results")

    add_results_questions(results=fof_results,
                          question="Write a standard report as specified in the syllabus. "+
                          "Explain your work with the detailed calculations, observations, and analysis.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=fof_results,
                          question="In your report, you must include the answers to the questions. The questions were in Hardware section.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=fof_results,
                          question="Submit the report to our <a href=\"https://blackboard.temple.edu\">blackboard</a> before the next lab (see syllabus for submission guideline).",
                          answer_text="",
                          answer_type='text')

    # Introduction to First Order Filters lab test

    fof_lab_test = add_lab_test(lab=first_order_filters, name="Introduction to First Order Filters Lab Test")

                        
    add_lab_test_element(labtest=fof_lab_test, name="fof lab test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab03/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=fof_lab_test, name="fof lab test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=fof_lab_test, name="fof lab test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab03/fig05.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=fof_lab_test, name="fof lab test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

 
    add_lab_test_question(labtest=fof_lab_test,
                             question="Given that the voltage  \(v(t)=120cos(314t+\\frac{3\pi}{4})\), what is the period (in millisecond) and phase angle (in degree)?",
                             answer_one="50 ms, 45 degree", answer_two="2 ms, 135 degree",
                             answer_three="20 ms, 45 degree", answer_four="20 ms, 135 degree",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=fof_lab_test,
                             question="Suppose, there are two branch currents in a network as: \(i_1(t)=2sin(377t+45^0)\) and \(i_2(t)=0.5cos(377t+10^0)\). "+
                             "What is the phase angle (in degree) by which \(i_1(t)\) leads \(i_2(t)\)?",
                             answer_one="45", answer_two="-55",
                             answer_three="55", answer_four="35",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=fof_lab_test,
                             question="Figure numbers are specific to this test. Refer to the circuit in Fig. I, suppose that the time constant \(\\tau\)  is 1/3.14 ms. What would be the cutoff frequency for this filter circuit?",
                             answer_one="5 kHz", answer_two="0.5 kHz",
                             answer_three="5 MHz", answer_four="0.5 MHz",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=fof_lab_test,
                             question="For the circuit in Fig. I, suppose that the time constant \(\\tau\) is 1/3.14 ms. Which frequency will this circuit block?",
                             answer_one="<0.5 kHz", answer_two="0.1 to 0.4 kHz",
                             answer_three="<0.1 kHz", answer_four=">0.5 kHz",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=fof_lab_test,
                             question="Refer to the circuit in Fig. II, suppose that the time constant \(\\tau\)  is 1/3.14 ms. What would be the cutoff frequency for this filter circuit?",
                             answer_one=">0.5 kHz", answer_two="<0.5kHz",
                             answer_three=">0.8 kHz", answer_four=">0.1 kHz",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")



    # Print out what we have added to the user.
    #for c in Course.objects.all():
    #    for l in Laboratory.objects.filter(course=c):
    #        print "- {0} - {1}".format(str(c), str(l))
            

    # Add labpermissions for new lab for each user 
    for u in User.objects.all():
        add_new_lab_permission(user=u, lab=first_order_filters)
    
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
