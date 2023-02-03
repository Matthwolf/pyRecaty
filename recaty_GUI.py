"""
reaction.py
GUI for the python script reaction.py to plot reactive pathways
Author: Matthwolf@github
License: GPL v3+
"""

import tkinter as tk
import tkinter.messagebox as messagebox
import importlib
from recaty import Diagram
import configs
from pathlib import Path
import os

#Find the correct path for the icon and image
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class DiagramGUI:
    def __init__(self, master):
        self.master = master
        master.title("Reactive Pathway Diagram")

        # Create a Diagram object
        self.diagram = Diagram()

        # Create a button to open new pathway window
        self.new_pathway_button = tk.Button(master, text="Add new reactive pathway", bg='#feefd6', command=self.open_new_pathway_window)
        self.new_pathway_button.grid(row=0, column=0, rowspan=1, padx=5, pady=(5, 5))

        # Create a button to open link window
        self.new_pathway_button = tk.Button(master, text="Add new link", bg='#feefd6', command=self.open_new_link_window)
        self.new_pathway_button.grid(row=1, column=0, rowspan=1, pady=(5, 5))

        # Create a button to plot the diagram
        self.plot_button = tk.Button(master, text="Plot", bg='#feefd6', command=self.diagram.plot)
        self.plot_button.grid(row=2, column=0, rowspan=1, pady=(5, 5))

        # Create a button to change the configurations
        self.plot_button = tk.Button(master, text="Configurations", bg='#feefd6', command=self.open_config_window)
        self.plot_button.grid(row=3, column=0, rowspan=1, pady=(5, 5))

    def open_new_pathway_window(self):
        new_pathway_window = tk.Toplevel(self.master)
        new_pathway_window.title("New Reactive Pathway")
        new_pathway_window.geometry("460x400")

        # Create input fields for ID levels
        levelID_label = tk.Label(new_pathway_window, text="ID :")
        levelID_label.grid(row=0, column=0, pady=(5, 5), padx=(10, 0))
        levelID_entry = tk.Entry(new_pathway_window)
        levelID_entry.grid(row=0, column=1, pady=(5, 5), padx=(0, 10))

        # Add a label to explain ID
        add_level_instructions_ID = tk.Label(new_pathway_window, text="ID (0,1...), it allows to create links")
        add_level_instructions_ID.grid(row=0, column=2, sticky="w")

        # Create input fields for order
        order_label = tk.Label(new_pathway_window, text="Order:")
        order_label.grid(row=1, column=0, pady=(5, 5), padx=(10, 0))
        order_entry = tk.Entry(new_pathway_window)
        order_entry.grid(row=1, column=1, pady=(5, 5), padx=(0, 10))

        # Add a label to explain order
        add_level_instructions_order = tk.Label(new_pathway_window, text="Order (1,2...), it allows to align level on the x-axis")
        add_level_instructions_order.grid(row=1, column=2, sticky="w")

        # Create input fields for energy Energy
        energy_label = tk.Label(new_pathway_window, text="Energy :")
        energy_label.grid(row=2, column=0, pady=(5, 5), padx=(10, 0))
        energy_entry = tk.Entry(new_pathway_window)
        energy_entry.grid(row=2, column=1, pady=(5, 5), padx=(0, 10))

        # Add a label to explain Energy
        add_level_instructions_Energy = tk.Label(new_pathway_window, text="Energy of the level")
        add_level_instructions_Energy.grid(row=2, column=2, sticky="w")

        # Create input fields for level labels
        label_label = tk.Label(new_pathway_window, text="Label:")
        label_label.grid(row=3, column=0, pady=(5, 5), padx=(10, 0))
        label_entry = tk.Entry(new_pathway_window)
        label_entry.grid(row=3, column=1, pady=(5, 5), padx=(0, 10))

        # Add a label to explain label
        add_level_instructions_label = tk.Label(new_pathway_window, text="Label of the level, ex : TS")
        add_level_instructions_label.grid(row=3, column=2, sticky="w")

        # Create a combobox for color selection
        color_label = tk.Label(new_pathway_window, text="Color:")
        color_label.grid(row=4, column=0, pady=(5, 5), padx=(10, 0))
        color_var = tk.Entry(new_pathway_window)
        color_var.grid(row=4, column=1, pady=(5, 5), padx=(0, 10))

        # Add a label to explain color
        add_level_instructions_color = tk.Label(new_pathway_window, text="Color of the level, ex : black | #0000")
        add_level_instructions_color.grid(row=4, column=2, sticky="w")

        # Create a button to add a new level
        add_level_button = tk.Button(new_pathway_window, text="Add Level", command=lambda: self.add_level_new_pathway(levelID_entry.get(), order_entry.get(), energy_entry.get(), label_entry.get(), color_var.get()))
        add_level_button.grid(row=5, column=0, columnspan=2, pady=(5, 5), padx=(10, 10))

        # Create a Listbox to display levels
        self.level_list = tk.Listbox(new_pathway_window, height=10, width=30)
        self.level_list.grid(row=7, column=0, columnspan=2, padx=(5,5), pady=(5,5), sticky="W")

        # Add a label to explain list
        add_level_instructions_list = tk.Label(new_pathway_window, text="List of all the different level created")
        add_level_instructions_list.grid(row=7, column=2, sticky="w")

    def open_new_link_window(self):
        new_pathway_window2 = tk.Toplevel(self.master)
        new_pathway_window2.title("New Reactive Pathway")
        new_pathway_window2.geometry("400x330")

        # Create input fields for ID levels 1
        level1_label = tk.Label(new_pathway_window2, text="level ID 1 :")
        level1_label.grid(row=0, column=0, pady=(5, 5), padx=(10, 0))
        level1_entry = tk.Entry(new_pathway_window2)
        level1_entry.grid(row=0, column=1, pady=(5, 5), padx=(0, 10))

        # Add a label to explain ID
        add_level_instructions_ID1 = tk.Label(new_pathway_window2, text="ID level of the first level to link")
        add_level_instructions_ID1.grid(row=0, column=2, sticky="w")

        # Create input fields for ID levels 2
        level2_label = tk.Label(new_pathway_window2, text="level ID 2")
        level2_label.grid(row=1, column=0, pady=(5, 5), padx=(10, 0))
        level2_entry = tk.Entry(new_pathway_window2)
        level2_entry.grid(row=1, column=1, pady=(5, 5), padx=(0, 10))

        # Add a label to explain ID
        add_level_instructions_ID2 = tk.Label(new_pathway_window2, text="ID level of the second level to link")
        add_level_instructions_ID2.grid(row=1, column=2, sticky="w")

        # Create a combobox for color selection
        color_link_label = tk.Label(new_pathway_window2, text="Color:")
        color_link_label.grid(row=2, column=0, pady=(5, 5), padx=(10, 0))
        color_link_var = tk.Entry(new_pathway_window2)
        color_link_var.grid(row=2, column=1, pady=(5, 5), padx=(0, 10))

        # Add a label to explain color
        add_level_instructions_color2 = tk.Label(new_pathway_window2, text="Color of the link, ex : black | #0000")
        add_level_instructions_color2.grid(row=2, column=2, sticky="w")

        # Create a button to add a new link
        add_level_button = tk.Button(new_pathway_window2, text="Add link", command=lambda: self.create_links_new_pathway(level1_entry.get(), level2_entry.get(), color_link_var.get()))
        add_level_button.grid(row=3, column=0, columnspan=2, pady=(5, 5), padx=(10, 10))

        # Create a Listbox to display links
        self.level_list2 = tk.Listbox(new_pathway_window2, height=10, width=30)
        self.level_list2.grid(row=4, column=0, columnspan=4, padx=(5,5), pady=(5,5), sticky="W")

        # Add a label to explain list
        add_level_instructions_list2 = tk.Label(new_pathway_window2, text="List of all the different link created")
        add_level_instructions_list2.grid(row=4, column=2, sticky="w")

    # This function opens a new window for configuring diagram parameters
    def open_config_window(self):
        # Create a new window using tkinter's Toplevel widget
        self.config_window = tk.Toplevel()
        self.config_window.title("Diagram Configurations")
        self.config_window.geometry("630x630")
        # Counter for the number of rows in the window
        self.row_num = 0
        # Dictionary to store the tkinter Entry widgets
        self.entries = {}

        # Loop through the attributes of the configs module
        for key in dir(configs):
            # Skip any attributes that start with double underscores
            if not key.startswith("__"):
                # Add a label to the window with the attribute name
                tk.Label(self.config_window, text=key).grid(row=self.row_num, column=0, sticky='w')
                # Create an Entry widget and insert the current value of the attribute
                entry = tk.Entry(self.config_window)
                entry.insert(0, str(getattr(configs, key)))
                entry.grid(row=self.row_num, column=1)
                # Add the Entry widget to the entries dictionary
                self.entries[key] = entry
                # Increment the row number
                self.row_num += 1 

        # Add a save button to the window
        save_button = tk.Button(self.config_window, text="Save", command=self.save_configs)
        save_button.grid(row=self.row_num + 1, column=0, columnspan=2, pady=10)

        # Add a label to explain the different parameters
        add_level_instructions_par1 = tk.Label(self.config_window, text="Label of the y axis, ex : eV | kcal/mol")
        add_level_instructions_par1.grid(row=0, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par2 = tk.Label(self.config_window, text="Fontsize of the y axis label, ex : normal | bold")
        add_level_instructions_par2.grid(row=1, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par3 = tk.Label(self.config_window, text="Fontweight of the y axis label, ex : 12")
        add_level_instructions_par3.grid(row=2, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par4 = tk.Label(self.config_window, text="Fontsize of the y axis ticks, ex : 10")
        add_level_instructions_par4.grid(row=3, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par5 = tk.Label(self.config_window, text="Length of the y axis ticks, ex : 8")
        add_level_instructions_par5.grid(row=4, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par6 = tk.Label(self.config_window, text="Width of the y axis ticks, ex : 0.5")
        add_level_instructions_par6.grid(row=5, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par7 = tk.Label(self.config_window, text="Color of the level energy label, ex : black | #0000")
        add_level_instructions_par7.grid(row=6, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par8 = tk.Label(self.config_window, text="Fontsize of the level energy label, ex : 12")
        add_level_instructions_par8.grid(row=7, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par9 = tk.Label(self.config_window, text="Fontweigth of the level energy label, ex : normal | bold")
        add_level_instructions_par9.grid(row=8, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par10 = tk.Label(self.config_window, text="Off-set (in the y direction) of the level energy label, ex : 0.05")
        add_level_instructions_par10.grid(row=9, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par11 = tk.Label(self.config_window, text="Padding (in the x direction) of the level energy label, ex : 0.5")
        add_level_instructions_par11.grid(row=10, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par12 = tk.Label(self.config_window, text="Color of the level label, ex : black | #0000")
        add_level_instructions_par12.grid(row=11, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par13 = tk.Label(self.config_window, text="Fontsize of the level label, ex : 12")
        add_level_instructions_par13.grid(row=12, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par14 = tk.Label(self.config_window, text="Fontweigth of the level label, ex : normal | bold")
        add_level_instructions_par14.grid(row=13, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par15 = tk.Label(self.config_window, text="Off-set (in the y direction) of the energy label, ex : -0.15")
        add_level_instructions_par15.grid(row=14, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par16 = tk.Label(self.config_window, text="Padding (in the x direction) of the energy label, ex : 0.5")
        add_level_instructions_par16.grid(row=15, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par17 = tk.Label(self.config_window, text="If not define, color of the line level, ex : black")
        add_level_instructions_par17.grid(row=16, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par18 = tk.Label(self.config_window, text="Length of the level line, ex : 0.6")
        add_level_instructions_par18.grid(row=17, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par19 = tk.Label(self.config_window, text="Thickness of the level line, ex : 1.5")
        add_level_instructions_par19.grid(row=18, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par20 = tk.Label(self.config_window, text="If not define, color of the links line, ex : black")
        add_level_instructions_par20.grid(row=19, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par21 = tk.Label(self.config_window, text="Style of the link line, ex : --")
        add_level_instructions_par21.grid(row=20, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par22 = tk.Label(self.config_window, text="Thickness of the link line, ex : 1.5")
        add_level_instructions_par22.grid(row=21, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par23 = tk.Label(self.config_window, text="DPI of the plot, ex : 200 | 300 | 600")
        add_level_instructions_par23.grid(row=22, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par24 = tk.Label(self.config_window, text="Font of the plot, ex : sans")
        add_level_instructions_par24.grid(row=23, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par25 = tk.Label(self.config_window, text="Heigth of the plot, ex : 4")
        add_level_instructions_par25.grid(row=24, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par26 = tk.Label(self.config_window, text="Width of the plot, ex : 6")
        add_level_instructions_par26.grid(row=25, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par27 = tk.Label(self.config_window, text="Maximum of the y axis | slightly higher than the max energy")
        add_level_instructions_par27.grid(row=26, column=2, padx=(5,5),sticky="w")

        add_level_instructions_par28 = tk.Label(self.config_window, text="Minimum of the y axis | slightly lower than the min energy")
        add_level_instructions_par28.grid(row=27, column=2, padx=(5,5),sticky="w")

    # This function saves the changes made to the configuration parameters
    def save_configs(self):
        # Open the configs.py file for writing
        with open("configs.py", "w") as f:
            # Loop through the entries dictionary
            for key in configs.__dict__:
                # Skip any attributes that start with double underscores
                if not key.startswith("__"):
                    # Get the value entered in the Entry widget
                    value = self.entries[key].get()
                    # Try to convert the value to an integer
                    try:
                        value = int(value)
                    except ValueError:
                        # If the conversion to integer fails, try to convert to a float
                        try:
                            value = float(value)
                        except ValueError:
                            # If the conversion to float also fails, check if the value is not None
                            if value:
                                value = "'{}'".format(value)
                            else:
                                value = 'None'
                    # Set the attribute of the configs module to the new value
                    setattr(configs, key, value)
                    # Write the new attribute value to the configs.py file
                    f.write("{} = {}\n".format(key, value))

        # Show a success message to the user
        messagebox.showinfo("Success", "Configuration changes have been saved.")
        # Reload the configs module to ensure it has the latest changes
        importlib.reload(configs)

    def add_level_new_pathway(self, level_id, order, energy, label, color):
        self.diagram.add_level(int(level_id), int(order), float(energy), label, color, color)
        self.level_list.insert(tk.END, f"Level {level_id} - order: {order} - Energy: {energy} - Label: {label} - Color: {color}")
        

    def create_links_new_pathway(self, level1, level2, color):
        self.diagram.add_link(int(level1), int(level2), color)
        self.level_list2.insert(tk.END, f"Level {level1} - Level : {level2} - Color: {color}")

root = tk.Tk()
root.geometry("160x150")
root.iconbitmap(__location__+"\\logo_.ico")
my_gui = DiagramGUI(root)
root.mainloop()
