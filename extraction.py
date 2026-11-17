import re
import json
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python extraction.py <sql_file>")
    sys.exit(1)

input_file = sys.argv[1]

if not os.path.isfile(input_file):
    print("Error: SQL file not found!")
    sys.exit(1)



with open(input_file, "r") as file:
    content = file.read()

procedures = re.findall(
    r"CREATE PROCEDURE\s+(\w+)\s*\(((?:[^()]|\([^()]*\))*)\)",
    content,
    re.DOTALL
)


all_procedures = []

for name, parameters in procedures:

    params = re.findall(
        r"(INOUT|IN|OUT)\s+(\w+)\s+(\w+(?:\([^)]*\))?)",
        parameters
    )

    procedure_data = {
        "name": name,
        "parameters": []
    }

    for mode, param_name, data_type in params:

        parameter_data = {
            "mode": mode,
            "name": param_name,
            "data_type": data_type
        }

        procedure_data["parameters"].append(parameter_data)

    all_procedures.append(procedure_data)


output_file = os.path.splitext(input_file)[0] + ".json"
output = {
    "procedures": all_procedures
}


with open(output_file, "w") as file:
    json.dump(output, file, indent=4)

print("JSON file created successfully!")