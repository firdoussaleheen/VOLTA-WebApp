import cv
import cv2
import numpy as np
import sys
import math
import os
from operator import itemgetter
# Classes and Methods for image processing of circuit image
# Class which describes a character
class Alphabet:

    def set_char(self,x,y,alpha,index):
        self.x = x
        self.y = y
        self.alpha = alpha
        self.index = index
        self.wordblock = False
        self.closest = ""

# Class which describes a component
class Component:

    def set_component(self,Type, term1, term2, index):
        self.Type = Type
        self.term1 = term1
        self.term2 = term2
        self.avg_x = ((term1[0] + term2[0])/2)
        self.avg_y = ((term1[1] + term2[1])/2)
        self.node1 = -1
        self.node2 = -1
        self.connections = []
        self.value = 0
        self.index = index
        self.wordblock = None


    def print_component(self):
        print "{" + " Type\t\t => " + str(self.Type) + "\t\t}"
        print "{" + " Term1\t\t => " + str(self.term1) + "\t}"
        print "{" + " Term2\t\t => " + str(self.term2) + "\t}"
        print "{" + " Node1\t\t => " + str(self.node1) + "\t\t}"
        print "{" + " Node2\t\t => " + str(self.node2) + "\t\t}"
        print "{" + " Value\t\t => " + str(self.value) + "\t\t}"
        print "{" + " Connections\t => " + str( len(self.connections)) +"\t\t}"
        print "{" + " Index \t => " + str(self.index) + "\t\t}"
        print "------------------------------------------"

    def add_connections(self, adj_comp):
        if (self.check_duplicate(adj_comp)):
            return
        else:
            self.connections.append(adj_comp.index)

    def check_duplicate(self,adj_comp):
        for x in self.connections:
            if adj_comp.index == x: return True
            else: return False
# Class which defines a word block
class wordblock:
    
    def __init__(self,index,alphas):
        self.index = index
        self.alphas = alphas
        self.avg_x = 0
        self.avg_y = 0
        self.name = ""
        self.value = ""

    def calc_average_loc(self):
        avg_x = 0; avg_y = 0
        for chars in self.alphas:
            avg_x += chars.x
            avg_y += chars.y
        self.avg_x = avg_x / len(self.alphas)
        self.avg_y = avg_y / len(self.alphas)

    def print_wordblock(self):
        print 'Wordblock number {0} with alphas {1} and average {2}'.format(self.index,[x.alpha for x in self.alphas],[self.avg_x,self.avg_y])
        
# Main function to associate a character in the image with a particular component
def alphabet_association(comp_list,alpha_list):
    # Find closest alphabetic characters, and associate them as one singular text block 
    block_list = get_text_block(alpha_list)
    # Associate text blocks with values
    decode_blocks(block_list)
    # Find components closest to text blocks
    get_closest_comp(comp_list,block_list)
    # Write these values to corresponding components on netlist
    # write_blocks(comp_list,block_list)


# Function to separate text from components
def area_thresholding(thresh):
    thresh_src = np.zeros((thresh.shape[0], thresh.shape[1],3), np.uint8)
    thresh_src[:] = (255,255,255)
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    area_thresh = 100
    for x in range(0,len(contours)):
        if len(contours[x]) > 100:
            cv2.drawContours(thresh_src,contours, x, (0,0,0), 1)
    cv2.imwrite("Area Thresh.png", thresh_src)
    return thresh_src

# function to calculate distance from two alpha characters (single points)
def calc_alpha_dist(outer_alpha,inner_alpha):
    return math.sqrt((outer_alpha[0]-inner_alpha[0])**2 + (outer_alpha[1]-inner_alpha[1])**2)


# Function to determine the distance between two components (four terminal points)
def calculate_distance(comp1pt1, comp1pt2, comp2pt1, comp2pt2):
    dx11 = comp1pt1[0] - comp2pt1[0]; dx12 = comp1pt1[0] - comp2pt2[0];
    dy11 = comp1pt1[1] - comp2pt1[1]; dy12 = comp1pt1[1] - comp2pt2[1];
    dx22 = comp1pt2[0] - comp2pt2[0]; dy22 = comp1pt2[1] - comp2pt2[1];
    dist_pt11 = math.sqrt(math.pow(dx11,2) + math.pow(dy11,2))
    dist_pt12 = math.sqrt(math.pow(dx12,2) + math.pow(dy12,2))
    dist_pt22 = math.sqrt(math.pow(dx22,2) + math.pow(dy22,2))
    return (dist_pt11,dist_pt12, dist_pt22)

# Function to find closest component when connections are lacking
def check_closest():

    return;

# Function to ensure connected wires have the same node
def check_wires():
    
    return;

