# Import the necessary libraries
from openpyxl import load_workbook

# Define the path and name of the input Excel file
input_file = 'example.xlsx'

# Define the path and name of the output Excel file
output_file = 'output.xlsx'

# Load the workbook
workbook = load_workbook(input_file)

# Save the workbook with a different name
workbook.save(output_file)