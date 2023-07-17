import pymysql
import time
import json
import csv
import tkinter as tk
from tkinter import ttk, messagebox
from os import system as os

# Import all the classes you want to use
from Classes.Person import Person
from Classes.Address import Address
from Classes.User import User

###############################
# Change these variables to your db credentials
# no other changes to this file are required.
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DATABASE = 'database_name'
###############################


def get_attributes_as_list(instance):
    attributes = []
    for attr_name, attr_value in instance.__dict__.items():
        if not callable(attr_value) and not attr_name.startswith("__"):
            attributes.append(attr_value)
    return attributes


def generator(class_combobox):
    class_input = class_combobox.get().capitalize()
    class_type = globals().get(class_input)
    num_instances = int(num_instances_entry.get())
    instances = []
    for _ in range(num_instances):
        instance = class_type()
        instances.append(instance)
    return {'class_name': class_input, 'instances': instances}

from tkinter import messagebox

# ...

def exporter(data):
    file_format = format_combobox.get()
    filename = f"{data['class_name']}.{file_format}"
    instances = data['instances']
    try:
        if file_format == "csv":
            with open(filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(instances[0].__dict__.keys())

                for instance in instances:
                    attributes = get_attributes_as_list(instance)
                    writer.writerow(attributes)

        elif file_format == "json":
            with open(filename, "w") as jsonfile:
                if data['class_name'] == 'Address':
                    json_instances = [address.__dict__ for address in instances]
                else:
                    json_instances = [instance.__dict__ for instance in instances]

                json.dump(json_instances, jsonfile, indent=4)

        else:
            messagebox.showerror("Error", "Invalid file format. Supported formats: csv, json")

        # Show success message box with Yes/No option
        result = messagebox.askyesno("Success", f"Data has been successfully exported to {filename}. Do you want to quit the program?")
        if result:
            root.destroy()  # Close the program

    except Exception as e:
        messagebox.showerror("Error", str(e))


def connect_to_database():
    attempts = 0
    maxAttempts = 5
    waitTime = 3
    while attempts <= maxAttempts:
        ts = time.strftime("%H:%M:%S", time.localtime())
        try:
            cnx = pymysql.connect(
                user=USERNAME,
                password=PASSWORD,
                host=HOST,
                database=DATABASE
            )
            cursor = cnx.cursor()
            address_instances = generator(class_combobox)
            break

        except Exception as e:
            if attempts < maxAttempts - 1:
                messagebox.showinfo("Info", '[{}] Connection to database failed ({}/{}). Trying again in {} seconds...  (Error: {})'.format(ts, attempts + 1, maxAttempts, round(waitTime), str(e)))
                time.sleep(waitTime)
                attempts += 1
                waitTime = waitTime * 1.5
            else:
                messagebox.showerror("Error", '[{}] Connection to database failed after {} attempts. Exiting program.'.format(ts, maxAttempts))
                root.destroy()
                break
    cnx.commit()
    cnx.close()


def on_database_combobox_change(event):
    database_connection = database_combobox.get()
    if database_connection == 'Yes':
        exporter_frame.pack_forget()  # Hide exporter options if "Yes" is selected
        format_combobox.configure(state="disabled")  # Disable format_combobox when "Yes" is selected
    else:
        exporter_frame.pack()  # Show exporter options if "No" is selected
        format_combobox.configure(state="enabled")  # Enable format_combobox when "No" is selected


def on_connect_button_click():
    database_connection = database_combobox.get()
    if database_connection.lower() == 'y':
        connect_to_database()
    else:
        data = generator(class_combobox)  # Pass class_combobox as an argument
        exporter(data)  # Pass data to the exporter function


# Create and place widgets
root = tk.Tk()
root.title("Data Exporter")
root.geometry("400x200")

database_label = tk.Label(root, text="Connect to a local database?")
database_label.pack()

database_combobox = ttk.Combobox(root, values=["Yes", "No"])
database_combobox.pack()
database_combobox.set("Yes")  # Set default value

class_label = tk.Label(root, text="Class to create:")
class_label.pack()

available_classes = ['User', 'Person', 'Address']
class_combobox = ttk.Combobox(root, values=available_classes)
class_combobox.pack()

num_instances_label = tk.Label(root, text="Number of instances:")
num_instances_label.pack()

num_instances_entry = tk.Entry(root)
num_instances_entry.pack()

format_label = tk.Label(root, text="Export format:")
format_label.pack()

format_combobox = ttk.Combobox(root, values=["csv", "json"])
format_combobox.pack()

exporter_frame = tk.Frame(root)  # Frame for exporter options

connect_button = tk.Button(root, text="Connect/Export", command=on_connect_button_click)
connect_button.pack()

# Bind the event to the function to detect changes in Combobox's value
database_combobox.bind("<<ComboboxSelected>>", on_database_combobox_change)

# Set the initial state of the format_combobox
on_database_combobox_change(None)

# Disable the format_combobox when the GUI starts
format_combobox.configure(state="disabled")

# Start the Tkinter event loop
root.mainloop()