# Function to merge small wires into larger ones
def conjoin_wires(wire_list):
    initial = len(wire_list)
    # Iterate through the wire list, looking for any wires within one another
    for comparator_wire in wire_list:
        checkx = False; checky = False;
        cterm1 = comparator_wire.term1
        cterm2 = comparator_wire.term2
        if cterm1[0] == cterm2[0]:
            checkx = True
        else: checky = True
        # Wire under test has differing Y, but same X.
        for inner_wire in wire_list:
            iterm1 = inner_wire.term1
            iterm2 = inner_wire.term2
            if checkx:
                if inner_wire.index == comparator_wire.index:
                    continue
                # Check if the x coordinates are close together:
                if iterm1[0] - 2 < cterm1[0] and iterm1[0] +2 > cterm1[0] and iterm2[0] - 2 < cterm2[0] and iterm2[0] + 2 > cterm1[0] :
                    # Check if the y coordinates are within each other:
                    if (cterm1[1] <= iterm1[1] and cterm2[1] >= iterm1[1]):
                        comparator_wire.term2 = iterm2
                        wire_list.remove(inner_wire)
                        break
            # Wire under test has differing X, but same Y.
            elif checky:
                if inner_wire.index == comparator_wire.index:
                    continue
                # Check if the Y coordinates are close together:
                if iterm1[1] - 2< cterm1[1] and iterm1[1] +2 > cterm1[1] and iterm2[1] -2 < cterm2[1] and iterm2[1] + 2 > cterm2[1]:
                    # Check if the X coordinates are within each other:
                    if (cterm1[0] <= iterm1[0] and cterm2[0] >= iterm1[0]):
                        cterm2 = iterm2
                        comparator_wire.term2 = cterm2
                        wire_list.remove(inner_wire)
                        break
            else:
                print "Something bad happened"
                break
    net_change = initial-len(wire_list)
    return net_change

# Function which looks at the values in the blocks and decodes the netlist value & label
def decode_blocks(block_list):
    # Locate the top left alpha in each block
    for blocks in block_list:
        min_y = 500
        name_list = []; name_string = ""
        value_list = []; value_string = ""
        for letters in blocks.alphas:
            if letters.y < min_y: min_y = letters.y
        for letters in blocks.alphas: 
            # Find all alphas with y within 1 pix
            if min_y - 1 < letters.y < min_y + 1:
                name_list.append(letters)
            else:
                value_list.append(letters)
        # Sort according to leftmost characters first 
        # Shitty bubble sort because I'm a shitty person
        for indexes in range(len(name_list)):
            for inner_indexes in range(0,len(name_list)-indexes-1):
                if name_list[inner_indexes].x > name_list[inner_indexes+1].x:
                    temp = name_list[inner_indexes] 
                    name_list[inner_indexes] = name_list[inner_indexes+1]
                    name_list[inner_indexes+1] = temp
        # Sort according to leftmost characters first 
        # Shitty bubble sort because I'm a shitty person
        for indexes in range(len(value_list)):
            for inner_indexes in range(0,len(value_list)-indexes-1):
                if value_list[inner_indexes].x > value_list[inner_indexes+1].x:
                    temp = value_list[inner_indexes] 
                    value_list[inner_indexes] = value_list[inner_indexes+1]
                    value_list[inner_indexes+1] = temp
        # Assign name/value to text block
        for elems in name_list: name_string += elems.alpha
        for elems in value_list: value_string += elems.alpha
        #print name_string
        #print value_string
        blocks.name = name_string
        blocks.value = value_string
    return

