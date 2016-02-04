# Temperature-Recorder
A system that reads and plots temperature readings from an Arduino with a temperature sensor

### temperature_controller
An Arduino program that reports temperature data measured by an LM34 temperature sensor. Additionally, the onboard LED is configured to light up at a given temperature threshold (currently set to 30 C).

### read.py
Reads the serial output from the Arduino. It records the data in CSV format that will be plotted by the R script.

### plot.R
Imports the collected temperature data and plots it against time.
