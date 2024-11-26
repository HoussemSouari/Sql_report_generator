import mysql.connector
import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk

def get_database_list(host, user, password):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in cursor.fetchall()]
        conn.close()
        return databases
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error fetching databases: {err}")
        return []

def generate_report(query, host, user, password, database, output_file, file_format):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conn.is_connected():
            print("Connected to MySQL database")
    except mysql.connector.Error as err:
        messagebox.showerror("Connection Error", f"Error: {err}")
        return

    # Execute the query and fetch data
    try:
        df = pd.read_sql(query, conn)
    except Exception as e:
        messagebox.showerror("Query Error", f"Error: {e}")
        conn.close()
        return

    # Export data to the selected format
    try:
        if file_format == "Excel":
            if not output_file.endswith(".xlsx"):
                output_file += ".xlsx"
            df.to_excel(output_file, index=False)
        elif file_format == "CSV":
            if not output_file.endswith(".csv"):
                output_file += ".csv"
            df.to_csv(output_file, index=False)
        elif file_format == "JSON":
            if not output_file.endswith(".json"):
                output_file += ".json"
            df.to_json(output_file, orient="records", indent=4)

        messagebox.showinfo("Success", f"Report generated successfully and saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Export Error", f"Error: {e}")
    finally:
        conn.close()

def on_generate_button_click():
    query = query_text.get("1.0", tk.END).strip()
    database = database_var.get()
    file_format = format_var.get()
    output_file = output_file_entry.get().strip()

    if not query:
        messagebox.showwarning("Input Error", "Please enter an SQL query.")
        return
    if not database:
        messagebox.showwarning("Input Error", "Please select a database.")
        return
    if not file_format:
        messagebox.showwarning("Input Error", "Please select a file format.")
        return
    if not output_file:
        messagebox.showwarning("Input Error", "Please enter a name for the output file.")
        return

    # Database connection details (adjust as needed)
    host = 'localhost'
    user = 'username'
    password = 'password'

    # Generate the report
    generate_report(query, host, user, password, database, output_file, file_format)

# Create the main window
root = tk.Tk()
root.title("SQL to Report Generator")

# Database connection details (adjust as needed)
host = '127.0.0.1'
user = 'root'
password = '240622hssqlIT300'

# Fetch the list of databases
databases = get_database_list(host, user, password)

# Database selection
database_label = tk.Label(root, text="Select Database:")
database_label.pack(pady=5)

database_var = tk.StringVar()
database_dropdown = ttk.Combobox(root, textvariable=database_var, values=databases, state="readonly")
database_dropdown.pack(pady=5)

# SQL Query input
query_label = tk.Label(root, text="Enter SQL Query:")
query_label.pack(pady=5)

query_text = tk.Text(root, height=10, width=60)
query_text.pack(pady=5)

# Output file format selection
format_label = tk.Label(root, text="Select File Format:")
format_label.pack(pady=5)

format_var = tk.StringVar()
format_dropdown = ttk.Combobox(root, textvariable=format_var, values=["Excel", "CSV", "JSON"], state="readonly")
format_dropdown.pack(pady=5)

# Output file name input
output_file_label = tk.Label(root, text="Enter Output File Name (without extension):")
output_file_label.pack(pady=5)

output_file_entry = tk.Entry(root, width=40)
output_file_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Report", command=on_generate_button_click)
generate_button.pack(pady=10)

# Run the GUI main loop
root.mainloop()
