import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
-EE Science II Course

LABORATORIES:

'''

    ###
    # EE Science II Lab 11: Introduction to Amplitude Modulation
    ###
def populate(ee_science_ii):
    amplitude_modulation = add_lab(course=ee_science_ii, name="Introduction to Amplitude Modulation",
                                  start_date=timezone.now(), due_date=timezone.now(),
                                  lab_number=11)

    add_lab_objective(lab=amplitude_modulation,
                      objective="In this lab, you will build a simple Amplitude Modulation (AM) radio. We will build the modulator in Matlab and use the Digilent board "+
                      "to build the demodulator. Once you have read about AM modulation, perform the following steps. The general goals are:")
                      
    add_lab_objective(lab=amplitude_modulation,
                      objective="Record an audio signal,")
    add_lab_objective(lab=amplitude_modulation,
                      objective= "AM modulate the audio signal (using Matlab),")
    add_lab_objective(lab=amplitude_modulation,
                      objective= "Use your AM modulated signal as voltage function source on your Digilent board,")
    add_lab_objective(lab=amplitude_modulation,
                      objective= "Demodulate the AM voltage using the given circuit, and ")
    add_lab_objective(lab=amplitude_modulation,
                      objective="Determine that your signal has been demodulated by playing the output through a speaker.")


    # Introduction to Amplitude Modulation Theory 
    am_theory = add_theory(lab=amplitude_modulation, name="Introduction to Amplitude Modulation Theory")
    
    add_theory_element(theory=am_theory, name="am theory 1", number=1,
                       text_input="For this lab, you need to do a literature review on Amplitude Modulation. "+
                       "However, we shall introduce the primary concept of AM here. "+
                       "There are two motivating reasons for modulation technique. The first reason is portability "+
                       ". To send our low frequency voice signal (bandwidth 4 kHz) over a long distance, we would need "+
                       "a huge (impractical size) antenna and very high transmitting power. On the other hand, for transmitting "+
                       "high frequency signal, it requires reduced size antenna. Modulation technique provides the advantage "+
                       "of using high frequency (carrier) signal to carry low frequency voice signal over a long "+
                       "distance efficiently. The second motivating reason for modulation is multiplexing. Multiple "+
                       "users can communicate using the same medium because of modulation.",
                       image_input=None, equation_input="", video_input="", element_type='text')

    add_theory_element(theory=am_theory, name="am theory 2", number=2,
                       text_input="In amplitude modulation technique, the modulating signal (information signal/baseband signal) "+
                       "varies the amplitude of the carrier sine wave. The instantaneous value of the carrier amplitude changes "+
                       "in accordance with amplitude and frequency variation of the modulating signal. Fig. 1 shows a modulated "+
                       "carrier. The carrier frequency remains constant during modulation, "+
                       "but the amplitude varies in accordance with modulating signal.",
                       image_input=None, equation_input="", video_input="", element_type='text')

  
    add_theory_element(theory=am_theory, name="am theory 3", number=3,
                       text_input="",
                       image_input='VLA/courses/EE_Science_II/Lab11/fig01.jpg', equation_input="", video_input="",
                       element_type='image')

    add_theory_element(theory=am_theory, name="am theory 4", number=4,
                       text_input="Figure 1",
                       image_input=None, equation_input="", video_input="", 
                       element_type='caption')

    add_theory_element(theory=am_theory, name="am theory 5", number=5,
                       text_input="Consider two sinusoidal waves for carrier and modulating signal expressed by:",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')

    add_theory_element(theory=am_theory, name="am theory 6", number=6,
                       text_input="",
                       image_input=None, equation_input="v_c = V_c\sin (2\pi {f_c}t)", video_input="", 
                       element_type='latex')

    add_theory_element(theory=am_theory, name="am theory 7", number=7,
                       text_input="",
                       image_input=None, equation_input="v_m = V_m\sin (2\pi {f_m}t)", video_input="", 
                       element_type='latex')

    add_theory_element(theory=am_theory, name="am theory 8", number=8,
                       text_input="'c' denotes carrier and 'm' denotes modulating signal. Instantaneous and "+
                       "peak value of signal are denoted by v and V, while f  is the frequency. These two waves "+
                       "are multiplied in AM modulator as shown in Fig. 2",
                       image_input=None, equation_input="", video_input="",
                       element_type='text')

    add_theory_element(theory=am_theory, name="am theory 9", number=9,
                       text_input="",
                       image_input='VLA/courses/EE_Science_II/Lab11/fig02.jpg', equation_input="", video_input="",
                       element_type='image')

    add_theory_element(theory=am_theory, name="am theory 10", number=10,
                       text_input="Figure 2",
                       image_input=None, equation_input="", video_input="", 
                       element_type='caption')

    add_theory_element(theory=am_theory, name="am theory 11", number=11,
                       text_input="From frequency domain point of view, the amplitude modulation generates new signal at different frequencies, "+
                       "which are called side band. More specifically, the sidebands occur at "+
                       "frequencies that are the sum and difference of the carrier and modulating frequencies. The upper sideband \(f_{USB}\) "+
                       "and lower sideband \(f_{LSB}\) are computed as, ",
                       image_input=None, equation_input="", video_input="",
                       element_type='text')
    

    add_theory_element(theory=am_theory, name="am theory 12", number=12,
                       text_input="",
                       image_input=None, equation_input="f_{USB} = f_c + f_m", video_input="", 
                       element_type='latex')

    add_theory_element(theory=am_theory, name="am theory 13", number=13,
                       text_input="",
                       image_input=None, equation_input="f_{LSB} = f_c - f_m", video_input="", 
                       element_type='latex')

    add_theory_element(theory=am_theory, name="am theory 14", number=14,
                       text_input="The total bandwidth is simply the difference between the upper and lower sideband frequencies:",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')
                       
    add_theory_element(theory=am_theory, name="am theory 15", number=15,
                       text_input="",
                       image_input=None, equation_input="BW = f_{USB} - f_{LSB}", video_input="", 
                       element_type='latex')

    add_theory_element(theory=am_theory, name="am theory 16", number=16,
                       text_input="The bandwidth of an AM signal is twice the highest frequency in the modulating signal:",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')
                       
    add_theory_element(theory=am_theory, name="am theory 17", number=17,
                       text_input="",
                       image_input=None, equation_input="BW = 2f_m", video_input="", 
                       element_type='latex')

    add_theory_element(theory=am_theory, name="am theory 18", number=18,
                       text_input="An AM modulated signal can be demodulated using an envelope detector. The envelope "+
                       "detector takes the high frequency signal as input and outputs the envelope of the original signal. "+
                       "A simple envelope detector can be a diode detector shown in Fig. 3. A diode detector is simply a diode "+
                       "between the input and output of a circuit, connected to a resistor and capacitor in parallel from the "+
                       "output of the circuit to the ground. If the resistor and capacitor are correctly chosen, the output "+
                       "of this circuit should approximate "+
                       "a voltage-shifted version of the original (baseband) signal. "+
                       "A simple filter can then be applied to filter out the DC bias.",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')

    add_theory_element(theory=am_theory, name="am theory 19", number=19,
                       text_input="",
                       image_input='VLA/courses/EE_Science_II/Lab11/fig03.jpg', equation_input="", video_input="",
                       element_type='image')

    add_theory_element(theory=am_theory, name="am theory 20", number=20,
                       text_input="Figure 3",
                       image_input=None, equation_input="", video_input="", 
                       element_type='caption')

    add_theory_element(theory=am_theory, name="am theory 21", number=21,
                       text_input="This is a brief description on amplitude modulation. This review will help you in the test. "+
                       "For completing the lab, do more research on amplitude modulation.",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')

    add_theory_element(theory=am_theory, name="am theory 22", number=22,
                       text_input="You can find a good lecture "+
                       "<a href=\"http://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/video-lectures/lecture-13-continuous-time-modulation\">HERE</a>.",
                       image_input=None, equation_input="", video_input="", 
                       element_type='text')
                     
    # Introduction to Amplitude Modulation Theory test
    am_theory_test = add_theory_test(lab=amplitude_modulation, name="Introduction to Amplitude Modulation Theory Test")
                 
    add_theory_test_question(theorytest=am_theory_test,
                             question="Consider an AM modulated signal expressed by the signal "+
                             "\(v_{mod} = V_c\sin 2\pi (600000)\pi t + V_m(\sin (4000)\pi t)(\sin 2\pi (600000)t)\) "+
                             "What is the carrier frequency?",
                             answer_one="600 kHz", answer_two="4 kHz",
                             answer_three="300 kHz", answer_four="2 kHz",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")


    add_theory_test_question(theorytest=am_theory_test,
                             question="Assume that a 400 Hz tone is modulates a 300 kHz carrier. What are the upper and lower sidebands?",
                             answer_one="700 Hz, 100 Hz", answer_two="300.4 kHz, 100 kHz",
                             answer_three="300.4 kHz, 299.6 kHz", answer_four="300 kHz, 100 Hz",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")


    add_theory_test_question(theorytest=am_theory_test,
                             question="If the carrier frequency is 2.8 MHz "+
                             "and the modulating signal frequency is 3 kHz, what is the bandwidth?",
                             answer_one="3.6MHz", answer_two="6kHz",
                             answer_three="2.803MHz", answer_four="2.797MHz",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=am_theory_test,
                             question="If the carrier voltage is 9V and the modulating signal voltage is 7.5V. What is the modulation index?",
                             answer_one="16.5", answer_two="2.5",
                             answer_three="0.83", answer_four="63",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_theory_test_question(theorytest=am_theory_test,
                             question="An envelope detector works as what type of filter??",
                             answer_one="Low pass", answer_two="High pass",
                             answer_three="Band pass", answer_four="Band stop",
                             correct_answer_number=1,
                             correct_response="",
                             incorrect_response="")
   
  
    # Introduction to Amplitude Modulation Simulation
    am_simulation = add_simulation(lab=amplitude_modulation, name="Amplitude Modulation Simulation")
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 1", number=1,
                           text_input=" First, You should read all about amplitude modulation at <a href=\"http://en.wikipedia.org/wiki/Amplitude_modulation\">Amplitude Modulation</a>.",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 2", number=2,
                           text_input=" Record an audio signal using any means you like. The only rules are that "+
                           "it must be saved as a mono (single channel, NOT stereo) .wav with a sampling rate of 44.1kHz. "+
                           "Keep it to ten seconds duration or less.",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 3", number=3,
                           text_input="Import your audio into Matlab using this command: ",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 4", number=4,
                           text_input="\(\\verb|[x,fs] = wavread('filename.wav');|\)",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 5", number=5,
                           text_input="You can listen to your audio file in Matlab by typing",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 6", number=6,
                           text_input="\(\\verb|soundsc(x,fs);|\)",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 7", number=7,
                           text_input="Lowpass filter the signal down to 2000 Hz. There are several ways to do this but "+
                           "a simple low-budget way is to reduce the sampling rate to 4000 Hz. In that process, Matlab will "+
                           "massively low-pass filter the signal:",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 8", number=8,
                           text_input="\(\\verb|y = resample(x,4000,44.1e3);|\)",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 9", number=9,
                           text_input="Now that your signal has been lowpass filtered, bring the sampling rate back up. We cannot bring "+
                           "it back up to our original value of 44.1 kHz since the Waveforms software will not play back signals at that frequency. "+
                           "So instead we shall pick the closest value that Waveforms supports: 50kHz:.",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 10", number=10,
                           text_input="\(\\verb|fs2 = 50e3;|\)",
                           image_input=None, equation_input= "", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 11", number=11,
                           text_input="\(\\verb|z = resample(y,50e3,4000);|\)",
                           image_input=None, equation_input= "", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 12", number=12,
                           text_input="AM modulate your signal by multiplying it by a 10 kHz cosine:",
                           image_input=None, equation_input= "", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 13", number=13,
                           text_input="\(\\verb|t = (1:length(z))/fs;|\)",
                           image_input=None, equation_input= "", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 14", number=14,
                           text_input="\(\\verb|t = reshape(t,size(z));|\)",
                           image_input=None, equation_input= "", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 15", number=15,
                           text_input="\(\\verb|a = (1+z).*cos(2*pi*10e3*t);|\)",
                           image_input=None, equation_input= "", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=am_simulation,
                           name="amplitude modulation simulation 16", number=16,
                           text_input=" Signal a is now your AM modulated signal. Export it as a .wav file and import it into Digilent Waveforms "+
                           "to create an Arbitrary Waveform. Be sure to use the 'Player, tab under the Basic tab of the arbitrary waveform software. "+
                           "Also, be sure to set the 'frequency' to 50 kHz to match the frequency of the .wav file.",
                           image_input=None, equation_input= "", video_input="", 
                           element_type='text')
                   

    
    # Introduction to Amplitude Modulation Hardware
    am_hardware = add_hardware(lab=amplitude_modulation, name="Introduction to Amplitude Modulation Hardware")

    add_hardware_element(hardware=am_hardware, name=" Introduction to amplitde modulation hardware 1", number=1,
                         text_input="Build the circuit shown here. Select values for R and C based on your research about AM demodulation.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    add_hardware_element(hardware=am_hardware, name="am hardware 2", number=2,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab11/fig03.jpg', equation_input="", video_input="",
                         element_type='image')

    add_hardware_element(hardware=am_hardware, name="am hardware 3", number=3,
                         text_input="Figure 4",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
                       
    add_hardware_element(hardware=am_hardware, name="amplitde modulation hardware 4", number=4,
                         text_input="Take the signal output and put it into the little speaker "+
                         "that should have been included in your parts kit. Can you hear your audio signal? Why? Why not?.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')


       

    # Introduction to Amplitude Modulation Results
    am_results = add_results(lab=amplitude_modulation, name="Introduction to Amplitude Modulation Results")

    add_results_questions(results=am_results,
                          question="Write a standard report explaining what you did and presenting your measurements, calculations, "+
                          "and observations. This is a two-week long lab. Submit it to our <a href=\"https://blackboard.temple.edu\">blackboard</a> in due date (see syllabus for submission guideline).",
                          answer_text="",
                          answer_type='text')



    # Introduction to Amplitude Modulation lab test
    am_lab_test = add_lab_test(lab=amplitude_modulation, name="Introduction to Amplitude Modulation Theory Test")

    add_lab_test_question(labtest=am_lab_test,
                             question="Consider an AM modulated signal expressed by the signal "+
                             "\(v_{mod} = V_c\sin (600000)\pi t + V_m(\sin (4000)\pi t)(\sin 2\pi (600000)t)\) "+
                             "What is the carrier frequency?",
                             answer_one="600kHz", answer_two="300kHz",
                             answer_three="4kHz", answer_four="2kHz",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")
                        
    add_lab_test_question(labtest=am_lab_test,
                             question="Assume that a 400 Hz tone is modulates a 300 kHz carrier. What are the upper and lower sidebands?",
                             answer_one="700 Hz, 100 Hz", answer_two="300.4 kHz, 100 kHz",
                             answer_three="300 kHz, 100 Hz", answer_four="300.4 kHz, 299.6 kHz",
                             correct_answer_number=4,
                             correct_response="",
                             incorrect_response="")


    add_lab_test_question(labtest=am_lab_test,
                             question="If the carrier frequency is 2.8 MHz "+
                             "and the modulating signal frequency is 3 kHz, what is the bandwidth?",
                             answer_one="3.6MHz", answer_two="2.803MHz",
                             answer_three="6kHz", answer_four="2.797MHz",
                             correct_answer_number=3,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=am_lab_test,
                             question="If the carrier voltage is 9V and the modulating signal voltage is 7.5V. What is the modulation index?",
                             answer_one="16.5", answer_two="0.83",
                             answer_three="2.5", answer_four="63",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")

    add_lab_test_question(labtest=am_lab_test,
                             question="An envelope detector works as what type of filter??",
                             answer_one="High pass", answer_two="Low pass",
                             answer_three="Band pass", answer_four="Band stop",
                             correct_answer_number=2,
                             correct_response="",
                             incorrect_response="")


    # Print out what we have added to the user.
    #for c in Course.objects.all():
    #    for l in Laboratory.objects.filter(course=c):
    #        print "- {0} - {1}".format(str(c), str(l))
            

    # Add labpermissions for new lab for each user 
    for u in User.objects.all():
        add_new_lab_permission(user=u, lab=amplitude_modulation)
    
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
