#!/usr/bin/env python
'''
Python program to convert a Multisim netlist to an acceptable format for 
circuit comparison

User's notes: The circuit comparator does not accept transistors and 
non-sine wave AC signals. Phase is also disregarded.

Inputs: 
  infile - Path to Multisim netlist
Outputs:
  outfile - String of converted 
Written by Zack Smith 2-05-15
'''
# Necessary Imports
from __future__ import division
import sys

# Functions
def read_file(filename):
    '''
    Read text file of filename;
    return lines in file
    '''
    try:
        with open(filename, 'r') as f:
            return f.read().splitlines()
    except IOError:
        print "Error opening or reading file: ", filename
        sys.exit()

def parse_file(lines, max_num):
  # Necessary flags and counters, I guess
  break_flag = 0; continue_flag = 0; dc_flag = 0; dc_counter = 0; ac_counter = 0; node_replacement = max_num
  # Dictionary to replace all user-defined nodes, because the comparator does not work with nodes which are strings
  replace_dict = {}
  replace_dict['0'] = '0'
  out_string = "* Translated Netlist *\n" 
  # Make sure we don't iterate over more lines than exist
  total_lines = len(lines); index = 0
  for main_loop in range(total_lines):
    continue_flag = 0; break_flag = 0; dc_flag = 0;
    # You're done if the index exceeds the length of the file. Congratulations!
    if index >= len(lines): 
        break
    # Remove lines with nothing in them
    if len(lines[index]) == 0:
        index += 1
        continue
    # Lines that start with * are to be ignored since they are comments
    if lines[index][0] == '*':
        index += 1
        continue
    # Remove sub circuit stuff
    if 'SUBCKT' in lines[index].upper():
        # Keep iterating until ENDS Or EOF
        continue_flag = 1
        while 'ENDS' not in lines[index].upper():
            index += 1
            if index >= len(lines): 
                # Break real hard
                break_flag = 1
                break
        # Increment one more time to remove the .ENDS
        index += 1
    if (break_flag): break
    if (continue_flag): continue
    # Remove model stuff
    if 'model' in lines[index].lower():
        # Keep iterating until + stop or EOF
        index += 1
        continue_flag = 1
        while '+' in lines[index]:
            index += 1
            if index >= len(lines): 
                # Break real hard
                break_flag = 1
                break
        # Increment one more time to remove the .ENDS
        index += 1
    if (break_flag): break
    if (continue_flag): continue
    ### Actual Parsing begin ###
    first_char = lines[index][0]
    split_line = lines[index].split()
    # Basic components
    if first_char == 'l' or first_char == 'r' or first_char == 'c' or first_char == 'd':
        # Line formatting
        name = split_line[0][1:]
        node1 = split_line[1]
        node2 = split_line[2]
        unit = ''
        # Dictionary Handler
        if node1 in replace_dict.keys():
            node1 = replace_dict[node1]
        else:
            replace_dict[node1] = node_replacement
            node1 = replace_dict[node1]
            node_replacement += 1
        if node2 in replace_dict.keys():
            node2 = replace_dict[node2]
        else:
            replace_dict[node2] = node_replacement
            node2 = replace_dict[node2]
            node_replacement += 1
        # Value handler
        if first_char != 'd': val = split_line[3]
        else: val = '' 
        # Evaluate because you can enter values as arithmetic expressions
        if len(val) != 0: 
            val = eval(val)
            if (not isinstance(val,(int,float))): val = list(val)[0]
        # Unit stuff
        if first_char == 'l' : unit = 'henry'
        elif first_char == 'r' : unit = 'ohms'
        elif first_char == 'c' : unit = 'farads'
        # Final result
        val = str(val)
        out_string += name + ' ' + str(node1) + ' ' + str(node2) + ' ' + val + unit + '\n'
        #print fin

    # Undefined component, required parse for component
    elif first_char == 'x':
        # 5-Term OpAmp
        if ('OPAMP' in lines[index].upper() or 'IDEAL_5' in lines[index].upper()) and len(split_line) == 7:
            name = split_line[0][1:]
            in_plus = split_line[1]; in_minus = split_line[2]
            out = split_line[3]
            vs_plus = split_line[4]; vs_minus = split_line[5]
            # Dictionary Handler
            if in_plus in replace_dict.keys(): 
                in_plus = replace_dict[in_plus]
            else:
                replace_dict[in_plus] = node_replacement
                node_replacement += 1

            if  in_minus in replace_dict.keys() :
                 in_minus = replace_dict[in_minus]
            else:
                replace_dict[in_minus] = node_replacement
                node_replacement += 1

            if  out in replace_dict.keys() :
                 out = replace_dict[out]
            else:
                replace_dict[out] = node_replacement
                node_replacement += 1

            if  vs_minus in replace_dict.keys() :
                 vs_minus = replace_dict[vs_minus]
            else:
                replace_dict[vs_minus] = node_replacement
                node_replacement += 1

            if  vs_plus in replace_dict.keys() :
                 vs_plus = replace_dict[vs_plus]
            else:
                replace_dict[vs_plus] = node_replacement
                node_replacement += 1
            # End string
            out_string += '*error1 ' + name + ' ' + str(in_plus) + ' ' + str(in_minus) + ' ' + str(out) + ' ' + str(vs_plus) + ' ' + str(vs_minus) + '\n'
            #print fin
        # 3-Term OpAmp
        elif ('IDEAL_3' in lines[index].upper()):
            name = split_line[0][1:]
            in_plus = split_line[1]; in_minus = split_line[2]
            out = split_line[3]
            # Dictionary Handler
            if in_plus in replace_dict.keys() :
                in_plus = replace_dict[in_plus]
            else:
                replace_dict[in_plus] = node_replacement
                node_replacement += 1

            if  in_minus in replace_dict.keys() :
                 in_minus = replace_dict[in_minus]
            else:
                replace_dict[in_minus] = node_replacement
                node_replacement += 1

            if  out in replace_dict.keys() :
                 out = replace_dict[out]
            else:
                replace_dict[out] = node_replacement
                node_replacement += 1
            
            out_string += '*error1' + name + ' ' + str(in_plus) + ' ' + str(in_minus) + ' ' + str(out)+'\n'
            #print fin

        # N MOSFET
        elif ('MOS_ENH_N' in lines[index].upper()):
            name = split_line[0][1:]; drain = split_line[1]; gate = split_line[2]; source = split_line[3]
            out_string += "*error1 m" + name + ' ' + drain + ' ' + gate + ' ' + source + '\n'

    # Check for voltage sources
    elif first_char == 'v':
        # Bring everything on to one line
        offset = 1; final_line = lines[index]
        while lines[index+offset][0] == '+':
            final_line += lines[index+offset][1:]
            offset+=1
            # Break on empty line
            if len(lines[index+offset]) == 0:
                break
        split_final = final_line.split()
        # DC handling
        if split_final[3] == 'dc' and not (split_final[1] == '0' and split_final[2] == '0') and split_final[4] != '0':
            node1 = split_final[1]; node2 = split_final[2]; value = split_final[4]
            # Dictionary Handler
            if node1 in replace_dict.keys() :
                node1 = replace_dict[node1]
            else:
                replace_dict[node1] = node_replacement
                node1 = replace_dict[node1]
                node_replacement += 1
            if node2 in replace_dict.keys() :
                node2 = replace_dict[node2]
            else:
                replace_dict[node2] = node_replacement
                node2 = replace_dict[node2]
                node_replacement += 1

            dc_flag = 1;
            name = "vDC" + str(dc_counter)
            dc_counter += 1
        # AC parsing
        matching = [v for v,s in enumerate(split_final) if "sin" in s or "pulse(" in s]
        # AC found
        if len(matching) == 1:
            func = split_final[matching[0]:]
            ac_name = "vAC" + str(ac_counter)
            # Comment this shit out for now
            if "pulse" in func[0]: 
                ac_name = "*error1(pulse)" + ac_name
            # Check if last digit is int to get amp and freq
            try:
            # Integer found
                discard_var = int(split_final[matching[0]][-1])
                amplitude = split_final[matching[0]+1]
                freq = split_final[matching[0]+2]
            # No integer found
            except:
                amplitude = split_final[matching[0]+2]
                freq = split_final[matching[0]+3]
            func = ' '.join(func)
            # take DC nodes if it's AC and DC, and reassign middle node
            if (dc_flag):
                # AC node 1 is connected to new node
                ac_node1 = node_replacement
                node_replacement += 1
                # AC node 2 is old DC node
                ac_node2 = node2
                # Old DC node connected to top AC node
                node2 = ac_node1
                # Solve arithmetic expressions for amplitude and freqency and value because they're all bad
                value = eval(value); amplitude = (eval(amplitude)); freq = (eval(freq));
                # If you didn't get an int that'd be real lame
                if (not isinstance(value,(int,float))): value = list(value)[0]
                if not isinstance(amplitude,(int,float)): amplitude = list(amplitude)[0]
                if (not isinstance(freq,(int,float))): freq = list(freq)[0]
                # Recast everything to strings because of life
                value = str(value); amplitude = str(amplitude); freq = str(freq); node1 = str(node1); node2 = str(node2);
                # Final output
                out_string += name + ' ' + str(node1) + ' ' + str(node2) + ' ' + value + 'volts\n'
                out_string += ac_name + ' ' + str(ac_node1) + ' ' + str(ac_node2) + ' junk1 ' + amplitude + ' ' + freq + ' junk4 junk5volts \n'
                #print fin                
            # Pure AC Signal
            else:
                # Do node parsing
                node1 = split_final[1]; node2 = split_final[2];
                # Dictionary Handler
                if node1 in replace_dict.keys() :
                    node1 = replace_dict[node1]
                else:
                    replace_dict[node1] = node_replacement
                    node1 = replace_dict[node1]
                    node_replacement += 1
                if node2 in replace_dict.keys() :
                    node2 = replace_dict[node2]
                else:
                    replace_dict[node2] = node_replacement
                    node2 = replace_dict[node2]
                    node_replacement += 1
                amplitude = (eval(amplitude)); freq = (eval(freq));
                # Eval handling
                if not isinstance(amplitude,(int,float)): amplitude = list(amplitude)[0]
                if not isinstance(freq,(int,float)): freq = list(freq)[0]
                amplitude = str(amplitude); freq = str(freq); node1 = str(node1); node2 = str(node2);
                # Final line
                out_string += ac_name + ' ' + str(node1) + ' ' + str(node2) + ' junk1 ' + amplitude + ' ' + freq + ' junk4 junk5volts\n'
            ac_counter += 1
        # No AC Component
        else:
            node1 = str(node1); node2 = str(node2);
            out_string += name + ' ' + node1 + ' ' + node2 + ' ' + value + ' volts\n'
            #print fin

    # Check for Wavegen
    elif first_char == 'X':
        pass
    # Check for BJT
    elif first_char == 'q':
        name = split_line[0][1:]; collector = split_line[1]; base = split_line[2]; emitter = split_line[3];
        # NPN/PNP handler
        matchingnpn = [v for v,s in enumerate(split_final) if "NPN" in s]
        matchingpnp = [v for v,s in enumerate(split_final) if "PNP" in s]
        if matchingpnp: name = "*error1(pnp)" + name
        elif matchingnpn: name = "*error1(npn)" + name
        else: name = '*error1' + name 
        # Dictionary Handler
        if collector in replace_dict.keys() :
            collector = replace_dict[collector]
        else:
            replace_dict[collector] = node_replacement
            collector = replace_dict[collector]
            node_replacement += 1
        if base in replace_dict.keys() :
            base = replace_dict[base]
        else:
            replace_dict[base] = node_replacement
            base = replace_dict[base]
            node_replacement += 1
        if emitter in replace_dict.keys() :
            emitter = replace_dict[emitter]
        else:
            replace_dict[emitter] = node_replacement
            emitter = replace_dict[emitter]
            node_replacement += 1
        collector = str(collector); base = str(base); emitter = str(emitter)
        out_string += name + ' ' + collector + ' ' + base + ' ' + emitter + '\n'

    # Check for MOSFET
    elif first_char == 'm' or first_char == 'M':
        name = split_line[0][1:]; drain = split_line[1]; gate = split_line[2]; source = split_line[3];
        # Dictionary Handler
        if drain in replace_dict.keys():
            drain = replace_dict[drain]
        else:
            replace_dict[drain] = node_replacement
            drain = replace_dict[drain]
            node_replacement += 1
        if gate in replace_dict.keys() :
            gate = replace_dict[gate]
        else:
            replace_dict[gate] = node_replacement
            gate = replace_dict[gate]
            node_replacement += 1
        if source in replace_dict.keys() :
            source = replace_dict[source]
        else:
            replace_dict[source] = node_replacement
            source = replace_dict[source]
            node_replacement += 1
        drain = str(drain); gate = str(gate); source = str(source)
        out_string += "*error1 (mosfet)" + name + ' ' + drain + ' ' + gate + ' ' + source + '\n'
        
    #out_string += lines[index] + '\n'
    index += 1

  # End of loop, finish with a .end and write to file
  out_string += ".end"
  with open('yolo.cir', 'w') as f:
    f.write(out_string)
  return out_string

def find_max(split_lines):
    ''' 
    Function to find max number in text file
    I am disgusted with myself
    '''
    max_num = 0
    for lines in split_lines:
        delimited_lines = lines.split()
        # Iterate over line looking for stupid bullshit. It's 2am.
        for elems in delimited_lines:
            try:
                discard_var = int(elems)
                if discard_var > max_num: max_num = discard_var
            except:
                continue
    return max_num

# Main function. Performs simple in/out operations
def main(in_file=''):
  # Read in file
  if not in_file:
    try:
      in_file = sys.argv[1]
      # Error handling
    except:
        print "No input file provided"
        sys.exit()
    # Open & read file
    split_lines = read_file(in_file)        
  # Data was already read in 
  else:
    # Break the lines down
    split_lines = in_file.split('\n')
  # Find max node in file
  max_num = find_max(split_lines)
  #Parse file for appropriate text
  out_string = parse_file(split_lines,max_num)
  return out_string.replace('\n', '<br />')


if __name__ == '__main__':
  main()
