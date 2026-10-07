# DC/RC Circuit Analysis & Visualization Tool

Python-based electrical engineering project for analyzing basic DC and RC circuits.

## Features

- Calculates equivalent resistance for series and parallel resistor networks
- Calculates current, voltage drops, and component power
- Validates circuit calculations using Ohm's law and Kirchhoff's laws
- Models RC capacitor charging and discharging
- Calculates the RC time constant
- Generates capacitor-voltage plots using Matplotlib

## Technologies

- Python
- Matplotlib

## Example Analysis

The program analyzes examples including:

- A 12 V source with 100 ohm and 220 ohm resistors in series
- Parallel resistor networks
- RC charging and discharging with a 1 kOhm resistor and 100 uF capacitor

For the RC example:

tau = R x C

Using:

R = 1000 ohms
C = 100 uF

the time constant is:

tau = 0.1 seconds

The program plots the capacitor response from 0 to 5 time constants.

## Output

The project generates:

- Circuit calculation results in the terminal
- `rc_response.png`, showing RC charging and discharging curves

## How to Run

Install the required dependency:

```bash
pip install matplotlib