# Function which iterates over matches, and stores them as long as reasonable conditions are met.
def explore_match(loc,index,comp_list,wire_list,super_list,w,h,Type,x,blank):
    comp_found = False
    # Iterate over matches, creating rectangles
    for pt in zip(*loc[::-1]):
        dont_draw = False
        temp_comp = Component()
        # Set terminal points
        if w > h   or "ground270" in x and "vsource0" not in x:
            term1 = (pt[0],pt[1]+h/2)
            term2 = (pt[0] + w, pt[1] + h/2)
        else:
            term1 =  (pt[0] + w/2, pt[1])
            term2 =  (pt[0] + w/2, pt[1] + h)

        # Iterate over lists, trying to delete any unnecessary wires
        if Type == "Wire":
            for iter_comp in comp_list:
                # If term1[0] (temp_comp X) is between any X and Y, don't draw
                if term2[0] <= iter_comp.term2[0] and term1[0] >= iter_comp.term1[0] and term1[1]  >= iter_comp.term1[1] and term2[1] <= iter_comp.term2[1]:
                    dont_draw = True
        if Type == "Wire":
            for iter_wire in wire_list:
                # If Both Y are within 2 pix, and starting term within 5 pix, don't draw
                if term1[1] - 2 <= iter_wire.term1[1] and term1[1] + 2 >= iter_wire.term1[1] and term1[0] - 5 <= iter_wire.term1[0] and term1[0] + 5 >= iter_wire.term1[0]:
                    pass
                    #dont_draw = True
                # If both X are within 2 pix, and starting term within 5 pix, don't draw
                if term1[0] -2 <= iter_wire.term1[0] and term1[0] + 2 >= iter_wire.term1[0] and term1[1] - 5 <= iter_wire.term1[1] and term1[1] + 5 >= iter_wire.term1[1]:
                    pass
                    #dont_draw = True

                # Iterate over comp list to make sure wire is not inside rect
            for iter_comp in comp_list:
                if term1[0] in range(iter_comp.vertex[0]-2, iter_comp.vertex[0] + iter_comp.cols+4) and term1[1] in range(iter_comp.vertex[1]-4, iter_comp.vertex[1] + iter_comp.rows+4):
                    if term2[0] in range(iter_comp.vertex[0]-2, iter_comp.vertex[0] + iter_comp.cols+4) and term2[1] in range(iter_comp.vertex[1]-4, iter_comp.vertex[1] + iter_comp.rows+4):
                        dont_draw = True

        # Check distance in
        for comp in super_list:
            (pt_11,pt_12, pt22) =  calculate_distance(comp.term1, comp.term2, comp.term1, comp.term2)
            if pt_11 == 0 or pt_12==0:
                continue
            elif pt_11 <= 1.5 or pt_12 <= 1.5:
                dont_draw = True

        # Ignore components which have triggered one of the if statements
        if (dont_draw):
            continue

        # Add component to the list
        temp_comp.set_component(Type,term1,term2,index)

        if Type != "Wire":
            temp_comp.cols = w; temp_comp.rows = h; temp_comp.vertex = pt
            comp_list.append(temp_comp)
            print "COMPONENT FOUND: " + temp_comp.Type
            super_list.append(temp_comp)
            comp_found = True
        else:
            wire_list.append(temp_comp)
            super_list.append(temp_comp)
            comp_found = True

        # Draw Rectangles
        cv2.rectangle(blank, pt, (pt[0] + w, pt[1] + h), (0,0,255),2)

        # Increment the index of the component
        index += 1
    # Closes for loop
    return comp_found,comp_list,wire_list,super_list,index

# Function to ensure wires are purely straight (x or y coordinates are equal)
def fix_coordinates(wire_list):
    for temp_wire in wire_list:
        dx = abs(temp_wire.term1[0] - temp_wire.term2[0])
        dy = abs(temp_wire.term1[1] - temp_wire.term2[1])
        if dx > dy:
            temp_wire.term1 = (temp_wire.term1[0],temp_wire.term2[1])
        else:
            temp_wire.term1 = (temp_wire.term2[0],temp_wire.term1[1])
    return

# Function to move wire terminals nearly outside of a component's space (rectangle)
def fix_wires(wire_list, comp_list):
    for iter_comp in comp_list:
        cterm1 = iter_comp.term1
        cterm2 = iter_comp.term2
        for current_wire in wire_list:
            wterm1 = current_wire.term1
            wterm2 = current_wire.term2
            # Check if wire is in same X vicinity:
            if cterm1[0] -3  <= wterm1[0] and cterm1[0] + 3 >= wterm1[0]:
                # Check if wire is nested inside component in Y direction (2 cases)
                if cterm1[1] <= wterm1[1] and cterm2[1] >= wterm1[1]:
                    current_wire.term1 = (cterm2[0],cterm2[1] -2 )
                    continue
                    # Case 2
                elif cterm1[1] <= wterm2[1] and cterm2[1] >= wterm2[1]:
                    current_wire.term2 = (cterm1[0],cterm1[1] + 2)
                    continue
                    # Check if wire is in same Y vicinity:
            if cterm1[1] -3 <= wterm1[1] and cterm1[1] + 3 > wterm1[1]:
                # Check if wire is nested inside component in X direction (2 cases)
                if cterm1[0] <= wterm1[0] and cterm2[0] >= wterm1[0]:
                    current_wire.term1 = (cterm2[0] - 2, cterm2[1])
                    continue
                # Case 2
                elif cterm1[0] <= wterm2[0] and cterm2[0] >= wterm2[0]:
                    current_wire.term2 = (cterm1[0] + 2, cterm2[1])

    return;

# Function to generate *.cir file for netlist
def generate_cir(comp_list,save_path):
    if not os.path.exists('./VLA' + save_path[:-9]):
	os.makedirs('./VLA' + save_path[:-9])
    f = open('./VLA' + save_path[:-9]+'VLAnetlist.cir', 'w')
    f.write("* Netlist *\n");
    for comp in comp_list:
        if comp.Type == "Gnd": continue
        f.write(comp.wordblock.name + " " + str(comp.node1) + " " + str(comp.node2) + " " + comp.wordblock.value + "\n")
    f.write(".end")
    f.close()
    return

