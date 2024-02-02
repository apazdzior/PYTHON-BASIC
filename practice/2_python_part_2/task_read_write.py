"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os

input_directory = "./files"
output_file = "result.txt"

# Function to read files and extract values
def read_and_extract_values(directory):
    values = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                value = file.read().strip()
                values.append(value)
    return values

# Function to write values to the output file
def write_to_output_file(values, output_filename):
    output_path = os.path.join(".", output_filename)
    with open(output_path, 'w') as output_file:
        output_file.write(", ".join(values))

# Read and extract values
extracted_values = read_and_extract_values(input_directory)

# Write values to the output file
write_to_output_file(extracted_values, output_file)

print(f"Values extracted from files and written to {output_file}.")
