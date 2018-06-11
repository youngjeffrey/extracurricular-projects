# extracurricular-projects
Projects done outside of school

_Color Clicker Game_

The Color Clicker is a game I am currently working on where the player is presented with a grid of red squares
and has to pick the odd one out. The higher the level, the more similar the odd square's color will be to that
of red. The code uses Tkinter as the frame for the game and relies on method calls to perform the actions. 
I plan on implementing the color change for the odd square, adding a timer, and improving the aesthetics
in the near future. 

_Interactive Dictionary_

The Interactive Dictionary is a Python based application where the user can search up and word, press 'Define', and
the definition of the word will be given. If the user mispelled the word, the app will give a suggestion of a similar
word. The program involves parsing of Tkinter, parsing of JSON files, and difflib to compare word similarities. In 
order to run it, run App2.py in SRC. 

_Mapping USA_

Mapping USA is a Python based program that maps out geographic locations within United States like cities and volcanoes
and saves it to a .html file. It also color codes the countries, cities, and volcanoes based on population and height 
respectively. The program uses Pandas to read and parse .csv and .txt files and uses folium to draw out the map. 
In order to run the program, click on Maps.html. 

_Slither_

Slither is the first game I created using Pygame. It is a variation of the classical game Snake. In this game the objective
is for the snake to eat as many apples as possible without running into the edge, itself, and the rocks. To make this game 
more challenging, I added rocks to the game that act as barriers and spawn as the player's score gets higher. In addition 
I incremented the frames per second of the snake movement linearly with jumps every time the length the snake increases by 6, 
this increases the speed of the snake. There is a lot of event handling such as responsiveness to the keyboard clicks and
collisions between the snake and various objects.The X and Y coordinates of each object were set up so that no two objects 
(apples, rocks) would be in the exact same position. The setup.py uses cx_Freeze to convert the Python program into an executable.
In the future I plan on adding a more efficient way of spawning rocks so that they do not spawn right next to the snake head. 
Screenshots of the game are in the Screenshots folder. 