# Function to get the comp closest to a word block
def get_closest_comp(comp_list,block_list):
    # Find closest comp for each text block
    for text_blocks in block_list:
        min_dist = 500; min_comp = None
        # Calculate distances for each comp 
        for comp in comp_list:
            temp_dist = calc_alpha_dist([text_blocks.avg_x,text_blocks.avg_y],[comp.avg_x,comp.avg_y])
            if temp_dist < min_dist and comp.wordblock == None:
                min_dist = temp_dist
                min_comp = comp
        # Associate word block with comp.wordblock
        #print text_blocks.name
        #print text_blocks.value
        if min_comp == None:
            print "Something went wrong in OCR"
            return
        if min_comp.Type == 'Vsrc' and ('V' not in text_blocks.name or 'v' not in text_blocks.name):
            if 'u' in text_blocks.name or 'U' in text_blocks.name:
                text_blocks.name = 'V' + text_blocks.name[1:]
            else:
                text_blocks.name = 'V' + text_blocks.name
        if min_comp.Type == 'Vsrc' and ('V' not in text_blocks.value or 'v' not in text_blocks.value):
            if 'u' in text_blocks.value or 'U' in text_blocks.value: 
                text_blocks.value = text_blocks.value[:-1] + 'V'
            else: text_blocks.value = text_blocks.value + 'V'
        text_blocks.name = text_blocks.name.upper()
        text_blocks.value = text_blocks.value[:-1]
        min_comp.wordblock = text_blocks
        #print '---------------------------'
        #min_comp.print_component()
        #print text_blocks.name
    return

# Function to associate letters with a text box 
def get_text_block(alpha_list):
    # For each alphabetic character, if in text group continue
    # Else check for alphas within threshold and add to text box
    distance_threshold = 25
    wordblock_list = []
    counter = 0
    for outer_alpha in alpha_list:     
        if (outer_alpha.wordblock == True): continue
        if (outer_alpha.alpha == ' '): continue
        #print '---------------------------------------------------'
        dist_array = [[]]
        # Check for distance from every component
        for indexes, inner_alpha in enumerate(alpha_list):
            if inner_alpha.alpha == ' ': continue
            alpha_dist = calc_alpha_dist([outer_alpha.x,outer_alpha.y] , [inner_alpha.x,inner_alpha.y])
            # Create distance array consisting of index and distance
            dist_array.append([indexes,alpha_dist])
            #print alpha_dist, inner_alpha.alpha
        # Sort to get min distances. Index is present in array so alpha information is maintained.
        dist_array.pop(0)
        sorted_dist_array = sorted(dist_array, key=itemgetter(1))
        # Take from this sorted array while less than threshold
        iterator = 0
        temp_wordblock = wordblock(counter,[])
        #print sorted_dist_array
        while (iterator < len(sorted_dist_array) and sorted_dist_array[iterator][1] < distance_threshold): 
            temp_wordblock.alphas.append(alpha_list[sorted_dist_array[iterator][0]])
            alpha_list[sorted_dist_array[iterator][0]].wordblock = True
            iterator += 1
        temp_wordblock.calc_average_loc()
        wordblock_list.append(temp_wordblock)
        # Associate alpha chars with a text block
        counter += 1
    return wordblock_list

