# SQL to Report Generator

A Python-based desktop application that allows users to execute SQL queries on a MySQL database and export the results into various file formats such as Excel, CSV, or JSON.

## Features

- **Dynamic Database Selection**: Automatically fetches and displays all available databases in the MySQL server.
- **SQL Query Execution**: Users can input any valid SQL query.
- **Multiple Export Formats**: Choose between Excel, CSV, or JSON formats for the output file.
- **Custom Output File Name**: Users can specify the name of the output file.
- **Simple GUI**: Built with Tkinter, providing an easy-to-use interface.
- **Error Handling**: Displays error messages for connection issues, query errors, or export issues.

---

## Prerequisites

Ensure you have the following installed:

1. **Python 3.7+**: [Download here](https://www.python.org/downloads/)
2. **MySQL Server**: [Download here](https://dev.mysql.com/downloads/mysql/)
3. **Required Python Libraries**:
   - Install them using `pip`:
     ```bash
     pip install mysql-connector-python pandas openpyxl tkinter
     ```

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HoussemSouari/Sql_report_generator.git
   cd Sql_report_generator
