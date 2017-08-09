import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
-EE Science II Course

LABORATORIES:
-Intro to Multisim using RC Circuit
'''

def populate():
    # Add EE Science II Course
    ee_science_ii = add_course("EE Science II", subj='ECE',
                                 course_number=2323, crn=25509,
                                 section_number=002, start_date=None,
                                 end_date=None,
                                 lecture_time=None,
                                 lecture_days="",
                                 lecture_location="",
                                 lab_time=None, lab_days="",
                                 lab_location="",
                                 course_description="Alternating Current (AC) circuit analsis are covered in the course. Topics include "+
                                    "frequency response analysis of R, L, and C Components, RC, RL and RLC networks, series and parallel sinuosoid circuits.",
                                 course_overview="",
                                 website="https://blackboard.temple.edu/",
                                 instructor_name="",
                                 instructor_email="",
                                 instructor_office_hours=None,
                                 instructor_office_days="",
                                 instructor_office_location="",
                                 instructor_phone="",
                                 TA_name="Firdous Saleheen",
                                 TA_email="f.saleheen@temple.edu",
                                 TA_office_hours=None,
                                 TA_office_days="",
                                 TA_office_location="",
                                 TA_phone="")

    ee_science_ii_prereq = add_prereq(course=ee_science_ii, name="EE Science II Prerequisites")

    ###
    # EE Science II Lab 1: Intro to Multisim using RC circuit
    ###
    multisim_intro = add_lab(course=ee_science_ii, name="Introduction to Multisim Using RC Circuit",
                                   start_date=timezone.now(), due_date=timezone.now(),
                                   lab_number=1)
    add_lab_objective(lab=multisim_intro,
                      objective="The goal of this laboratory is to familiarize you with the circuit simulation software Multisim. "+
                      "In this first lab, you will go through a Multisim tutorial, and demonstrate the use of it in analyzing a basic "+
                      "RC circuit using DC and AC sources.")
    
    # Multisim Intro using RC Circuit theory
    multisim_intro_theory = add_theory(lab=multisim_intro, name="RC Circuit Theory Review")
    
    add_theory_element(theory=multisim_intro_theory, name="multisim theory 1", number=1,
                       text_input="Resistor-Capacitor (RC) circuit is popular in building low and high pass filters. "+
                       "This section is a review of DC RC circuit. The simplest "+
                       "RC circuit is composed of a capacitor and a resistor. Fig.1 shows an example of DC RC circuit",
                       image_input=None, equation_input="", video_input="", element_type='text')

    # fig 1 and caption goes here
    add_theory_element(theory=multisim_intro_theory,name="multisim theory 2", number=2,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig01.jpg', equation_input="", video_input="", 
                      element_type='image')

    add_theory_element(theory=multisim_intro_theory, name="multisim theory 3", number=3,
                      text_input="Figure 1",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_element(theory=multisim_intro_theory, name="multisim theory 4", number=4,
                       text_input="We start our analysis by investigating the transient response of this RC circuit. Initially, the capacitor "+
                       "is uncharged; its initial voltage is zero. The capacitor cannot change its voltage discontinuously when a DC source is "+
                       "applied to this circuit. As the current begins to flow, the capacitor acquires a charge and its voltage increases. The rate "+
                       "of the charge is determined by the time constant \(\\tau\) , which is equal to the product of \(RC\) . If there are multiple resistors and "+
                       "capacitors the time constant formula will be \(R_{equivalent}C_{equivalent}\). After one time constant period (when \(t=\\tau=RC\)), the capacitor will charge up to 63.2\(\%\) "+
                       "of its final voltage (here the final voltage indicates the applied DC voltage). The percentage value 63.2\(\%\) is true for any value of R and C.",
                       image_input=None, equation_input="", video_input="", element_type='text')

    add_theory_element(theory=multisim_intro_theory, name="multisim theory 5", number=5,
                       text_input="Let us see how this percentage value 63.2\(\%\) is calculated. The charging equation for the voltage of the capacitor is:",
                       image_input=None, equation_input="", video_input="", element_type='text')

    add_theory_element(theory=multisim_intro_theory, name="multisim theory 6", number=6,
                       text_input="",
                       image_input=None, equation_input='V_0 = V_s(1-e^{-\\frac{t}{RC}})\hspace{10mm}\\mbox{Eq. 1}', video_input="", element_type='latex') 

    add_theory_element(theory=multisim_intro_theory, name="multisim theory 7", number=7,
                       text_input="where \(V_0\)  is the voltage across capacitor, \(V_s\) is the applied voltage source, and \(RC\) is the time constant. For one time constant period (when \(t=\\tau=RC\)), "+
                       "then the charging equation becomes \(V_0 = V_s(1-e^{-\\frac{t}{RC}})\). Therefore, the capacitor output voltage \(V_0\) in one time constant will be 63.2\(\%\) of \(V_s\). In a similar fashion, for two, three, four, "+
                       "or five time constant periods, we can figure out the capacitor output voltage \(V_0\) in terms of percentage value of \(V_s\)  by setting \(t = 2RC, 3RC, 4RC, 5RC\). For details about "+
                       "the RC circuit, consult Chapter 7 of the ECE 2322 textbook.",
                       image_input=None, equation_input="", video_input="", element_type='text')

    # Multisim Intro using RC circuit theory test
    multisim_intro_theory_test = add_theory_test(lab=multisim_intro, name="Multisim Introduction using RC Circuit Theory Test")

                        
    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 2", number=2,
                      text_input="Figure 1",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig05.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 4", number=4,
                      text_input="Figure 2",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 5", number=5,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig06.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 6", number=6,
                      text_input="Figure 3",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 7", number=7,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig07.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 8", number=8,
                      text_input="Figure 4",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 9", number=9,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig08.jpg', equation_input="", video_input="",
                      element_type='image')

    add_theory_test_element(theorytest=multisim_intro_theory_test, name="multisim theory test element 10", number=10,
                      text_input="Figure 5",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_theory_test_question(theorytest=multisim_intro_theory_test,
                             question="Refer to Fig. 1 which one is an RC circuit?",
                             answer_one="a", answer_two="b",
                             answer_three="c", answer_four="d",
                             correct_answer_number=2,
                             correct_response="Because the circuit has at least one resistor and one capacitor.",
                             incorrect_response="An RC circuit must have at least one resistor and one capacitor.")

    add_theory_test_question(theorytest=multisim_intro_theory_test,
                             question="Refer to the circuit in Fig. 2. Fill in the blanks using the charging equation \(V_0 = V_s(1-e^{-\\frac{t}{RC}})\) "+
                             "For two time constant period (t = 2RC) , the capacitor will charge up to _______ percentage of  \(V_s\)",
                             answer_one="63.2%", answer_two="126.4%",
                             answer_three="88.5%", answer_four="86.5%",
                             correct_answer_number=4,
                             correct_response="Because replacing t with 2RC gives the capacitor voltage.",
                             incorrect_response="For two time constant period, t should be replaced by 2RC.")

    add_theory_test_question(theorytest=multisim_intro_theory_test,
                             question="If the applied DC voltage is 10 V, in one time constant period what would be the final capacitor voltage?",
                             answer_one="6.23 V", answer_two="6.20 V",
                             answer_three="5.32 V", answer_four="6.32 V",
                             correct_answer_number=4,
                             correct_response="In one time constant, the capacitor voltages reaches 63.2% of the applied voltage.",
                             incorrect_response="Check the percentage value of capacitor with respect to applied voltage for one time constant.")

    add_theory_test_question(theorytest=multisim_intro_theory_test,
                             question="Refer to the circuit in Fig. 3. What would be the time constant for this circuit?",
                             answer_one="2RC", answer_two="0",
                             answer_three="\(RC^2\)", answer_four="RC",
                             correct_answer_number=1,
                             correct_response="Because the equivalent capacitance is 2C which is multiplied by resistance R.",
                             incorrect_response="Check the equivalent capacitance and resistance before the calculation.")

    add_theory_test_question(theorytest=multisim_intro_theory_test,
                             question="Refer to the circuit in Fig. 4. For a square pulse input signal, what would the capacitor voltage "+
                             "Vc look like? Choose from Fig. 5",
                             answer_one="(i)", answer_two="(iii)",
                             answer_three="(ii)", answer_four="both (ii) and (iv)",
                             correct_answer_number=3,
                             correct_response="Because the capacitor charging and discharging follows exponential rise or decay.",
                             incorrect_response="Check the formula for charging and discharging of capacitor in a simple RC circuit.")


    # Multisim Intro using RC Circuit Simulation
    multisim_intro_simulation = add_simulation(lab=multisim_intro, name="Multisim Introduction using RC Circuit Simulation")
    
    add_simulation_element(simulation=multisim_intro_simulation,
                           name="Multisim Intro simulation 1", number=1,
                           text_input="<h3>Part 1: Multisim Tutorial</h3>",
                           image_input=None, equation_input="", video_input="", element_type='text')

    add_simulation_element(simulation=multisim_intro_simulation,
                           name="Multisim Intro simulation 2", number=2,
                           text_input="Go through the tutorial by clicking this URL: <a href=\"http://www.ni.com/white-paper/10710/en\">Multisim Tutorial</a>. Do not worry about the details of the components. "+
                           "The goal of this part of the lab is to make sure you know how to run Multisim. Also go through these URLs: <a href=\"http://www.ni.com/white-paper/12774/en\">Transient Analysis in Multisim</a> and "+
                           "<a href=\"http://digital.ni.com/public.nsf/allkb/030CDBEF18515D6486257199006AEF56\">Slow-down simulation in Multisim</a>. <strong><em>Do not include anything from this part of the lab in your report.</em></strong>",
                           image_input=None, equation_input="", video_input="", element_type='text')

    add_simulation_element(simulation=multisim_intro_simulation,
                           name="Multisim Intro simulation 3", number=3,
                           text_input="<h3>Part 2: RC Circuit with DC voltage source</h3>",
                           image_input=None, equation_input="", video_input="", element_type='text')

    add_simulation_element(simulation=multisim_intro_simulation,
                           name="Multisim Intro simulation 4", number=4,
                           text_input="Construct the RC circuit in Fig. 1 in Multisim using these values: \(V_s=10\) V, \(R=100\\Omega\), \(C=1\\mu F\). <strong><em>Determine the time constant for the network using the formula. Also determine the capacitor "+
                           "voltage after one time constant period. Simulate the circuit in the Multisim. Find the capacitor voltage at one time constant period (Hint: Use the transient analysis feature in Multisim. "+
                           "Plot a capacitor voltage versus time graph). Compare this voltage to the value you get from the formula.</em></strong>",
                           image_input=None, equation_input="", video_input="", element_type='text')

    add_simulation_element(simulation=multisim_intro_simulation,
                           name="Multisim Intro simulation 5", number=5,
                           text_input="Repeat the previous steps for \(R=1k\\Omega\), \(C=1\\mu F\) and \(R=100\\Omega\), \(C=1nF\). <strong><em>Finally, show that the capacitor voltage reaches 63.2% of the applied voltage after one time constant "+
                           "regardless the values of R and C.</em></strong>",
                           image_input=None, equation_input="", video_input="", element_type='text')

    add_simulation_element(simulation=multisim_intro_simulation,
                           name="Multisim Intro simulation 6", number=6,
                           text_input="You can do this part outside the lab. Consider the parallel RC circuit in Fig. 2 and derive an expression for Ir in terms of Vs, R, C, t. "+
                           "The values of the resistor, capacitor, and voltage source are given symbolically in the Fig. 2. Assume that initially the capacitor is full charged and conducts "+
                           "no current. Simulation is not mandatory, but the derivation is (Hint: get help from the textbook example). <strong><em>Include the derivation into your report.</em></strong>",
                           image_input=None, equation_input="", video_input="", element_type='text')

# fig 2 and caption goes here
    add_simulation_element(simulation=multisim_intro_simulation,name="multisim theory 7", number=7,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig02.jpg', equation_input="", video_input="", 
                      element_type='image')

    add_simulation_element(simulation=multisim_intro_simulation, name="multisim theory 8", number=8,
                      text_input="Figure 2",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_simulation_element(simulation=multisim_intro_simulation,
                           name="Multisim Intro simulation 9", number=9,
                           text_input="<h2>Part 3: RC Circuit with Alternating Voltage Source </h2>",
                           image_input=None, equation_input="", video_input="", element_type='text')

    add_simulation_element(simulation=multisim_intro_simulation,
                           name="Multisim Intro simulation 10", number=10,
                           text_input="Now consider an RC circuit with an alternating voltage source. One such source can be a square pulse voltage source with minimum 0V and maximum 1V. Since for a short period of time, "+
                           "the applied voltage is DC, we can still use the theory for DC RC circuit for that period. Using Multisim, build and simulate the circuit in Fig. 3. "+
                           "Use a 0-1V square pulse voltage source with 50 Hz (time period = 20 ms) with the pulse duration of 10 ms. To view the scope screen, right click the object during "+
                           "the simulation and select Properties. Adjust the scope knobs/scale as necessary in order to visualize two complete cycles of the signals",
                           image_input=None, equation_input="", video_input="", element_type='text')

    # fig 3 and caption goes here
    add_simulation_element(simulation=multisim_intro_simulation,name="multisim theory 11", number=11,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig03.jpg', equation_input="", video_input="", 
                      element_type='image')

    add_simulation_element(simulation=multisim_intro_simulation, name="multisim theory 12", number=12,
                      text_input="Figure 3",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_simulation_element(simulation=multisim_intro_simulation,
                           name="Multisim Intro simulation 13", number=13,
                           text_input="<strong><em>Take a screenshot. What is the time constant of this circuit? What is the capacitor voltage after one time constant? Compare this theoretical value to the value you find  "+
                           "from the simulation. Find the theoretical and simulated capacitor voltage after 5 time constant period \(t=5\\tau\). For two complete cycles of the square pulse signal, plot the capacitor output "+
                           "voltage (Hint: In the same graph plot time at x-axis and square pulse signal and the capacitor output voltage in y-axis).</em></strong>",
                           image_input=None, equation_input="", video_input="", element_type='text')

    
      
    # Multisim Intro using RC circuit simulation test
    multisim_intro_simulation_test = add_simulation_test(lab=multisim_intro,
                                                   name="Multisim Introduction using RC Circuit Simulation Test")

    add_sim_test_element(simulationtest=multisim_intro_simulation_test, name="multisim simulation test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig09.jpg', equation_input="", video_input="",
                      element_type='image')

    add_sim_test_element(simulationtest=multisim_intro_simulation_test, name="multisim simulation test element 2", number=2,
                      text_input="Figure 1",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    
    add_simulation_test_question(simulationtest=multisim_intro_simulation_test,
                                 question="Refer to the circuit in Fig. 1. with \(V_s=1V\),\(R=1k\\Omega\), \(C=1\\mu F\) "+
                                 "These values are same for rest of the questions too. Now, 1.	for the circuit in Fig. 1, "+
                                 "how much current goes through the resistor initially at t=0+",
                                 answer_one="1 uA", answer_two="1 mA",
                                 answer_three="10 mA", answer_four="100 mA",
                                 correct_answer_number=2,
                                 correct_response="Initially the voltage across the capacitor 0. Only source voltage and the resistor value need to be considered.",
                                 incorrect_response="Check what is the voltage across the capacitor initially.")
    add_simulation_test_question(simulationtest=multisim_intro_simulation_test,
                                 question="For the circuit in Fig. 1, what is the voltage across the capacitor in one time constant period?",
                                 answer_one="0.623 V", answer_two="0.632 V",
                                 answer_three="6.32 V", answer_four="6.23 V",
                                 correct_answer_number=2,
                                 correct_response="For one time constant, the capacitor voltage is 63.2% of the applied voltage after one time constant.",
                                 incorrect_response="Check the percentage of applied voltage after one time constant for the capacitor voltage.")
    add_simulation_test_question(simulationtest=multisim_intro_simulation_test,
                                 question="Suppose the resistor in the circuit in Fig. 1 is parallel to the capacitor instead. What would be the voltage across capacitor?",
                                 answer_one="\(V_o=2 V\)", answer_two="\(V_o=0.632 V\)",
                                 answer_three="\(V_o=1 V\)", answer_four="\(V_o=0 V\)",
                                 correct_answer_number=3,
                                 correct_response="The nodes across the votlage source and the capacitor become same in the new configuration.",
                                 incorrect_response="Check the value across the nodes of the voltage source and the capacitor.")
    add_simulation_test_question(simulationtest=multisim_intro_simulation_test,
                                 question="For the circuit in Fig. 1, if the source voltage is sinusoidal instead of square pulse, what happens to the time constant of the RC circuit?",
                                 answer_one="Increases", answer_two="Decreases",
                                 answer_three="Stays same", answer_four="Becomes zero",
                                 correct_answer_number=3,
                                 correct_response="The time constant of DC or AC RC circuit depend on R and C values only",
                                 incorrect_response="Check the definition of time constant")
                           
    # Multisim Intro & RC Time Constant Hardware
    multisim_intro_hardware = add_hardware(lab=multisim_intro, name="Multisim Introduction using RC Circuit Hardware")
    
    add_hardware_element(hardware=multisim_intro_hardware, name="Multisim hardware 1", number=1,
                         text_input="In this lab, there is no hardware experiment. However, the concept of this lab will flow into the next lab, where you will do the hardware experiment.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')


    # Multisim Intro Results
    multisim_intro_results = add_results(lab=multisim_intro, name="Multisim Introduction using RC Circuit Results")

    add_results_questions(results=multisim_intro_results,
                          question="You must include the answers to the questions in Simulation section (shown as BOLD, ITALICIZED letter) "+
                          "in your report. ",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=multisim_intro_results,
                          question="YWrite a standard report of 3 to 6 pages (see syllabus for details). "+
                          "Explain what you did, presenting your calculations, and observations. ",
                          answer_text="",
                          answer_type='text')

    add_results_questions(results=multisim_intro_results,
                          question="Submit the report to our blackboard before the next lab (see syllabus for submission guideline). ",
                          answer_text="",
                          answer_type='text')

    # Multisim Intro using RC circuit Lab test
    multisim_intro_lab_test = add_lab_test(lab=multisim_intro, name="Multisim Introduction using RC Circuit Laboratory Test")

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 1", number=1,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig04.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 2", number=2,
                      text_input="Figure 1",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 3", number=3,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig05.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 4", number=4,
                      text_input="Figure 2",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 5", number=5,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig06.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 6", number=6,
                      text_input="Figure 3",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 7", number=7,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig07.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 8", number=8,
                      text_input="Figure 4",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 9", number=9,
                      text_input="",
                      image_input='VLA/courses/EE_Science_II/Lab01/fig08.jpg', equation_input="", video_input="",
                      element_type='image')

    add_lab_test_element(labtest=multisim_intro_lab_test, name="multisim lab test element 10", number=10,
                      text_input="Figure 5",
                      image_input=None, equation_input="", video_input="", 
                      element_type='caption')
    

    add_lab_test_question(labtest=multisim_intro_lab_test,
                             question="Refer to Fig. 1 which one is an RC circuit?",
                             answer_one="a", answer_two="b",
                             answer_three="c", answer_four="d",
                             correct_answer_number=2,
                             correct_response="Because the circuit has at least one resistor and one capacitor.",
                             incorrect_response="An RC circuit must have at least one resistor and one capacitor.")

    add_lab_test_question(labtest=multisim_intro_lab_test,
                             question="Refer to the circuit in Fig. 2. Fill in the blanks using the charging equation \(V_0 = V_s(1-e^{-\\frac{t}{RC}})\) "+
                             "For two time constant period (t = 2RC) , the capacitor will charge up to _______ percentage of  \(V_s\)",
                             answer_one="63.2%", answer_two="126.4%",
                             answer_three="86.5%", answer_four="88.5%",
                             correct_answer_number=3,
                             correct_response="Because replacing t with 2RC gives the capacitor voltage.",
                             incorrect_response="For two time constant period, t should be replaced by 2RC.")

    add_lab_test_question(labtest=multisim_intro_lab_test,
                             question="If the applied DC voltage is 10 V, in one time constant period what would be the final capacitor voltage?",
                             answer_one="6.23 V", answer_two="6.32 V",
                             answer_three="6.2 V", answer_four="5.2 V",
                             correct_answer_number=2,
                             correct_response="In one time constant, the capacitor voltages reaches 63.2% of the applied voltage.",
                             incorrect_response="Check the percentage value of capacitor with respect to applied voltage for one time constant.")

    add_lab_test_question(labtest=multisim_intro_lab_test,
                             question="Refer to the circuit in Fig. 3. What would be the time constant for this circuit?",
                             answer_one="2RC", answer_two="0",
                             answer_three="\(RC^2\)", answer_four="RC",
                             correct_answer_number=1,
                             correct_response="Because the equivalent capacitance is 2C which is multiplied by resistance R.",
                             incorrect_response="Check the equivalent capacitance and resistance before the calculation.")

    add_lab_test_question(labtest=multisim_intro_lab_test,
                             question="Refer to the circuit in Fig. 4. For a square pulse input signal, what would the capacitor voltage "+
                             "Vc look like? Choose from Fig. 5",
                             answer_one="(i)", answer_two="both (ii) and (iv)",
                             answer_three="(iii)", answer_four="(ii)",
                             correct_answer_number=4,
                             correct_response="Because the capacitor charging and discharging follows exponential rise or decay.",
                             incorrect_response="Check the formula for charging and discharging of capacitor in a simple RC circuit.")

    # Print out what we have added to the user.
    for c in Course.objects.all():
        for l in Laboratory.objects.filter(course=c):
            print "- {0} - {1}".format(str(c), str(l))

# Add course, prerq, lab, lab section (theory, simulation, hardware)
def add_course(name, crn, subj, course_number, section_number, start_date,
               end_date, lecture_time, lecture_days, lecture_location,
               lab_time, lab_days, lab_location, course_description,
               course_overview, website, instructor_name, instructor_email,
               instructor_office_hours, instructor_office_days,
               instructor_office_location, instructor_phone, TA_name, TA_email,
               TA_office_hours, TA_office_days, TA_office_location, TA_phone):
    c = Course.objects.get_or_create(name=name, subj=subj, course_number=course_number,
                                     section_number=section_number, start_date=start_date,
                                     end_date=end_date, lecture_time=lecture_time,
                                     lecture_days=lecture_days, lecture_location=lecture_location,
                                     lab_time=lab_time, lab_days=lab_days,
                                     lab_location=lab_location, course_description=course_description,
                                     course_overview=course_overview, website=website,
                                     instructor_name=instructor_name, instructor_email=instructor_email,
                                     instructor_office_hours=instructor_office_hours,
                                     instructor_office_days=instructor_office_days,
                                     instructor_office_location=instructor_office_location,
                                     instructor_phone=instructor_phone, TA_name=TA_name,
                                     TA_email=TA_email, TA_office_hours=TA_office_hours,
                                     TA_office_days=TA_office_days,
                                     TA_office_location=TA_office_location, TA_phone=TA_phone)[0]
    return c

def add_prereq(course, name):
    p = Prereq.objects.get_or_create(course=course, name=name)[0]
    return p

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

# Start execution here!
if __name__ == '__main__':
    print "Starting VLA population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    from VLA.models import *
    populate()
