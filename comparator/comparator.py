# Necessary Imports
# coding=<encoding name>
from __future__ import division
import numpy as np
import os,sys

#!/usr/bin/env python
# -*- coding: <encoding name> -*-

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
        pass

		

# Main function. Performs simple in/out operations
def main(in_file1='',in_file2=''):
  # Read in file
  if not in_file1 or in_file2:
    try:
        in_file1 = sys.argv[2]
	in_file2 = sys.argv[3]
      # Error handling
    except:
        print "No input file provided"
        pass
    # Open & read file
    split_lines_1 = in_file1.splitlines()
    [dict_value_1,dict_node_1,element_number_1]=buildgraph(split_lines_1)

    [a_matrix,a_nodes,a_elements,a_loops]=buildmatrix(dict_value_1,dict_node_1,element_number_1)
    print a_matrix
    path_1=[]
    path_1=find_all_paths(0,a_matrix,dict_node_1,path_1,a_loops)


    split_lines_2 =  in_file2.splitlines()
    [dict_value_2,dict_node_2,element_number_2]=buildgraph(split_lines_2)
    [b_matrix,b_nodes,b_elements,b_loops]=buildmatrix(dict_value_2,dict_node_2,element_number_2)
    print b_matrix

    path_2=[]
    path_2=find_all_paths(0,b_matrix,dict_node_2,path_2,b_loops)

    print path_1
    print path_2

    print loopvaluecheck(dict_value_1,dict_value_2,path_1,path_2)
    return loopvaluecheck(dict_value_1,dict_value_2,path_1,path_2)

'''
def loopvaluecheck(dict_value_1,dict_value_2,path_1,path_2):
	for key in path_1:		
		for key2 in path_2:
				print "###"
				print key
				print key2
				print "++++++++"
				print dict_value_1[key]
				print dict_value_2[key2]
				if ()
				if ( value not in dict_value_2[key2]):

					answer= 'not equal'

					return answer
					
				else:
					answer ='equal'
	return answer
	'''

def loopvaluecheck(dict_value_1,dict_value_2,path_1,path_2):
	if not path_1:

		answer = 'not equal'
		return answer
	if not path_2:

		answer = 'not equal'
		return answer


	for key2 in path_1:
		if (key2 not in path_2):
			answer='unrequired element '
			print key2
			
			return answer 
			break

	for key in path_1:



				if ( dict_value_1[key] != dict_value_2[key]):
					print "dict_value_1[key]"
					print dict_value_1[key]
					print "dict_value_2[key]"
					print dict_value_2[key]

					answer= 'incorrect values'
					return answer
					break

				else:
					answer ='equal'



	return answer
	
	



