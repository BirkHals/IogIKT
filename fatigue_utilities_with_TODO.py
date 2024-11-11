# -*- coding: utf-8 -*-
"""
@author: bjohau
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_from_file( fileName ):
    
    data = np.loadtxt(fileName)

    plt.plot(data[:,0],data[:,1], label=fileName)
    plt.title('plot_from_file')
    plt.legend()
    plt.show()
    
    return
    
    
def PVX_from_file( fileName ):
    """
    Read the data from the file and return list of turningpoints
    
    Each line int the file contains two floats; time and stress value
    The function return a list of all turningpoints with [time, stress]
    for each 
    """
    
    turningPoints = []
    
    dataFile = open(fileName,'r')
       
    data1 = []
    data2 = []
    data3 = []
    
    # If data insert first point
    line = dataFile.readline()
    if ( line ):
        data1 = list(map(float, line.split()))   
        turningPoints.append(data1)
        
    #TODO: Read point 2 from the file
    
    #TODO: Loop over all point and append all turningpoints
    
    #TODO: Append the last point as well
        
    return turningPoints


def beginAndEndAtExtremes( turningPoints ):
    """
    Alter value of stress at first and last point to match max/min
    """
    
    if (len(turningPoints) < 3) :
        return
    
    #TODO: Find max and min stress value
    
    #TODO: Move first and last point to max or min depending
    #TODO: on which direction the curve has at begining and end
            
    return

        

def getCycles( stressList ):
    """Return list of all stress cycles with [mean,amplitude] for each cycle
    """
    
    cycles = []
    
    #TODO: Dummy cycles as example, delete these
    
    S_mean = 0.0
    S_ampl = 100.0
    cycles.append([S_mean,S_ampl])
    
    S_mean = 50.0
    S_ampl = 50.0
    cycles.append([S_mean,S_ampl])
    
    #TODO: Append values of real cycles based on the turning points

    
    return cycles



def getDamage( bUseMeanStress, cycles, S_u):
    """"Return accumulated damage based on the cycles in the input list
    """
    
    damage = 0.0 # No damage so far
    
    # S er samme som spenning. (Stort sett kallt sigma tidlgere)
    # Dette skyldes at kurvene kalles ofte S-N kurver
    
    S_1k = 0.9 * S_u #
    S_e  = 0.1 * S_u
    
    for i in range(len(cycles)):
        S = cycles[i][1]
        
        if (bUseMeanStress): #Only correct for S_mean < S_u
            ...
            #TODO Fill in code to perform the mean value correction
            
        newDamage = 0.0
        
        if ( S > S_u ):     # Stress above S_u immediately "kills" the material
            newDamage = 1.0
            
        elif ( S > S_1k ):  # Stress above S_1k but below S_u
            ...
            #TODO: Fill in code here
            
        elif ( S > S_e ):   # Stress above S_e but below S_1k
            ...
            #TODO: Fill in code here
            
        else:
            newDamage = 0.0 # We are below S_e, and have no damage
            
        damage += newDamage
        
    return damage
           

    
    