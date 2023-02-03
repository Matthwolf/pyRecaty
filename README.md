## pyRecaty
A simple and felxible python script to plot multiple chemical reactive pahtways. It also contains a graphical interface (GUI) script if prefered. It was created from the inital idea of @MFTabriz.
<img src="https://user-images.githubusercontent.com/60096547/216609453-828240a7-210d-49d5-9c76-6ee1c8950496.jpg" width="200" alt="centered image"/>

## Requirements

You must have an environement with Matplotlib (tkinter for the interface). In the reposotery the environment.yml allows to create an environement with Matplotlib 3.6.2. 

## Customization

They are many parameters in the configs.py file that can be tune to modify the diagram. At the end of the README.md file there is a explanation for all the different parameters. 

## Example 

```python

from recaty import Diagram

#Example usage:

#Initialization
diagram = Diagram()

#Add the level to the diagram, precising the ID allowing to link the level, the order (positoning on the x axis), the energy and the label
diagram.add_level(level_id=0, order=1, energy=0, label="A")
diagram.add_level(level_id=1, order=2, energy=2, label="TS")
diagram.add_level(level_id=2, order=3, energy=1, label="B")
diagram.add_level(level_id=9, order=4, energy=1.1, label="C")
diagram.add_level(level_id=3, order=1, energy=1.5, label="A2", line_color="red")
diagram.add_level(level_id=4, order=2, energy=2.5, label="TS2", line_color="red")
diagram.add_level(level_id=5, order=3, energy=0.5, label="B2", line_color="red")
diagram.add_level(level_id=6, order=1, energy=0.5, label="A3", line_color="green")
diagram.add_level(level_id=7, order=2, energy=1.5, label="TS3", line_color="green")
diagram.add_level(level_id=8, order=3, energy=0.8, label="B3", line_color="green")

#Add the link using the ID of each level
diagram.add_link(0, 1)
diagram.add_link(1, 2)
diagram.add_link(2, 9)
diagram.add_link(3, 4, color="red")
diagram.add_link(4, 5, color="red")
diagram.add_link(6, 7, color="green")
diagram.add_link(7, 8, color="green")
diagram.add_link(3, 4, color="red")
diagram.add_link(4, 5, color="red")

#plot the Diagram and it save it in a "diagram.png" file
diagram.plot()
```
![diagram](https://user-images.githubusercontent.com/60096547/216622782-e3b33e9c-ee3a-49fe-b26c-f4e5daecbda8.png)

## pyRecaty - GUI

For fun, and for people non familiar with python usage, I create a GUI interface for recaty (It is still necessary to install Python 3.10.+) which give the user four different buttons. The two first allow to add level indicating the level, order, enrgy, label, color (Add level), and adding links, indicating the ID of each level. The user can also modify the parameters inside the configs.py file using the configurations button that will modify the plot. The plot button, will display the diagram with the different level and links.   

![recatygui](https://user-images.githubusercontent.com/60096547/216627703-03604a12-c70f-463e-a208-97cf26a794b2.png)


## configs.py Parameters

This file contains the different parameters allowing to modify the diagram, here it is given simple description of each parameter :

| Parameter | Description |
|-----------|-------------|
| plot_height | Heigth of the plot |
| plot_width | Width of the plot |
| plot_dpi | DPI of the plot |
| plot_font | Font of the plot |
| y_min | Minimum of the y axis |
| y_max | Maximum of the y axis |
| energy_axis_label | Label of the y axis |
| energy_axis_label_fontsize | Fontsize of the y axis label |
| energy_axis_label_fontweight | Fontweight of the y axis label |
| energy_axis_ticks_fontsize | Fontsize of the y axis ticks |
| energy_axis_ticks_width | Width of the y axis ticks |
| energy_axis_ticks_length | Length of the y axis ticks |
| energy_tags_color | Color of the level energy label |
| energy_tags_fontsize | Fontsize of the level energy label |
| energy_tags_fontweight | Fontweigth of the level energy label |
| energy_tags_offset | Off-set (in the y direction) of the level energy label |
| energy_tags_padding | Padding (in the x direction) of the level energy label |
| level_labels_color | Color of the level label |
| level_labels_fontsize | Fontsize of the level label |
| level_labels_fontweight | Fontweigth of the level label |
| level_labels_offset | Off-set (in the y direction) of the energy label |
| level_labels_padding | Padding (in the x direction) of the energy label |
| level_lines_color | If not define, color of the line level |
| level_lines_thickness | Thickness of the level line |
| level_lines_length | Length of the level line |
| links_color | If not define, color of the links line |
| links_width | Thickness of the link line |
| links_style | Style of the link line |

