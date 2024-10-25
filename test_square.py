
# Importing required module
import subprocess
 
# Using system() method to
# execute shell commands
subprocess.Popen('echo "Setting up Tessy path to system variable..."', shell=True)

PATH= "C:\Program Files\Razorcat\TESSY_5.1\bin" 

subprocess.run(["set","PATH"], shell=True)


subprocess.Popen('echo "Selecting Project tessy.pdbx..."', shell=True)
subprocess.run(["tessyd","--file C:\prj\WUP_ENG_BASE_SDP\Tessy\tessy.pdbx"], shell=True)
