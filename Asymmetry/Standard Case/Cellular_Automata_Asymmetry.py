print("Cellular_Automata_Basic.py")
import numpy as np # Unused
import time as tm 
import matplotlib.pyplot as plt
import matplotlib as mpl
print("> Imports complete")

mpl.use('PS')
print('> [Warning]: MatPlotLib will use PS backend instead of AGG backend. Plots may not be displayed within console. They will be saved directly.')
# System parameters:

N = 500 + 1 # Number of cell
if N % 2 == 0: # Check if N is even
    print("> [Warning]: N is an even number. You may generate eronious results!")
          
def rule(cell_number , row): # Define system rule ((UNDEFINED)):
    
    # Acquire data regarding immediate neighbour cells:
        
    if cell_number != 0: # Selected cell is not the first cell
        if cells[row][cell_number - 1] == 1: # If previous cell is 1, then condition True
            R_Prev = True
        else:
            R_Prev = False # If the previous cell is 0, then condition True
    else:
        R_Prev = False # If cell is first cell, previous cell is automatically 0 and False
        
    if cell_number !=  N - 1: # If the selected cell isn't the last cell
        if cells[row][cell_number + 1] == 1: # If the next cell is 1, then condition True
            R_Nxt = True
        else:
            R_Nxt = False # If the next cell is 0, then condition False
    else:
        R_Nxt = False # If it is the last cell, next cell is automatically the  0, condition False
    
    if cells[row][cell_number] == True:  # Check if the current cell is coloured or not and store that data
        R_This = True
    else:
        R_This = False
        
        
    if R_Nxt ^ R_Prev ^ R_This: # XOR logic - returns true iff only one of the triad is coloured
        return True
    elif R_This == True and R_Nxt == True and R_Prev == False: # If the current and next cell are coloured, current cell will remain coloured - directional bias leading to asymmetry
        return True
    else:
        return False
        
print("> System rule defined")          

Cell_0 = [] # Create an initial row (Row 0) where the centered square is marked True 
for i in range(N):
    if i == (N - 1)/2:
        Cell_0.append(1)
    else:
        Cell_0.append(0)

cells = [Cell_0] # Inckude initial row (Row 0) in the cells list
# Generate cells using the system rule

for j in range(int((N + 1) /2)): # Loop for each row:
    cell_index = []
    cells.append(cell_index)
    for i in range(N): # Loop for each cell:
        if rule(i , j) == True:
            cells[j + 1].append(1)
            
        else:
            cells[j + 1].append(0)
            
# Displaying results:
            
if len(cells[0]) > 10 :
    print("> Result is too large to display in console. Results will be plotted")
else:
    print("> Printing Result: ")
    for k in range(len(cells)):
        print(cells[k])
    
# Plotting resultant data:
 
s_time = tm.time()

R = mpl.patches.Rectangle 
plt.figure()    
fig , ax = plt.subplots()
for I in range(len(cells)): # Loop for every row
    for J in range(len(cells[I])): # Loop for every cell
        if cells[I][J] == 1:
            c = 'black'
        elif cells[I][J] == 0:
            c = 'grey'
        else:
            print("> [Error]: Catastrophic Error")
            c = 'red'
        r = R(xy = (J , I), width = 1 , height = 1 , color = c)
        ax.add_patch(r)
        
ax.set_xlim(0, J + 1)  
ax.set_ylim(int((N + 1) /2) , 0)   
plt.grid(True)  
plt.show()

e_time = tm.time()

print('> Plot generated')
plt.savefig("CellularAutomata.ps" , format = 'ps')
print("> Plot .ps file saved")
print(f"> Time taken to generate plot figure: {e_time - s_time:.3f} seconds")
        
    
    