# Function to break up arrays and call other traversal operations
def intersection_operations(comp_under_test, comp_list, wire_list):
    # Create individual arrays for each component
    gnd_array = []; vsrc_array = []; isrc_array = []; res_array = []; ind_array = []; cap_array = []; future_traverses = [];
    gnd_count = 0; vsrc_count = 0; isrc_count = 0; res_count = 0; ind_count = 0; cap_count = 0; current_node = 0;
    for comp in comp_list:
        if comp.Type == "Gnd":
            gnd_array.append(comp)
            gnd_count += 1
        elif comp.Type == "Vsrc":
            vsrc_array.append(comp)
            vsrc_count +=1
        elif comp.Type == "Isrc":
            isrc_array.append(comp)
            isrc_count += 1
        elif comp.Type == "R":
            res_array.append(comp)
            res_count += 1
        elif comp.Type == "L":
            ind_array.append(comp)
            ind_count += 1
        elif comp.Type == "C":
            cap_array.append(comp)
            cap_count += 1
        else:
            print comp.Type + " unable to be sorted"

    # Try to conjoin wires:
    net_change = 1
    while net_change != 0:
        net_change = conjoin_wires(wire_list)
    # After conjoining wires, fix wires so that they won't be inside components
    fix_wires(wire_list, comp_list)
    fix_coordinates(wire_list)
    super_list = comp_list + wire_list
    # Iterate through components, starting with ground, assigning nodes
    # Iterate through ground
    for gnd_iter in gnd_array:
        current_node = 0
        future_traverses = list_traversal(comp_list, wire_list, future_traverses, gnd_iter, current_node,super_list)
        while len(future_traverses) > 0:
            future_traverses = list_traversal(comp_list,wire_list,future_traverses,future_traverses[0],current_node,super_list)

    # Iterate through vsources
    for vsrc_iter in vsrc_array:
        if vsrc_iter.node1 != -1 and vsrc_iter.node2 != -1:
            continue
        else:
            current_node += 1
            future_traverses = list_traversal(comp_list, wire_list, future_traverses, vsrc_iter, current_node,super_list)
            while len(future_traverses) > 0:
                future_traverses = list_traversal(comp_list,wire_list,future_traverses,future_traverses[0],current_node,super_list)
    # Iterate through current sources
    for isrc_iter in isrc_array:
        if isrc_iter.node1 != -1 and isrc_iter.node2 != -1:
            continue
        else:
            current_node += 1
            future_traverses = list_traversal(comp_list, wire_list, future_traverses, isrc_iter, current_node,super_list)
            while len(future_traverses) > 0:
                future_traverses = list_traversal(comp_list,wire_list,future_traverses,future_traverses[0],current_node,super_list)
    # Iterate through resistors
    for res_iter in res_array:
        if res_iter.node1 != -1 and res_iter.node2 != -1:
            continue
        else:
            current_node += 1
            future_traverses = list_traversal(comp_list, wire_list, future_traverses, res_iter, current_node,super_list)
            while len(future_traverses) > 0:
                future_traverses = list_traversal(comp_list,wire_list,future_traverses,future_traverses[0],current_node,super_list)
    # Iterate through inductors
    for ind_iter in ind_array:
        if ind_iter.node1 != -1 and ind_iter.node2 != -1:
            continue
        else:
            current_node += 1
            future_traverses = list_traversal(comp_list, wire_list, future_traverses, ind_iter, current_node,super_list)
            while len(future_traverses) > 0:
                future_traverses = list_traversal(comp_list,wire_list,future_traverses,future_traverses[0],current_node,super_list)
    # Iterate through capacitors
    for cap_iter in cap_array:
        if cap_iter.node1 != -1 and cap_iter.node2 != -1:
            continue
        else:
            current_node += 1
            future_traverses = list_traversal(comp_list, wire_list, future_traverses, cap_iter, current_node,super_list)
            while len(future_traverses) > 0:
                future_traverses = list_traversal(comp_list,wire_list,future_traverses,future_traverses[0],current_node,super_list)

    return 

