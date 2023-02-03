## pyRecaty
A simple and felxible python script to plot multiple chemical reactive pahtways. It also contains a graphical interface (GUI) script if prefered. It was created from the inital idea of @MFTabriz.
<img src="https://user-images.githubusercontent.com/60096547/216609453-828240a7-210d-49d5-9c76-6ee1c8950496.jpg" width="200" alt="centered image"/>

## Requirements

## Customization

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

## configs.py Parameters

This file contains the different parameters allowing to modify the diagram, here it is given simple description of each parameter :
