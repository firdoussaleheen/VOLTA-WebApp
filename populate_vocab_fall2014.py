# -*- coding: utf-8 -*-
import os
from django.utils import timezone

'''
Script to populate the complete Vocabulary Domain Database for Circuits

Creates one VocabDomain, 11 VocabTopics:
1.  Circuit elements and equipment (resistor, breadboard, dc source)
2.  Action word (compute, change, use)
3.  Question word (why, what, how)
4.  Problem word (wrong, don't, cannot)
5.  Circuit concepts (resistance, power, energy)
6.  Other, useful (positive, gain, division, unit)
7.  Other, not useful (password, )
8.  Circuit Laws (thevenin, conservation, superposition)
9.  Circuit diagram and measurements (series, parallel, rms, ground)
10.  Math words (sum, difference, equivalent)
11. Units (ohm, watt, joule)
11. Help

Also adds Synonyms, and Defintions

Add RuleBase with Questions and Answers
'''

def populate():
    
    circuits_domain = add_vocab_domain(name = 'Circuits')
    
    # Circuit ELements and Equipment
    topic_elements = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Elements and Equipment",
                    def_useful=True)
    
    resistor_node = add_node("Resistor",
                    definition="A resistor is a passive two-terminal electrical component that implements electrical resistance " +
                    "as a circuit element. Resistors act to reduce current flow, and, at the same time, act to lower voltage " +
                    "levels within circuits. Resistors may have fixed resistances or variable resistances, such as those found " +
                    "in thermistors, varistors, trimmers, photoresistors, humistors, piezoresistors and potentiometers.",
                    topic=topic_elements)
    add_synonym("Res", node=resistor_node)
    add_synonym("R", node=resistor_node)
    add_synonym("Ohm", node=resistor_node)
    add_synonym("Conductor", node=resistor_node)
    
    capacitor_node = add_node("Capacitor",
                    definition="A capacitor (originally known as a condenser) is a passive two-terminal electrical component used " +
                    "to store energy electrostatically in an electric field. The forms of practical capacitors vary widely, " +
                    "but all contain at least two electrical conductors (plates) separated by a dielectric (i.e., insulator). " +
                    "The conductors can be thin films of metal, aluminum foil or disks, etc. The 'nonconducting' dielectric acts to " +
                    "increase the capacitor's charge capacity. A dielectric can be glass, ceramic, plastic film, air, paper, mica, etc. " +
                    "Capacitors are widely used as parts of electrical circuits in many common electrical devices. Unlike a " +
                    "resistor, an ideal capacitor does not dissipate energy. Instead, a capacitor stores energy in the form of an electrostatic field between its plates.",
                    topic=topic_elements)
    add_synonym("Cap", node=capacitor_node)
    add_synonym("F", node=capacitor_node)
    add_synonym("Farad", node=capacitor_node)
    
    inductor_node = add_node("Inductor",
                    definition="An inductor, also called a coil or reactor, is a passive two-terminal electrical component which " +
                    "resists changes in electric current passing through it. It consists of a conductor such as a wire, usually " +
                    "wound into a coil. When a current flows through it, energy is stored temporarily in a magnetic field in the " +
                    "coil. When the current flowing through an inductor changes, the time-varying magnetic field induces a voltage " +
                    "in the conductor, according to Faraday's law of electromagnetic induction, which opposes the change in current that created it.",
                    topic=topic_elements)
    add_synonym("Ind", node=inductor_node)
    add_synonym("L", node=inductor_node)
    add_synonym("Henry", node=inductor_node)
    add_synonym("H", node=inductor_node)
    
    opamp_node = add_node("OpAmp",
                    definition="An operational amplifier (op-amp) is a DC-coupled high-gain electronic voltage amplifier with a differential input and, usually, a single-ended output. In this configuration, an op-amp produces " +
                       "an output potential (relative to circuit ground) that is typically hundreds of thousands of times larger than the potential difference between its input terminals. Operational amplifiers had their origins " +
                       "in analog computers, where they were used to do mathematical operations in many linear, non-linear and frequency-dependent circuits. Characteristics of a circuit using an op-amp are set by external components " +
                       "with little dependence on temperature changes or manufacturing variations in the op-amp itself, which makes op-amps popular building blocks for circuit design. Op-amps are among the most widely used electronic " +
                       "devices today, being used in a vast array of consumer, industrial, and scientific devices. Op-amps may be packaged as components, or used as elements of more complex integrated circuits.",
                    topic=topic_elements)
    
    dc_source_node = add_node("DC Source",
                              definition="A power supply is an electronic device that supplies electric energy to an electrical load." + 
                              "The primary function of a power supply is to convert one form of electrical energy to another and, as a result, power supplies are sometimes referred to as electric power converters." + 
                              "Some power supplies are discrete, stand-alone devices, whereas others are built into larger devices along with their loads." + 
                              "Examples of the latter include power supplies found in desktop computers and consumer electronics devices." + 
                              "A DC power supply is one that supplies a voltage of fixed polarity (either positive or negative) to its load." +
                              "Depending on its design, a DC power supply may be powered from a DC source or from an AC source such as the power mains.",
                              topic=topic_elements)
    add_synonym("DC Supply", node=dc_source_node)
    add_synonym("Supply", node=dc_source_node)
    add_synonym("Source", node=dc_source_node)
    add_synonym("DCS", node=dc_source_node)
    add_synonym("Battery", node=dc_source_node)
    add_synonym("Cell", node=dc_source_node)
    
    multimeter_node = add_node("Multimeter",
                    definition="A multimeter or a multitester, also known as a VOM (Volt-Ohm meter), is an electronic measuring instrument " +
                    "that combines several measurement functions in one unit. A typical multimeter would include basic features such " +
                    "as the ability to measure voltage, current, and resistance. Analog multimeters use a microammeter whose pointer moves " +
                    "over a scale calibrated for all the different measurements that can be made. Digital multimeters (DMM, DVOM) display the " +
                    "measured value in numerals, and may also display a bar of a length proportional to the quantity being measured. Digital " +
                    "multimeters are now far more common than analog ones, but analog multimeters are still preferable in some cases, for " +
                    "example when monitoring a rapidly varying value.",
                    topic=topic_elements)
    add_synonym("Voltmeter", node=multimeter_node)
    add_synonym("Ammeter", node=multimeter_node)
    add_synonym("Ohmmeter", node=multimeter_node)
    add_synonym("Meter", node=multimeter_node)
    add_synonym("Multim", node=multimeter_node)
    
    func_gen_node = add_node("Function Generator",
                    definition="A function generator is usually a piece of electronic test equipment or software used to generate different " +
                    "types of electrical waveforms over a wide range of frequencies. Some of the most common waveforms produced by the " +
                    "function generator are the sine, square, triangular and sawtooth shapes. These waveforms can be either repetitive or " +
                    "single-shot (which requires an internal or external trigger source). Integrated circuits used to generate waveforms " +
                    "may also be described as function generator ICs.",
                    topic=topic_elements)
    add_synonym("AC Supply", node=func_gen_node)
    add_synonym("Generator", node=func_gen_node)
    add_synonym("AC Source", node=func_gen_node)
    add_synonym("Func Gen", node=func_gen_node)
    
    oscilloscope_node = add_node("Oscilloscope",
                    definition="An oscilloscope, previously called an oscillograph, and informally known as a scope, CRO (for " +
                    "cathode-ray oscilloscope), or DSO (for the more modern digital storage oscilloscope), is a type of " +
                    "electronic test instrument that allows observation of constantly varying signal voltages, usually as a " +
                    "two-dimensional plot of one or more signals as a function of time. Non-electrical signals (such as sound " +
                    "or vibration) can be converted to voltages and displayed.",
                    topic=topic_elements)
    add_synonym("Oscope", node=oscilloscope_node)
    add_synonym("Display", node=oscilloscope_node)
    add_synonym("CRT", node=oscilloscope_node)
    add_synonym("Cathode", node=oscilloscope_node)
    
    spect_anal_node = add_node("Spectrum Analyzer",
                    definition="A spectrum analyzer measures the magnitude of an input signal versus frequency within the full " +
                    "frequency range of the instrument. The primary use is to measure the power of the spectrum of known and " +
                    "unknown signals. The input signal that a spectrum analyzer measures is electrical, however, spectral " +
                    "compositions of other signals, such as acoustic pressure waves and optical light waves, can be considered " +
                    "through the use of an appropriate transducer. Optical spectrum analyzers also exist, which use direct optical " +
                    "techniques such as a monochromator to make measurements.",
                    topic=topic_elements)
    add_synonym("Spectrum", node=spect_anal_node)
    add_synonym("Analyzer", node=spect_anal_node)
    add_synonym("Sweep", node=spect_anal_node)
    add_synonym("SA", node=spect_anal_node)
    
    diode_node = add_node("Diode",
                    definition="In electronics, a diode is a two-terminal electronic component with asymmetric conductance; it has " +
                    "low (ideally zero) resistance to current in one direction, and high (ideally infinite) resistance in the other. " +
                    "A semiconductor diode, the most common type today, is a crystalline piece of semiconductor material with a p-n " +
                    "junction connected to two electrical terminals. A vacuum tube diode has two electrodes, a plate (anode) and a " +
                    "heated cathode. Semiconductor diodes were the first semiconductor electronic devices. The discovery of crystals' " +
                    "rectifying abilities was made by German physicist Ferdinand Braun in 1874. The first semiconductor diodes, " +
                    "called cat's whisker diodes, developed around 1906, were made of mineral crystals such as galena. Today, most " +
                    "diodes are made of silicon, but other semiconductors such as selenium or germanium are sometimes used.",
                    topic=topic_elements)
    add_synonym("Rectifier", node=diode_node)
    add_synonym("Semiconductor", node=diode_node)
    add_synonym("Junction", node=diode_node)
    
    wire_node = add_node("Wire",
                         definition="A wire is a single, usually cylindrical, flexible strand or rod of metal."+  
                         " Wires are used to bear mechanical loads or electricity and telecommunications signals."+
                         " Wire is commonly formed by drawing the metal through a hole in a die or draw plate."+ 
                         " Wire gauges come in various standard sizes, as expressed in terms of a gauge number." + 
                         " The term wire is also used more loosely to refer to a bundle of such strands, as in 'multistranded wire', which is more correctly termed a wire rope in mechanics, or a cable in electricity."+
                         " Wire comes in solid core, stranded, or braided forms.",
                    topic=topic_elements)
    add_synonym("Cable", node=wire_node)
    add_synonym("Line", node=wire_node)
    add_synonym("Short", node=wire_node)
    add_synonym("Connector", node=wire_node)
    
    potentiometer_node = add_node("Potentiometer",
                    definition="A potentiometer, informally a pot, is a three-terminal resistor with a sliding or rotating contact " +
                    "that forms an adjustable voltage divider. If only two terminals are used, one end and the wiper, it acts as a " +
                    "variable resistor or rheostat.",
                    topic=topic_elements)
    
    element_node = add_node("Element",
                    definition="Electrical elements are conceptual abstractions representing idealized electrical components, such as " +
                    "resistors, capacitors, and inductors, used in the analysis of electrical networks. Any electrical network can " +
                    "be analysed as multiple, interconnected electrical elements in a schematic diagram or circuit diagram, each of " +
                    "which affects the voltage in the network or current through the network. These ideal electrical elements represent " +
                    "real, physical electrical or electronic components but they do not exist physically and they are assumed to have " +
                    "ideal properties according to a lumped element model, while components are objects with less than ideal properties, " +
                    "a degree of uncertainty in their values and some degree of nonlinearity, each of which may require a combination of " +
                    "multiple electrical elements in order to approximate its function.",
                    topic=topic_elements)
    add_synonym("Component", node=element_node)
    add_synonym("Entity", node=element_node)
    add_synonym("Instrument", node=element_node)
    add_synonym("Device", node=element_node)
    
    breadboard_node = add_node("Breadboard",
                    definition="A breadboard (or protoboard) is usually a construction base for prototyping of electronics. The term " +
                    "'breadboard' is commonly used to refer to a solderless breadboard (plugboard).",
                    topic=topic_elements)
    add_synonym("Board", node=breadboard_node)
    
    switch_node = add_node("Switch",
                    definition="In electrical engineering, a switch is an electrical component that can break an electrical circuit, interrupting the current or diverting it from one conductor to another.",
                    topic=topic_elements)
    
    transistor_node = add_node("Transistor",
                    definition="A transistor is a semiconductor device used to amplify and switch electronic signals and electrical power. " +
                    "It is composed of semiconductor material with at least three terminals for connection to an external circuit. A " +
                    "voltage or current applied to one pair of the transistor's terminals changes the current through another pair of " +
                    "terminals. Because the controlled (output) power can be higher than the controlling (input) power, a transistor " +
                    "can amplify a signal. Today, some transistors are packaged individually, but many more are found embedded in " +
                    "integrated circuits.",
                    topic=topic_elements)
    add_synonym("BJT", node=transistor_node)
    
    ammeter_node = add_node("Ammeter",
                    definition="An ammeter is a measuring instrument used to measure the electric current in a circuit. Electric " +
                    "currents are measured in amperes (A), hence the name. Instruments used to measure smaller currents, in the " +
                    "milliampere or microampere range, are designated as milliammeters or microammeters. Early ammeters were laboratory " +
                    "instruments which relied on the Earth's magnetic field for operation. By the late 19th century, improved " +
                    "instruments were designed which could be mounted in any position and allowed accurate measurements in electric " +
                    "power systems.",
                    topic=topic_elements)
    
    voltmeter_node = add_node("Voltmeter",
                    definition="A voltmeter is an instrument used for measuring electrical potential difference between two points in " +
                    "an electric circuit. Analog voltmeters move a pointer across a scale in proportion to the voltage of the " +
                    "circuit; digital voltmeters give a numerical display of voltage by use of an analog to digital converter.",
                    topic=topic_elements)
    
    ohmmeter_node = add_node("Ohmmeter",
                    definition="An ohmmeter is an electrical instrument that measures electrical resistance, the opposition to an " +
                    "electric current. Micro-ohmmeters (microhmmeter or microohmmeter) make low resistance measurements. Megohmmeters " +
                    "(aka megaohmmeter or in the case of a trademarked device Megger) measure large values of resistance. The " +
                    "unit of measurement for resistance is ohms.",
                    topic=topic_elements)
    
    # Action Words
    topic_action = add_vocab_topic(domain=circuits_domain,
                    topic="Action Words",
                    def_useful=False)
    measure_node = add_node("Measure", definition="", topic=topic_action)
    add_synonym("Know", node=measure_node)
    add_synonym("Get", node=measure_node)
    add_synonym("See", node=measure_node)
    add_synonym("Take", node=measure_node)
    add_synonym("Find", node=measure_node)
    add_synonym("Quantify", node=measure_node)
    add_synonym("Need", node=measure_node)
    add_synonym("Bill", node=measure_node)
    
    compute_node = add_node("Compute", definition="", topic=topic_action)
    add_synonym("Calculate", node=compute_node)
    add_synonym("Evaluate", node=compute_node)
    add_synonym("Build", node=compute_node)
    add_synonym("Verify", node=compute_node)
    add_synonym("Formula", node=compute_node)
    
    change_node = add_node("Change", definition="", topic=topic_action)
    add_synonym("Set", node=change_node)
    add_synonym("Reverse", node=change_node)
    add_synonym("Tune", node=change_node)
    add_synonym("Vary", node=change_node)
    
    use_node = add_node("Use", definition="", topic=topic_action)
    add_synonym("Used", node=use_node)
    add_synonym("Place", node=use_node)
    add_synonym("Connect", node=use_node)
    add_synonym("Create", node=use_node)
    add_synonym("Drag Drop", node=use_node)
    add_synonym("Bill", node=use_node)
    
    move_node = add_node("Move", definition="", topic=topic_action)
    
    remove_node = add_node("Remove", definition="", topic=topic_action)
    add_synonym("Erase", node=remove_node)
    add_synonym("Delete", node=remove_node)
    add_synonym("Take Off", node=remove_node)
    add_synonym("Eliminate", node=remove_node)
    add_synonym("Clear", node=remove_node)
    
    save_node = add_node("Save", definition="", topic=topic_action)
    
    open_node = add_node("Open", definition="", topic=topic_action)
    
    work_node = add_node("Work", definition="", topic=topic_action)
    add_synonym("Does", node=work_node)
    add_synonym("Define", node=work_node)
    add_synonym("Definition", node=work_node)
    add_synonym("Mean", node=work_node)
    add_synonym("Signify", node=work_node)
    add_synonym("Understand", node=work_node)
    add_synonym("Whats", node=work_node)
    add_synonym("Whys", node=work_node)
    add_synonym("Hows", node=work_node)
    add_synonym("Wheres", node=work_node)
    add_synonym("Do", node=work_node)
    add_synonym("Is", node=work_node)
    add_synonym("Be", node=work_node)
    add_synonym("Are", node=work_node)
    add_synonym("This", node=work_node)
    add_synonym("That", node=work_node)
    add_synonym("Bill", node=work_node)
    
    read_node = add_node("Read", definition="", topic=topic_action)
    
    # Question Words
    topic_question = add_vocab_topic(domain=circuits_domain,
                                    topic="Question Words",
                                    def_useful=False)
    how_node = add_node("How", definition="", topic=topic_question)
    add_synonym("Hows", node=how_node)
    add_synonym("Howz", node=how_node)
    
    what_node = add_node("What", definition="", topic=topic_question)
    add_synonym("Whats", node=what_node)
    add_synonym("Whatz", node=what_node)
    
    why_node = add_node("Why", definition="", topic=topic_question)
    add_synonym("Whys", node=why_node)
    add_synonym("Whyz", node=why_node)
    
    when_node = add_node("When", definition="", topic=topic_question)
    add_synonym("Whens", node=when_node)
    add_synonym("Whenz", node=when_node)
    
    # Problem Words
    topic_problems = add_vocab_topic(domain=circuits_domain,
                                    topic="Problem Words",
                                    def_useful=False)
    wrong_node = add_node("Wrong", definition="", topic=topic_problems)
    add_synonym("Incorrect", node=wrong_node)
    add_synonym("Not Correct", node=wrong_node)
    add_synonym("Error", node=wrong_node)
    add_synonym("Mistake", node=wrong_node)
    add_synonym("Not Right", node=wrong_node)
    add_synonym("Not", node=wrong_node)
    add_synonym("Fault", node=wrong_node)
    add_synonym("Do Not", node=wrong_node)
    add_synonym("Dont", node=wrong_node)
    add_synonym("Cant", node=wrong_node)
    add_synonym("Cannot", node=wrong_node)
    add_synonym("Cant", node=wrong_node)
    add_synonym("Doesnt", node=wrong_node)
    add_synonym("Isnt", node=wrong_node)
    
    # Circuit Concepts
    topic_concepts = add_vocab_topic(domain=circuits_domain,
                                    topic="Circuit Concepts",
                                    def_useful=True)
    voltage_node = add_node("Voltage", 
                            definition="Voltage, electrical potential difference, electric tension or electric pressure (denoted ∆V and measured in units of electric potential: volts, or joules per coulomb) is the electric potential difference between two points, or the difference in electric potential energy of a unit charge transported between two points." + 
                            " Voltage is equal to the work done per unit charge against a static electric field to move the charge between two points."+ 
                            " A voltage may represent either a source of energy (electromotive force), or lost, used, or stored energy (potential drop)."+
                            " A voltmeter can be used to measure the voltage (or potential difference) between two points in a system; often a common reference potential such as the ground of the system is used as one of the points."+ 
                            " Voltage can be caused by static electric fields, by electric current through a magnetic field, by time-varying magnetic fields, or some combination of these three.", 
                            topic=topic_concepts)
    add_synonym("Volt", node=voltage_node)
    add_synonym("Volts", node=voltage_node)
    add_synonym("V", node=voltage_node)
    add_synonym("Potential", node=voltage_node)
    add_synonym("PD", node=voltage_node)
    add_synonym("KVL", node=voltage_node)
    
    current_node = add_node("Current", definition="An electric current is a flow of electric charge." +  
                            " In electric circuits this charge is often carried by moving electrons in a wire." + 
                            " It can also be carried by ions in an electrolyte, or by both ions and electrons such as in a plasma." +
                            " The SI unit for measuring an electric current is the ampere, which is the flow of electric charge across a surface at the rate of one coulomb per second." + 
                            " Electric current is measured using a device called an ammeter." + 
                            " Electric currents can have many effects, notably heating, but they also create magnetic fields, which are used in motors, inductors and generators.", 
                            topic=topic_concepts)
    add_synonym("Amp", node=current_node)
    add_synonym("Amps", node=current_node)
    add_synonym("Ampere", node=current_node)
    add_synonym("KCL", node=current_node)
    add_synonym("DC", node=current_node)
    add_synonym("AC", node=current_node) 
    
    dissipation_node = add_node("Dissipation",
                               definition="As power is defined as the rate of energy transfer, 'power dissipation' is a measure of the rate at which energy is dissipated, or lost, from an electrical system.",
                               topic=topic_concepts)
    
    filter_node = add_node("Filter",
                            definition="Electronic filters are analog circuits which perform signal processing functions, specifically to remove unwanted frequency components from the signal, to enhance wanted ones, or both.",
                            topic=topic_concepts)
    
    timeconstant_node = add_node("Time Constant",
                                  definition="The RC time constant, also called tau, is the time constant (in seconds) of an RC circuit, is equal to the product of the circuit resistance (in ohms) and the circuit capacitance (in farads). ",
                                  topic=topic_concepts)
    add_synonym("constant", node=timeconstant_node)
    add_synonym("time", node=timeconstant_node)
    
    resistance_node = add_node("Resistance",
                               definition="The electrical resistance of an electrical conductor is the opposition to the passage of an electric current through that conductor." +  
                               " The inverse quantity is electrical conductance, the ease with which an electric current passes."+
                               " Electrical resistance shares some conceptual parallels with the mechanical notion of friction." + 
                               " The SI unit of electrical resistance is the ohm (Ω), while electrical conductance is measured in siemens (S).",
                               topic=topic_concepts)
    add_synonym("Ohm", node=resistance_node)
    add_synonym("Ohms", node=resistance_node)
    
    capacitance_node = add_node("Capacitance", 
                                definition="Capacitance is the ability of a body to store an electrical charge." + 
                                " Any object that can be electrically charged exhibits capacitance." +  
                                " A common form of energy storage device is a parallel-plate capacitor." + 
                                " In a parallel plate capacitor, capacitance is directly proportional to the surface area of the conductor plates and inversely proportional to the separation distance between the plates.", 
                                topic=topic_concepts)
    add_synonym("Farad", node=capacitance_node)
    add_synonym("F", node=capacitance_node)
    
    inductance_node = add_node("Inductance", 
                               definition="In electromagnetism and electronics, inductance is the property of a conductor by which a change in current flowing through it 'induces' (creates) a voltage (electromotive force) in both the conductor itself (self-inductance) and in any nearby conductors (mutual inductance)." + 
                               "The term 'inductance' was coined by Oliver Heaviside in February 1886." + 
                               "It is customary to use the symbol L for inductance, in honour of the physicist Heinrich Lenz." + 
                               "In the SI system the measurement unit for inductance is the henry, H, named in honor of the scientist who discovered inductance, Joseph Henry.", 
                               topic=topic_concepts)
    add_synonym("Henry", node=inductance_node)
    add_synonym("H", node=inductance_node)
    
    power_node = add_node("Power",
                          definition="Electric power is the rate at which electric energy is transferred by an electric circuit." + 
                          " The SI unit of power is the watt, one joule per second." + 
                          " Electric power is usually produced by electric generators, but can also be supplied by sources such as electric batteries." + 
                          " Electric power is generally supplied to businesses and homes by the electric power industry." + 
                          " Electric power is usually sold by the kilowatt hour (3.6 MJ) which is the product of power in kilowatts multiplied by running time in hours." + 
                          " Electric utilities measure power using an electricity meter, which keeps a running total of the electric energy delivered to a customer.", 
                          topic=topic_concepts)
    add_synonym("Watt", node=power_node)
    add_synonym("W", node=power_node)
    
    time_node = add_node("Time", 
                         definition="",
                         topic=topic_concepts)
    add_synonym("Term", node=time_node)
    add_synonym("Second", node=time_node)
    add_synonym("MS", node=time_node)
    add_synonym("S", node=time_node)
    
    frequency_node = add_node("Frequency", 
                              definition="Frequency is the number of occurrences of a repeating event per unit time." +  
                              " It is also referred to as temporal frequency, which emphasizes the contrast to spatial frequency and angular frequency." + 
                              " The period is the duration of one cycle in a repeating event, so the period is the reciprocal of the frequency." + 
                              " For example, if a newborn baby's heart beats at a frequency of 120 times a minute, its period – the interval between beats – is half a second (60 seconds (i.e. a minute) divided by 120 beats).",
                              topic=topic_concepts)
    add_synonym("Hetz", node=frequency_node)
    add_synonym("CPS", node=frequency_node)
    add_synonym("Hz", node=frequency_node)
    
    waveform_node = add_node("Waveform",
                             definition="A waveform is the shape and form of a signal such as a wave moving in a physical medium or an abstract representation." + 
                             " In many cases the medium in which the wave is being propagated does not permit a direct visual image of the form."+
                             " In these cases, the term 'waveform' refers to the shape of a graph of the varying quantity against time or distance."+
                             " An instrument called an oscilloscope can be used to pictorially represent a wave as a repeating image on a screen.", 
                             topic=topic_concepts)
    add_synonym("Wave", node=waveform_node)
    add_synonym("Crest", node=waveform_node)
    add_synonym("Trough", node=waveform_node)
    add_synonym("Sine", node=waveform_node)
    add_synonym("Sinusoid", node=waveform_node)
    add_synonym("Square", node=waveform_node)
    
    amplitude_node = add_node("Amplitude",
                              definition="Peak-to-peak amplitude is the change between peak (highest amplitude value) and trough (lowest amplitude value, which can be negative)."+
                              " With appropriate circuitry, peak-to-peak amplitudes of electric oscillations can be measured by meters or by viewing the waveform on an oscilloscope.", 
                              topic=topic_concepts)
    add_synonym("Value", node=amplitude_node)
    add_synonym("Magnitude", node=amplitude_node)
    add_synonym("Reading", node=amplitude_node)
    add_synonym("Entry", node=amplitude_node)
    add_synonym("Meter", node=amplitude_node)
    add_synonym("Metre", node=amplitude_node)
    add_synonym("Y", node=amplitude_node)
    
    reactance_node = add_node("Reactance", 
                              definition="In electrical and electronic systems, reactance is the opposition of a circuit element to a change of electric current or voltage, due to that element's inductance or capacitance."+
                              " A built-up electric field resists the change of voltage on the element, while a magnetic field resists the change of current."+
                              " The notion of reactance is similar to electrical resistance, but they differ in several respects." + 
                              " An ideal resistor has zero reactance, while ideal inductors and capacitors consist entirely of reactance."+
                              " The magnitude of the reactance of an inductor is proportional to frequency, while the magnitude of the reactance of a capacitor is inversely proportional to frequency.",
                              topic=topic_concepts)
    add_synonym("XC", node=reactance_node)
    add_synonym("XL", node=reactance_node)
    
    impedance_node = add_node("Impedance", 
                              definition="Electrical impedance is the measure of the opposition that a circuit presents to a current when a voltage is applied." +
                              "In quantitative terms, it is the complex ratio of the voltage to the current in an alternating current (AC) circuit."+
                              " Impedance extends the concept of resistance to AC circuits, and possesses both magnitude and phase, unlike resistance, which has only magnitude."+
                              " When a circuit is driven with direct current (DC), there is no distinction between impedance and resistance; the latter can be thought of as impedance with zero phase angle.", 
                              topic=topic_concepts)
    add_synonym("Z", node=impedance_node)
    
    conductance_node = add_node("Conductance",
                                definition="The electrical resistance of an electrical conductor is the opposition to the passage of an electric current through that conductor."+
                                " The inverse quantity is electrical conductance, the ease with which an electric current passes."+
                                " Electrical resistance shares some conceptual parallels with the mechanical notion of friction."+
                                " The SI unit of electrical resistance is the ohm (Ω), while electrical conductance is measured in siemens (S).",
                                topic=topic_concepts)
    add_synonym("G", node=conductance_node)
    add_synonym("Mho", node=conductance_node)
    add_synonym("Mhos", node=conductance_node)
    
    energy_node = add_node("Energy", definition="Electrical energy is energy newly derived from electrical potential energy."+
                           " When loosely used to describe energy absorbed or delivered by an electrical circuit (for example, one provided by an electric power utility) 'electrical energy' refers to energy which has been converted from electrical potential energy."+
                           " This energy is supplied by the combination of electric current and electrical potential that is delivered by the circuit."+
                           " At the point that this electrical potential energy has been converted to another type of energy, it ceases to be electrical potential energy."+
                           " Thus, all electrical energy is potential energy before it is delivered to the end-use."+
                           " Once converted from potential energy, electrical energy can always be described as another type of energy (heat, light, motion, etc.).", topic=topic_concepts)
    add_synonym("Joule", node=energy_node)
    add_synonym("J", node=energy_node)
    
    cycle_node = add_node("Cycle", 
                          definition="A turn is a unit of angle measurement equal to 360° or 2π radians."+
                          " A turn is also referred to as a revolution or complete rotation or full circle or cycle or rev or rot.",
                          topic=topic_concepts)
    
    period_node = add_node("Period",
                           definition="The period is the duration of one cycle in a repeating event, so the period is the reciprocal of the frequency."+
                          " For example, if a newborn baby's heart beats at a frequency of 120 times a minute, its period – the interval between beats – is half a second (60 seconds (i.e. a minute) divided by 120 beats).",  
                           topic=topic_concepts)
    
    wabelength_node = add_node("Wavelength", 
                               definition="In physics, the wavelength of a sinusoidal wave is the spatial period of the wave—the distance over which the wave's shape repeats."+
                               " It is usually determined by considering the distance between consecutive corresponding points of the same phase, such as crests, troughs, or zero crossings, and is a characteristic of both traveling waves and standing waves, as well as other spatial wave patterns."+
                               " Wavelength is commonly designated by the Greek letter lambda (λ)."+
                               " The concept can also be applied to periodic waves of non-sinusoidal shape."+
                               " The term wavelength is also sometimes applied to modulated waves, and to the sinusoidal envelopes of modulated waves or waves formed by interference of several sinusoids."+
                               " The SI unit of wavelength is the meter.", 
                               topic=topic_concepts)
    add_synonym("Wave Length", node=wabelength_node)
    
    circuit_node = add_node("Circuit",
                            definition="An electrical network is an interconnection of electrical elements such as resistors, inductors, capacitors, voltage sources, current sources and switches."+
                            " An electrical circuit is a network consisting of a closed loop, giving a return path for the current.", 
                            topic=topic_concepts)
    add_synonym("Loop", node=circuit_node)
    
    button_node = add_node("Button",
                           definition="A push-button (also spelled pushbutton) or simply button is a simple switch mechanism for controlling some aspect of a machine or a process."+
                           " Buttons are typically made out of hard material, usually plastic or metal."
                           , topic=topic_concepts)
    
    phasor_node = add_node("Phasor",
                           definition="In physics and engineering, a phase vector, or phasor, is a complex number representing a sinusoidal function whose amplitude (A), frequency (ω), and phase (θ) are time-invariant."+
                           " It is a subset of a more general concept called analytic representation. Phasors separate the dependencies on A, ω, and θ into three independent factors."+
                           " This can be particularly useful because the frequency factor (which includes the time-dependence of the sinusoid) is often common to all the components of a linear combination of sinusoids.",
                           topic=topic_concepts)
    
    phase_node = add_node("Phase",
                          definition="Phase in sinusoidal functions or in waves has two different, but closely related, meanings."+
                          " One is the initial angle of a sinusoidal function at its origin and is sometimes called phase offset or phase difference."+
                          " Another usage is the fraction of the wave cycle which has elapsed relative to the origin.", 
                          topic=topic_concepts)
    add_synonym("Angle", node=phase_node)
    
    # Other, useful
    topic_other = add_vocab_topic(domain=circuits_domain,
                                  topic="Other",
                                  def_useful=True)
    positive_node = add_node("Positive", 
                             definition=" In DC circuits, the positive pole is usually marked red (or '+'). Electrons flow from the negative pole to the positive pole."+
                             " In a direct current (DC) circuit, one pole is always negative, the other pole is always positive and the electrons flow in one direction only."+
                             " In an alternating current (AC) circuit the two poles alternate between negative and positive and the direction of the electron flow reverses.",
                                topic=topic_other)
    
    negative_node = add_node("Negative", 
                             definition=" In DC circuits, the negative pole is usually marked black (or '-'). Electrons flow from the negative pole to the positive pole."+
                             " In a direct current (DC) circuit, one pole is always negative, the other pole is always positive and the electrons flow in one direction only."+
                             " In an alternating current (AC) circuit the two poles alternate between negative and positive and the direction of the electron flow reverses."
                            , topic=topic_other)
    
    polarity_node = add_node("Polarity", definition="Electrical polarity (positive and negative) is present in every electrical circuit. Electrons flow from the negative pole to the positive pole."+
                             " In a direct current (DC) circuit, one pole is always negative, the other pole is always positive and the electrons flow in one direction only."+
                             " In an alternating current (AC) circuit the two poles alternate between negative and positive and the direction of the electron flow reverses."+
                             " In DC circuits, the positive pole is usually marked red (or '+') and the negative pole is usually marked black (or '−'), but other color schemes are sometimes used in automotive and telecommunications systems."
                            , topic=topic_other)
    add_synonym("Sign", node=polarity_node)
    
    law_node = add_node("Law", definition="A scientific law is a statement based on repeated experimental observations that describes some aspect of the universe."+
                        " A scientific law always applies under the same conditions, and implies that there is a causal relationship involving its elements."+
                        " Factual and well-confirmed statements like 'Mercury is liquid at standard temperature and pressure' are considered too specific to qualify as scientific laws. "+
                        "Laws differ from scientific theories in that they do not posit a mechanism or explanation of phenomena: they are merely distillations of the results of repeated observation."+
                        " As such, a law is limited in applicability to circumstances resembling those already observed, and may be found false when extrapolated."+
                        " Ohm's law only applies to linear networks, Newton's law of universal gravitation only applies in weak gravitational fields, the early laws of aerodynamics such as Bernoulli's principle do not apply in case of compressible flow such as occurs in transonic and supersonic flight, Hooke's law only applies to strain below the elastic limit, etc."+
                        " These laws remain useful, but only under the conditions where they apply."
                        , topic=topic_other)
    add_synonym("Rule", node=law_node)
    add_synonym("Principle", node=law_node)
    add_synonym("Theorem", node=law_node)
    
    gain_node = add_node("Gain", definition="In electronics, gain is a measure of the ability of a circuit (often an amplifier) to increase the power or amplitude of a signal from the input to the output by adding energy converted from some power supply to the signal."+
                         " It is usually defined as the mean ratio of the signal output of a system to the signal input of the same system."+
                         " It is often expressed using the logarithmic decibel (dB) units ('dB gain')."+
                         " A gain greater than one (zero dB), that is, amplification, is the defining property of an active component or circuit, while a passive circuit will have a gain of less than one."
                         , topic=topic_other)
    
    loss_node = add_node("Loss", definition="Joule heating, also known as ohmic heating and resistive heating, is the process by which the passage of an electric current through a conductor releases heat. "+
                         "Joule heating is referred to as ohmic heating or resistive heating because of its relationship to Ohm's Law. "+
                         "It forms the basis for the large number of practical applications involving electric heating."+
                         " However, in applications where heating is an unwanted by-product of current use (e.g., load losses in electrical transformers) the diversion of energy is often referred to as resistive loss."+
                         " The use of high voltages in electric power transmission systems is specifically designed to reduce such losses in cabling by operating with commensurately lower currents."
                         , topic=topic_other)
    
    division_node = add_node("Division", 
                             definition="In electronics or EET, a voltage divider (also known as a potential divider) is a linear circuit that produces an output voltage (Vout) that is a fraction of its input voltage (Vin)."+
                             " Voltage division refers to the partitioning of a voltage among the components of the divider."
                             , topic=topic_other)
    add_synonym("Divider", node=division_node)
    
    unit_node = add_node("Unit",
                         definition="The International System of Units (abbreviated SI from French: Le Système international d'unités) is the modern form of the metric system and is the world's most widely used system of measurement, used in both everyday commerce and science."+
                         " It comprises a coherent system of units of measurement built around seven base units, 22 named and an indeterminate number of unnamed coherent derived units, and a set of prefixes that act as decimal-based multipliers."
                         , topic=topic_other)
    
    color_code_node = add_node("Color Code",
                               definition="The electronic color code is used to indicate the values or ratings of electronic components, very commonly for resistors, but also for capacitors, inductors, and others."+
                               " A separate code, the 25-pair color code, is used to identify wires in some telecommunications cables."
                               , topic=topic_other)
    add_synonym("Colorcode", node=color_code_node)
    add_synonym("Color", node=color_code_node)
    
    vla_node = add_node("VLA",
                               definition="VLA, or Virtual Lab Assistant, aims to create an interactive and intelligent framework for laboratory course work. VLA is a new way to present laboratory work to students, " +
                               "and features an intelligent help module and a circuit recognition module. It was developed by the CSNAP Laboratory at Temple University " +
                               "and is supported by the NSF."
                               , topic=topic_other)
    
    multisim_node = add_node("Multisim",
                               definition="MultiSIM is an electronic schematic capture and simulation program which is part of a suite of circuit design programs, along with NI Ultiboard. Multisim is one of the few " +
                               "circuit design programs to employ the original Berkeley SPICE based software simulation. Multisim was originally created by a company named Electronics Workbench, which is " +
                               "now a division of National Instruments. Multisim includes microcontroller simulation (formerly known as MultiMCU), as well as integrated import and export features to the " +
                               "Printed Circuit Board layout software in the suite, NI Ultiboard. Multisim is widely used in academia and industry for circuits education, electronic schematic design and " +
                               "SPICE simulation."
                               , topic=topic_other)
    
    spice_node = add_node("SPICE",
                               definition="SPICE stands for Simulation Program with Integrated Circuit Emphasis. It is a general-purpose, open source analog electronic circuit simulator. It is a powerful program that is " +
                               "used in integrated circuit and board-level design to check the integrity of circuit designs and to predict circuit behavior."
                               , topic=topic_other)
    
    # Other, not useful
    topic_other_not = add_vocab_topic(domain=circuits_domain,
                                  topic="Other, not useful",
                                  def_useful=False)
    password_node = add_node("Password",
                             definition="",
                             topic=topic_other_not)
    pass_node = add_node("Pass",
                         definition="",
                         topic=topic_other_not)
    low_node = add_node("Low",
                         definition="",
                         topic=topic_other_not)
    high_node = add_node("High",
                         definition="",
                         topic=topic_other_not)
    rating_node = add_node("Rating",
                         definition="",
                         topic=topic_other_not)
    
    # Circuit Laws
    topic_laws = add_vocab_topic(domain=circuits_domain,
                                 topic="Circuit Laws",
                                 def_useful=True)
    ohms_law_node = add_node("Ohms Law", definition="Ohm's law states that the current through a conductor between two points is directly proportional to the potential difference across the two points. "+
                             " Introducing the constant of proportionality, the resistance, one arrives at the usual mathematical equation that describes this relationship: V = IR."+
                             " Where I is the current through the conductor in units of amperes, V is the potential difference measured across the conductor in units of volts, and R is the resistance of the conductor in units of ohms.", topic=topic_laws)
    add_synonym("Ohmic", node=ohms_law_node)
    
    kirchoffs_node = add_node("Kirchoffs Law", 
                              definition="Kirchoff's Current Law (KCL)  is also called Kirchhoff's first law, Kirchhoff's point rule, or Kirchhoff's junction rule (or nodal rule)."+
                              "The principle of conservation of electric charge implies that at any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node, or the algebraic sum of currents in a network of conductors meeting at a point is zero."
                              " Kirchoff's Voltage Law (KVL) is also called Kirchhoff's second law, Kirchhoff's loop (or mesh) rule, and Kirchhoff's second rule." + 
                              " The principle of conservation of energy implies that the directed sum of the electrical potential differences (voltage) around any closed network is zero, or"+
                              "more simply, the sum of the emfs in any closed loop is equivalent to the sum of the potential drops in that loop."
                            , topic=topic_laws)
    add_synonym("Kirchoffs", node=kirchoffs_node)
    add_synonym("Kirchoff", node=kirchoffs_node)
    add_synonym("Kircho", node=kirchoffs_node)
    
    thevenin_node = add_node("Thevenins Law",
                             definition="Thévenin's theorem and its dual, Norton's theorem, are widely used for circuit analysis simplification and to study circuit's initial-condition and steady-state response."+
                             " Thévenin's theorem can be used to convert any circuit's sources and impedances to a Thévenin equivalent; use of the theorem may in some cases be more convenient than use of Kirchhoff's circuit laws."
                             , topic=topic_laws)
    add_synonym("Thevenins", node=thevenin_node)
    add_synonym("Thevenin", node=thevenin_node)
    
    norton_node = add_node("Nortons Law", 
                           definition="Norton's Theorem states that it is possible to simplify any linear circuit, no matter how complex, to an equivalent circuit with just a single current source and parallel resistance connected to a load."+
                           " Just as with Thevenin's Theorem, the qualification of “linear” is identical to that found in the Superposition Theorem: all underlying equations must be linear (no exponents or roots). ",
                           topic=topic_laws)
    add_synonym("Nortons", node=norton_node)
    add_synonym("Norton", node=norton_node)
    
    max_power_node = add_node("Max Power Transfer",
                              definition="In electrical engineering, the maximum power transfer theorem states that, to obtain maximum external power from a source with a finite internal resistance, the resistance of the load must equal the resistance of the source as viewed from its output terminals."+
                              " Moritz von Jacobi published the maximum power (transfer) theorem around 1840; it is also referred to as 'Jacobi's law'."
                              , topic=topic_laws)
    add_synonym("Power Transfer", node=max_power_node)
    
    node_node = add_node("Node",
                         definition="In electrical engineering, node refers to any point on a circuit where two or more circuit elements meet."+
                         " For two nodes to be different, their voltages must be different."+
                         " Without any further knowledge, it is easy to establish how to find a node by using Ohm's Law: V=IR."+
                         " When looking at circuit schematics, ideal wires have a resistance of zero."+
                         " Since it can be assumed that there is no change in the potential across any part of the wire, all of the wire in between any components in a circuit is considered part of the same node.", 
                         topic=topic_laws)
    add_synonym("Nodes", node=node_node)
    
    conservation_node = add_node("Conservation",
                                 definition="In physics, charge conservation is the principle that electric charge can neither be created nor destroyed."+
                                 " The net quantity of electric charge, the amount of positive charge minus the amount of negative charge in the universe, is always conserved."+
                                 " The first written statement of the principle was by American scientist and statesman Benjamin Franklin in 1747.",
                                 topic=topic_laws)
    
    transformation_node = add_node("Transformation",
                                   definition="Source transformation is simplifying a circuit solution, especially with mixed sources, by transforming a voltage into a current source, and vice versa."+
                                   " Finding a solution to a circuit can be difficult without using methods such as this to make the circuit appear simpler."+
                                   " Source transformation is an application of Thévenin's theorem and Norton's theorem."+
                                   " Performing a source transformation consists of using Ohm's law to take an existing voltage source in series with a resistance, and replace it with a current source in parallel with the same resistance. ",
                                   topic=topic_laws)
    add_synonym("Conversion", node=transformation_node)
    
    superposition_node = add_node("Superposition",
                                  definition="The superposition theorem for electrical circuits states that for a linear system the response (voltage or current) in any branch of a bilateral linear circuit having more than one independent source equals the algebraic sum of the responses caused by each independent source acting alone, where all the other independent sources are replaced by their internal impedances.",
                                  topic=topic_laws)
    add_synonym("Super Position", node=superposition_node)
    
    linear_node = add_node("Linear", 
                           definition="In common usage, linearity refers to a mathematical relationship or function that can be graphically represented as a straight line, as in two quantities that are directly proportional to each other, such as voltage and current in a simple DC circuit, or the mass and weight of an object."+
                           " A crude but simple example of this concept can be observed in the volume control of an audio amplifier."+
                           " While our ears may (roughly) perceive a relatively even gradation of volume as the control goes from 1 to 10, the electrical power consumed in the speaker is rising geometrically with each numerical increment."+
                           " The 'loudness' is proportional to the volume number (a linear relationship), while the wattage is doubling with every unit increase (a non-linear, exponential relationship).", 
                           topic=topic_laws)
    
    nonlinear_node = add_node("Nonlinear", 
                              definition="In physics and other sciences, a nonlinear system, in contrast to a linear system, is a system which does not satisfy the superposition principle – meaning that the output of a nonlinear system is not directly proportional to the input.",
                              topic=topic_laws)
    add_synonym("Non Linear", node=nonlinear_node)
    
    variable_node = add_node("Variable", definition="In elementary mathematics, a variable is an alphabetic character representing a number, the value of the variable, which is either arbitrary or not fully specified or unknown."+
                             " Making algebraic computations with variables as if they were explicit numbers allows one to solve a range of problems in a single computation."
                             "Alternatively, a variable is an element, feature, or factor that is able to be changed or adapted, such as a variable resistor (see: potentiometer).",
                             topic=topic_laws)
    
    dc_node = add_node("Direct Current", 
                       definition="Direct current (DC) is the unidirectional flow of electric charge."+
                       " Direct current is produced by sources such as batteries, thermocouples, solar cells, and commutator-type electric machines of the dynamo type."+
                       " Direct current may flow in a conductor such as a wire, but can also flow through semiconductors, insulators, or even through a vacuum as in electron or ion beams."+
                       " The electric current flows in a constant direction, distinguishing it from alternating current (AC)."+
                       " A term formerly used for direct current was galvanic current.",
                       topic=topic_laws)
    add_synonym("DC", node=dc_node)
    
    ac_node = add_node("Alternating Current", definition="In alternating current (AC, also ac), the flow of electric charge periodically reverses direction."+
                       " In direct current (DC, also dc), the flow of electric charge is only in one direction."+
                       " The abbreviations AC and DC are often used to mean simply alternating and direct, as when they modify current or voltage.",
                       topic=topic_laws)
    add_synonym("AC", node=ac_node)
    add_synonym("Alternate", node=ac_node)
    
    channel_node = add_node("Channel", definition="a means of communication or expression: as (1) :  a path along which information (as data or music) in the form of an electrical signal passes (2) plural :  a fixed or official course of communication <went through established military channels with his grievances> ", topic=topic_laws)
    add_synonym("Chanel", node=channel_node)
    
    dualtrace_node = add_node("Dualtrace", 
                              definition="A dual trace oscilloscope is an oscilloscope which can compare two waveforms on the face of a single cathode-ray tube, using any one of several methods.",
                              topic=topic_laws)
    add_synonym("Dual", node=dualtrace_node)
    
    
    # Circuit Diagrams and Measurement
    topic_diagrams = add_vocab_topic(domain=circuits_domain,
                                     topic="Circuit Diagrams and Measurement",
                                     def_useful=True)
    combination_node = add_node("Series Parallel Combination",
                                definition="Circuit elements can be connected by means of series connections or by means of parallel connections."+
                                " When all the devices in a circuit are connected by series connections, then the circuit is referred to as a series circuit."+
                                " When all the devices in a circuit are connected by parallel connections, then the circuit is referred to as a parallel circuit."+
                                " A third type of circuit involves the dual use of series and parallel connections in a circuit; such circuits are referred to as compound circuits or combination circuits.",
                                topic=topic_diagrams)
    add_synonym("Combination", node=combination_node)
    add_synonym("Bill", node=combination_node)
    
    series_node = add_node("Series", 
                           definition=" In a series circuit, each device is connected in a manner such that there is only one pathway by which charge can traverse the external circuit." + 
                           " In series, components share the same current but have different voltages."  ,
                           topic=topic_diagrams)
    add_synonym("Serial", node=series_node)
    
    parallel_node = add_node("Parallel", definition="In a parallel circuit, each device is placed in its own separate branch."+
                             " The presence of branch lines means that there are multiple pathways by which charge can traverse the external circuit" + 
                             " In a parellel circuit, components share the same voltage but have different currents. " , topic=topic_diagrams)
    
    peak_node = add_node("Peak", definition="A peak is the greatest or highest point of a waveform. A peak represents a maximum of a signal."
                         , topic=topic_diagrams)
    add_synonym("Maximum", node=peak_node)
    add_synonym("Bill", node=peak_node)
    
    instantaneous_node = add_node("Instantaneous", 
                                  definition="Instantaneous represents a single moment in time." + 
                                  " When used in reference to a measurement, it represents a value at a specific point in time, as opposed to average or RMS measurements." ,
                                  topic=topic_diagrams)
    
    rms_node = add_node("RMS", 
                        definition="In mathematics, the root mean square (abbreviated RMS or rms), also known as the quadratic mean, is a statistical measure of the magnitude of a varying quantity."+
                        " It is especially useful when variates are positive and negative, e.g., sinusoids."+
                        " In the field of electrical engineering, the effective (RMS) value of a periodic current is equal to the DC current that delivers the same average power to a resistor as the periodic current.",
                        topic=topic_diagrams)
    add_synonym("Mean", node=rms_node)
    
    average_node = add_node("Average", 
                            definition="In mathematics and statistics, the arithmetic mean,  or simply the mean or average when the context is clear, is the sum of a collection of numbers divided by the number of numbers in the collection."+
                            " The collection is often a set of results of an experiment, or a set of results from a survey."+
                            " The term 'arithmetic mean' is preferred in some contexts in mathematics and statistics because it helps distinguish it from other means, such as the geometric mean and the harmonic mean.",
                            topic=topic_diagrams)
    add_synonym("Mean", node=average_node)
    
    ground_node = add_node("Ground", 
                           definition="In electrical engineering, ground or earth can refer to the reference point in an electrical circuit from which voltages are measured, a common return path for electric current, or a direct physical connection to the Earth.",
                           topic=topic_diagrams)
    add_synonym("Grnd", node=ground_node)
    add_synonym("Gnd", node=ground_node)

    peaktopeak_node = add_node("Peak to Peak", 
                               definition="Peak-to-peak (pk-pk) is the difference between the maximum positive and the maximum negative amplitudes of a waveform."+
                               " If there is no direct current ( DC ) component in an alternating current ( AC ) wave, then the pk-pk amplitude is twice the peak amplitude.",
                               topic=topic_diagrams)
    add_synonym("Bill", node=peaktopeak_node)
    
    xy_node = add_node("XY", definition="A Cartesian coordinate system is a coordinate system that specifies each point uniquely in a plane by a pair of numerical coordinates, which are the signed distances from the point to two fixed perpendicular directed lines, measured in the same unit of length."+
                       " Each reference line is called a coordinate axis or just axis of the system, and the point where they meet is its origin, usually at ordered pair (0, 0)."+
                       " The coordinates can also be defined as the positions of the perpendicular projections of the point onto the two axes, expressed as signed distances from the origin.",
                       topic=topic_diagrams)
    
    # Math words
    topic_math = add_vocab_topic(domain=circuits_domain,
                                 topic="Math",
                                 def_useful=True)
    net_node = add_node("Net", 
                        definition="The difference from the final resting point and the initial starting point."
                        , topic=topic_math)
    add_synonym("Total", node=net_node)
    add_synonym("Overall", node=net_node)
    add_synonym("Sum", node=net_node)
    add_synonym("Equivalent", node=net_node)
    
    difference_node = add_node("Difference",
                               definition="The result of subtracting one number from another. ", 
                               topic=topic_math)
    
    # Units
    topic_units = add_vocab_topic(domain=circuits_domain,
                                  topic="Units",
                                  def_useful=True)
    ohm_node = add_node("Ohm",
                        definition="An ohm is the SI unit of electrical resistance, expressing the resistance in a circuit transmitting a current of one ampere when subjected to a potential difference of one volt.", 
                        topic=topic_units)
    add_synonym("Ohms", node=ohm_node)
    
    farad_node = add_node("Farad", 
                          definition="A farad is the SI unit of electrical capacitance, equal to the capacitance of a capacitor in which one coulomb of charge causes a potential difference of one volt.",
                          topic=topic_units)
    add_synonym("F", node=farad_node)
    
    henry_node = add_node("Henry",
                          definition="A henry is the SI unit of inductance, equal to an electromotive force of one volt in a closed circuit with a uniform rate of change of current of one ampere per second."
                          , topic=topic_units)
    add_synonym("H", node=henry_node)
    
    volt_node = add_node("Volt", 
                         definition="A volt is the SI unit of electromotive force, the difference of potential that would drive one ampere of current against one ohm resistance.", 
                         topic=topic_units)
    add_synonym("V", node=volt_node)
    
    ampere_node = add_node("Ampere",
                           definition="An ampere is a unit of electric current equal to a flow of one coulomb per second.",
                           topic=topic_units)
    add_synonym("Amps", node=ampere_node)
    add_synonym("Amp", node=ampere_node)
    add_synonym("A", node=ampere_node)
    
    watt_node = add_node("Watt", 
                         definition="A watt is the SI unit of power, equivalent to one joule per second, corresponding to the power in an electric circuit in which the potential difference is one volt and the current one ampere.",
                         topic=topic_units)
    add_synonym("W", node=watt_node)
    
    joule_node = add_node("Joule", 
                          definition="A joule is the SI unit of work or energy, equal to the work done by a force of one newton when its point of application moves one meter in the direction of action of the force, equivalent to one 3600th of a watt-hour.",
                          topic=topic_units)
    add_synonym("J", node=joule_node)
    
    second_node = add_node("Second", 
                           definition="The second (symbol: s) is the base unit of time in the International System of Units (SI) and is also a unit of time in other systems of measurement (abbreviated s or sec); it is the second division of the hour by sixty, the first division by 60 being the minute.", 
                           topic=topic_units)
    add_synonym("S", node=second_node)
    add_synonym("MS", node=second_node)
    
    hertz_node = add_node("Hertz", 
                          definition="A hertz is the SI unit of frequency, equal to one cycle per second.",
                          topic=topic_units)
    add_synonym("Hz", node=hertz_node)
    add_synonym("Cps", node=hertz_node)
    add_synonym("Cycles", node=hertz_node)
    
    inverse_ohm_node = add_node("Inverse Ohm", 
                                definition="A mho is the reciprocal of an ohm, a former unit of electrical conductance. (See: Siemens)", 
                                topic=topic_units)
    add_synonym("mho", node=inverse_ohm_node)
    add_synonym("mhos", node=inverse_ohm_node)
    add_synonym("1/ohm", node=inverse_ohm_node)
    
    # Help
    topic_help = add_vocab_topic(domain=circuits_domain,
                                 topic="Help",
                                 def_useful=False)
    help_node = add_node("Help", definition="", topic=topic_help)
    safety_node = add_node("Safety", definition="", topic=topic_help)
    

    # add rulebase
    rb = add_rulebase(name='Circuits')
    
    # add answer topics
    general = add_answer_topic(rulebase=rb, topic='General')
    safety = add_answer_topic(rulebase=rb, topic='Safety')
    equipment = add_answer_topic(rulebase=rb, topic='Equipment')
    VLA = add_answer_topic(rulebase=rb, topic='VLA')
    simulation = add_answer_topic(rulebase=rb, topic='Simulation')
    hardware = add_answer_topic(rulebase=rb, topic='Hardware')
    theory = add_answer_topic(rulebase=rb, topic='Theory')
    
    ###
    # add answers with questions
    ###
    
    # What is a capacitor?
    awq1 = add_answer_with_question(rulebase=rb,
                                    question="What is a capacitor")
    awq1.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq1,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq1,
                       node=capacitor_node)
    add_answer_element(answer_with_question=awq1, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/CmII_BmOf0I",
                       element_type="video")
    add_answer_element(answer_with_question=awq1, 
                       text_input="A capacitor (condenser) is a passive two-terminal electrical component used to store energy electrostatically in an electric field. " +
                       "The forms of practical capacitors vary widely, but all contain at least two electrical conductors (plates) separated by a dielectric (insulator). " +
                       "The conductors can be thin films of metal, aluminum foil or disks, etc. The 'nonconducting' dielectric acts to increase the capacitor's charge " +
                       "capacity. A dielectric can be glass, ceramic, plastic film, air, paper, mica, etc. Capacitors are widely used as parts of electrical circuits " +
                       "in many common electrical devices. Unlike a resistor, an ideal capacitor does not dissipate energy. Instead, a capacitor stores energy in the " +
                       "form of an electrostatic field between its plates. When there is a potential difference across the conductors (e.g., when a capacitor is " +
                       "attached across a battery), an electric field develops across the dielectric, causing positive charge +Q to collect on one plate and negative " +
                       "charge −Q to collect on the other plate. If a battery has been attached to a capacitor for a sufficient amount of time, no current can flow through " +
                       "the capacitor. However, if a time-varying voltage is applied across the leads of the capacitor, a displacement current can flow.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq1, 
                       text_input="An ideal capacitor is characterized by a single constant value for its capacitance. Capacitance is expressed as the ratio of the electric " +
                       "charge Q on each conductor to the potential difference V between them. The SI unit of capacitance is the farad (F), which is equal to one coulomb per " +
                       "volt (1 C/V). Typical capacitance values range from about 1 pF (\(10^{−12}\) F) to about 1 mF (\(10^{−3}\) F). ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a resistor?
    awq2 = add_answer_with_question(rulebase=rb,
                                    question="What is a resistor")
    awq2.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq2,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq2,
                       node=resistor_node)
    add_answer_element(answer_with_question=awq2, 
                       text_input="A resistor is a passive two-terminal electrical component that implements electrical resistance as a circuit element. Resistors act to reduce current " +
                       "flow, and, at the same time, act to lower voltage levels within circuits. In electronic circuits resistors are used to limit current flow, to adjust signal " +
                       "levels, bias active elements, terminate transmission lines among other uses. High-power resistors that can dissipate many watts of electrical power as heat may " +
                       "be used as part of motor controls, in power distribution systems, or as test loads for generators. Resistors may have fixed resistances that only change a little " +
                       "with temperature, time or operating voltage. Variable resistors can be used to adjust circuit elements (such as a volume control or a lamp dimmer), or as sensing " +
                       "devices for heat, light, humidity, force, or chemical activity.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq2, 
                       text_input="Resistors are common elements of electrical networks and electronic circuits and are ubiquitous in electronic equipment. Practical resistors as discrete " +
                       "components can be composed of various compounds and forms. Resistors are also implemented within integrated circuits.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is an inductor?
    awq3 = add_answer_with_question(rulebase=rb,
                                    question="What is an inductor")
    awq3.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq3,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq3,
                       node=inductor_node)
    add_answer_element(answer_with_question=awq3, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="https://www.youtube.com/embed/NgwXkUt3XxQ",
                       element_type="video")
    add_answer_element(answer_with_question=awq3, 
                       text_input="An inductor, also called a coil or reactor, is a passive two-terminal electrical component which resists changes in electric current passing through it. " +
                       "It consists of a conductor such as a wire, usually wound into a coil. When a current flows through it, energy is stored temporarily in a magnetic field in the coil. " +
                       "When the current flowing through an inductor changes, the time-varying magnetic field induces a voltage in the conductor, according to Faraday’s law of " +
                       "electromagnetic induction, which opposes the change in current that created it. An inductor is characterized by its inductance, the ratio of the voltage to " +
                       "the rate of change of current, which has units of Henries (H). Inductors have values that typically range from 1 µH (10−6H) to 1 H. Many inductors have a magnetic " +
                       "core made of iron or ferrite inside the coil, which serves to increase the magnetic field and thus the inductance. Along with capacitors and resistors, inductors " +
                       "are one of the three passive linear circuit elements that make up electric circuits. Inductors are widely used in alternating current (AC) electronic equipment, " +
                       "particularly in radio equipment. They are used to block the flow of AC current while allowing DC to pass; inductors designed for this purpose are called chokes. " +
                       "They are also used in electronic filters to separate signals of different frequencies, and in combination with capacitors to make tuned circuits, used to tune radio and TV receivers. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a potentiometer?
    awq4 = add_answer_with_question(rulebase=rb,
                                    question="What is a potentiometer")
    awq4.topic.add(equipment, hardware, simulation)
    add_answer_keyword(answer_with_question=awq4,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq4,
                       node=potentiometer_node)
    add_answer_element(answer_with_question=awq4, 
                       text_input="A potentiometer (informally a pot) is a three-terminal resistor with a sliding or rotating contact that forms an adjustable voltage divider. If only two terminals are used, " +
                       "one end and the wiper, it acts as a variable resistor or rheostat. A potentiometer measuring instrument is essentially a voltage divider used for measuring electric potential (voltage); " +
                       "the component is an implementation of the same principle, hence its name. Potentiometers are commonly used to control electrical devices such as volume controls on audio equipment. " +
                       "Potentiometers operated by a mechanism can be used as position transducers, for example, in a joystick. Potentiometers are rarely used to directly control significant power (more " +
                       "than a watt), since the power dissipated in the potentiometer would be comparable to the power in the controlled load. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is superposition?
    awq5 = add_answer_with_question(rulebase=rb,
                                    question="What is superposition")
    awq5.topic.add(theory)
    add_answer_keyword(answer_with_question=awq5,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq5,
                       node=superposition_node)
    add_answer_element(answer_with_question=awq5, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="https://www.youtube.com/embed/Szd7QqjP2-k",
                       element_type="video")
    add_answer_element(answer_with_question=awq5, 
                       text_input="The superposition theorem for electrical circuits states that for a linear system the response (voltage or current) in any branch of a bilateral linear circuit having more than " +
                       "one independent source equals the algebraic sum of the responses caused by each independent source acting alone, where all the other independent sources are replaced by their internal impedances. " +
                       "To ascertain the contribution of each individual source, all of the other sources first must be 'turned off' (set to zero) by: a) replacing all other independent voltage sources with a short circuit " +
                       "(thereby eliminating difference of potential i.e. V=0; internal impedance of ideal voltage source is zero (short circuit)); b) replacing all other independent current sources with an open circuit " +
                       "(thereby eliminating current i.e. I=0; internal impedance of ideal current source is infinite (open circuit)). This procedure is followed for each source, then the resultant responses are added to " +
                       "determine the true operation of the circuit. The resultant circuit operation is the superposition of the various voltage and current sources.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq5, 
                       text_input="The superposition theorem is very important in circuit analysis. It is used in converting any circuit into its Norton equivalent or Thevenin equivalent. The theorem is applicable to linear " +
                       "networks (time varying or time invariant) consisting of independent sources, linear dependent sources, linear passive elements (resistors, inductors, capacitors) and linear transformers. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq5, 
                       text_input="Another point that should be considered, is that superposition only works for voltage and current but not power. In other words the sum of the powers of each source with the other sources " +
                       "turned off is not the real consumed power. To calculate power we should first use superposition to find both current and voltage of each linear element and then calculate the sum of the multiplied voltages and currents. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to read resistor color code?
    awq6 = add_answer_with_question(rulebase=rb,
                                    question="How to read resistor color code")
    awq6.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq6,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq6,
                       node=resistor_node)
    add_answer_keyword(answer_with_question=awq6,
                       node=color_code_node)
    add_answer_element(answer_with_question=awq6, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="https://www.youtube.com/embed/SjlnW5g9np4",
                       element_type="video")
    add_answer_element(answer_with_question=awq6, 
                       text_input="The electronic color code is used to indicate the values or ratings of electronic components, very " +
                       "commonly for resistors, but also for capacitors, inductors, and others. A separate code, the 25-pair color code, " +
                       "is used to identify wires in some telecommunications cables. The electronic color code was developed in the early " +
                       "1920s by the Radio Manufacturers Association (now part of Electronic Industries Alliance (EIA)), and was published as " +
                       "EIA-RS-279. The current international standard is IEC 60062. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to use a Breadboard?
    awq7 = add_answer_with_question(rulebase=rb,
                                    question="How to use a Breadboard")
    awq7.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq7,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq7,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq7,
                       node=breadboard_node)
    add_answer_element(answer_with_question=awq7, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/cf6XZ4gs7Ao",
                       element_type="video")
    
    # How to use a DC Power Supply?
    awq8 = add_answer_with_question(rulebase=rb,
                                    question="How to use a DC Power Supply")
    awq8.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq8,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq8,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq8,
                       node=dc_source_node)
    add_answer_element(answer_with_question=awq8, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/mOpCxeqXWEI",
                       element_type="video")
    add_answer_element(answer_with_question=awq8, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq8, 
                       text_input="A power supply is an electronic device that supplies electric energy to an electrical load. The primary function of a power " +
                       "supply is to convert one form of electrical energy to another and, as a result, power supplies are sometimes referred to as electric power " +
                       "converters. Some power supplies are discrete, stand-alone devices, whereas others are built into larger devices along with their loads. " +
                       "Every power supply must obtain the energy it supplies to its load, as well as any energy it consumes while performing that task, from an " +
                       "energy source. Depending on its design, a power supply may obtain energy from various types of energy sources, including electrical energy " +
                       "transmission systems, energy storage devices such as a batteries and fuel cells, electromechanical systems such as generators and alternators, " +
                       "solar power converters, or another power supply. All power supplies have a power input, which receives energy from the energy source, and a power " +
                       "output that delivers energy to the load. In most power supplies the power input and output consist of electrical connectors or hardwired circuit " +
                       "connections, though some power supplies employ wireless energy transfer in lieu of galvanic connections for the power input or output. Some power " +
                       "supplies have other types of inputs and outputs as well, for functions such as external monitoring and control.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to use a Multimeter?
    awq9 = add_answer_with_question(rulebase=rb,
                                    question="How to use a Multimeter")
    awq9.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq9,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq9,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq9,
                       node=multimeter_node)
    add_answer_element(answer_with_question=awq9, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/_o8M34NbXpk",
                       element_type="video")
    add_answer_element(answer_with_question=awq9, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq9, 
                       text_input="A multimeter or a multitester, also known as a VOM (Volt-Ohm meter), is an electronic measuring instrument that combines several " +
                       "measurement functions in one unit. A typical multimeter would include basic features such as the ability to measure voltage, current, and " +
                       "resistance. Analog multimeters use a microammeter whose pointer moves over a scale calibrated for all the different measurements that can be " +
                       "made. Digital multimeters (DMM, DVOM) display the measured value in numerals, and may also display a bar of a length proportional to the quantity " +
                       "being measured. Digital multimeters are now far more common than analog ones, but analog multimeters are still preferable in some cases, for " +
                       "example when monitoring a rapidly varying value. A multimeter can be a hand-held device useful for basic fault finding and field service work, " +
                       "or a bench instrument which can measure to a very high degree of accuracy. They can be used to troubleshoot electrical problems in a wide array of " +
                       "industrial and household devices such as electronic equipment, motor controls, domestic appliances, power supplies, and wiring systems. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to measure Current?
    awq10 = add_answer_with_question(rulebase=rb,
                                    question="How to measure Current")
    awq10.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq10,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq10,
                       node=measure_node)
    add_answer_keyword(answer_with_question=awq10,
                       node=current_node)
    add_answer_element(answer_with_question=awq10, 
                       text_input="Current has to be measured in series. If voltage is measured by poking at VCC and GND (in parallel), " +
                       "to measure current you have to physically interrupt the flow of current and put the meter in one line. To learn more please follow the link: ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq10, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/wLA6Wkb-TLQ",
                       element_type="video")
    add_answer_element(answer_with_question=awq10, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to measure Voltage?
    awq11 = add_answer_with_question(rulebase=rb,
                                    question="How to measure Voltage")
    awq11.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq11,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq11,
                       node=measure_node)
    add_answer_keyword(answer_with_question=awq11,
                       node=voltage_node)
    add_answer_element(answer_with_question=awq11, 
                       text_input="Voltage is the difference of electrical potential between two points of an electrical or electronic " +
                       "circuit, expressed in volts. It measures the potential energy of an electric field to cause an electric current " +
                       "in an electrical conductor. Most measurement devices can measure voltage. Two common voltage measurements are " +
                       "direct current (DC) and alternating current (AC). ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq11, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/wLA6Wkb-TLQ",
                       element_type="video")
    add_answer_element(answer_with_question=awq11, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to use a Function Generator?
    awq12 = add_answer_with_question(rulebase=rb,
                                    question="How to use a Function Generator")
    awq12.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq12,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq12,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq12,
                       node=func_gen_node)
    add_answer_element(answer_with_question=awq12, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/uBm7veURIFk",
                       element_type="video")
    add_answer_element(answer_with_question=awq12, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq12, 
                       text_input="",
                       image_input=None,
                       equation_input="A function generator is a piece of electronic test equipment or software used to generate different types " +
                       "of electrical waveforms over a wide range of frequencies. Some of the most common waveforms produced by the function " +
                       "generator are the sine, square, triangular and sawtooth shapes. These waveforms can be either repetitive or single-shot " +
                       "(which requires an internal or external trigger source). Integrated circuits used to generate waveforms may also be " +
                       "described as function generator ICs. Although function generators cover both audio and RF frequencies, they are usually " +
                       "not suitable for applications that need low distortion or stable frequency signals. When those traits are required, other " +
                       "signal generators would be more appropriate. Some function generators can be phase-locked to an external signal source " +
                       "(which may be a frequency reference) or another function generator. Function generators are used in the development, test " +
                       "and repair of electronic equipment. For example, they may be used as a signal source to test amplifiers or to introduce an " +
                       "error signal into a control loop. ",
                       video_input="",
                       element_type="text")
    
    # How to use an Oscilloscope?
    awq13 = add_answer_with_question(rulebase=rb,
                                    question="How to use an Oscilloscope")
    awq13.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq13,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq13,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq13,
                       node=oscilloscope_node)
    add_answer_element(answer_with_question=awq13, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/uBm7veURIFk",
                       element_type="video")
    add_answer_element(answer_with_question=awq13, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq13, 
                       text_input="An oscilloscope is a type of electronic test instrument that allows observation of constantly varying " +
                       "signal voltages, usually as a two-dimensional plot of one or more signals as a function of time. Non-electrical " +
                       "signals (such as sound or vibration) can be converted to voltages and displayed. Oscilloscopes are used to observe " +
                       "the change of an electrical signal over time, such that voltage and time describe a shape which is continuously " +
                       "graphed against a calibrated scale. The observed waveform can be analyzed for such properties as amplitude, frequency, " +
                       "rise time, time interval, distortion and others. Modern digital instruments may calculate and display these properties " +
                       "directly. Originally, calculation of these values required manually measuring the waveform against the scales built into " +
                       "the screen of the instrument. The oscilloscope can be adjusted so that repetitive signals can be observed as a continuous " +
                       "shape on the screen. A storage oscilloscope allows single events to be captured by the instrument and displayed for a " +
                       "relatively long time, allowing human observation of events too fast to be directly perceptible. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq13, 
                       text_input="The signal to be measured is fed to one of the input connectors, which is usually a coaxial connector such as a " +
                       "BNC or UHF type. Binding posts or banana plugs may be used for lower frequencies. If the signal source has its own coaxial " +
                       "connector, then a simple coaxial cable is used; otherwise, a specialized cable called a 'scope probe', supplied with the " +
                       "oscilloscope, is used. In general, for routine use, an open wire test lead for connecting to the point being observed is not " +
                       "satisfactory, and a probe is generally necessary. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # Safety Measures
    awq14 = add_answer_with_question(rulebase=rb,
                                    question="Safety Measures")
    awq14.topic.add(hardware, safety)
    add_answer_keyword(answer_with_question=awq14,
                       node=safety_node)
    add_answer_element(answer_with_question=awq14, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/Uck73jLjy7E",
                       element_type="video")
    add_answer_element(answer_with_question=awq14, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to use Multisim?
    awq15 = add_answer_with_question(rulebase=rb,
                                    question="How to use Multisim")
    awq15.topic.add(simulation, VLA)
    add_answer_keyword(answer_with_question=awq15,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq15,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq15,
                       node=multisim_node)
    add_answer_element(answer_with_question=awq15, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/J8i3VLGJpQg",
                       element_type="video")
    add_answer_element(answer_with_question=awq15, 
                       text_input="Multisim is an industry-standard, best-in-class SPICE simulation environment. It is the cornerstone " +
                       "of the NI circuits teaching solution to build expertise through practical application in designing, prototyping, and testing " +
                       "electrical circuits. The Multisim design approach helps you save prototype iterations and optimize printed circuit board (PCB) " +
                       "designs earlier in the process. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to get help with VLA?
    awq16 = add_answer_with_question(rulebase=rb,
                                    question="How to get help with VLA")
    awq16.topic.add(general, VLA)
    add_answer_keyword(answer_with_question=awq16,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq16,
                       node=help_node)
    add_answer_keyword(answer_with_question=awq16,
                       node=vla_node)
    add_answer_element(answer_with_question=awq16, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/QRxqXkI7VhE",
                       element_type="video")
    
    # How to change your password in VLA?
    awq17 = add_answer_with_question(rulebase=rb,
                                    question="How to change your password in VLA")
    awq17.topic.add(general, VLA)
    add_answer_keyword(answer_with_question=awq17,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq17,
                       node=change_node)
    add_answer_keyword(answer_with_question=awq17,
                       node=vla_node)
    add_answer_keyword(answer_with_question=awq17,
                       node=password_node)
    add_answer_element(answer_with_question=awq17, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/mYmT1Gy6KdE",
                       element_type="video")
    
    # What is SPICE?
    awq18 = add_answer_with_question(rulebase=rb,
                                    question="What is SPICE")
    awq18.topic.add(simulation)
    add_answer_keyword(answer_with_question=awq18,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq18,
                       node=spice_node) 
    add_answer_element(answer_with_question=awq18, 
                       text_input="SPICE stands for Simulation Program with Integrated Circuit Emphasis. It is a " +
                       "general-purpose, open source analog electronic circuit simulator. It is a powerful program " +
                       "that is used in integrated circuit and board-level design to check the integrity of circuit " +
                       "designs and to predict circuit behavior.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is Multisim?
    awq19 = add_answer_with_question(rulebase=rb,
                                    question="What is Multisim")
    awq19.topic.add(simulation)
    add_answer_keyword(answer_with_question=awq19,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq19,
                       node=multisim_node)
    add_answer_element(answer_with_question=awq19, 
                       text_input="Multisim is an industry-standard, best-in-class SPICE simulation environment. The Multisim " +
                       "design approach helps you save prototype iterations and optimize printed circuit board (PCB) designs earlier in the process. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a power supply?
    awq20 = add_answer_with_question(rulebase=rb,
                                    question="What is a power supply")
    awq20.topic.add(hardware, simulation, equipment)
    add_answer_keyword(answer_with_question=awq20,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq20,
                       node=dc_source_node)
    add_answer_element(answer_with_question=awq20, 
                       text_input="A power supply is an electronic device that supplies electric energy to an electrical load. The primary function of a " +
                       "power supply is to convert one form of electrical energy to another and, as a result, power supplies are sometimes referred to as " +
                       "electric power converters. Some power supplies are discrete, stand-alone devices, whereas others are built into larger devices along " +
                       "with their loads. Every power supply must obtain the energy it supplies to its load, as well as any energy it consumes while performing " +
                       "that task, from an energy source. Depending on its design, a power supply may obtain energy from various types of energy sources, " +
                       "including electrical energy transmission systems, energy storage devices such as a batteries and fuel cells, electromechanical systems " +
                       "such as generators and alternators, solar power converters, or another power supply. All power supplies have a power input, which receives " +
                       "energy from the energy source, and a power output that delivers energy to the load. In most power supplies the power input and output consist " +
                       "of electrical connectors or hardwired circuit connections, though some power supplies employ wireless energy transfer in lieu of galvanic " +
                       "connections for the power input or output. Some power supplies have other types of inputs and outputs as well, for functions such as external " +
                       "monitoring and control.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a function generator?
    awq21 = add_answer_with_question(rulebase=rb,
                                    question="What is a function generator")
    awq21.topic.add(hardware, simulation, equipment)
    add_answer_keyword(answer_with_question=awq21,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq21,
                       node=func_gen_node)
    add_answer_element(answer_with_question=awq21, 
                       text_input="A function generator is a piece of electronic test equipment or software used to generate different types of electrical waveforms over " +
                       "a wide range of frequencies. Some of the most common waveforms produced by the function generator are the sine, square, triangular and sawtooth " +
                       "shapes. These waveforms can be either repetitive or single-shot (which requires an internal or external trigger source). Integrated circuits used " +
                       "to generate waveforms may also be described as function generator ICs. Although function generators cover both audio and RF frequencies, they are " +
                       "usually not suitable for applications that need low distortion or stable frequency signals. When those traits are required, other signal generators " +
                       "would be more appropriate. Some function generators can be phase-locked to an external signal source (which may be a frequency reference) or another " +
                       "function generator. Function generators are used in the development, test and repair of electronic equipment. For example, they may be used as a signal " +
                       "source to test amplifiers or to introduce an error signal into a control loop. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a multimeter?
    awq22 = add_answer_with_question(rulebase=rb,
                                    question="What is a multimeter")
    awq22.topic.add(hardware, simulation, equipment)
    add_answer_keyword(answer_with_question=awq22,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq22,
                       node=multimeter_node)
    add_answer_element(answer_with_question=awq22, 
                       text_input="A multimeter or a multitester, also known as a VOM (Volt-Ohm meter), is an electronic measuring instrument that combines several measurement " +
                       "functions in one unit. A typical multimeter would include basic features such as the ability to measure voltage, current, and resistance. Analog multimeters " +
                       "use a microammeter whose pointer moves over a scale calibrated for all the different measurements that can be made. Digital multimeters (DMM, DVOM) display " +
                       "the measured value in numerals, and may also display a bar of a length proportional to the quantity being measured. Digital multimeters are now far more " +
                       "common than analog ones, but analog multimeters are still preferable in some cases, for example when monitoring a rapidly varying value. A multimeter can be " +
                       "a hand-held device useful for basic fault finding and field service work, or a bench instrument which can measure to a very high degree of accuracy. They can " +
                       "be used to troubleshoot electrical problems in a wide array of industrial and household devices such as electronic equipment, motor controls, domestic appliances, " +
                       "power supplies, and wiring systems.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is an oscilloscope?
    awq23 = add_answer_with_question(rulebase=rb,
                                    question="What is an oscilloscope")
    awq23.topic.add(hardware, simulation, equipment)
    add_answer_keyword(answer_with_question=awq23,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq23,
                       node=oscilloscope_node)
    add_answer_element(answer_with_question=awq23, 
                       text_input="An oscilloscope is a type of electronic test instrument that allows observation of constantly varying signal voltages, usually as a two-dimensional plot of " +
                       "one or more signals as a function of time. Non-electrical signals (such as sound or vibration) can be converted to voltages and displayed. Oscilloscopes are used to " +
                       "observe the change of an electrical signal over time, such that voltage and time describe a shape which is continuously graphed against a calibrated scale. The observed " +
                       "waveform can be analyzed for such properties as amplitude, frequency, rise time, time interval, distortion and others. Modern digital instruments may calculate and display " +
                       "these properties directly. Originally, calculation of these values required manually measuring the waveform against the scales built into the screen of the instrument. " +
                       "The oscilloscope can be adjusted so that repetitive signals can be observed as a continuous shape on the screen. A storage oscilloscope allows single events to be captured " +
                       "by the instrument and displayed for a relatively long time, allowing human observation of events too fast to be directly perceptible. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to measure resistance of a resistor?
    awq24 = add_answer_with_question(rulebase=rb,
                                    question="How to measure resistance of a resistor")
    awq24.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq24,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq24,
                       node=measure_node)
    add_answer_keyword(answer_with_question=awq24,
                       node=resistance_node)
    add_answer_keyword(answer_with_question=awq24,
                       node=resistor_node)
    add_answer_element(answer_with_question=awq24, 
                       text_input="Resistors have color codes on them. However, if you have no color code table to look-up the resistor values, a multimeter is very handy at measuring resistance. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is the time-constant of a RC circuit?
    awq25 = add_answer_with_question(rulebase=rb,
                                    question="What is the time constant of a RC circuit")
    awq25.topic.add(theory)
    add_answer_keyword(answer_with_question=awq25,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq25,
                       node=timeconstant_node)
    add_answer_keyword(answer_with_question=awq25,
                       node=circuit_node)
    add_answer_element(answer_with_question=awq25, 
                       text_input="The RC time constant, also called tau, is the time constant (in seconds) of an RC circuit, is equal to the product of the circuit resistance (in ohms) and the circuit capacitance (in farads). ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to calculate the time-constant in an RC circuit?
    awq26 = add_answer_with_question(rulebase=rb,
                                    question="How to calculate the time constant in an RC circuit")
    awq26.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq26,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq26,
                       node=compute_node)
    add_answer_keyword(answer_with_question=awq25,
                       node=timeconstant_node)
    add_answer_keyword(answer_with_question=awq26,
                       node=circuit_node)
    add_answer_element(answer_with_question=awq26, 
                       text_input="The RC time constant, also called tau, is the time constant (in seconds) of an RC circuit, is equal to the product of the circuit resistance (in ohms) and the circuit capacitance (in farads). ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is Ohm's Law?
    awq27 = add_answer_with_question(rulebase=rb,
                                    question="What is Ohms Law")
    awq27.topic.add(theory)
    add_answer_keyword(answer_with_question=awq27,
                       node=what_node)
    add_answer_element(answer_with_question=awq27, 
                       text_input="Ohm's law states that the current through a conductor between two points is directly proportional to the potential difference across the two points. Introducing the constant of proportionality, " +
                       "the resistance, one arrives at the usual mathematical equation that describes this relationship:",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq27, 
                       text_input="I = \\frac{V}{R}",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="latex")
    add_answer_element(answer_with_question=awq27, 
                       text_input="where I is the current through the conductor in units of amperes, V is the potential difference measured across the conductor in units of volts, and R is the resistance of the conductor in units of ohms. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to calculate series resistance?
    awq28 = add_answer_with_question(rulebase=rb,
                                    question="How to calculate series resistance")
    awq28.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq28,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq28,
                       node=compute_node)
    add_answer_keyword(answer_with_question=awq28,
                       node=series_node)
    add_answer_keyword(answer_with_question=awq28,
                       node=resistance_node)
    add_answer_element(answer_with_question=awq28, 
                       text_input="Equivalent resistance of the circuit with series of resistors is calculated as follows,",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq28, 
                       text_input="",
                       image_input=None,
                       equation_input="R_{eq} = R_1 + R_2 + \\cdots + R_n",
                       video_input="",
                       element_type="latex")
    
    # How to calculate parallel resistance?
    awq29 = add_answer_with_question(rulebase=rb,
                                    question="How to calculate parallel resistance")
    awq29.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq29,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq29,
                       node=compute_node)
    add_answer_keyword(answer_with_question=awq29,
                       node=parallel_node)
    add_answer_keyword(answer_with_question=awq29,
                       node=resistance_node)
    add_answer_element(answer_with_question=awq29, 
                       text_input="Equivalent resistance of the circuit with resistors in parallel is calculated as follows:",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq29, 
                       text_input="",
                       image_input=None,
                       equation_input="\\frac{1}{R_{eq}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \cdots + \\frac{1}{R_n}",
                       video_input="",
                       element_type="latex")
    
    # How to calculate capacitance in parallel?
    awq30 = add_answer_with_question(rulebase=rb,
                                    question="How to calculate capacitance in parallel")
    awq30.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq30,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq30,
                       node=compute_node)
    add_answer_keyword(answer_with_question=awq30,
                       node=parallel_node)
    add_answer_keyword(answer_with_question=awq30,
                       node=capacitance_node)
    add_answer_element(answer_with_question=awq30, 
                       text_input="Capacitors in a parallel configuration each have the same applied voltage. Their capacitances add up. Charge is apportioned among them by size. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq30, 
                       text_input="",
                       image_input=None,
                       equation_input="C_{eq} = C_1 + C_2 + \\cdots + C_n",
                       video_input="",
                       element_type="latex")
    
    # How to calculate capacitance in series?
    awq31 = add_answer_with_question(rulebase=rb,
                                    question="How to calculate capacitance in series")
    awq31.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq31,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq31,
                       node=compute_node)
    add_answer_keyword(answer_with_question=awq31,
                       node=series_node)
    add_answer_keyword(answer_with_question=awq31,
                       node=capacitance_node)
    add_answer_element(answer_with_question=awq31, 
                       text_input="The reciprocal of the equivalent capacitance of n capacitors connected in series is the sum of the reciprocals of the individual capacitances.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq31, 
                       text_input="",
                       image_input=None,
                       equation_input="\\frac{1}{C_{eq}} = \\frac{1}{C_1} + \\frac{1}{C_2} + \\cdots + \\frac{1}{C_n}",
                       video_input="",
                       element_type="latex")
    
    # How to calculate inductance in series?
    awq32 = add_answer_with_question(rulebase=rb,
                                    question="How to calculate inductance in series")
    awq32.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq32,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq32,
                       node=compute_node)
    add_answer_keyword(answer_with_question=awq32,
                       node=series_node)
    add_answer_keyword(answer_with_question=awq32,
                       node=inductance_node)
    add_answer_element(answer_with_question=awq32, 
                       text_input="Inductors in series configuration each have the same applied voltage. Their inductances add up:",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq32, 
                       text_input="",
                       image_input=None,
                       equation_input="L_{eq} = L_1 + L_2 + \\cdots + L_n",
                       video_input="",
                       element_type="latex")
    
    # How to calculate inductance in parallel?
    awq33 = add_answer_with_question(rulebase=rb,
                                    question="How to calculate inductance in parallel")
    awq33.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq33,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq33,
                       node=compute_node)
    add_answer_keyword(answer_with_question=awq33,
                       node=parallel_node)
    add_answer_keyword(answer_with_question=awq33,
                       node=inductance_node)
    add_answer_keyword(answer_with_question=awq33,
                       node=inductance_node)
    add_answer_element(answer_with_question=awq33, 
                       text_input="The reciprocal of the equivalent inductance of two capacitors connected in parallel is the sum of the reciprocals of the individual inductances.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq33, 
                       text_input="",
                       image_input=None,
                       equation_input="\\frac{1}{L_{eq}} = \\frac{1}{L_1} + \\frac{1}{L_2} + \\cdots + \\frac{1}{L_n}",
                       video_input="",
                       element_type="latex")
    
    # What is maximum power transfer?
    awq34 = add_answer_with_question(rulebase=rb,
                                    question="What is maximum power transfer")
    awq34.topic.add(theory)
    add_answer_keyword(answer_with_question=awq34,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq34,
                       node=max_power_node)
    add_answer_element(answer_with_question=awq34, 
                       text_input="In electrical engineering, the maximum power transfer theorem states that to obtain maximum external power from a source with a finite internal resistance, the resistance of the load must equal the resistance of the source as viewed from its output terminals. The theorem results in " +
                       "maximum power transfer, and not maximum efficiency. If the resistance of the load is made larger than the resistance of the source, then efficiency is higher, since a higher percentage of the source power is transferred to the load, but the magnitude of the load power is lower since the total circuit resistance goes up.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq34, 
                       text_input="If the load resistance is smaller than the source resistance, then most of the power ends up being dissipated in the source, and although the total power dissipated is higher, due to a lower total resistance, it turns out that the amount dissipated in the load is reduced.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq34, 
                       text_input="The theorem states how to choose (so as to maximize power transfer) the load resistance, once the source resistance is given. It is a common misconception to apply the theorem in the opposite scenario. It does not say how to choose the source resistance for a given load resistance. In fact, the source resistance that " +
                       "maximizes power transfer is always zero, regardless of the value of the load resistance. The theorem can be extended to alternating current circuits that include reactance, and states that maximum power transfer occurs when the load impedance is equal to the complex conjugate of the source impedance.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is Norton's theorem?
    awq35 = add_answer_with_question(rulebase=rb,
                                    question="What is Nortons theorem")
    awq35.topic.add(theory)
    add_answer_keyword(answer_with_question=awq35,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq35,
                       node=norton_node)
    add_answer_element(answer_with_question=awq35, 
                       text_input="Norton's Theorem states that it is possible to simplify any linear circuit, no matter how complex, to an equivalent circuit with just a single current source and parallel resistance connected to a load. All underlying equations must be linear (no exponents or roots). ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is Thevinin's theorem?
    awq36 = add_answer_with_question(rulebase=rb,
                                    question="What is Thevinins theorem")
    awq36.topic.add(theory)
    add_answer_keyword(answer_with_question=awq36,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq36,
                       node=thevenin_node)
    add_answer_element(answer_with_question=awq36, 
                       text_input="Thevenin's Theorem states that it is possible to simplify any linear circuit, no matter how complex, to an equivalent circuit with just a single voltage source and series resistance connected to a load. " +
                       "The qualification of “linear” is identical to that found in the Superposition Theorem, where all the underlying equations must be linear (no exponents or roots). If we're dealing with passive components (such as " +
                       "resistors, and later, inductors and capacitors), this is true. However, there are some components (especially certain gas-discharge and semiconductor components) which are nonlinear: that is, their opposition " +
                       "to current changes with voltage and/or current. As such, we would call circuits containing these types of components, nonlinear circuits. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq36, 
                       text_input="Thevenin's Theorem is especially useful in analyzing power systems and other circuits where one particular resistor in the circuit (called the “load” resistor) is subject to change, and re-calculation " +
                       "of the circuit is necessary with each trial value of load resistance, to determine voltage across it and current through it. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is the power rating of resistors?
    awq37 = add_answer_with_question(rulebase=rb,
                                    question="What is the power rating of resistors")
    awq37.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq37,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq37,
                       node=power_node)
    add_answer_keyword(answer_with_question=awq37,
                       node=rating_node)
    add_answer_keyword(answer_with_question=awq37,
                       node=resistor_node)
    add_answer_element(answer_with_question=awq37, 
                       text_input="In engineering, the power rating of a device is a guideline set by the manufacturer as a maximum power to be used with that device. This limit is usually set somewhat lower than the level where the " +
                       "device will be damaged, to allow a margin of safety. In devices which primarily dissipate electric power or convert it into mechanical power, such as resistors, electric motors, and speakers, the power " +
                       "rating given is usually the maximum power that can be safely dissipated by the device. The usual reason for this limit is heat, although in certain electromechanical devices, particularly speakers, it is " +
                       "to prevent mechanical damage. When heat is the limiting factor, the power rating is easily calculated.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to calculate power rating of resistors?
    awq38 = add_answer_with_question(rulebase=rb,
                                    question="How to calculate power rating of resistors")
    awq38.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq38,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq38,
                       node=compute_node)
    add_answer_keyword(answer_with_question=awq38,
                       node=power_node)
    add_answer_keyword(answer_with_question=awq38,
                       node=resistor_node)
    add_answer_element(answer_with_question=awq38, 
                       text_input="In engineering, the power rating of a device is a guideline set by the manufacturer as a maximum power to be used with that device. This limit is usually set somewhat lower than the level " +
                       "where the device will be damaged, to allow a margin of safety. In devices which primarily dissipate electric power or convert it into mechanical power, such as resistors, electric motors, and speakers, " +
                       "the power rating given is usually the maximum power that can be safely dissipated by the device. The usual reason for this limit is heat, although in certain electromechanical devices, particularly " +
                       "speakers, it is to prevent mechanical damage. When heat is the limiting factor, the power rating is easily calculated.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How is a potentiometer used in a circuit?
    awq39 = add_answer_with_question(rulebase=rb,
                                    question="How is a potentiometer used in a circuit")
    awq39.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq39,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq39,
                       node=potentiometer_node)
    add_answer_keyword(answer_with_question=awq39,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq39,
                       node=circuit_node)
    add_answer_element(answer_with_question=awq39, 
                       text_input="A potentiometer is a three-terminal resistor with a sliding or rotating contact that forms an adjustable voltage divider. If only two terminals are used, one end and the wiper, it acts as a " +
                       "variable resistor or rheostat. A potentiometer measuring instrument is essentially a voltage divider used for measuring electric potential (voltage); the component is an implementation of the same " +
                       "principle, hence its name. Potentiometers are commonly used to control electrical devices such as volume controls on audio equipment. Potentiometers operated by a mechanism can be used as position " +
                       "transducers, for example, in a joystick. Potentiometers are rarely used to directly control significant power (more than a watt), since the power dissipated in the potentiometer would be comparable " +
                       "to the power in the controlled load.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is power dissipation in a resistor?
    awq40 = add_answer_with_question(rulebase=rb,
                                    question="What is power dissipation in a resistor")
    awq40.topic.add(simulation, hardware)
    add_answer_keyword(answer_with_question=awq40,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq40,
                       node=power_node)
    add_answer_keyword(answer_with_question=awq40,
                       node=dissipation_node)
    add_answer_keyword(answer_with_question=awq40,
                       node=resistor_node)
    add_answer_element(answer_with_question=awq40, 
                       text_input="If a current I flows through a given element in a circuit, losing voltage V in the process, then the power dissipated by that circuit element is the product of that current and voltage:",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq40, 
                       text_input="",
                       image_input=None,
                       equation_input="P+VI",
                       video_input="",
                       element_type="latex")
    
    # What are Kirchoff's Laws?
    awq41 = add_answer_with_question(rulebase=rb,
                                    question="What are Kirchoffs Laws")
    awq41.topic.add(theory)
    add_answer_keyword(answer_with_question=awq41,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq41,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq41,
                       node=kirchoffs_node)
    add_answer_element(answer_with_question=awq41, 
                       text_input="Also known as Kirchhoff's First Law / Kirchhoff's Current Law / KCL / Kirchhoff's Point Rule / Kirchhoff's Junction Rule / The Nodal Rule. The principle of conservation of " +
                       "electric charge implies that at any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node. " +
                       "Or in other words, the algebraic sum of currents in a network of conductors meeting at a point is zero.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq41, 
                       text_input="When current is a signed (positive or negative) quantity reflecting direction towards or away from a node, this principle can be stated as:",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq41, 
                       text_input="",
                       image_input=None,
                       equation_input="\\sum_{k=1}^n I_k = 0",
                       video_input="",
                       element_type="latex")
    add_answer_element(answer_with_question=awq41, 
                       text_input="where n is the total number of branches with currents flowing towards or away from the node. The formula is valid for complex currents. The law is based on the conservation of " +
                       "charge whereby the charge (measured in coulombs) is the product of the current (in amperes) and the time (in seconds).",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq41, 
                       text_input="Kirchhoff's voltage law (KVL) states that the sum of all the voltages around the loop is equal to zero. This law is also called Kirchhoff's second law, Kirchhoff's loop (or mesh) " +
                       "rule, and Kirchhoff's second rule. The principle of conservation of energy implies that the directed sum of the electrical potential differences (voltage) around any closed network is zero. " +
                       "KVL can be stated as follows, ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq41, 
                       text_input="",
                       image_input=None,
                       equation_input="\\sum_{k=1}^n V_k = 0",
                       video_input="",
                       element_type="latex")
    add_answer_element(answer_with_question=awq41, 
                       text_input="where n is the total number of voltages measured. The voltages may also be complex. This law is based on the conservation of energy whereby voltage is defined as the energy per unit " +
                       "charge. The total amount of energy gained per unit charge must equal the amount of energy lost per unit charge, as energy and charge are both conserved.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a voltage divider?
    awq42 = add_answer_with_question(rulebase=rb,
                                    question="What is a voltage divider")
    awq42.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq42,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq42,
                       node=voltage_node)
    add_answer_keyword(answer_with_question=awq42,
                       node=division_node)
    add_answer_element(answer_with_question=awq42, 
                       text_input="In electronics, a voltage divider (also known as a potential divider) is a passive linear circuit that produces an output voltage (Vout) that is a fraction of its input voltage " +
                       "(Vin). Voltage division is the result of distributing the input voltage among the components of the divider. A simple example of a voltage divider is two resistors connected in series, with " +
                       "the input voltage applied across the resistor pair and the output voltage emerging from the connection between them.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq42, 
                       text_input="Resistor voltage dividers are commonly used to create reference voltages, or to reduce the magnitude of a voltage so it can be measured, and may also be used as signal attenuators at " +
                       "low frequencies. For direct current and relatively low frequencies, a voltage divider may be sufficiently accurate if made only of resistors; where frequency response over a wide range is required " +
                       "(such as in an oscilloscope probe), a voltage divider may have capacitive elements added to compensate load capacitance. In electric power transmission, a capacitive voltage divider is used for measurement of high voltage.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a current divider?
    awq43 = add_answer_with_question(rulebase=rb,
                                    question="What is a current divider")
    awq43.topic.add(theory, simulation, hardware)
    add_answer_keyword(answer_with_question=awq43,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq43,
                       node=current_node)
    add_answer_keyword(answer_with_question=awq43,
                       node=division_node)
    add_answer_element(answer_with_question=awq43, 
                       text_input="In electronics, a current divider is a simple linear circuit that produces an output current (IX) that is a fraction of its input current (IT). Current division refers to the splitting of current " +
                       "between the branches of the divider. The currents in the various branches of such a circuit will always divide in such a way as to minimize the total energy expended. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a breadboard?
    awq44 = add_answer_with_question(rulebase=rb,
                                    question="What is a breadboard")
    awq44.topic.add(equipment, hardware)
    add_answer_keyword(answer_with_question=awq44,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq44,
                       node=breadboard_node)
    add_answer_element(answer_with_question=awq44, 
                       text_input="A breadboard (or protoboard) is a construction base for prototyping of electronics. Because the solderless breadboard does not require soldering, it is reusable. This makes it easy to use for " +
                       "creating temporary prototypes and experimenting with circuit design. Older breadboard types did not have this property. A stripboard (veroboard) and similar prototyping printed circuit boards, which " +
                       "are used to build semi-permanent soldered prototypes or one-offs, cannot easily be reused. A variety of electronic systems may be prototyped by using breadboards, from small analog and digital circuits " +
                       "to complete central processing units (CPUs).",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is an Opamp?
    awq45 = add_answer_with_question(rulebase=rb,
                                    question="What is an OpAmp")
    awq45.topic.add(theory)
    add_answer_keyword(answer_with_question=awq45,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq45,
                       node=opamp_node)
    add_answer_element(answer_with_question=awq45, 
                       text_input="An operational amplifier (op-amp) is a DC-coupled high-gain electronic voltage amplifier with a differential input and, usually, a single-ended output. In this configuration, an op-amp produces " +
                       "an output potential (relative to circuit ground) that is typically hundreds of thousands of times larger than the potential difference between its input terminals. Operational amplifiers had their origins " +
                       "in analog computers, where they were used to do mathematical operations in many linear, non-linear and frequency-dependent circuits. Characteristics of a circuit using an op-amp are set by external components " +
                       "with little dependence on temperature changes or manufacturing variations in the op-amp itself, which makes op-amps popular building blocks for circuit design. Op-amps are among the most widely used electronic " +
                       "devices today, being used in a vast array of consumer, industrial, and scientific devices. Op-amps may be packaged as components, or used as elements of more complex integrated circuits.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a filter?
    awq46 = add_answer_with_question(rulebase=rb,
                                    question="What is a filter")
    awq46.topic.add(theory)
    add_answer_keyword(answer_with_question=awq46,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq46,
                       node=filter_node)
    add_answer_element(answer_with_question=awq46, 
                       text_input="Electronic filters are analog circuits which perform signal processing functions, specifically to remove unwanted frequency components from the signal, to enhance wanted ones, or both.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a low pass filter?
    awq47 = add_answer_with_question(rulebase=rb,
                                    question="What is a low pass filter")
    awq47.topic.add(theory)
    add_answer_keyword(answer_with_question=awq47,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq47,
                       node=filter_node)
    add_answer_keyword(answer_with_question=awq47,
                       node=low_node)
    add_answer_keyword(answer_with_question=awq47,
                       node=pass_node)
    add_answer_element(answer_with_question=awq47, 
                       text_input="A low-pass filter is a filter that passes low-frequency signals and attenuates (reduces the amplitude of) signals with frequencies higher than the cutoff frequency. The actual " +
                       "amount of attenuation for each frequency varies depending on specific filter design. It is sometimes called a high-cut filter, or treble cut filter in audio applications. A low-pass filter " +
                       "is the opposite of a high-pass filter. A band-pass filter is a combination of a low-pass and a high-pass. ",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    add_answer_element(answer_with_question=awq47, 
                       text_input="Low-pass filters exist in many different forms, including electronic circuits (such as a hiss filter used in audio), anti-aliasing filters for conditioning signals prior to " +
                       "analog-to-digital conversion, digital filters for smoothing sets of data, acoustic barriers, blurring of images, and so on. The moving average operation used in fields such as finance " +
                       "is a particular kind of low-pass filter, and can be analyzed with the same signal processing techniques as are used for other low-pass filters. Low-pass filters provide a smoother " +
                       "form of a signal, removing the short-term fluctuations, and leaving the longer-term trend.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is a high pass filter?
    awq48 = add_answer_with_question(rulebase=rb,
                                    question="What is a high pass filter")
    awq48.topic.add(theory)
    add_answer_keyword(answer_with_question=awq48,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq48,
                       node=filter_node)
    add_answer_keyword(answer_with_question=awq48,
                       node=high_node)
    add_answer_keyword(answer_with_question=awq48,
                       node=pass_node)
    add_answer_element(answer_with_question=awq48, 
                       text_input="A high-pass filter (HPF) is an electronic filter that passes high-frequency signals but attenuates (reduces the amplitude of) signals with frequencies lower than the cutoff " +
                       "frequency. The actual amount of attenuation for each frequency varies from filter to filter. A high-pass filter is usually modeled as a linear time-invariant system. It is sometimes " +
                       "called a low-cut filter or bass-cut filter. High-pass filters have many uses, such as blocking DC from circuitry sensitive to non-zero average voltages or RF devices. They can " +
                       "also be used in conjunction with a low-pass filter to make a bandpass filter.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # What is VLA?
    awq49 = add_answer_with_question(rulebase=rb,
                                    question="What is VLA")
    awq49.topic.add(VLA)
    add_answer_keyword(answer_with_question=awq49,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq49,
                       node=vla_node)
    add_answer_element(answer_with_question=awq49, 
                       text_input="The Virtual Lab Assistant (VLA) is a software tool currently under development by Temple University's Control, Sensor, Network, and Perception (CSNAP) " + 
                                   "laboratory to support open laboratory. The VLA project aims to create an interactive and intelligent framework for laboratory course work. " +
                                   "VLA is a new way to present laboratory work to students, and features an intelligent help module and a circuit recognition module. This project is sponsored by the NSF.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # How to use VLA?
    awq50 = add_answer_with_question(rulebase=rb,
                                    question="How to use VLA")
    awq50.topic.add(VLA)
    add_answer_keyword(answer_with_question=awq50,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq50,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq50,
                       node=vla_node)
    add_answer_element(answer_with_question=awq50, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="https://www.youtube.com/embed/sfsAhbkKrUs",
                       element_type="video")
    
    # Print out what we have added to the user.
    for vd in VocabDomain.objects.all():
        for vt in VocabTopic.objects.filter(domain=vd):
            print "- {0} - {1}".format(str(vd), str(vt))

# Add Vocab Domain, Vocab Topics, Words, definitions, and synonyms
def add_vocab_domain(name):
    vd = VocabDomain.objects.get_or_create(name=name)[0]
    return vd

def add_vocab_topic(topic, domain, def_useful):
    vt = VocabTopic.objects.get_or_create(topic=topic, domain=domain,
                                          def_useful=def_useful)[0]
    return vt

def add_node(word, definition, topic, views=0):
    n = Node.objects.get_or_create(word=word, definition=definition,
                                   topic=topic, views=views,
                                   date_added=timezone.now())[0]
    return n

def add_synonym(word, node):
    s = Synonym.objects.get_or_create(word=word, node=node)[0]
    return s

# Add Rulebase, answers, answer topics, etc.
def add_rulebase(name):
    rb = Rulebase.objects.get_or_create(name=name)[0]
    return rb

def add_answer_with_question(rulebase, question, views=0):
    awq = AnswerWithQuestion.objects.get_or_create(rulebase=rulebase,
                                                   question=question,
                                                   views=views,
                                                   date_added=timezone.now())[0]
    return awq

def add_answer_topic(rulebase, topic):
    at = AnswerTopic.objects.get_or_create(rulebase=rulebase,
                                           topic=topic)[0]
    return at

def add_answer_keyword(answer_with_question, node):
    ak = AnswerKeyword.objects.get_or_create(answer_with_question=answer_with_question,
                                             node=node)[0]
    return ak

 # element_type must be one of: 'text', 'image', 'equation', 'latex', 'video', 'table'
def add_answer_element(answer_with_question, text_input, image_input,
                         equation_input, video_input, element_type):
     ae = AnswerElement.objects.get_or_create(answer_with_question=answer_with_question,
                                              text_input=text_input,
                                              image_input=image_input,
                                              equation_input=equation_input,
                                              video_input=video_input,
                                              element_type=element_type)[0]
     return ae

# Start execution here!
if __name__ == '__main__':
    print "Starting VOCAB DOMAIN population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    from tutor.models import *
    populate()