# Function to assign nodes to all components
def list_traversal(comp_list, wire_list, future_traverses, comp_under_test, current_node, super_list):
    # Pop off current component
    if len(future_traverses) > 0:
        future_traverses.pop(0)
    # If it's ground, its nodes are both 0
    if comp_under_test.Type == "Gnd":
        comp_under_test.node1 = 0
        comp_under_test.node2 = 0
    # Print comp under test
    print "*******************NEW ITERATION*******************"
    comp_under_test.print_component()
    # Grab terminal points
    cterm1 = comp_under_test.term1
    cterm2 = comp_under_test.term2
    # Iterate through all the components searching for those nearby comp under test
    for super_comp in super_list:
        # Skip over if they're the same component
        if super_comp.index == comp_under_test.index:
            continue
        # Grab terminal points
        sterm1 = super_comp.term1
        sterm2 = super_comp.term2
        # Check if the comp under test and super comp are nested:
        if (
                        (((cterm1[0] -5 <= sterm1[0] and cterm2[0] + 5 >= sterm1[0]) or (cterm1[0] -5 <= sterm2[0] and cterm2[0] + 5 >= sterm2[0])) and
                        ((cterm1[1] -5 <= sterm1[1] and cterm2[1] + 5 >= sterm1[1]) or (cterm1[1] -5 <= sterm2[1] and cterm2[1] + 5 >= sterm2[1]))) or
                        (((sterm1[0] -5 <= cterm1[0] and sterm2[0] + 5 >= cterm1[0]) or (sterm1[0] -5 <= cterm2[0] and sterm2[0] + 5 >= cterm2[0])) and
                        ((sterm1[1] -5 <= cterm1[1] and sterm2[1] + 5 >= cterm1[1]) or (sterm1[1] -5 <= cterm2[1] and sterm2[1] + 5 >= cterm2[1])))
        ):
            # Component found nearby!
            print "FOUND COMPONENT:"
            super_comp.print_component()
            if super_comp.Type == "Wire":
                # Add wire to connection list
                super_comp.add_connections(comp_under_test)
                comp_under_test.add_connections(super_comp)
                if super_comp.node1 != -1 and super_comp.node2 != -1:
                    continue
                # Set nodes of wire to current node
                super_comp.node1 = current_node
                super_comp.node2 = current_node
                super_comp.print_component()
                # Add wire to future traversal list
                future_traverses.append(super_comp)
            else:
                # Calculate distance to figure out which node is closer (important for polarity)
                (d11, d12, d22) = calculate_distance(cterm1, cterm2, sterm1, sterm2)
                print "d11: " + str(d11) + " d12: " + str(d12)
                if d11 == 0 or d12 == 0:
                    print " MISS ? "
                    super_comp.print_component()
                    comp_under_test.print_component()
                    print "END MISS"
                    continue
                elif d11 > d12:
                    # Assign to node 2
                    if super_comp.node2 == -1:
                        super_comp.node2 = current_node
                    # Node 2 already assigned debug statements
                    else:
                        print " NODE 2 ALREADY ASSIGNED: "
                        super_comp.print_component()
                        comp_under_test.print_component()
                        print " END OF NODE 2"
                    # Add to connections
                    super_comp.add_connections(comp_under_test)
                    comp_under_test.add_connections(super_comp)

                else:
                    # Assign to node 1
                    if super_comp.node1 == -1:
                        super_comp.node1 = current_node
                    # Node 1 is already assigned debug statements
                    else:
                        print " NODE 1 ALREADY ASSIGNED: "
                        super_comp.print_component()
                        comp_under_test.print_component()
                    # Add to connections
                    super_comp.add_connections(comp_under_test)
                    comp_under_test.add_connections(super_comp)
    # Ensure a hanging component doesn't have a nearby solution
    if (len(comp_under_test.connections) < 2 and len(future_traverses) == 0 and comp_under_test.Type == "Wire") or len(comp_under_test.connections) == 0:
        # Perform distance calculations on entire super list to determine any nearby matches
        print "Less than one connection!"
        min_dist = 1000; breakvar = False; min_comp = None
        for super_comp in super_list:
            if super_comp.index == comp_under_test.index:
                continue
            for connection in super_comp.connections:
                if connection == comp_under_test.index:
                    breakvar = True
            if breakvar:
                continue
            (d11, d12, d22) = calculate_distance(comp_under_test.term1, comp_under_test.term2, super_comp.term1, super_comp.term2)
            if d11 < d12 and d11 < min_dist and d11< d22:
                new_min_dist = d11
                min_comp = super_comp
                min_term = super_comp.term1
            elif d12 < d11 and d12 < min_dist and d12 < d22:
                new_min_dist = d12
                min_comp = super_comp
                min_term = super_comp.term2
            elif d22 < d11 and d22 < d12 and d22 < min_dist:
                new_min_dist = d22
                min_comp = super_comp
                min_term = super_comp.term2
            if new_min_dist < min_dist:
                min_dist = new_min_dist
        print "Closest comp found has index: " + str(min_comp.index) + " And Type: " + min_comp.Type + " At a distance: " + str(min_dist)
        min_avg_dist = calc_alpha_dist(min_term,[comp_under_test.avg_x, comp_under_test.avg_y])
        if min_dist < 8.0 or min_avg_dist < 8.0 :

            print "MIN COMPONENT FOUND :"
            min_comp.print_component()
            if min_comp.Type == "Wire":
                # Add wire to connection list
                min_comp.add_connections(comp_under_test)
                comp_under_test.add_connections(min_comp)
                if min_comp.node1 != -1 and super_comp.node2 != -1:
                    print "Comp already found"
                    return
                # Set nodes of wire to current node
                min_comp.node1 = current_node
                min_comp.node2 = current_node
                # Add wire to future traversal list
                future_traverses.append(min_comp)
            else:
                # Calculate distance to figure out which node is closer (important for polarity)
                if d11 > d12 or d11 > d22:
                    # Assign to node 2
                    if min_comp.node2 == -1:
                        min_comp.node2 = current_node
                    # Node 2 already assigned debug statements
                    else:
                        print " NODE 2 ALREADY ASSIGNED: "
                        min_comp.print_component()
                        comp_under_test.print_component()
                        print " END OF NODE 2"
                    # Add to connections
                    min_comp.add_connections(comp_under_test)
                    comp_under_test.add_connections(min_comp)
                else:
                    # Assign to node 1
                    if min_comp.node1 == -1:
                        min_comp.node1 = current_node
                    # Node 1 is already assigned debug statements
                    else:
                        print " NODE 1 ALREADY ASSIGNED: "
                        min_comp.print_component()
                        comp_under_test.print_component()
                    # Add to connections
                    min_comp.add_connections(comp_under_test)
                    comp_under_test.add_connections(min_comp)
    return future_traverses

