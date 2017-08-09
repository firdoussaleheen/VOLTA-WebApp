#!/usr/bin/env python


# Form component dictionary
# INPUT: line from the netlist file, converted into a list of strings
# OUTPUT: dictionary for the component, including type and connecting nodes.
# TODO: make sure ALL possible components are included here.
#
def formComponentDictionary(lineList):
    
    componentDict = {}
    componentDict['name'] = lineList[1] # all component types have 'name' first

    if any([lineList[0][0] == 'v', lineList[0][0] == 'V']): # voltage source: connect to exactly 2 nodes
        componentDict['type'] = 'voltage source'
        componentDict['connections'] = lineList[2:4]
        componentDict['terminals'] = ['Positive lead','Negative lead']
    elif any([lineList[0][0] == 'X',lineList[0][0] == 'x']): #alternate source: connect to exactly 2 nodes
        componentDict['type'] = 'source'
        componentDict['connections'] = lineList[2:4]
        componentDict['terminals'] = ['Positive lead','Negative lead']
    elif any([lineList[0][0] == 'R',lineList[0][0] == 'r']): # resistor: connect to exactly 2 nodes
        componentDict['type'] = 'resistor'
        componentDict['connections'] = lineList[2:4]
        componentDict['terminals'] = ['One lead','One lead']
    elif any([lineList[0][0] == 'C',lineList[0][0] == 'c']): # capacitor: connect to exactly 2 nodes
        componentDict['type'] = 'capacitor'
        componentDict['connections'] = lineList[2:4]
        componentDict['terminals'] = ['One lead','One lead']
    elif any([lineList[0][0] == 'L',lineList[0][0] == 'l']): # inductor: connect to exactly 2 nodes
        componentDict['type'] = 'inductor'
        componentDict['connections'] = lineList[2:4]
        componentDict['terminals'] = ['One lead','One lead']
    elif any([lineList[0][0] == 'D',lineList[0][0] == 'd']): # diode: connect to exactly 2 nodes
        componentDict['type'] = 'diode'
        componentDict['connections'] = lineList[2:4]
        componentDict['terminals'] = ['Anode','Cathode']
    elif any([lineList[0][0] == 'Q',lineList[0][0] == 'q']): # Transistor: connect to exactly 3 nodes
        componentDict['type'] = 'transistor'
        componentDict['connections'] = lineList[2:5]
        componentDict['terminals'] = ['Drain','Gate','Source']
    elif any([lineList[0][0] == 'U',lineList[0][0] == 'u']): # Opamp: connect to exactly 2 nodes
        componentDict['type'] = 'Amplifier'
        componentDict['connections'] = lineList[2:8]
        componentDict['terminals'] = ['Output','Inverted Input', 'Noninverted Input', 'Ground', 'Vcc']
    return componentDict


# Main functionality
#
def translateNetlist(fname):

    # read the file and split into lines, 
    # ignoring empty lines, header lines, and lines beginning with "."
    headerLines=0
    footerLines=1
    with open(fname,'rb') as file:
        fileText = file.read()
    fileLines = fileText.split("\n")
    fileLines = [line for line in fileLines if len(line) > 2 and line[0] is not '.' and line[0] is not '*']
    fileLines = fileLines[headerLines:len(fileLines)]
    
    # create a dictionary for each unique component
    circuitDict = {}
    for line in fileLines: 
        splitLine = line.split(' ') # make a list from the string
        componentDict = formComponentDictionary(splitLine)
        circuitDict[splitLine[0]] = componentDict

    # form a list of tuples representing the circuit trace:
    # (node, connectedComponent, componentType, terminal(at index of node))
    allConnections = []
    for k in circuitDict.keys():
        for node in circuitDict[k]['connections']:
            allConnections.append( (node, circuitDict[k]['name'], circuitDict[k]['type'], circuitDict[k]['terminals'][circuitDict[k]['connections'].index(node)] ) )
    #Net_string is the html table of help directions
    net_string = "<html><body><table style='Width:100%'><tr><td>Remember each node corresponds to one numbered row on your breadboard. </td></tr>"
    #create sorted set sorted by node number
    for node in sorted(set([connection[0] for connection in allConnections])):
        # get tuple values for node
        connectedComponents= [connection[1] for connection in allConnections if connection[0] is node]
        componentType = [connection[2] for connection in allConnections if connection[0] is node]
        connectedTerminal = [connection[3] for connection in allConnections if connection[0] is node]
        #Add a human readable line with this info to a HTML table   
        for conComp in connectedComponents:
            net_string = net_string + "<tr><td>" + connectedTerminal[connectedComponents.index(conComp)] + " of " + componentType[connectedComponents.index(conComp)] + " " + conComp + " should be connected to node " + node + ". </td>   </tr>"
    net_string = net_string + "</table></body></html>"

    return net_string


# Run the main program
#
if __name__ == "__main__":
    translateNetlist(fname="VLAnetlist.cir")
