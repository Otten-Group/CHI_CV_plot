# CHI_CV_Plot

This project provides a script to convert and plot cyclic voltammetry (CV) data from CHI potentiostats. The script reads the data, processes it, and generates publication-quality plots.

## Prerequisites

- Python 3.x
- Required Python packages:
  - pandas
  - matplotlib
  - seaborn
  - numpy

You can install the required packages using pip:

`pip install pandas matplotlib seaborn numpy`

## Usage

1. **Export as csv**
    you need to convert your CHI potentiostat data to a CSV file. This can be done using the chimodto tool. Follow these steps:  
    Step 1: open the  CHI600c_mod.exe file and use this to save as csv from your original bin file. 

2. **Plot the Data**
    Once you have your CSV file, you can use the provided script to plot the data.  
    Place your CSV file in the appropriate directory.
    Update the file_paths variable in the script to include the path to your CSV file.
    define the output name in the plot_name variable in the script.
    define the aspect ratio and referencing to ferrocene

## Vairables
`Std_ox` and `Std_re`: Standard oxidation and reduction potentials.
`offset`: Offset applied to the potential.
`electrode_diameter_mm`: Diameter of the electrode in millimeters.
`ferrocene_potential`: Reference potential for ferrocene.
`x_label` and `y_label`: Labels for the x and y axes.
`aspect_ratio`: Aspect ratio of the plot.
`compute_current_density`: Whether to compute current density.
`plot_name`: Name of the output plot file.
`file_paths`: List of paths to the CSV files to be plotted.