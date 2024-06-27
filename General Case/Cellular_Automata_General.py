print("Cellular_Automata_Basic.py")
import numpy as np
import time as tm
import matplotlib.pyplot as plt
import matplotlib as mpl
print("> Imports complete")

mpl.use('PS')
print('> [Warning]: MatPlotLib will use PS backend instead of AGG backend. Plots may not be displayed within console. They will be saved directly.')
# System parameters:

N = 81 # Number of cells
if N % 2 == 0: # Check if N is even
    print("> [Warning]: N is an even number. You may generate eronious results!")

          
def rule(cell_number , row): # Define system rule ((UNDEFINED))
    print("> [Error]: Rule function has not been defined."
    # Must return True to colour a cell and False to discolour a square
  
print("> System rule defined")          

Cell_0 = [] # Create an initial row (Row 0) where the centered square is marked True 
for i in range(N):
    if i == (N - 1)/2:
        Cell_0.append(1)
    else:
        Cell_0.append(0)

cells = [Cell_0] # Inckude initial row (Row 0) in the cells list
# Generate cells using the system rule

for j in range(N): # Loop for each row:
    cell_index = []
    cells.append(cell_index)
    for i in range(N): # Loop for each cell:
        if rule(i , j) == True:
            cells[j + 1].append(1)
            
        else:
            cells[j + 1].append(0)
            
            
print("> Printing Result: ")
if len(cells[0]) > 10 :
    print("> Result is too large to display in console. Results will be plotted")
else:
    for k in range(len(cells)):
        print(cells[k])
    
# Plotting resultant data:
   
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
ax.set_ylim(N , 0)   
plt.grid(True)  
plt.show()
print('> Plot generated')
plt.savefig("CellularAutomata.ps" , format = 'ps')
print("> Plot .ps file saved")
        
    
    

