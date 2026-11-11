import csv
import datetime
import os


def show_menu():
    print("\n============================================================")
    print("      MECHATRONICS ENGINEERING WORKBENCH & CONVERTER")
    print("============================================================")
    print(" 1. mm ---> Inches          |  9. Bar ---> PSI (Pressure)")
    print(" 2. Inches ---> mm          | 10. N·m ---> ft·lb (Torque)")
    print(" 3. Celsius ---> Fahrenheit | 11. Motor Efficiency & Visual Bar")
    print(" 4. Fahrenheit ---> Celsius | 12. Gear Ratio & Torque Simulator")
    print(" 5. kg ---> Pounds          | 13. 4-Band Resistor Color Decoder")
    print(" 6. Pounds ---> kg          | 14. View CSV Lab Report & Stats")
    print(" 7. km/h ---> m/s           |")
    print(" 8. m/s ---> km/h           |  0. Exit Workbench")
    print("============================================================")


def export_csv(tool, inp, out):
    exists = os.path.exists("mechatronics_report.csv")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("mechatronics_report.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["Timestamp", "Tool", "Input", "Output"])
        writer.writerow([now, tool, inp, out])


def motor_lab():
    print("\n--- MOTOR EFFICIENCY & VISUAL DIAGNOSTIC LAB ---")
    try:
        p_in = float(input("Electrical Input Power (W): "))
        p_out = float(input("Mechanical Output Power (W): "))
        if p_in <= 0 or p_out < 0 or p_out > p_in:
            print("[!] ERROR: Input must be > 0 and Output cannot exceed Input.")
            return
        eff = (p_out / p_in) * 100
        hp = p_out / 745.7
        blocks = int(eff // 5)
        bar = "█" * blocks + "░" * (20 - blocks)
        status = "OPTIMAL" if eff >= 80 else ("NORMAL" if eff >= 60 else "HIGH HEAT LOSS")
        print(f"\nOutput: {p_out:.2f} W ({hp:.4f} hp) | Heat Loss: {p_in - p_out:.2f} W")
        print(f"Efficiency: [{bar}] {eff:.2f}% ({status})")
        export_csv("Motor Lab", f"In:{p_in}W, Out:{p_out}W", f"{eff:.2f}% ({hp:.3f}hp)")
    except ValueError:
        print("[!] ERROR: Enter valid numbers.")


def gear_sim():
    print("\n--- GEAR RATIO, SPEED & TORQUE SIMULATOR ---")
    try:
        t1 = int(input("Driver Gear Teeth (Motor): "))
        t2 = int(input("Driven Gear Teeth (Load): "))
        rpm = float(input("Input Speed (RPM): "))
        trq = float(input("Input Torque (N·m): "))
        if t1 <= 0 or t2 <= 0 or rpm < 0 or trq < 0:
            print("[!] ERROR: Teeth must be > 0 and speed/torque >= 0.")
            return
        ratio = t2 / t1
        out_rpm = rpm / ratio
        out_trq = trq * ratio
        mode = "TORQUE MULTIPLIER" if ratio > 1 else ("SPEED MULTIPLIER" if ratio < 1 else "DIRECT DRIVE")
        print(f"\nRatio: {ratio:.2f}:1 ({mode})")
        print(f"Output Speed: {out_rpm:.2f} RPM | Output Torque: {out_trq:.2f} N·m")
        export_csv("Gear Simulator", f"{t1}T:{t2}T @ {rpm}RPM", f"{ratio:.2f}:1, {out_trq:.2f}Nm")
    except ValueError:
        print("[!] ERROR: Enter whole numbers for teeth and numbers for speed/torque.")


def resistor_decoder():
    print("\n--- 4-BAND RESISTOR COLOR CODE DECODER ---")
    print("Colors: black, brown, red, orange, yellow, green, blue, violet, grey, white")
    digits = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
              "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    tols = {"brown": "±1%", "red": "±2%", "green": "±0.5%", "blue": "±0.25%", "gold": "±5%", "silver": "±10%"}
    b1 = input("Band 1: ").strip().lower()
    b2 = input("Band 2: ").strip().lower()
    b3 = input("Band 3 (Multiplier): ").strip().lower()
    b4 = input("Band 4 (Tolerance) [default=gold]: ").strip().lower() or "gold"
    if b1 not in digits or b2 not in digits or b3 not in digits:
        print("[!] ERROR: Invalid color name.")
        return
    ohms = (digits[b1] * 10 + digits[b2]) * (10 ** digits[b3])
    tol = tols.get(b4, "±5%")
    res = f"{ohms / 1e6:.2f} MΩ {tol}" if ohms >= 1e6 else (f"{ohms / 1e3:.2f} kΩ {tol}" if ohms >= 1e3 else f"{ohms} Ω {tol}")
    print(f"\nResistance: {res}")
    export_csv("Resistor Decoder", f"{b1}-{b2}-{b3}-{b4}", res)


def view_report():
    print("\n--- SAVED CSV LAB REPORT ---")
    if not os.path.exists("mechatronics_report.csv"):
        print("No records found yet.")
        return
    with open("mechatronics_report.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"Total Logged Experiments: {len(lines) - 1}\n")
    for line in lines[1:]:
        print(line.strip())


def convert_unit(c, v):
    if (c == 5 or c == 6 or c == 9) and v < 0:
        return None, "PHYSICS ERROR: Mass or pressure cannot be negative!", ""
    if c == 3 and v < -273.15:
        return None, "PHYSICS ERROR: Below Absolute Zero (-273.15°C)!", ""
    if c == 4 and v < -459.67:
        return None, "PHYSICS ERROR: Below Absolute Zero (-459.67°F)!", ""

    if c == 1:
        return v / 25.4, f"{v} mm = {v / 25.4:.4f} in", "mm->in"
    elif c == 2:
        return v * 25.4, f"{v} in = {v * 25.4:.4f} mm", "in->mm"
    elif c == 3:
        r = (v * 9 / 5) + 32
        return r, f"{v} °C = {r:.4f} °F", "°C->°F"
    elif c == 4:
        r = (v - 32) * 5 / 9
        return r, f"{v} °F = {r:.4f} °C", "°F->°C"
    elif c == 5:
        r = v * 2.20462
        return r, f"{v} kg = {r:.4f} lb", "kg->lb"
    elif c == 6:
        r = v / 2.20462
        return r, f"{v} lb = {r:.4f} kg", "lb->kg"
    elif c == 7:
        r = v / 3.6
        return r, f"{v} km/h = {r:.4f} m/s", "km/h->m/s"
    elif c == 8:
        r = v * 3.6
        return r, f"{v} m/s = {r:.4f} km/h", "m/s->km/h"
    elif c == 9:
        r = v * 14.5038
        return r, f"{v} Bar = {r:.4f} PSI", "Bar->PSI"
    elif c == 10:
        r = v * 0.73756
        return r, f"{v} N·m = {r:.4f} ft·lb", "Nm->ft-lb"
    return None, "Invalid choice.", ""


def main():
    while True:
        show_menu()
        try:
            choice = int(input("Select an option (0-14): "))
        except ValueError:
            print("[!] ERROR: Enter a number between 0 and 14.")
            input("Press Enter...")
            continue

        if choice == 0:
            print("Workbench closed. Data saved in 'mechatronics_report.csv'.")
            break
        elif choice == 11:
            motor_lab()
        elif choice == 12:
            gear_sim()
        elif choice == 13:
            resistor_decoder()
        elif choice == 14:
            view_report()
        elif 1 <= choice <= 10:
            try:
                val = float(input("Enter value: "))
            except ValueError:
                print("[!] ERROR: Enter a valid number.")
                input("Press Enter...")
                continue
            res, msg, label = convert_unit(choice, val)
            print(f"\nRESULT: {msg}")
            if res is not None:
                export_csv(label, str(val), msg)
        else:
            print("[!] ERROR: Choose between 0 and 14.")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
