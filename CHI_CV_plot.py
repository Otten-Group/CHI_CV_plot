import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Parameters
# Standard oxidation and reduction potentials
Std_ox = 0.0
Std_re = 0.0
# Offset applied to the potential
offset = (Std_re + Std_ox) / 2
# Diameter of the electrode in millimeters
electrode_diameter_mm = 3

# Ferrocene potential (example value)
ferrocene_potential = 0.0  # V vs. Ag/Ag+

# Plotting parameters
x_label = "Potential (V vs Ag/Ag$^{+}$)"  # X-axis label
y_label = "Current Density (mA cm$^{-2}$)"  # Y-axis label with LaTeX formatting
plot_labels = ["CV"]  # Labels for the plot legend
aspect_ratio = (10, 6)  # Aspect ratio of the plot
compute_current_density = True  # Whether to compute current density
plot_name = "example.png"  # Name of the output plot file

# File paths
file_paths = ["/Users/fionnferreira/PycharmProjects/CHI_CV_Plo/example_data/FF015CVa.csv"]

# Set the style for the plot
sns.set_style("white")
sns.set_context("paper", font_scale=1.5, rc={"lines.linewidth": 1})

def plot_voltammogram(file_path, color, label, compute_current_density=False, electrode_diameter_mm=None):
    """
    Function to plot a voltammogram from a CSV file.

    Parameters:
    - file_path: Path to the CSV file
    - color: Color for the plot line
    - label: Label for the plot legend
    - compute_current_density: Whether to compute current density
    - electrode_diameter_mm: Diameter of the electrode in millimeters
    """
    # Read the file into a list of lines to find the header
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Locate the line with the header
    header_line = [i for i, line in enumerate(lines) if 'Potential/V, Current/A' in line][0]

    # Read the CSV data, skipping rows before the header
    data = pd.read_csv(file_path, skiprows=header_line, delimiter=',', na_values=["", " "])

    # Ensure that we strip any whitespace from the headers
    data.columns = [col.strip() for col in data.columns]

    # Check if 'Potential/V' and 'Current/A' are in the DataFrame after stripping whitespace
    if 'Potential/V' not in data.columns or 'Current/A' not in data.columns:
        raise ValueError(
            f"Columns 'Potential/V' or 'Current/A' not found in {file_path}. Available columns: {data.columns.tolist()}")

    # Apply the offset to the 'Potential/V' column
    data['Potential/V'] = data['Potential/V'] - offset

    # Shift potential axis to reference to ferrocene
    data['Potential/V'] -= ferrocene_potential

    # Convert current to current density if requested
    if compute_current_density and electrode_diameter_mm:
        radius_cm = electrode_diameter_mm / 20  # Convert mm to cm for radius
        electrode_surface_area = np.pi * (radius_cm ** 2)  # Area in cm^2
        data['Current/A'] /= electrode_surface_area
        data['Current/A'] *= 1000  # Convert from A/cm^2 to mA/cm^2
        y_label = "Current Density (mA cm$^{-2}$)"  # Updated y-label with LaTeX formatting
    else:
        y_label = "Current (A)"

    # Multiply the y-axis values by -1 to invert them
    data['Current/A'] *= -1

    # Plot the voltammogram
    plt.plot(data['Potential/V'], data['Current/A'], color=color, label=label)

# Plotting
plt.figure(figsize=aspect_ratio)
colors = sns.color_palette('tab10', len(file_paths))  # Get a color palette with as many colors as files

for file_path, color, label in zip(file_paths, colors, plot_labels):
    plot_voltammogram(file_path, color, label, compute_current_density, electrode_diameter_mm)

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.tight_layout()

# Add a black line on the outside of the plot
for spine in plt.gca().spines.values():
    spine.set_color('black')

plt.savefig(plot_name, dpi=600)
plt.show()