import math
import matplotlib.pyplot as plt


# -----------------------------
# DC CIRCUIT HELPER FUNCTIONS
# -----------------------------

def series_resistance(resistors):
    """Return equivalent resistance for resistors connected in series."""
    return sum(resistors)


def parallel_resistance(resistors):
    """Return equivalent resistance for resistors connected in parallel."""
    inverse_total = 0

    for resistance in resistors:
        inverse_total += 1 / resistance

    return 1 / inverse_total


def power_from_current(current, resistance):
    """Calculate resistor power using P = I^2 R."""
    return current ** 2 * resistance


def power_from_voltage(voltage, resistance):
    """Calculate resistor power using P = V^2 / R."""
    return voltage ** 2 / resistance


# -----------------------------
# RC CIRCUIT HELPER FUNCTIONS
# -----------------------------

def capacitor_charging_voltage(source_voltage, resistance, capacitance, time):
    """
    Calculate capacitor voltage while charging:
    Vc(t) = Vs * (1 - e^(-t/RC))
    """
    tau = resistance * capacitance
    return source_voltage * (1 - math.exp(-time / tau))


def capacitor_discharging_voltage(initial_voltage, resistance, capacitance, time):
    """
    Calculate capacitor voltage while discharging:
    Vc(t) = V0 * e^(-t/RC)
    """
    tau = resistance * capacitance
    return initial_voltage * math.exp(-time / tau)


# -----------------------------
# SERIES CIRCUIT ANALYSIS
# -----------------------------

print("SERIES CIRCUIT ANALYSIS")
print("-----------------------")

source_voltage = 12
series_resistors = [100, 220]

equivalent_resistance = series_resistance(series_resistors)
current = source_voltage / equivalent_resistance

print(f"Source voltage: {source_voltage:.2f} V")
print(f"Equivalent resistance: {equivalent_resistance:.2f} ohms")
print(f"Circuit current: {current:.4f} A")

total_voltage_drop = 0
total_power = 0

for index, resistance in enumerate(series_resistors, start=1):
    voltage_drop = current * resistance
    power = power_from_current(current, resistance)

    total_voltage_drop += voltage_drop
    total_power += power

    print(
        f"R{index}: {resistance} ohms | "
        f"Voltage drop: {voltage_drop:.2f} V | "
        f"Power: {power:.4f} W"
    )

print(f"Sum of voltage drops: {total_voltage_drop:.2f} V")
print(f"Total resistor power: {total_power:.4f} W")


# -----------------------------
# PARALLEL CIRCUIT ANALYSIS
# -----------------------------

print("\nPARALLEL CIRCUIT ANALYSIS")
print("-------------------------")

source_voltage = 12
parallel_resistors = [100, 220]

equivalent_resistance = parallel_resistance(parallel_resistors)
total_current = source_voltage / equivalent_resistance

print(f"Source voltage: {source_voltage:.2f} V")
print(f"Equivalent resistance: {equivalent_resistance:.2f} ohms")
print(f"Total current: {total_current:.4f} A")

branch_current_sum = 0
total_power = 0

for index, resistance in enumerate(parallel_resistors, start=1):
    branch_current = source_voltage / resistance
    power = power_from_voltage(source_voltage, resistance)

    branch_current_sum += branch_current
    total_power += power

    print(
        f"R{index}: {resistance} ohms | "
        f"Branch current: {branch_current:.4f} A | "
        f"Power: {power:.4f} W"
    )

print(f"Sum of branch currents: {branch_current_sum:.4f} A")
print(f"Total resistor power: {total_power:.4f} W")


# -----------------------------
# RC CIRCUIT ANALYSIS
# -----------------------------

print("\nRC CIRCUIT ANALYSIS")
print("-------------------")

source_voltage = 5
resistance = 1000
capacitance = 100e-6

time_constant = resistance * capacitance

print(f"Resistance: {resistance} ohms")
print(f"Capacitance: {capacitance} F")
print(f"Time constant: {time_constant:.4f} seconds")
print(f"Five time constants: {5 * time_constant:.4f} seconds")

times = []
charging_voltages = []
discharging_voltages = []

number_of_points = 200
maximum_time = 5 * time_constant

for i in range(number_of_points + 1):
    time = maximum_time * i / number_of_points

    charging_voltage = capacitor_charging_voltage(
        source_voltage,
        resistance,
        capacitance,
        time
    )

    discharging_voltage = capacitor_discharging_voltage(
        source_voltage,
        resistance,
        capacitance,
        time
    )

    times.append(time)
    charging_voltages.append(charging_voltage)
    discharging_voltages.append(discharging_voltage)


# Print a useful validation point at one time constant
voltage_at_tau = capacitor_charging_voltage(
    source_voltage,
    resistance,
    capacitance,
    time_constant
)

print(
    f"Charging voltage after one time constant: "
    f"{voltage_at_tau:.3f} V "
    f"({100 * voltage_at_tau / source_voltage:.1f}% of source voltage)"
)


# -----------------------------
# PLOT RC RESPONSE
# -----------------------------

plt.plot(times, charging_voltages, label="Charging")
plt.plot(times, discharging_voltages, label="Discharging")

plt.xlabel("Time (seconds)")
plt.ylabel("Capacitor Voltage (V)")
plt.title("RC Capacitor Charging and Discharging")

plt.grid()
plt.legend()
plt.tight_layout()

# Save a copy for your GitHub repository / project documentation
plt.savefig("rc_response.png", dpi=200)

plt.show()
