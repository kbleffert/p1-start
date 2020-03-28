# Project 1  
* Author: Katie Bleffert  
* Class: MSE 150   
* Semester: Spring 2020  
  
## Overview 
  
This project plots stress 
  
## Compiling and Using  
  
This program will require a csv .raw file with columns of stress and strain data with 32 lines of space at the top of the file. Each file should only have one sample's data. These files must  be in the main project directly or in an accessible folder within the main project directory.

Additionally, your terminal will need a current version of python that is capable of running matplotlib. You can find information on downloading python from: https://www.python.org/downloads/ . The graphs are saved in .pdf format, so a pdf viewer is needed in order to view the saved files. 
  
To run this code, use the following command in the main project directory:  
` `  
$ python plot.py filepath/filename 
` `  
  
You should expect to see a window pop up with the graph displayed, you may need to adjust the window sizing. In addition, you should see the Young's modulus printed in the terminal in Mpa.

An example of running this code within the main project directory with a data file called "tungsten1.raw" in a folder called "raw-data" that is in the main project directory:  
` `  
$ python plot.py raw-data/tungsten1.raw
` `  
  
 ## Reflection
This project helped me become much more familiar with git and vim. I learned how very useful they can be. Working with Jenny and Eric during help sessions helped me learn useful git commands like "line#gg" to navigate through large text files. Using git to easily update files and get back the old files with git checkout after I messed things up really bad on my plot a few times was a lifesaver. I also learned that matplotlib doesn't function the same way I am used to in that the order of lines of code, such as plot.show(), is very important.
