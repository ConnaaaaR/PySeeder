import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import time
import json
import csv
from os import system as os
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


def generator():
    class_input = class_entry.get().capitalize()
    class_type = globals().get(class_input)
    num_instances = int(num_instances_entry.get())
    instances = []
    for _ in range(num_instances):
        instance = class_type()
        instances.append(instance)
    return {'class_name': class_input, 'instances': instances}


def exporter():
    file_format = format_combobox.get()

    data = generator()

    filename = f"{data['class_name']}.{file_format}"
    instances = data['instances']
    try:
        if file_format == "csv":
            with open(filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(instances[0].__dict__.keys())

                for instance in instances:
                    writer.writerow(instance.__dict__.values())

        elif file_format == "json":
            with open(filename, "w") as jsonfile:
                json.dump(data, jsonfile, indent=4)

        else:
            messagebox.showerror("Error", "Invalid file format. Supported formats: csv, json")
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
            address_instances = generator()
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


def on_connect_button_click():
    database_connection = database_combobox.get()
    if database_connection.lower() == 'y':
        connect_to_database()
    else:
        exporter()


# Create the main application window
root = tk.Tk()
root.title("Data Exporter")
root.geometry("400x200")

# Create and place widgets
class_label = tk.Label(root, text="Class to create:")
class_label.pack()

class_entry = tk.Entry(root)
class_entry.pack()

num_instances_label = tk.Label(root, text="Number of instances:")
num_instances_label.pack()

num_instances_entry = tk.Entry(root)
num_instances_entry.pack()

format_label = tk.Label(root, text="Export format:")
format_label.pack()

format_combobox = ttk.Combobox(root, values=["csv", "json"])
format_combobox.pack()

database_label = tk.Label(root, text="Connect to a local database? (y/n):")
database_label.pack()

database_combobox = ttk.Combobox(root, values=["y", "n"])
database_combobox.pack()

connect_button = tk.Button(root, text="Connect/Export", command=on_connect_button_click)
connect_button.pack()

# Start the Tkinter event loop
root.mainloop()



