#!/usr/bin/env python
'''
Python program to convert a Multisim netlist to an acceptable format for 
circuit tracing

User's notes: The circuit tracer is only concerned with node & name

Inputs: 
  infile - Path to Multisim netlist
Outputs:
  outfile - Converted file 
Written by Zack Smith 2-05-15
'''

# Necessary Imports
import sys

def read_file(filename):
    '''
    Read text file of filename;
    return lines in file
    '''
    try:
        with open(filename, 'r') as f:
            for line in f:
                    yield line.split()
    except IOError:
        print "Error opening or reading file: ", filename
        sys.exit()

def parse_file(lines,in_file):
  out_string = "* Translated Netlist *\n" 
  plus_flag = 0; ac_flag = 0; save_lst = []; curr_src = 0; cont_flag = 0
  for line in lines:
    if len(line) == 0: continue
    # Check for first character
    first_char = line[0][0]

    # Continue until .ENDS found
    if cont_flag:
      if 'ENDS' in line[0].upper(): cont_flag = 0
      continue

    # Don't write any line starting with *
    if first_char == '*' or first_char == '.' or first_char == '+':
      if 'SUBCKT' in line[0].upper(): cont_flag = 1
      continue

    ### Check for available components: R, L, C, D
    if first_char == 'r' or first_char == 'l' or first_char == 'c' or first_char == 'd' or first_char == 'v':
      line[0] = line[0][1:]
      if (len(line) > 3): line = line[0:3]
      out_string += first_char  + ' '.join(line) + '\n'
    ### Check for non-two pole components (transistor, op amp, wave gen)
    # Transistor
    if first_char == 'x':
      if 'MOS' in line[-1]:
        first_char = 'q'
        line[0] = line[0][1:]
        line = line[0:4]
        out_string += first_char + ' '.join(line) + '\n'
        continue
      elif 'OPAMP' in line[-1]:
        first_char = 'u'
        line[0] = line[0][1:]
        line = line[0:-1]
        out_string += first_char  + ' '.join(line) + '\n'
        continue


  out_string += ".end"
  print out_string
  with open(in_file[0:-4]+'_trace.cir', 'w') as f:
    f.write(out_string)


# Main function. Performs simple in/out operations
def main():
  # Read in file
  try:
    in_file = sys.argv[1]
  # Error handling
  except:
    print "No input file provided"
    sys.exit()
  # Open & read file
  split_lines = read_file(in_file)
  # Parse file for appropriate text
  parse_file(split_lines,in_file)

if __name__ == '__main__':
  main()