# Optical Character Recognition application stage - apply ML on new image
def ocr_learning(source,contours,thresh):
    print '---------------------------------------------'
    print 'ACTIVATING OCR ON SOURCE.'
    # Define variables
    alpha_list = []
    xy_storage = [-5,-5]
    avg_counter = 0; counter = 0
    # Grab training documents
    # Feature set
    samples = np.loadtxt('generalsamples.data',np.float32)
    # Response set
    responses = np.loadtxt('generalresponses.data', np.float32)
    responses = responses.reshape((responses.size,1))
    # Load & train model
    model = cv2.KNearest()
    model.train(samples,responses)
    # Apply algorithm on source image
    out = np.zeros(source.shape,np.uint8)
    # Get most common size in contours
    h_array = []
    for conts in contours:
        if cv2.contourArea(conts) < 100:
            [x,y,w,h] = cv2.boundingRect(conts)
            h_array.append(h)
    # Find most common height through count sort
    count_array = [0]*(max(h_array) + 2) 
    for h_val in h_array:
        count_array[h_val] += 1
    # Quasi-count sorted array of heights, index = most common height, value = number
    index,value = max(enumerate(count_array),key=itemgetter(1))
    alpha_index = 0
    for conts in contours:
        # Look for the small contours which are text
        if cv2.contourArea(conts) < 100:
            # Draw bounding rectangles around them
            [x,y,w,h] = cv2.boundingRect(conts)
            # Continue if height is not most common height
            if h != index: continue
            # Check proximity to previous x/y
            if (x - 2 < xy_storage[0] and x+2 > xy_storage[0]) and (y - 2 < xy_storage[1] and y+2 > xy_storage[1]): continue            
            xy_storage[0] = x; xy_storage[1] = y;
            # Draw rectangle around matching contour
            temp_char = Alphabet()
            cv2.rectangle(source,(x,y),(x+w,y+h),(0,0,255))
            #print "Contour position: " + str(x) +',' +  str(y) 
            #print "Contour size: " + str(w) + ',' + str(h)
            # Apply Knearest algo
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval,results,neigh_resp,dists = model.find_nearest(roismall,k=1)
            # Convert result to output string
            string = str(int((results[0][0])))
            if int(string) > 9: 
                string = chr(int(string))
            # Store instance of alphabet class like we did for components
            temp_char.set_char(x,y,string,alpha_index)
            alpha_list.append(temp_char)
            alpha_index+=1
            # Write string to image
            cv2.putText(out,string,(x,y+h),0,.25,(0,255,0))
            #print "OutString is: '" + string + "'"
            # Show image w/ just text & full image
            #cv2.imshow('out',out)
            #cv2.imshow('source',source)
            #cv2.waitKey(0)
    # Finished OCR, exit
    return alpha_list

# Function to print netlist
def print_netlist(comp_list):
    net_string = "<html><body><table style='Width:100%'><tr><td>Type </td> <td>Node 1 </td> <td>Node 2</td> <td>Value </td></tr>"
    for x in comp_list:
        if x.Type == 'Gnd': continue
        try: 
            net_string = net_string + "<tr><td>" + x.wordblock.name + "</td> <td>" + str(x.node1) + "</td> <td>  " + str(x.node2) + " </td> <td>  " + x.wordblock.value + "</td>   </tr>"
        except:
            x.print_component()
    net_string = net_string + "</table></body></html>"
    return net_string


# Function to print node numbers on all wires
# Takes wire list, writes numbers to input file. 
def print_nodes(wire_list,src,save_path):
    # Initialize important variables
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Iterate over every wire 
    for wire in wire_list:
        # Find average wire location
        wire_avg = [(wire.term1[0] + wire.term2[0])/2, (wire.term1[1] + wire.term2[1])/2]
        # Draw wire's node on to source
        wire_node = "Node " + str(wire.node1)
        cv2.putText(src,wire_node, (wire_avg[0],wire_avg[1]), font, .4, (0,0,0),2)
    print os.getcwd() + "/VLA/" + save_path   
    cv2.imwrite("./VLA" + save_path, src)
    return


