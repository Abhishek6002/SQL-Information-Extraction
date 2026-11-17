# SQL Information Extraction using Python

## 1. Project Overview

This project is a Python-based SQL Information Extraction tool that reads a `.sql` file and extracts information about stored procedures using Regular Expressions (Regex).

The extracted information is converted into JSON format and saved in a corresponding `.json` file.

For example:

- Input: `sample_stored_procedure.sql`
- Output: `sample_stored_procedure.json`

## 2. Features

- Reads SQL files provided through command-line arguments.
- Extracts stored procedure names.
- Extracts procedure parameters.
- Identifies parameter modes such as `IN`, `OUT`, and `INOUT`.
- Extracts parameter names and data types.
- Handles data types with sizes, such as `VARCHAR(50)` and `DECIMAL(10,2)`.
- Converts extracted information into structured JSON format.
- Automatically generates the output filename.
- Includes basic error handling for missing arguments and files.

## 3. Technologies Used

- **Python:** Main programming language.
- **re module:** Used for extracting SQL information using Regular Expressions.
- **json module:** Used to convert extracted information into JSON format.
- **sys module:** Used to accept command-line arguments.
- **os module:** Used to generate the corresponding output filename.

## 4. Project Structure

```text
sql-information-extraction/
│
├── extraction.py
├── sample_stored_procedure.sql
├── sample_stored_procedure.json
└── README.md
```

## 5. How It Works

1. The script accepts a SQL filename as a command-line argument.
2. It reads the contents of the SQL file.
3. Regular Expressions identify stored procedure names and their parameter blocks.
4. Another Regex extracts parameter modes, names, and data types.
5. The extracted information is organized into Python dictionaries and lists.
6. The Python data is converted into JSON format.
7. The JSON output is saved using the same filename as the original SQL file, with a `.json` extension.

## 6. How to Run

Open a terminal in the project directory and execute:

```bash
python extraction.py sample_stored_procedure.sql
```

The script generates:

```text
sample_stored_procedure.json
```

## 7. Example JSON Output

```json
{
    "procedures": [
        {
            "name": "GetCustomerOrders",
            "parameters": [
                {
                    "mode": "IN",
                    "name": "customerId",
                    "data_type": "INT"
                },
                {
                    "mode": "IN",
                    "name": "startDate",
                    "data_type": "DATE"
                }
            ]
        }
    ]
}
```

The actual output contains all stored procedures and their extracted parameters.

## 8. Future Enhancements

The project can be extended to extract additional SQL information, including:

- **SQL Operations:** Identify statements such as SELECT, INSERT, UPDATE, and DELETE.
- **Table Extraction:** Identify table names referenced within stored procedures.
- **SQL Statement Extraction:** Extract and organize complete SQL statements from each procedure.
- **Improved SQL Support:** Handle more complex SQL syntax and different stored procedure formats.

These enhancements can make the tool more comprehensive by extracting not only procedure definitions and parameters but also the operations performed inside them.

## 9. Conclusion

This project demonstrates how Python Regular Expressions can be used to extract structured information from SQL files and convert it into JSON format. It also provides practical experience with file handling, dictionaries, JSON serialization, command-line arguments, and basic error handling.# SQL Information Extraction using Python

## 1. Project Overview

This project is a Python-based SQL Information Extraction tool that reads a `.sql` file and extracts information about stored procedures using Regular Expressions (Regex).

The extracted information is converted into JSON format and saved in a corresponding `.json` file.

For example:

- Input: `sample_stored_procedure.sql`
- Output: `sample_stored_procedure.json`

## 2. Features

- Reads SQL files provided through command-line arguments.
- Extracts stored procedure names.
- Extracts procedure parameters.
- Identifies parameter modes such as `IN`, `OUT`, and `INOUT`.
- Extracts parameter names and data types.
- Handles data types with sizes, such as `VARCHAR(50)` and `DECIMAL(10,2)`.
- Converts extracted information into structured JSON format.
- Automatically generates the output filename.
- Includes basic error handling for missing arguments and files.

## 3. Technologies Used

- **Python:** Main programming language.
- **re module:** Used for extracting SQL information using Regular Expressions.
- **json module:** Used to convert extracted information into JSON format.
- **sys module:** Used to accept command-line arguments.
- **os module:** Used to generate the corresponding output filename.

## 4. Project Structure

```text
sql-information-extraction/
│
├── extraction.py
├── sample_stored_procedure.sql
├── sample_stored_procedure.json
└── README.md
```

## 5. How It Works

1. The script accepts a SQL filename as a command-line argument.
2. It reads the contents of the SQL file.
3. Regular Expressions identify stored procedure names and their parameter blocks.
4. Another Regex extracts parameter modes, names, and data types.
5. The extracted information is organized into Python dictionaries and lists.
6. The Python data is converted into JSON format.
7. The JSON output is saved using the same filename as the original SQL file, with a `.json` extension.

## 6. How to Run

Open a terminal in the project directory and execute:

```bash
python extraction.py sample_stored_procedure.sql
```

The script generates:

```text
sample_stored_procedure.json
```

## 7. Example JSON Output

```json
{
    "procedures": [
        {
            "name": "GetCustomerOrders",
            "parameters": [
                {
                    "mode": "IN",
                    "name": "customerId",
                    "data_type": "INT"
                },
                {
                    "mode": "IN",
                    "name": "startDate",
                    "data_type": "DATE"
                }
            ]
        }
    ]
}
```

The actual output contains all stored procedures and their extracted parameters.

## 8. Future Enhancements

The project can be extended to extract additional SQL information, including:

- **SQL Operations:** Identify statements such as SELECT, INSERT, UPDATE, and DELETE.
- **Table Extraction:** Identify table names referenced within stored procedures.
- **SQL Statement Extraction:** Extract and organize complete SQL statements from each procedure.
- **Improved SQL Support:** Handle more complex SQL syntax and different stored procedure formats.

These enhancements can make the tool more comprehensive by extracting not only procedure definitions and parameters but also the operations performed inside them.

## 9. Conclusion

This project demonstrates how Python Regular Expressions can be used to extract structured information from SQL files and convert it into JSON format. It also provides practical experience with file handling, dictionaries, JSON serialization, command-line arguments, and basic error handling.