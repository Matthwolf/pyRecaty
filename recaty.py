"""
reaction.py
Python script for drawing reaction pathways
Author: Matthwolf@github
License: GPL v3+
See example.py for a simple example of the usage
"""

import matplotlib.pyplot as plt
from collections import namedtuple
import configs
from pathlib import Path
import os

#Find the correct path for the icon and image

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

print(__location__)

# Define namedtuples to store information about levels and links
Level = namedtuple("Level", [ "level_id", "order","energy", "label", "line_color", "label_color"])
Link = namedtuple("Link", ["level_id1", "level_id2", "color", "width", "style"])

# Definition of the Diagram class
class Diagram:
    def __init__(self):
        self.levels = [] # list to store levels
        self.links = [] # list to store links

    # Function to add level on the diagram
    def add_level(self, level_id, order, energy, label, line_color=None, label_color=None):
        """
        Add a new level to the diagram
            ID : give a number to the level to make the link
            order : to determine the x axis postion of the level
            energy : Energy of the new level
            label : tag for the new level
            line_color : color of the level line
            label_color : color of the level label
        """

        if not order:
            order = len(self.levels)
        if not line_color:
            line_color = configs.level_lines_color
        if not label_color:
            label_color = configs.level_labels_color
        self.levels.append(Level(level_id, order, energy, label, line_color, label_color))
 
    # Function to add link between level on the diagram
    def add_link(self, level_id1, level_id2, color=None, width=None, style=None):
        """
        Add a new link between levels in the diagram
            level_id1 : ID of the first level
            level_id2 : ID of the second level
            color : color of the link
            width : width of the link
            style : style of the link
        """
        if not color:
            color = configs.links_color
        if not width:
            width = configs.links_width
        if not style:
            style = configs.links_style
        self.links.append(Link(level_id1, level_id2, color, width, style))

    # Function to plot and save the diagram
    def plot(self):
        """
        Plot the diagram using the settings in the configs dictionary
        """
        # Set plot dimensions
        plt.figure(figsize=(configs.plot_width, configs.plot_height), dpi=configs.plot_dpi)
        plt.rc("font", **{"serif": [configs.plot_font]})
        # remove axis
        plt.rcParams['axes.spines.right'] = False
        plt.rcParams['axes.spines.top'] = False
        plt.rcParams['axes.spines.bottom'] = False
        plt.ylabel(
            configs.energy_axis_label,
            fontweight=configs.energy_axis_label_fontweight,
            size=configs.energy_axis_label_fontsize,
        )
        plt.tick_params(
            width=configs.energy_axis_ticks_width,
            length=configs.energy_axis_ticks_length,
            labelsize=configs.energy_axis_ticks_fontsize,
        )
        
        # Sort levels by order
        self.levels = sorted(self.levels, key=lambda x: x.order)
        
        for level in self.levels:
            level_id, order, energy, label, line_color, label_color = level
            plt.hlines(energy, xmin=order+0.5-(float(configs.level_lines_length))/2, xmax=order+0.5+(float(configs.level_lines_length))/2, color=line_color, linewidth=configs.level_lines_thickness)
            plt.text(order+configs.level_labels_padding, energy+configs.level_labels_offset, label, fontsize=configs.level_labels_fontsize, color=label_color, ha='center')
            plt.text(order+configs.energy_tags_padding, energy+configs.energy_tags_offset, str(energy), fontsize=configs.energy_tags_fontsize, color=configs.energy_tags_color, ha='center')

        for link in self.links:
            level_id1, level_id2, color, width, style = link
            level1 = next(level for level in self.levels if level[0] == level_id1)
            level2 = next(level for level in self.levels if level[0] == level_id2)
            order1, energy1 = level1[1], level1[2]
            order2, energy2 = level2[1], level2[2]
            plt.plot([order1+0.8, order2+0.2], [energy1, energy2], color=color, linewidth=width, linestyle=style)
                    
        # remove x-axis
        plt.tight_layout()
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.ylabel(configs.energy_axis_label, fontsize=configs.energy_axis_label_fontsize, fontweight=configs.energy_axis_label_fontweight)
        plt.ylim(configs.y_min, configs.y_max)
        plt.savefig(__location__+"\\diagram.png")
        plt.show()

