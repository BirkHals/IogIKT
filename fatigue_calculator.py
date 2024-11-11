# -*- coding: utf-8 -*-
"""
@author: bjohau
"""



import numpy as np
import matplotlib.pyplot as plt
import fatigue_utilities_with_TODO as util

inFileName = "StressTimeHistory.asc"
bPrintAndPlot = True
if (bPrintAndPlot):
    util.plot_from_file( inFileName )


# Part 1: Finish the TODO in PVX_from_file

turningPoints = util.PVX_from_file( inFileName )

if (bPrintAndPlot):
    tpArray = np.array(turningPoints)
    plt.plot(tpArray[:,0],tpArray[:,1])
    plt.title('Turningpoints')
    plt.legend()
    plt.show()

    print('Number of turningpoints {}\n'.format(len(turningPoints)))
    for i in range( len(turningPoints) ):
        print('{:6d}  time, S_value: {:12.3e}  {:12.3e}'.format( i+1, turningPoints[i][0], turningPoints[i][1]))
        

# Part 2: Alter the values of first and last point so that they start at max/min
#         This is done by completing the TODO in beginAndEndAtExtremes
        
util.beginAndEndAtExtremes(turningPoints)

if (bPrintAndPlot):
    tpArray = np.array(turningPoints)
    plt.plot(tpArray[:,0],tpArray[:,1])
    plt.title('Turningpoints')
    plt.legend()
    plt.show()

#Part 3: Generate the stress cycles by doint the TODO in getCycles
    
cycles = util.getCycles( turningPoints )

if (bPrintAndPlot):
    print('Number of cycles {}\n'.format(len(cycles)))
    for i in range( len(cycles) ):
        print('{:6d}  S_mean, S_ampl: {:12.3e}  {:12.3e}'.format( i+1, cycles[i][0], cycles[i][1]))


S_u = 200.0
#S_u = 200.0e6

#Part 4: Combine the cycles with the S-N curve and calculate damage
#        with and without mean stress correction
#        This is done by completing the TODO in getDamage

bUseMeanStress = False
damage = util.getDamage( bUseMeanStress, cycles, S_u)
print('Damage without mean stress correction {:12.3e}'.format(damage))

bUseMeanStress = True
damage = util.getDamage( bUseMeanStress, cycles, S_u)
print('Damage using mean stress correction   {:12.3e}'.format(damage))

