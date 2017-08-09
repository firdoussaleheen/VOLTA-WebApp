import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
EE Science I Course

LABORATORIES:
Ohm's Law Laboratory
'''

def populate():
    # EE Science I course
    circuits_course = add_course("EE Science I", subj='ECE',
                                 course_number=2312, crn=999999,
                                 section_number=1, start_date=timezone.now(),
                                 end_date=timezone.now(),
                                 lecture_time=timezone.now(),
                                 lecture_days="MWF",
                                 lecture_location="ENGR 302",
                                 lab_time=timezone.now(), lab_days="TH",
                                 lab_location="ENGR 705",
                                 course_description="Electric circuit fundamentals including DC and transient circuit analysis are covered in the course. Topics include" +
                                    "independent and dependent sources, circuit elements such as resistors, inductors, capacitors and operational amplifiers, linearity, source" +
                                    "transformation, Thevenin and Norton equivalent circuits, as well as the analysis and design of first and second order circuits. ",
                                 course_overview="The goal of this course is NOT to teach you the intracies of circuit analysis as though it is some art. Circuit analysis is a " +
                                    "topic that applies to many fields beyond electrical engineering (e.g. acoustics, fluid flow). This is really a course in linear system theory." +
                                    " Eventually you will learn all the techniques discussed in this class can be replaced with a generalized approach based on state variables. " +
                                    "However, the specific goals for this course are to teach you the basics on AC and DC circuit analysis. We will build on what you have learned" +
                                    " in physics about inductors and capacitors, and what you are learning in match about differential equations, and will develop simple models of " +
                                    "these components that allow electrical circuits to be designed and analyzed using some simple theoretical calculations. We will also rely heavily " +
                                    "on computer simulation tools such as MutliSim, to handle complex circuits. The laboratory experience will teach you how to design, prototype" +
                                    "and fabricate simple electrical circuits. Extensive use of simulation tools will be made to debug and verify hardware performance. ",
                                 website="http://www.course.com",
                                 instructor_name="Dr. Chang-Hee Won",
                                 instructor_email="instructor@instructor.com",
                                 instructor_office_hours=timezone.now(),
                                 instructor_office_days="MWF",
                                 instructor_office_location="ENGR 703",
                                 instructor_phone="(999) 999-9999",
                                 TA_name="Firdous Saleheen",
                                 TA_email="TA@TA.com",
                                 TA_office_hours=timezone.now(),
                                 TA_office_days="TH",
                                 TA_office_location="ENGR 703d",
                                 TA_phone="(999) 999-9999")

    # Ohms law lab
    ohms_law = add_lab(course=circuits_course, name="Ohms Law",
                       start_date=timezone.now(), due_date=timezone.now(),
                       lab_number=1)
    
    add_lab_objective(lab=ohms_law,
                      objective="Become familiar with the DC power supply and setting the output voltage.")
    add_lab_objective(lab=ohms_law,
                      objective="Measure the current in a DC circuit.")
    add_lab_objective(lab=ohms_law,
                      objective="Apply and plot Ohm's law.")
    add_lab_objective(lab=ohms_law,
                      objective="Determine the slope of an I-V curve.")
    add_lab_objective(lab=ohms_law,
                      objective="Become more familiar with the use of the analog VOM and digital DMM.")
    
    add_lab_equipment(lab=ohms_law,
                      equipment="1 - 1 k&#937; Resistor")
    add_lab_equipment(lab=ohms_law,
                      equipment="1 - 3.3 k&#937; Resistor")
    add_lab_equipment(lab=ohms_law,
                      equipment="Digital Multimeter (DMM)")
    add_lab_equipment(lab=ohms_law,
                      equipment="DC Power Supply")
    add_lab_equipment(lab=ohms_law,
                      equipment="Volt-Ohm-Milliampere Meter (VOM)")

    # Ohms law theory
    ohms_law_theory = add_theory(lab=ohms_law, name="Ohms Law Theory")
    
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 1", number=1,
                       text_input="In any active circuit there must be source of power. In the laboratory, it is convenient to use " +
                       "a source that requires a minimum of maintenance and, more important, whose output voltage can be varies easily. " +
                       "Power supplies are rated as to maximum voltage and current output. For example, a supply rated 0-40 V at 500 mA " +
                       "will provide a maximum voltage of 40 V and a maximum current of 500 mA at any voltage.",
                       image_input=None, equation_input="", video_input="", element_type='text')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 2", number=2,
                       text_input="Most DC power supplies have three terminals, labeled as shown in Fig. 1. The three terminals permit " +
                       "the establishment of a positive or negative voltage, which can be grounded or ungrounded. The " +
                       "variable voltage is available only between terminals \(A\) and \(B\). Both \(A\) and \(B\) must be part of any " +
                       "connection scheme. If only terminals \(A\) and \(B\) are employed, as shown in Fig 2, the supply is " +
                       "considered 'floating' and not connected to the common ground of the network. For common ground " +
                       "and safety reasons, the supply is normally grounded as shown in Fig 3 for a positive voltage " +
                       "and as in Fig. 4 for a negative voltage.",
                       image_input=None, equation_input="", video_input="", element_type='text')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 3", number=3,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/fig01.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 4", number=4,
                         text_input="Figure 1",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 5", number=5,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/fig02.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 6", number=6,
                         text_input="Figure 2",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 7", number=7,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/fig03.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 8", number=8,
                         text_input="Figure 3",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 9", number=9,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/fig04.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 10", number=10,
                         text_input="Figure 4",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 11", number=11,
                       text_input="When measuring voltage levels, make sure the voltmeter is connected in parallel (across) " +
                       "the element being measures, as shown in Fig 5. In addition, recognize that if the leads are " +
                       "connected as shown in the figure, the reading will be upscale and positive. If the meter were " +
                       "hooked up in the reverse manner, a negative (downscale, belowzero) reading would result. The " +
                       "voltmeter is therefore an excellent instrument not only for measuring the voltage level but also " +
                       "for determining the polarity. Since the meter is always placed in parallel with the element, there " +
                       "is no need to disturb the network when the measurement is made.",
                       image_input=None, equation_input="", video_input="", element_type='text')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 12", number=12,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/fig05.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 13", number=13,
                         text_input="Figure 5",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 14", number=14,
                       text_input="Ammeters are always connected in series with the brance in which the current is being " +
                       "measured, as shown in Fig. 6, normally requiring that the branch be opened and the meter inserted. " +
                       "Ammeters also have polarity markings to inficate the manner in which they should be connected to " +
                       "obtain an upscale reading. Since the current \(I\) of Fig. 6 would establish a voltage drop across " +
                       "the ammeter as illustrated, the reading of the ammeter will be upscale and positive. If the meter " +
                       "were hooked up in the reverse manner, the reading would be negative or downscale. In other words, " +
                       "simply reversing the leads will change a belowzero indication to an upscale reading.",
                       image_input=None, equation_input="", video_input="", element_type='text')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 15", number=15,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/fig06.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 16", number=16,
                         text_input="Figure 6",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 17", number=17,
                       text_input="Until you become familiar with the use of the ammeter, draw in the ammeter in the network " +
                       "with the polarities determined by the current direction. It is then easier to ensure that the  meter " +
                       "is connceted properly to the surrounding elements. This process will be frmonstrated in more detail " +
                       "in a later experiment.",
                       image_input=None, equation_input="", video_input="", element_type='text')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 18", number=18,
                       text_input="For both the voltmeter and the ammeter, always start with the higher ranges and work down " +
                       "the the operating level to avoid damaging the instrument. When the VOM and DMM are returned to the " +
                       "stockroom, be sure the VOM is on the highest voltage scale and the DMM is in the off position.",
                       image_input=None, equation_input="", video_input="", element_type='text')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 19", number=19,
                       text_input="The voltage across and the current through a resistor can be used to determine its resistance using Ohm's law in the following form:",
                       image_input=None, equation_input="", video_input="", element_type='text')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 20", number=20,
                         text_input="",
                         image_input=None, equation_input='R = \\frac{V}{I}\\hspace{10mm}\\mbox{Eq. 1}', video_input="", 
                         element_type='latex')
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 21", number=21,
                       text_input="The magnitude of \(R\) will be determined by the units of measure for \(V\) and \(I\).",
                       image_input=None, equation_input="", video_input="", element_type='text')
    
    # Ohms law theory test
    ohms_law_theory_test = add_theory_test(lab=ohms_law, name="Ohms Law Theory Test")
    
    add_theory_test_question(theorytest=ohms_law_theory_test,
                             question="A common DC power supply usually has how many terminals?",
                             answer_one="1", answer_two="2",
                             answer_three="3", answer_four="4",
                             correct_answer_number=1,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    add_theory_test_question(theorytest=ohms_law_theory_test,
                             question="When using a voltmeter, measurments should be taken in...",
                             answer_one="Series", answer_two="Parallel",
                             answer_three="", answer_four="",
                             correct_answer_number=2,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    add_theory_test_question(theorytest=ohms_law_theory_test,
                             question="When using an ammeter, measurements should be taken in...",
                             answer_one="Series", answer_two="Parallel",
                             answer_three="", answer_four="",
                             correct_answer_number=1,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    add_theory_test_question(theorytest=ohms_law_theory_test,
                             question="Which one of these variables is not found in Ohm's Law?",
                             answer_one="Current", answer_two="Power",
                             answer_three="Resistance", answer_four="Voltage",
                             correct_answer_number=2,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    
    # Ohms law simulation
    ohms_law_simulation = add_simulation(lab=ohms_law, name="Ohms Law Simulation")
    
    add_simulation_element(simulation=ohms_law_simulation,
                           name="ohms law simulation 1", number=1,
                           text_input="Using  a circuit similator, build the following circuit. Measure \(I_R(DMM)\) for the following " +
                           "values of \(V_R\): 0 V, 2 V, 4 V, 6 V, 8 V, and 10 V. ",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=ohms_law_simulation,
                           name="ohms law simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_I/Lab01/fig08.jpg', equation_input="", video_input="", 
                           element_type='image')
    
    # Ohms law simulation test
    ohms_law_simulation_test = add_simulation_test(lab=ohms_law,
                                                   name="Ohms Law Simulation Test")
    
    add_simulation_test_question(simulationtest=ohms_law_simulation_test,
                                 question="What is the measured current through IR when VB = 2 V?",
                                 answer_one="5 mA", answer_two="10 mA",
                                 answer_three="15 mA", answer_four="20 mA",
                                 correct_answer_number=4,
                                 correct_response="This is why...",
                                 incorrect_response="This is a hint why...")
    add_simulation_test_question(simulationtest=ohms_law_simulation_test,
                                 question="What is the measured current through IR when VB = 4 V?",
                                 answer_one="5 mA", answer_two="10 mA",
                                 answer_three="15 mA", answer_four="20 mA",
                                 correct_answer_number=3,
                                 correct_response="This is why...",
                                 incorrect_response="This is a hint why...")
    add_simulation_test_question(simulationtest=ohms_law_simulation_test,
                                 question="What is the measured current through IR when VB = 6 V?",
                                 answer_one="5 mA", answer_two="10 mA",
                                 answer_three="15 mA", answer_four="20 mA",
                                 correct_answer_number=2,
                                 correct_response="This is why...",
                                 incorrect_response="This is a hint why...")
    add_simulation_test_question(simulationtest=ohms_law_simulation_test,
                                 question="What is the measured current through IR when VB = 8 V?",
                                 answer_one="5 mA", answer_two="10 mA",
                                 answer_three="15 mA", answer_four="20 mA",
                                 correct_answer_number=1,
                                 correct_response="This is why...",
                                 incorrect_response="This is a hint why...")
    
    # Ohms law hardware
    ohms_law_hardware = add_hardware(lab=ohms_law, name="Ohms Law Hardware")
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 1", number=1,
                         text_input="The purpose of this laboratory exercise is to acquaint you with the equipment, so do " +
                         "not rush. If you are a member of a squad, don't let one individual make all the measurements. " +
                         "You must become comfortable with the instruments if you expect to perform your future job " +
                         "function in a professional manner. Read the instruments carefully. The more accurate a reading, " +
                         "the more accurate the results obtained. One final word of caution. For obvious reasons, " +
                         "do not make network changes with the power on! If you have any questions about the procedure, " +
                         "be sure to contact your instructor.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 2", number=2,
                         text_input="<h4>Part 1. Setting the Output Voltage of a DC Power Supply with a DMM and VOM</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 3", number=3,
                         text_input="<b>(a)</b> Connect the DMM to the DC power supply as shown in Fig. 7.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 4", number=4,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/fig07.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 5", number=5,
                         text_input="Figure 7",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 6", number=6,
                         text_input="Using the DMM, set the power supply to the voltage levels \(E_{AB}\) appearing in Table 1. " +
                         "Ignore the meter on the supply when setting the voltage levels. For each setting, choose the scope of the DMM " +
                         "that will result in the highest degree of accuracy. Once a particular level is set, remove the DMM and measure the same " +
                         "voltage with the VOM using the scale of the meter that results in the most accurate reading. Do not be " +
                         "influenced by the level set with the DMM. Simply remove the DMM from the supply when the voltage " +
                         "\(E_{AB}\) is set and measured the terminal voltage with the VOM.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 7", number=7,
                         text_input="",
                         image_input=None, equation_input="", video_input="", 
                         element_type='table')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 8", number=8,
                         text_input="Table 1",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 9", number=9,
                         text_input="Calculate the magnitude of the percent difference between the DMM setting and the " +
                         "VOM reading using the following formula and complete Table 1.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 10", number=10,
                         text_input="",
                         image_input=None, equation_input='\\mbox{% Difference} = \\frac{DMM - VOM}{DMM}\\times 100\\%\\hspace{10mm}\\mbox{Eq. 2}', video_input="", 
                         element_type='latex')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 1", number=1,
                         text_input="Is the magnitude of the percent difference for each level sufficiently small " +
                         "to verify the fact that the reading of one meter will be very close to the other even though " +
                         "one is analog and the other is digital?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 11", number=11,
                         text_input="<b>(b)</b> This part of the experiment will provide some additional practice in the " +
                         "use of the DMM and VOM. The supply voltage will now be set by the VOM and the setting checked by the " +
                         "DMM. Set the voltage levels indicated in Table 2 with the VOM and then measure the set lebel with the DMM " +
                         "For each setting, calculate the magnitude of the percent difference using Eq. (3) and complete " +
                         "Table 2",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 12", number=12,
                         text_input="",
                         image_input=None, equation_input='\\mbox{% Difference} = \\frac{VOM - DMM}{VOM}\\times 100\\%\\hspace{10mm}\\mbox{Eq. 3}', video_input="", 
                         element_type='latex')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 13", number=13,
                         text_input="",
                         image_input=None, equation_input="", video_input="", 
                         element_type='table')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 14", number=14,
                         text_input="Table 2",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 15", number=15,
                         text_input="How do the magnitudes of the percent differences of Table 2 compare to those of Table 1? Can you make any general " +
                         "conclusions based on the results?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 16", number=16,
                         text_input="<b>(c)</b> We will now investigate the effect of reversing the leads of the meter when measuring a voltage. " +
                         "Using the setup of Fig. 7, reset the voltage \(E_{AB}\) to 5 V using the DMM. " +
                         "Then disconnect the DMM and connect the red, or \(V-\Omega\), lead to the \(B\) terminal and " +
                         "the black, or COM, lead to the \(A\) terminal. What is the effect on the reading?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 17", number=17,
                         text_input="Repeat the previous reading using the VOM and the connections just described. " +
                         "What is the effect on the reading?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 18", number=18,
                         text_input="<b>(d)</b> Based on the results of parts 1(a)-(c), which meter do you prefer to use? " +
                         "Does one appear more accurate? What are the relative advantages of one compared to the other? " +
                         "Answer each question in sentence form.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 19", number=19,
                         text_input="<h4>Part 2. Ohm's Law (Determining <i>I</i>)</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 20", number=20,
                         text_input="In this section, the current of a dc series circuit will be determined by a direct " +
                         "measurement and using Ohm's law. In practice, most current levels are determined using Ohm's " +
                         "law and a measured voltage level to avoid having to break the circuit to insert the ammeter. " +
                         "However, one should be aware of the procedure associated with using an ammeter, and one " +
                         "should feel confident that the measured value and that calculated using Ohm's law are very " +
                         "close in magnitude.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 21", number=21,
                         text_input="<b>(a)</b> Construct the Circuit in Fig. 8 using the DMM as a milliammeter. Be sure the " +
                         "milliammeter is connected so that conventional current enters the red terminal of the meter and " +
                         "leaves the black terminal to ensure a positive reading. Insert the measured value of R in " +
                         "Fig. 8 into Table 3. Initially set the DMM on the high milliammeter scale. For most DMMs, " +
                         "the red or positive lead must be moved from the \(V-\Omega\) connection to the \(A\) terminal of the meter. " +
                         "The COM connection remains the same.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 22", number=22,
                         text_input="Adjust the power supply until \(V_R\) = 2 V (the voltage across the resistor, not the " +
                         "supply voltage) using the COM to monitor \(V_R\). Be sure the red lead is connected to the point " +
                         "of higher potential (the terminal that conventional current enters) and the black lead is " +
                         "connected to the point of lower potential (the terminal that conventional current leaves). " +
                         "You may find that searching for the best scale for the milliammeter will affect the voltage " +
                         "across \(V_R\), since changing ammeter scales will change the internal resistance of the milliammeter. " +
                         "Find a scale that provides a reading of good accuracy with \(V_R\) set at the required 2 V.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 23", number=23,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/fig08.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 24", number=24,
                         text_input="Figure 8",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 25", number=25,
                         text_input="In Table 3, record the measured value of \(I_R\) from the DMM. Then calculate " +
                         "the level of \(I_R\) using Ohm's law and the measured resistor value and record in the table " +
                         "below using mA as the unit of measurement. Finally, determine the magnitude of the " +
                         "percent difference from the following equation and complete the line for \(V_R\) = 2 V in Table 3.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 26", number=26,
                         text_input="",
                         image_input=None, equation_input='\\mbox{% Difference} = \\frac{I_R(DMM) - I_R(\\mbox{Ohm\'s Law})}{I_R(DMM)}\\times 100\\%\\hspace{10mm}\\mbox{Eq. 4}', video_input="", 
                         element_type='latex')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 27", number=27,
                         text_input="Repeat this procedure for the other levels of \(V_R\) in the table below. Note that when \(V_R\) = 0 V, \(I_R\) = 0 mA and the percent difference = 0%",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 28", number=28,
                         text_input="",
                         image_input=None, equation_input="", video_input="", 
                         element_type='table')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 29", number=29,
                         text_input="Table 3",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 30", number=30,
                         text_input="Comment on the level of percent difference in Table 3. Are the percent differences " +
                         "sufficiently small to establish firmly the fact that the current determined by Ohm's Law will be " +
                         "very close (if not equal) to that measured directly? Answer the question in sentence form.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 31", number=31,
                         text_input="<h4>Part 3. Plotting Ohms Law</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 32", number=32,
                         text_input="<b>(a)</b> Using the data (measured values) of Table 3, plot \(I\) (DMM) versus \(V_R\) " +
                         "(VOM) on Graph 1. Clearly indicate each data point on the graph. Also label the curve as \(R = 1 k\Omega\). ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 33", number=33,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/graph01.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 34", number=34,
                         text_input="Graph 1",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 35", number=35,
                         text_input="<b>(b)</b> Once the curve of part (a) is drawn, the level of resistance can be determined " +
                         "at any level of voltage or current.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 36", number=36,
                         text_input="For instance, at \(I_R\) = 5.6 mA, draw a horizontal line from the vertical axis to the curve. " +
                         "Then draw a line down from the intersection to the horizontal voltage axis. Record the level of \(V_R\) " +
                         "in Table 4. Calculate the resistance using Ohm's Law and insert in Table 4.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 37", number=37,
                         text_input="Using a similar procedure, determine the level of \(V_R\) corresponding to \(I_R\) " +
                         "= 1.2 mA. Determine the value of \(R\) using Ohm's Law anc ompare with the level at \(I_R\) = 5.6 mA. " +
                         "Record both results in Table 3.4.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 38", number=38,
                         text_input="To continue, determine the level of \(I_R\) corresponding to \(V_R\) = 8.3 V and calculate " +
                         "the resulting resistance level. Again, record both results in Table 3.4.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 39", number=39,
                         text_input="",
                         image_input=None, equation_input="", video_input="", 
                         element_type='table')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 40", number=40,
                         text_input="Table 4",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 41", number=41,
                         text_input="<b>(c)</b> The resistance level also can be determined from the equation: ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 42", number=42,
                         text_input="",
                         image_input=None, equation_input='R = \\frac{\\Delta V_R}{\\Delta I_R}\\hspace{10mm}\\mbox{Eq. 5}', video_input="", 
                         element_type='latex')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 43", number=43,
                         text_input="where \(\Delta V\) is the change in \(V\) due to a change in current \(\Delta I\) " +
                         "(or vice versa). as demonstrated in Fig. 9.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 44", number=44,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/fig09.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 45", number=45,
                         text_input="Figure 9",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 46", number=46,
                         text_input="For instance, if we choose \(\Delta I_R\) = 6 mA - 2 mA = 4 mA for the \(1 k\Omega\) resistor " +
                         "of Graph 1, we can determine the resulting \(\Delta V_R\) and apply Eq. 4. That is, draw a horizontal " +
                         "line from \(I_R\) = 2 mA and 6 mA on the vertical axis to the curve and then drop lines down to the " +
                         "horizontal axis to determine the corresponding values of \(V_R\). Find the resulting change in " +
                         "\(V_R\) and apply equation 5.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 47", number=47,
                         text_input="Determine \(\Delta V_R\) for \(\Delta I_R\) = 6 mA - 2 mA = 4 mA for the \(1 k\Omega\) resistor " +
                         "of Graph 1 and record in Table 5.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 48", number=48,
                         text_input="Determine \(R\) using Eq. 5 and record in Table 5.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 49", number=49,
                         text_input="Determine \(\Delta V_R\) for \(\Delta I_R\) = 4.6 mA - 3.2 mA = 1.4 mA for the \(1 k\Omega\) resistor " +
                         "of Graph 1 and record in Table 5.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 50", number=50,
                         text_input="Determine \(R\) using Eq. 5 and record in Table 5.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 51", number=51,
                         text_input="",
                         image_input=None, equation_input="", video_input="", 
                         element_type='table')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 52", number=52,
                         text_input="Table 5",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 53", number=53,
                         text_input="<b>(d)</b> The slope of a curve is related to the resistance by",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 54", number=54,
                         text_input="",
                         image_input=None, equation_input='\\mbox{Slope} = m =\\frac{\Delta y}{\Delta x}=\\frac{\Delta I_R}{\Delta V_R}=\\frac{1}{R}\\hspace{10mm}\\mbox{Eq. 6}', video_input="", 
                         element_type='latex')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 55", number=55,
                         text_input="revealing that the smaller the resistance, the steeper the slope, or the more the resistance, " +
                         "the less the slope",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 56", number=56,
                         text_input="Determine the slope for the \(1 k\Omega\) resistor in mS using the measured resistor value from Fig " +
                         "8 and record in Table 6.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 57", number=57,
                         text_input="",
                         image_input=None, equation_input="", video_input="", 
                         element_type='table')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 58", number=58,
                         text_input="Table 6",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 59", number=59,
                         text_input="<h4>Part 4. Plotting R = 3.3k\(\Omega\)</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 60", number=60,
                         text_input="<b>(a)</b> Reconstruct the circuit in Fig. 8 using \(R\) = 3.3 \(k\Omega\). Insert the measured " +
                         "value of \(R\) in Table 5 and use this value for all the calculation.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 61", number=61,
                         text_input="Using the procedure described in Part 2, complete Table 7.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 62", number=62,
                         text_input="",
                         image_input=None, equation_input="", video_input="", 
                         element_type='table')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 63", number=63,
                         text_input="Table 7",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 64", number=64,
                         text_input="<b>(b)</b> Using the data of Table 7, plot \(I_R(DMM)\) versus \(V_R(DMM)\) on Graph 2. Clearly " +
                         "indicate each data point on the graph. Also label the curve as \(R = 3.3 k\Omega\).",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 65", number=65,
                         text_input="",
                         image_input='VLA/courses/EE_Science_I/Lab01/graph02.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 66", number=66,
                         text_input="Graph 2",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 67", number=67,
                         text_input="<b>(c)</b> Determine the level of \(V_R\) corresponding to \(I_R\) = 2.4 mA and calculate the resistance " +
                         "using Eq 1. Record both results in Table 8.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 68", number=68,
                         text_input="<b>(d)</b> Determine the level of \(\Delta V_R\) corresponding to \(\Delta I_R\) = 2.2 mA - 1.4 mA = 0.8 mA and calculate " +
                         "\(R\) using Eq 5. Record both results in Table 8.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 69", number=69,
                         text_input="",
                         image_input=None, equation_input="", video_input="", 
                         element_type='table')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 70", number=70,
                         text_input="Table 8",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 71", number=71,
                         text_input="<b>(e)</b> Determine the slope of the 3.3 \(k\Omega\) resistor using the measured value (from Table 7) and " +
                         "Eq 6 and record in Table 6.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ohms_law_hardware, name="ohms law hardware 72", number=72,
                         text_input="How does the magnitude of the slope compare to the magnitude determined for the 1 \(k\Omega\) resistor? "
                         + "Is the following conclusion verified: The larger the resistance, the less the slope?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    # Ohms law Results
    ohms_law_results = add_results(lab=ohms_law, name="Ohms Law Results")

    add_results_questions(results=ohms_law_results,
                          question="Plot the linear curve for 100 \(\Omega\) and 10 \(k\Omega\) resistors.",
                          answer_text="",
                          answer_type='text')
    add_results_questions(results=ohms_law_results,
                          question="As the resistance increases, does the slope defined by \(m=\Delta I_r/\Delta V_R\) " +
                          "increase or decrease?",
                          answer_text="",
                          answer_type='text')
    add_results_questions(results=ohms_law_results,
                          question="Under ideal conditions, is the plot of \(I_R\) versus \(V_R\) for a fixed resistor " +
                          "always a straight line that intersects \(I_R\) = 0 A and \(V_R\) = 0 V?",
                          answer_text="",
                          answer_type='text')
    add_results_questions(results=ohms_law_results,
                          question="Which two terminals of a DC power supply must always be connected to obtain the desired voltage?",
                          answer_text="",
                          answer_type='text')
    
    # Ohms law Lab test
    ohms_law_lab_test = add_lab_test(lab=ohms_law, name="Ohms Law Laboratory Test")
    
    add_lab_test_question(labtest=ohms_law_lab_test,
                             question="A common DC power supply usually has how many terminals?",
                             answer_one="1", answer_two="2",
                             answer_three="3", answer_four="4",
                             correct_answer_number=1,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    add_lab_test_question(labtest=ohms_law_lab_test,
                             question="When using a voltmeter, measurments should be taken in...",
                             answer_one="Series", answer_two="Parallel",
                             answer_three="", answer_four="",
                             correct_answer_number=2,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    add_lab_test_question(labtest=ohms_law_lab_test,
                             question="When using an ammeter, measurements should be taken in...",
                             answer_one="Series", answer_two="Parallel",
                             answer_three="", answer_four="",
                             correct_answer_number=1,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    add_lab_test_question(labtest=ohms_law_lab_test,
                             question="Which one of these variables is not found in Ohm's Law?",
                             answer_one="Current", answer_two="Power",
                             answer_three="Resistance", answer_four="Voltage",
                             correct_answer_number=2,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")

    # Print out what we have added to the user.
    for c in Course.objects.all():
        for l in Laboratory.objects.filter(course=c):
            print "- {0} - {1}".format(str(c), str(l))

# Add course, lab, lab section (theory, simulation, hardware)
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