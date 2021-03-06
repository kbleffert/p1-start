import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data = np.loadtxt(filename, skiprows=32,delimiter=",")   # Attempts to load filename into local variable data.

## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)

maxLen= (len(data)-1)
strain= -data[0:maxLen,7]
stress= -data[0:maxLen,3]

iDash= filename.rindex('-')
mylabel= filename[iDash+1:-4]

a0,a1= np.polyfit(strain,stress,1)
	
plt.plot(strain,stress,color='b',linestyle='-', label=mylabel)
plt.plot(strain,(a0*strain)+a1,color='r',linestyle='--',label='linear fit')

plt.xlabel("Strain [Ext%]")
plt.ylabel("Stress [Mpa]")
plt.title(filename)
plt.legend(loc='best')
plt.grid(True)

plt.savefig(filename+'.pdf')

plt.show()

print("Young's Modulus: "+str(a0)+" MPa")

## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
#git clone https://github.com/dracula/terminal-app.git# Edit the files (use git liberally here!) to mak#e them more usable

## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)


## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.



