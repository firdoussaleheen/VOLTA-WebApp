import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
-EE Science II Course

LABORATORIES:

'''

    ###
    # EE Science II Lab 9: Gain-Bandwidth Product and Slew Rate of Op-Amp
    ###
def populate(ee_science_ii):
    gbp_opamp = add_lab(course=ee_science_ii, name="Gain Bandwidth Product and Slew Rate of Op Amp",
                                  start_date=timezone.now(), due_date=timezone.now(),
                                  lab_number=9)
    add_lab_objective(lab=gbp_opamp,
                      objective="The objective of this lab is to explore two important characteristics "+
                      "of practical Op-Amps: Gain-Bandwidth Product and slew rate.")


    # Gain Bandwidth Product and Slew Rate of Op Amp Theory 
    gbp_theory = add_theory(lab=gbp_opamp, name="Gain Bandwidth Product and Slew Rate of Op Amp Theory")
    
    add_theory_element(theory=gbp_theory, name="gbp theory 1", number=1,
                       text_input="Op-Amps have some interesting characteristics which we have to take "+
                       "into account when we design AC circuits. Specifically, there is a limit to what "+
                       "frequencies they can operate at. Beyond these limits, the transistors inside the "+
                       "Op-Amp cannot charge or discharge fast enough to produce the desired output. For "+
                       "this limitation, practical Op-Amps have two performance limiting characteristics: Gain-Bandwidth Product and slew rate.",
                       image_input=None, equation_input="", video_input="", element_type='text')

    add_theory_element(theory=gbp_theory, name="gbp theory 2", number=2,
                       text_input="As the name suggests, the Gain-Bandwidth Product (GBP) is the product of "+
                       "the theoretical gain (\(G_{theoretical}\)) of the Op-Amp amplifier and the internal cutoff frequency (\(f_c\)),",
                       image_input=None, equation_input="", video_input="", element_type='text')

    add_theory_element(theory=gbp_theory, name="gbp theory 3", number=3,
                       text_input="",
                       image_input=None, equation_input="GBP=G_{theoretical} f_c", video_input="", 
                       element_type='latex')

    add_theory_element(theory=gbp_theory, name="gbp theory 4", number=4,
                       text_input="",
                       image_input='VLA/courses/EE_Science_II/Lab09/fig01.jpg', equation_input="", video_input="",
                       element_type='image')

    add_theory_element(theory=gbp_theory, name="gbp theory 5", number=5,
                       text_input="Figure 1",
                       image_input=None, equation_input="", video_input="", 
                       element_type='caption')

    add_theory_element(theory=gbp_theory, name="gbp theory 6", number=6,
                       text_input="For a given Op-Amp, GBP is constant. The unit of GBP is Hz. When very high frequency inputs are "+
                       "applied, the Op-Amp acts like a first order low pass filter with a cutoff frequency \(f_c\). So, the actual gain "+
                       "of the Op-Amp amplifier drops off at higher frequencies, just like a low pass filter as shown in Fig.1.",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')

    add_theory_element(theory=gbp_theory, name="gbp theory 7", number=7,
                       text_input="Similarly, GBP effects are related to the Op-Amp's slew rate. Slew rate is defined as "+
                       "the maximum rate of change in output voltage when the input is a step change of voltage. The unit "+
                       "of slew rate is typically volts per microsecond, V/us. A classic example is when the input "+
                       "is a square pulse and with high frequency and the output signal looks like the one that is "+
                       "shown in Fig. 2. In this case, the slew rate can be expressed by,",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')

    add_theory_element(theory=gbp_theory, name="gbp theory 8", number=8,
                       text_input="",
                       image_input=None, equation_input="SR=max(\\frac{\\Delta v}{\\Delta t})", video_input="", 
                       element_type='latex')

    add_theory_element(theory=gbp_theory, name="gbp theory 9", number=9,
                       text_input="",
                       image_input='VLA/courses/EE_Science_II/Lab09/fig02.jpg', equation_input="", video_input="",
                       element_type='image')

    add_theory_element(theory=gbp_theory, name="gbp theory 10", number=10,
                       text_input="Figure 2",
                       image_input=None, equation_input="", video_input="", 
                       element_type='caption')

    add_theory_element(theory=gbp_theory, name="gbp theory 11", number=11,
                       text_input="For a sinusoidal waveform, the slew rate can be calculated using ",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')

    add_theory_element(theory=gbp_theory, name="gbp theory 12", number=12,
                       text_input="",
                       image_input=None, equation_input="SR=2\pi f V_p", video_input="", 
                       element_type='latex')

    add_theory_element(theory=gbp_theory, name="gbp theory 13", number=13,
                       text_input="where f is the frequency of the input sinusoid, and Vp is the maximum peak voltage. This review will help you in test and lab.",
                       image_input=None, equation_input="", video_input="", element_type='text')

   

    # Gain Bandwidth Product and Slew Rate of Op Amp Theory test
    gbp_theory_test = add_theory_test(lab=gbp_opamp, name="Gain Bandwidth Product and Slew Rate of Op Amp Theory Test")

                        
    add_theory_test_element(theorytest=gbp_theory_test, name="gbp theory test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab09/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=gbp_theory_test, name="gbp theory test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=gbp_theory_test, name="gbp theory test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab09/fig05.jpg', equation_input="", video_input="",
                      element_type='image')


    add_theory_test_element(theorytest=gbp_theory_test, name="gbp theory test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=gbp_theory_test, name="gbp theory test element 5", number=5,
                      text_input="Note: Figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')
    

    add_theory_test_question(theorytest=gbp_theory_test,
                             question="Consider the circuit in Fig. I, what is transfer function?",
                             answer_one="\(\\frac{V_{out}}{V_{in}}=\\frac{R2}{R1}\)", answer_two="\(\\frac{V_{out}}{V_{in}}=1+\\frac{R1}{R2}\)",
                             answer_three="\(\\frac{V_{out}}{V_{in}}=1+\\frac{R2}{R1}\)", answer_four="\(\\frac{V_{out}}{V_{in}}=-\\frac{R2}{R1}\)",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")


    add_theory_test_question(theorytest=gbp_theory_test,
                             question="Consider the circuit in Fig. I, where \(R1=1k\\Omega\) and \(R2=5k\\Omega\). What will be the theoretical gain?",
                             answer_one="-5", answer_two="6",
                             answer_three="1.2", answer_four="5",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")


    add_theory_test_question(theorytest=gbp_theory_test,
                             question="Consider the circuit in Fig. I, where Gain-bandwidth product (GBP) is 1 MHz and the theoretical gain is 10. What is the value of internal cutoff frequency, \(f_c\)?",
                             answer_one="10 kHz", answer_two="1kHz",
                             answer_three="100 kHz", answer_four="0.1 kHz",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=gbp_theory_test,
                             question="Consider the circuit in Fig. I, where the maximum peak voltage is 2V and the input voltage frequency is 100 kHz. What is the value of slew rate?",
                             answer_one="1256637 \(V/\\mu s\)", answer_two="1.256637 \(V/\\mu s\)",
                             answer_three="125.6637 \(V/\\mu s\)", answer_four="12566.37 \(V/\\mu s\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=gbp_theory_test,
                             question="Consider the circuit in Fig. II, what is transfer function?",
                             answer_one="\(\\frac{V_{out}}{V_{in}}=\\frac{R2}{R1}\)", answer_two="\(\\frac{V_{out}}{V_{in}}=1+\\frac{R1}{R2}\)",
                             answer_three="\(\\frac{V_{out}}{V_{in}}=1+\\frac{R2}{R1}\)", answer_four="\(\\frac{V_{out}}{V_{in}}=-\\frac{R2}{R1}\)",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")
   
  
    # Gain-Bandwidth Product and Slew Rate of Op-Amp Simulation
    gbp_simulation = add_simulation(lab=gbp_opamp, name="Gain Bandwidth Product and Slew Rate of Op Amp Simulation")

    add_simulation_element(simulation=gbp_simulation,
                           name = "Gain-Bandwidth Product and Slew Rate of Op-Amp simulation 1", number=1,
                           text_input="Simulate the following circuit in Multisim for a gain of 10, 20, and 40. Calculate the bandwidth gain product "+
                           "for each case. Bring your simulation results to the lab. Follow the example here: "+
                           "<a href=\"https://www.youtube.com/watch?v=GNuSLHf2Pgg\"> GBP Calculation of a non-inverting Op-Amp amplifier </a> .", 
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')

    add_simulation_element(simulation=gbp_simulation,
                           name = "Gain-Bandwidth Product and Slew Rate of Op-Amp simulation 2", number=2,
                           text_input="", 
                           image_input='VLA/courses/EE_Science_II/Lab09/fig04.jpg', equation_input="", video_input="", 
                           element_type='image')

    add_simulation_element(simulation=gbp_simulation,
                           name = "Gain-Bandwidth Product and Slew Rate of Op-Amp simulation 3", number=3,
                           text_input="Fig. 3", 
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')

           

    
    # Gain-Bandwidth Product and Slew Rate of Op-Amp Hardware
    gbp_hardware = add_hardware(lab=gbp_opamp, name="Gain Bandwidth Product and Slew Rate of Op Amp Hardware")
    
    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 1", number=1,
                         text_input="<h4>Part 1. CIRCUIT 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 2", number=2,
                         text_input="Build the circuit shown in Fig. 4 in EE board. Apply 1Vpp input sine wave with "+
                         "1 kHz and measure the gain. Repeat over the range of frequencies: 1kHz, 2kHz, 5kHz, 10kHz, "+
                         "20kHz, 50kHz, 100kHz, 200kHz, 500kHz, 1MHz, 2MHz, 4MHz. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 3", number=3,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab09/fig03.jpg', equation_input="", video_input="", 
                         element_type='image')
    
    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 4", number=4,
                         text_input="Figure 4: Circuit 1",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 5", number=5,
                         text_input="Perform the following steps and answer the questions:",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 6", number=6,
                         text_input="i. Create a plot of gain versus frequency. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 7", number=7,
                         text_input="ii. From the plot, determine the frequency at which the gain is 70.7% of DC gain. "+
                         "DC gain is also called open-loop gain. This is the internal cutoff frequency.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 8", number=8,
                         text_input="iii. Calculate the gain-bandwidth product from DC gain and internal cutoff frequency.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 9", number=9,
                         text_input="iv. Measure the slew rate for each frequency. "+
                         "Determine the average slew rate, and compare to the typical slew rate value mentioned in the datasheet.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 10", number=10,
                         text_input="v.	Which one of the characteristics is limiting the high-frequency performance of your circuit: Gain-Bandwidth product or slew rate?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 11", number=11,
                         text_input="vi. Repeat the above steps for a smaller input signal of 100mVpp.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 12", number=12,
                         text_input="<h4>Part 2. CIRCUIT 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 13", number=13,
                         text_input="Build the circuit shown in Fig. 5 in EE board for a gain of 2. Apply 1Vpp input sine wave with "+
                         "1 kHz and measure the gain. Repeat over the range of frequencies: 1kHz, 2kHz, 5kHz, 10kHz, "+
                         "20kHz, 50kHz, 100kHz, 200kHz, 500kHz, 1MHz, 2MHz, 4MHz. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 14", number=14,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab09/fig04.jpg', equation_input="", video_input="", 
                         element_type='image')
    
    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 15", number=15,
                         text_input="Figure 5: Circuit 2",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 16", number=16,
                         text_input="Perform the following steps and answer the questions:",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 17", number=17,
                         text_input="i. Create a plot of gain versus frequency. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 18", number=18,
                         text_input="ii. From the plot, determine the frequency at which the gain is 70.7% of DC gain. "+
                         "DC gain is also called open-loop gain. This is the internal cutoff frequency.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 19", number=19,
                         text_input="iii. Calculate the gain-bandwidth product from DC gain and internal cutoff frequency.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 18", number=18,
                         text_input="iv. Measure the slew rate for each frequency. "+
                         "Determine the average slew rate, and compare to the typical slew rate value mentioned in the datasheet.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 19", number=19,
                         text_input="v.	Which one of the characteristics is limiting the high-frequency performance of your circuit: Gain-Bandwidth product or slew rate?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=gbp_hardware, name="Gain-Bandwidth Product and Slew Rate of Op-Amp hardware 20", number=20,
                         text_input="vi. Repeat the above steps for a gain of 10 and 100.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
     

    # Gain-Bandwidth Product and Slew Rate of Op-Amp Results
    gbp_results = add_results(lab=gbp_opamp, name="Gain Bandwidth Product and Slew Rate of Op Amp Results")

    add_results_questions(results=gbp_results,
                          question="Write a standard report as specified in the syllabus. "+
                          "Explain your work with the detailed calculations, observations, and analysis. In your report, you must include the answers to the questions in hardware section.",
                          answer_text="",
                          answer_type='text')
     
    add_results_questions(results=gbp_results,
                          question="Submit the report to our <a href=\"https://blackboard.temple.edu\">blackboard</a> before the next lab (see syllabus for submission guideline).",
                          answer_text="",
                          answer_type='text')

    # Gain-Bandwidth Product and Slew Rate of Op-Amp lab test
    gbp_lab_test = add_lab_test(lab=gbp_opamp, name="Gain Bandwidth Product and Slew Rate of Op Amp lab test")

                        
    add_lab_test_element(labtest=gbp_lab_test, name="gbp lab test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab09/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=gbp_lab_test, name="gbp lab test element 2", number=2,
                      text_input="Figure I",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=gbp_lab_test, name="gbp lab test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab09/fig05.jpg', equation_input="", video_input="",
                      element_type='image')


    add_lab_test_element(labtest=gbp_lab_test, name="gbp lab test element 4", number=4,
                      text_input="Figure II",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=gbp_lab_test, name="gbp lab test element 5", number=5,
                      text_input="Note: Figure numbers are specific to this test.",
                      image_input=None, equation_input="", video_input="", 
                      element_type='text')


    add_lab_test_question(labtest=gbp_lab_test,
                             question="Consider the circuit in Fig. I, what is the transfer function?",
                             answer_one="\(\\frac{V_{out}}{V_{in}}=\\frac{R2}{R1}\)", answer_two="\(\\frac{V_{out}}{V_{in}}=1+\\frac{R1}{R2}\)",
                             answer_three="\(\\frac{V_{out}}{V_{in}}=-\\frac{R2}{R1}\)", answer_four="\(\\frac{V_{out}}{V_{in}}=1+\\frac{R2}{R1}\)",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")


    add_lab_test_question(labtest=gbp_lab_test,
                             question="Consider the circuit in Fig. I, where \(R1=1k\\Omega\) and \(R2=5k\\Omega\). What will be the theoretical gain?",
                             answer_one="-5", answer_two="1.2",
                             answer_three="5", answer_four="6",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")


    add_lab_test_question(labtest=gbp_lab_test,
                             question="Consider the circuit in Fig. I, where Gain-bandwidth product (GBP) is 1 MHz and the theoretical gain is 10. What is the value of internal cutoff frequency, \(f_c\)?",
                             answer_one="10 kHz", answer_two="1kHz",
                             answer_three="0.1 kHz", answer_four="100 kHz",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=gbp_lab_test,
                             question="Consider the circuit in Fig. I, where the maximum peak voltage is 2V and the input voltage frequency is 100 kHz. What is the value of slew rate?",
                             answer_one="1256637 \(V/\\mu s\)", answer_two="125.6637 \(V/\\mu s\)",
                             answer_three="12566.37 \(V/\\mu s\)", answer_four="1.256637 \(V/\\mu s\)",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=gbp_lab_test,
                             question="Consider the circuit in Fig. II, what is the transfer function?",
                             answer_one="\(\\frac{V_{out}}{V_{in}}=\\frac{R2}{R1}\)", answer_two="\(\\frac{V_{out}}{V_{in}}=1+\\frac{R1}{R2}\)",
                             answer_three="\(\\frac{V_{out}}{V_{in}}=1+\\frac{R2}{R1}\)", answer_four="\(\\frac{V_{out}}{V_{in}}=-\\frac{R2}{R1}\)",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")


    # Print out what we have added to the user.
    #for c in Course.objects.all():
    #    for l in Laboratory.objects.filter(course=c):
    #        print "- {0} - {1}".format(str(c), str(l))
            

    # Add labpermissions for new lab for each user 
    for u in User.objects.all():
        add_new_lab_permission(user=u, lab=gbp_opamp)
    
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
