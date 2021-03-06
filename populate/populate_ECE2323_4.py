import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
-EE Science II Course

LABORATORIES:

'''

    ###
    # EE Science II Lab 4: Step Response of a Second Order Filters
    ###
def populate(ee_science_ii):
    second_order_filters = add_lab(course=ee_science_ii, name="Step Response of a Second Order Filter",
                                  start_date=timezone.now(), due_date=timezone.now(),
                                  lab_number=4)
    add_lab_objective(lab=second_order_filters,
                      objective="The purpose of this week's lab is to build a second order filter and analyze its step response. "+
                      "This lab includes a pre-lab. You are expected to simulate a circuit before coming to the lab.")


    # Step Response of a Second Order Filter Theory 
    sof_theory = add_theory(lab=second_order_filters, name="Step Response of a Second Order Filter Theory")
    
    add_theory_element(theory=sof_theory, name="sof theory 1", number=1,
                       text_input="",
                       image_input="VLA/courses/EE_Science_II/Lab04/fig01.jpg", equation_input="", video_input="", element_type='image')

    add_theory_element(theory=sof_theory, name="sof theory 2", number=2,
                       text_input="Figure 1: A series RLC Circuit",
                       image_input=None, equation_input="", video_input="", element_type='caption')   

    add_theory_element(theory=sof_theory, name="sof theory 3", number=3,
                       text_input="Consider the series RLC circuit in Fig. 1 where a step input \(v_s(t)\) is applied. In order to find the output voltage \(v_c(t)\), first we obtain a second order differential equation: "+
                       "\(\\frac{{{d}^{2}}{{v}_{c}}(t)}{d{{t}^{2}}}+\\frac{R}{L}\\frac{d{{v}_{c}}(t)}{dt}+\\frac{1}{LC}{{v}_{c}}(t)=\\frac{1}{LC}{{v}_{s}}(t)\).",
                       image_input=None, equation_input="", video_input="", element_type='text')

  
    add_theory_element(theory=sof_theory,name="sof theory 4", number=4,
                      text_input="The solution of this equation consists of two parts: the complementary solution and the particular solution. "+
                      "Let us focus on the complementary solution. The form of this solution depends on the roots of the characteristic equation: "+
                      "\({{s}^{2}}+2\\zeta {{\\omega }_{0}}s+{{\\omega }_{0}}^{2}=0\)",
                      image_input='', equation_input="", video_input="", 
                      element_type='text')

    add_theory_element(theory=sof_theory, name="sof theory 5", number=5,
                      text_input="where \(\\zeta\) is called the damping ratio and \(\\omega_{0}\)  is called the undamped natural frequency or oscillating frequency. The roots of the quadratic equation are: "+
                      "\(s=-\\zeta {{\\omega }_{0}}\pm {{\\omega }_{0}}\\sqrt{{{\\zeta }^{2}}-1}\)",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')

    add_theory_element(theory=sof_theory, name="sof theory 6", number=6,
                      text_input="For example, for our series RLC circuit, the characteristic equation can be written as: "+
                      "\({{s}^{2}}+\\frac{R}{L}s+\\frac{1}{LC}=0\)",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')

    add_theory_element(theory=sof_theory, name="sof theory 7", number=7,
                      text_input="Then the damping ratio and oscillating frequency can be found as \(\\zeta =\\frac{R}{2}\\sqrt{\\frac{C}{L}}\) "+","
                      "\({{\\omega }_{0}}=\\frac{1}{\\sqrt{LC}}\). Depending on the value of the damping ratio, there can be three types of responses: Critically damped response (\(\\zeta=1\)), underdamped "+
                      "response (\(\\zeta<1\)), and overdamped response (\(\\zeta>1\)).",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')

    add_theory_element(theory=sof_theory, name="sof theory 8", number=8,
                      text_input="The three types of responses are shown in Fig. 2. This review will help you take the test and write the lab report.",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')

    add_theory_element(theory=sof_theory, name="sof theory 9", number=9,
                       text_input="",
                       image_input="VLA/courses/EE_Science_II/Lab04/fig05.jpg", equation_input="", video_input="", element_type='image')

    add_theory_element(theory=sof_theory, name="sof theory 10", number=10,
                       text_input="Figure 2: Underdamped, critically damped, and overdamped step responses",
                       image_input=None, equation_input="", video_input="", element_type='caption')


    # Step Response of a Second Order Filter theory test
    sof_theory_test = add_theory_test(lab=second_order_filters, name="Step Response of a Second Order Filter Theory Test")

                        
    add_theory_test_element(theorytest=sof_theory_test, name="sof theory test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab04/fig02.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=sof_theory_test, name="sof theory test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=sof_theory_test, name="sof theory test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab04/fig03.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=sof_theory_test, name="sof theory test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=sof_theory_test, name="sof theory test element 5", number=5,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab04/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=sof_theory_test, name="sof theory test element 6", number=6,
                      text_input="Figure III",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=sof_theory_test, name="sof theory test element 7", number=7,
                      text_input="Note: Figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')
   
    add_theory_test_question(theorytest=sof_theory_test,
                             question="Consider the series RLC circuit in Fig. I. A step input \(v_s(t)\) is applied. "+
                             "Given, L=4mH and C =1nF. Which value of the resistor will make the step response critically damped?",
                             answer_one="100\(\\Omega\)", answer_two="1k\(\\Omega\)",
                             answer_three="4k\(\\Omega\)", answer_four="10k\(\\Omega\)",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=sof_theory_test,
                             question="Refer to the series RLC circuit in Fig. I. A step input \(v_s(t)\) is applied. Given, R=1k\(\\Omega\) , C=1nF, and L=4mH. "+
                             "What would be the step response?",
                             answer_one="overdamped", answer_two="underdamped",
                             answer_three="critically damped", answer_four="superficially damped",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=sof_theory_test,
                             question="Refer to the series RLC circuit in Fig. I. A step input \(v_s(t)\) is applied. Given, R=1k\(\\Omega\) , C=1nF, and L=4mH. "+
                             "What is the oscillating frequency (in Hz) of the circuit?",
                             answer_one="79.6 Hz", answer_two="7.96 kHz",
                             answer_three="500 kHz", answer_four="100 kHz",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=sof_theory_test,
                             question="Refer to the series RLC circuit in Fig. I. A step input \(v_s(t)\) is applied. Given, R=1\(\\Omega\) , C=1\(\\mu\)F, and L=1mH. "+
                             "What will be the characteristic equation?",
                             answer_one="\(s^2+100s+10^9=0\)", answer_two="\(s^2+1000s+10^9=0\)",
                             answer_three="\(s^2+1000s+10^{-9}=0\)", answer_four="\(s^2+1000s+10=0\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=sof_theory_test,
                             question="Refer to the circuit in Fig. II, Suppose, this series RLC circuit has R=1.5 k\(\\Omega\), C=4.7 nF, and L=1 mH. "+
                             "Which one of Fig. III will be the step response?",
                             answer_one="ii", answer_two="iv",
                             answer_three="i", answer_four="iii",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")

    # Step Response of a Second Order Filter Simulation
    sof_simulation = add_simulation(lab=second_order_filters, name="Step Response of a Second Order Filter Simulation")
    
    add_simulation_element(simulation=sof_simulation,
                           name="sof intro simulation 1", number=1,
                           text_input="Using a circuit simulator (for example, Multisim), build the circuit in Fig. 3. For simulating the step response, "+
                           "a square wave input will be applied as a step input. Allow \(v_s(t)\)  to be a 1 kHz square wave with 1V "+
                           "amplitude (high voltage 1 and low voltage 0). Let R=100\(\\Omega\), C=4.7 nF, and L=1 mH. This is the first circuit to simulate. Run your "+
                           "simulation (1ms should be enough) and print out what the step response (i.e. \(v_c(t)\)) looks like. Using the cursors, determine the "+
                           "frequency of oscillation (i.e. the reciprocal of the time between peaks) and the time it takes for the oscillations to damp out.",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')

    add_simulation_element(simulation=sof_simulation,
                           name="sof intro simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab04/fig02.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=sof_simulation,
                           name="sof intro simulation 3", number=3,
                           text_input="Figure 3",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')

    add_simulation_element(simulation=sof_simulation,
                           name="sof intro simulation 4", number=4,
                           text_input="Then, repeat this process for a second circuit with R=1.5 k\(\\Omega\) keeping other parameters same. "+
                           "In this case, the circuit will not oscillate. Measure the rise time of the circuit. The rise time of the circuit is "+
                           "defined as the time it takes for the capacitor voltage to go from 10% to 90% of the applied voltage (step input voltage).",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')

    add_simulation_element(simulation=sof_simulation,
                           name="sof intro simulation 5", number=5,
                           text_input="You will submit the following in the beginning of the lab: "+
                           "For the first circuit, plot the step response ( \(v_c(t)\) versus t plot). "+
                           "Mention the frequency of oscillation and the time it takes for the oscillations to damp out. "+
                           "For the second circuit, plot the step response ( \(v_c(t)\) versus t plot). Mention the rise time.(use circuit comparator for the 2 circuits)",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
       
                      

    # Step Response of a Second Order Filter Hardware
    sof_hardware = add_hardware(lab=second_order_filters, name="Step Response of a Second Order Filter Hardware")

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 1", number=1,
                         text_input="<h4>Part 1. FILTER 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 2", number=2,
                         text_input="Using your Digilent EE board, build the first circuit (same as Pre-lab) as shown in Fig. 4. "+
                         "Allow \(v_s(t)\) to be a 1 kHz square wave with 1V amplitude (high voltage 1 and low voltage 0). "+
                         "In Waveforms software, you need to set the frequency at 1 kHz, amplitude 500 mV, and offset 500 mV in "+
                         "Wavegen section. Let R=100\(\\Omega\), C=4.7 nF, and L=1 mH. Save a printout of the step response. "+
                         "Measure the frequency of oscillation and damping time.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=sof_hardware,
                           name="sof board hardware 3", number=3,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab04/fig02.jpg', equation_input="", video_input="", 
                           element_type='image')
    
    add_hardware_element(hardware=sof_hardware,
                           name="sof board hardware 4", number=4,
                           text_input="Figure 4",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 5", number=5,
                         text_input="<h4>Part 1. Questions:</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 6", number=6,
                         text_input="a. Superimpose the step response from Pre-lab and Digilent EE board.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 7", number=7,
                         text_input="b. Do they agree? If not, why? ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 8", number=8,
                         text_input="c. Determine the oscillation frequency and damping time from theory. "+
                         "Compare these values to the measured values from Digilent EE board. Calculate the percentage "+
                         "error between theoretical and Digilent EE board values.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')


    add_hardware_element(hardware=sof_hardware, name="sof board hardware 9", number=9,
                         text_input="<h4>Part 2. FILTER 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 10", number=10,
                         text_input="Using your Digilent EE board, build the second circuit from Fig. 4. "+
                         "Allow \(v_s(t)\) to be a 1 kHz square wave with 1V amplitude (high voltage 1 and low voltage 0). "+
                         "In Waveforms software, you need to set the frequency at 1 kHz, amplitude 500 mV, and offset 500 mV in "+
                         "Wavegen section. Let R=1.5k\(\\Omega\), C=4.7 nF, and L=1 mH. Save a printout of the step response. "+
                         "Measure the oscillation frequency and damping time.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')


    add_hardware_element(hardware=sof_hardware, name="sof board hardware 11", number=11,
                         text_input="<h4>Part 2. Questions:</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 12", number=12,
                         text_input="a. Superimpose the step response from Pre-lab and Digilent EE board.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 13", number=13,
                         text_input="b. Do they agree? If not, why? ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=sof_hardware, name="sof board hardware 14", number=14,
                         text_input="c. Determine the oscillation frequency and damping time from theory. "+
                         "Compare these values to the measured values from Digilent EE board. Calculate the percentage "+
                         "error between theoretical and Digilent EE board values.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    

    # Step Response of a Second Order Filter Results
    sof_results = add_results(lab=second_order_filters, name="Step Response of a Second Order Filter Results")

    add_results_questions(results=sof_results,
                          question="Write a standard report as specified in the syllabus. "+
                          "Explain your work with the detailed calculations, observations, and analysis.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=sof_results,
                          question="In your report, you must include the answers to the questions in Hardware section.",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=sof_results,
                          question="Submit the report to our <a href=\"https://blackboard.temple.edu\">blackboard</a> before the next lab (see syllabus for submission guideline).",
                          answer_text="",
                          answer_type='text')

    # Step Response of a Second Order Filter lab test
    sof_lab_test = add_lab_test(lab=second_order_filters, name="Step Response of a Second Order Filter Lab Test")

                        
    add_lab_test_element(labtest=sof_lab_test, name="sof lab test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab04/fig02.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=sof_lab_test, name="sof lab test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=sof_lab_test, name="sof lab test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab04/fig03.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=sof_lab_test, name="sof lab test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=sof_lab_test, name="sof lab test element 5", number=5,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab04/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=sof_lab_test, name="sof lab test element 6", number=6,
                      text_input="Figure III",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=sof_lab_test, name="sof lab test element 6", number=6,
                      text_input="Note: Figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')

    add_lab_test_question(labtest=sof_lab_test,
                             question="Consider the series RLC circuit in Fig. I. A step input \(v_s(t)\) is applied. "+
                             "Given, L=4mH and C =1nF. Which value of the resistor will make the step response critically damped?",
                             answer_one="100\(\\Omega\)", answer_two="4k\(\\Omega\)",
                             answer_three="1k\(\\Omega\)", answer_four="10k\(\\Omega\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=sof_lab_test,
                             question="Refer to the series RLC circuit in Fig. I. A step input \(v_s(t)\) is applied. Given, R=1k\(\\Omega\), C=1nF, and L=4mH. "+
                             "What would be the step response?",
                             answer_one="overdamped", answer_two="underdamped",
                             answer_three="superficially damped", answer_four="critically damped",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=sof_lab_test,
                             question="Refer to the series RLC circuit in Fig. I. A step input \(v_s(t)\) is applied. Given, R=1k\(\\Omega\), C=1nF, and L=4mH. "+
                             "What is the oscillating frequency (in Hz) of the circuit?",
                             answer_one="500 kHz", answer_two="79.6 Hz",
                             answer_three="7.96 kHz", answer_four="100 kHz",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=sof_lab_test,
                             question="Refer to the series RLC circuit in Fig. I. A step input \(v_s(t)\) is applied. Given, R=1\(\\Omega\), C=1\(\\mu\)F, and L=1mH. "+
                             "What will be the characteristic equation?",
                             answer_one="\(s^2+1000s+10=0\)", answer_two="\(s^2+100s+10^9=0\)",
                             answer_three="\(s^2+1000s+10^9=0\)", answer_four="\(s^2+100s+10^{-9}=0\)",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=sof_lab_test,
                             question="Refer to the circuit in Fig. II, Suppose, this series RLC circuit has R=1.5 k\(\\Omega\), C=4.7 nF, and L=1 mH. "+
                             "Which one of Fig. III will be the step response?",
                             answer_one="ii", answer_two="iv",
                             answer_three="i", answer_four="iii",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")


    # Print out what we have added to the user.
    #for c in Course.objects.all():
    #    for l in Laboratory.objects.filter(course=c):
    #        print "- {0} - {1}".format(str(c), str(l))
            

    # Add labpermissions for new lab for each user 
    for u in User.objects.all():
        add_new_lab_permission(user=u, lab=second_order_filters)
    
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
