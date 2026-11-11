# Mechatronics Engineering Workbench & Converter

## What it does
This is a command-line Python engineering suite built for ND1 Mechatronics Engineering lab work. It converts core engineering measurements (mm/inches, °C/°F, kg/lb, km/h and m/s) while validating physical laws to prevent impossible inputs like negative mass or temperatures below Absolute Zero.

## How to run it
Install Python 3 on your PC or use Pydroid 3 on Android, then run:
`python mechatronics_workbench.py`

## Sample output
```text
============================================================

      MECHATRONICS ENGINEERING WORKBENCH & CONVERTER
============================================================

 1. mm ---> Inches          |  9. Bar ---> PSI (Pressure)
 2. Inches ---> mm          | 10. N·m ---> ft·lb (Torque)
 3. Celsius ---> Fahrenheit | 11. Motor Efficiency & Visual Bar
 4. Fahrenheit ---> Celsius | 12. Gear Ratio & Torque Simulator
 5. kg ---> Pounds          | 13. 4-Band Resistor Color Decoder
 6. Pounds ---> kg          | 14. View CSV Lab Report & Stats
 7. km/h ---> m/s           |

 8. m/s ---> km/h           |  0. Exit Workbench
============================================================
Select an option (0-14): 11


--- MOTOR EFFICIENCY & VISUAL DIAGNOSTIC LAB ---
Electrical Input Power (W): 1000
Mechanical Output Power (W): 850

Output: 850.00 W (1.1399 hp) | Heat Loss: 150.00 W
Efficiency: [█████████████████░░░] 85.00% (OPTIMAL)
```

## My own twist
To make this practical for Mechatronics workshops, I added five custom features beyond the basic unit conversions:
1. **Pneumatic & Mechanical Units:** Added Bar to PSI (pressure) and N·m to ft·lb (torque).
2. **Motor Efficiency & Visual Diagnostic Bar:** Calculates mechanical horsepower, heat loss in Watts, and renders an ASCII progress bar in the terminal.
3. **Gear Ratio & Torque Simulator:** Calculates gear ratios, output speed (RPM), and output torque from driver and driven gear teeth.
4. **4-Band Resistor Color Decoder:** Converts standard resistor color bands into Ohms, kOhms, or MOhms with tolerance ratings.
5. **Automated CSV Lab Export:** Logs every calculation with a timestamp into `mechatronics_report.csv` for viewing in Excel.

## What I learned
I learned how to break a complex program into clean, reusable Python functions and handle invalid user inputs with `try-except` blocks. I also learned how to use Python's `csv` and `datetime` modules to save permanent engineering records automatically.

## Author
Okolie paul , ND1 Mechatronics Engineering, YabaTech.