# Function to detect components
def test_template_method(not_black, templates):
    # Read in RGB img and initialize variables
    src = cv2.imread('Contours.png',-1)
    blank = np.zeros((src.shape[0],src.shape[1],3),np.uint8)
    blank[:] = (255,255,255)
    index = 0
    comp_tup = ([])
    comp_list = []; wire_list = []; super_list = [];
    #Iterate over all template images
    for x in templates:
        # Set Type of component
        if "ground" in x       : Type = "Gnd"
        elif "capacitor" in x : Type = "C"
        elif "inductor" in x   : Type = "L"
        elif "resistor" in x    : Type = "R"
        elif "vsource" in x   : Type = "Vsrc"
        elif "isource" in x    : Type = "Isrc"
        elif "wire" in x        : Type = "Wire"
        else: Type = "none"
        # Apply template matching
        threshold = 0.9
        copycat = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
        template = cv2.imread(x, 0)
        res = cv2.matchTemplate(copycat, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where (res >= threshold)
        w,h = template.shape[::-1]
        loc = np.where( res >= threshold)
        # Look for matches with high threshold
        comp_found,comp_list,wire_list,super_list,index=explore_match(loc,index,comp_list,wire_list,super_list,w,h,Type,x,blank)
        if (comp_found == False and Type != "Isrc" and Type != "Vsrc"):
            # If not a vsrc/isrc, try again with lower threshold (isrc/vsrc provide a lot of false negatives).
            loc = np.where( res >= threshold - 0.10)
            print "Recalling explore_match on " + x
            comp_found,comp_list,wire_list,super_list,index=explore_match(loc,index,comp_list,wire_list,super_list,w,h,Type,x,blank)

    # Write blank to final result
    cv2.imwrite('res.png', blank)
    return (super_list, blank)

def circuit_recognizer(argv, save_path):
    #Make Template List
    templates = []
    path_to_templates = "./VLA/static/VLA/circuit_templates/"
    templates.append(path_to_templates + "capacitor0.png")
    templates.append(path_to_templates + "capacitor90.png")
    templates.append(path_to_templates + "inductor0.png")
    templates.append(path_to_templates + "inductor90.png")
    templates.append(path_to_templates + "inductor180.png")
    templates.append(path_to_templates + "inductor270.png")
    templates.append(path_to_templates + "vsource0.png")
    templates.append(path_to_templates + "vsource90.png")
    templates.append(path_to_templates + "vsource180.png")
    templates.append(path_to_templates + "vsource270.png")
    templates.append(path_to_templates + "isource0.png")
    templates.append(path_to_templates + "isource90.png")
    templates.append(path_to_templates + "isource180.png")
    templates.append(path_to_templates + "isource270.png")
    templates.append(path_to_templates + "resistor0.png")
    templates.append(path_to_templates + "resistor90.png")
    templates.append(path_to_templates + "ground0.png")
    templates.append(path_to_templates + "ground90.png")
    templates.append(path_to_templates + "ground180.png")
    templates.append(path_to_templates + "ground270.png")
    templates.append(path_to_templates + "wire0.png")
    templates.append(path_to_templates + "wire90.png")

    # Create color arrays
    black = np.array([0,0,0])
    not_black = np.array([100,100,100])
    white = np.array([255,255,255])

    # Read in source
    source = cv2.imread(str(argv),-1)
    width,height = source.shape[:2]

    # Create blank matrix
    blank = np.zeros((width,height,3), np.uint8)
    blank[:] = white
    cv2.imwrite("blank.png",blank)

    # Apply thresholding
    hsv =  cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
    upper_thresh = np.array([215,215,215])
    lower_thresh = np.array([0,0,0])
    thresh = cv2.inRange(hsv, lower_thresh,upper_thresh)
    cv2.imwrite("inrange.png", thresh)
    
    # Draw contours onto copycat image
    copycat = blank.copy()
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(copycat,contours, -1, lower_thresh, 1)
    cv2.imwrite("Contours.png", copycat)

    alpha_list = ocr_learning(source.copy(),contours,thresh)
    # Apply Template Matching & Area Thresholding
    super_list = []; comp_list = []; wire_list = []
    super_list,matched_src = test_template_method(not_black, templates)
    # Split the lists in to wire and component lists
    for temp_comp in super_list:
        if temp_comp.Type == "Wire":
            wire_list.append(temp_comp)
        else:
            comp_list.append(temp_comp)
    # Apply area thresholding to remove text
    thresh_src = area_thresholding(thresh)
    final_src = cv2.addWeighted(thresh_src,0.5,matched_src,0.5,0)
    cv2.imwrite("add weighted.png", final_src)
    #  Connect Components
    intersection_operations(super_list, comp_list, wire_list)
    # Preform alphabetic association
    alphabet_association(comp_list, alpha_list)
    # Return html formatted netlist string
    net_string = print_netlist(comp_list)
    print "Net String:"
    print net_string
    # Generate .cir file for netlist comparison
    generate_cir(comp_list,save_path)
    print "Cir generated succesfully"
    # Print nodes on to original image
    print_nodes(wire_list,source,save_path)
    print "Nodes written okay."
    # Final return value of function: Html formatted netlist. Could write second function which parses netlists, in which case output would be the .cir file. 
    return net_string


