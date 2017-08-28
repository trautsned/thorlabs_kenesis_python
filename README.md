# thorlabs_kenesis_python
Simple script for controlling a linear stage (LTS300) with Python and the Thorlabs Kinesis .NET library
Thorlabs has a new kinesis library to replace their legacy APT library. I wanted to program with Python so used pythonnet to import and use the Thorlabs library.
## Requirements:
1. Python (I used 3.6)
1. numpy and matplotlib (these are optional)
2. Python for .NET https://github.com/pythonnet/pythonnet
3. Thorlabs Kenesis (I used 32bit for 32 bit systems)

I used Windows 7 32 bit with Python 3.6 and the 32 bit Thorlabs system for 32 bit systems. I assume that it works with other combinations but it has not been tested.
## Hardware:
I have three LTS300 Thorlab stages in X, Y, Z arrangment connected directly to the computer USB.
## Usage:
This is an example script so hack the code for your purposes.
Make sure to change the constants section at the start of the code for the Thorlab device serial numbers and the location of the Kenesis library. Change the variable x in the while loop to measurement data aquisition. Currently it just generates random data at each point.
## Disclaimer: 
While this code works it was the first time I had used Python for .net. Use it to get started but not as a template for best practices.