def buildgraph(file): 
	index_VAC=1
	index_VDC=1
	index_C=1
	index_L=1
	index_R=1	
	index_D=1
	index_S=1
	index_IDC=1
	index_IAC=1
	index_U=1
	dict_value={}
	dict_node={}
	element_number=0
	for line in file: 
			'''
			splitLine= line.split(' ') 
			# Voltage source in Multisim label, the first node is +, second node is -, but we label - node first and + second for voltage source
			if (splitLine[0][0:3]=='VAC'):
				dict_value.update({'VAC' : [splitLine[4],splitLine[5]]})
				dict_node.update({'VAC': [int(splitLine[2]),int(splitLine[1])]})
				index_VAC +=1
			if (splitLine[0][0:3]=='VDC'):
				dict_value.update({'VDC': [splitLine[3]]})
				dict_node.update({'VDC': [int(splitLine[2]),int(splitLine[1])]})
				index_VDC +=1	
			if (splitLine[0][0:3]=='IAC'):
				dict_value.update({'IAC' : [splitLine[4],splitLine[5]]})
				dict_node.update({'IAC': [int(splitLine[2]),int(splitLine[1])]})
				index_IAC +=1
			if (splitLine[0][0:3]=='IDC'):
				dict_value.update({'IDC': [splitLine[3]]})
				dict_node.update({'IDC': [int(splitLine[2]),int(splitLine[1])]})
				index_IDC +=1	
			if (splitLine[0][0:1]=='C'):
				dict_value.update({'C': [splitLine[3]]})
				dict_node.update({'C': [int(splitLine[1]),int(splitLine[2])]})
				index_C +=1	
			if (splitLine[0][0:1]=='L'):
				dict_value.update({'L': [splitLine[3]]})
				dict_node.update({'L': [int(splitLine[1]),int(splitLine[2])]})
				index_L +=1	
			if (splitLine[0][0:1]=='R'):
				dict_value.update({'R': [splitLine[3]]})
				dict_node.update({'R': [int(splitLine[1]),int(splitLine[2])]})
				index_R +=1	
			if (splitLine[0][0:1]=='D'):
				dict_value.update({'D': [0]})
				dict_node.update({'D': [int(splitLine[1]),int(splitLine[2])]})	
				index_D +=1
			if (splitLine[0][0:1]=='S'):
				dict_value.update({'S': [0]})
				dict_node.update({'S': [int(splitLine[2]),int(splitLine[1])]})	
				index_S +=1
			'''
			splitLine= line.split(' ') 
			# Voltage source in Multisim label, the first node is +, second node is -, but we label - node first and + second for voltage source
			if (splitLine[0][0:3]=='VAC'):
				dict_value.update({'VAC'+str(index_VAC) : [splitLine[4],splitLine[5]]})
				dict_node.update({'VAC'+str(index_VAC): [int(splitLine[2]),int(splitLine[1])]})
				index_VAC +=1
				element_number+=1
			if (splitLine[0][0:3]=='VDC'):
				dict_value.update({'VDC'+str(index_VDC): [splitLine[3]]})
				dict_node.update({'VDC'+str(index_VDC): [int(splitLine[2]),int(splitLine[1])]})
				index_VDC +=1
				element_number+=1	
			if (splitLine[0][0:3]=='IAC'):
				dict_value.update({'IAC'+str(index_IAC) : [splitLine[4],splitLine[5]]})
				dict_node.update({'IAC'+str(index_IAC): [int(splitLine[2]),int(splitLine[1])]})
				index_IAC +=1
				element_number+=1
			if (splitLine[0][0:3]=='IDC'):
				dict_value.update({'IDC'+str(index_IDC): [splitLine[3]]})
				dict_node.update({'IDC'+str(index_IDC): [int(splitLine[2]),int(splitLine[1])]})
				index_IDC +=1	
				element_number+=1
			if (splitLine[0][0:1]=='C'):
				dict_value.update({'C'+str(index_C): [splitLine[3]]})
				dict_node.update({'C'+str(index_C): [int(splitLine[1]),int(splitLine[2])]})
				index_C +=1	
				element_number+=1
			if (splitLine[0][0:1]=='L'):
				dict_value.update({'L'+str(index_L): [splitLine[3]]})
				dict_node.update({'L'+str(index_L): [int(splitLine[1]),int(splitLine[2])]})
				index_L +=1	
				element_number+=1
			if (splitLine[0][0:1]=='R'):
				dict_value.update({'R'+str(index_R): [splitLine[3]]})
				dict_node.update({'R'+str(index_R): [int(splitLine[1]),int(splitLine[2])]})
				index_R +=1	
				element_number+=1
			if (splitLine[0][0:1]=='D'):
				dict_value.update({'D'+str(index_D): [0]})
				dict_node.update({'D'+str(index_D): [int(splitLine[1]),int(splitLine[2])]})	
				index_D +=1
				element_number+=1
			if (splitLine[0][0:1]=='S'):
				dict_value.update({'S'+str(index_S): [0]})
				dict_node.update({'S'+str(index_S): [int(splitLine[2]),int(splitLine[1])]})	
				index_S +=1
				element_number+=1
			if (splitLine[0][0:1]=='U'):
				dict_value.update({'U_input'+str(index_U): [str(splitLine[4])]})
				dict_node.update({'U_input'+str(index_U): [int(splitLine[2]),int(splitLine[3])]})	
				dict_node.update({'U_output'+str(index_U): [int(splitLine[1]),int(0)]})	
				dict_value.update({'U_output'+str(index_U): [str(splitLine[4])]})
				index_U +=1
				element_number+=2



	print dict_value
	print dict_node
	'''
	print element_number
	'''
	return [dict_value,dict_node,element_number]	
def find_all_paths(start_vertex,matrix,dict_node,path,loops):

		numrows=len(matrix)
		numcols= len(matrix[0])	
		for columns in range (numcols):
						if matrix[start_vertex,columns] == -1:
							path.append(dict_node.keys()[columns])
							for rows in  range (numrows):
								if matrix[rows,columns]==1 :
									end_vertex=rows
									if end_vertex==0:
										return path
									else:
										return find_all_paths(end_vertex,matrix,dict_node,path,loops)
									
'''

def find_all_paths(start_vertex,matrix,dict_node,path,loops):



		
										for n in range (loops):
											path=[]
											find_all_paths(start_vertex,matrix,dict_node,path,loops)
		
		numrows=len(matrix)
		numcols= len(matrix[0])
		paths=[]
		print '++++++++++++++'
		print loops
		##for p in range(loops)
		index=0
		for columns in range (numcols):
					
					##for p in range (numcols):

						if matrix[start_vertex,columns] == -1:
							##print matrix[start_vertex,columns]
							path.append(dict_node.keys()[columns])
							# not sure this command
							index+=1
							if index >1:

								matrix[start_vertex,columns]=9
								print matrix

							for rows in  range (numrows):
								if matrix[rows,columns]==1 :
									
								##if "-1" in matrix[rows,columns] :S
									end_vertex=rows

									# end at node 0
		if end_vertex==0:
							
										paths.append(path)

										print '++++1'
										print paths
										return paths
		else:
										find_all_paths(end_vertex,matrix,dict_node,path,loops)
										
										for q in extended_paths:
										paths.append(extended_paths)
										print '+++++2'
										print paths
										return paths

										
'''
def buildmatrix(values,nodes,element_number):
# build a matrix with by component and nodes, first node label -1, second node label +1.
		number_nodes=int(max(max(nodes.values()))+1)
		'''
		print "number of element "
		# number of nodes, len(nodes) is the numeber of 2 terminal element, op-amp counters 2 elements
		
		print [number_nodes,len(nodes)]
		print element_number 
		'''
		independent_loop=len(nodes)-number_nodes+1
		# the number of independent loop is b-n+1
		print independent_loop

		matrix=np.zeros(((number_nodes),element_number))

		for i in range(0,len(nodes)):
			matrix[nodes.values()[i][1],i]=1
			matrix[nodes.values()[i][0],i]=-1
		return [matrix,number_nodes,len(nodes),independent_loop]


if __name__ == '__main__':
  main()
