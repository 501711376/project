

CS Project
Tianhao Dai
Mr. Aronson
17/11/2017

     Big picture: 
     I want to write a program that helps spaceships calculate the different distance its has to different planets. and also, after the spaceship reaches a planet, the program also has option to continue calculating the distance to another planet if it’s not at its destination yet, in the future, I want to furthermore develop on this program by adding function that could help the spaceship find a route that’s safest and fastest at the same time. for the round 2 of the project, I plan to combine my distance calculating project with a pygame similiar to asteroid. I will first put images of planets on the game screen, and have a small triangle representing the location of the user. Then when user input the name of the planet, the program will not only calculate the distance between planets, but also, the small trigangle will automatically move the image of the project.

     1st steps: the calculation of distance has become a reality in my code. I mostly use If and Elif arguments as well as multiple functions to build up this program. it contains knowledge that we haven’t learned yet such as input and calling of 3-D coordinates. Luckily, with help of teacher, this project is completely doable.
      

  
  Application C:
       In the universe, there are all kinds of events which could get in the way of the spaceship’s route, such as star explosion, space trash, invasion of alien ships etc. With this program, just by inputting the possibilities of different events, and run it, you could get the safest route based on the calculations.

      For example, if you want to travel in the solar system, this program needs first based on the map of the solar system and all the risks that are already known. And also other things what are  important are your current location, time, and where is your final destination. There are infinite amounts of possibilities of routes first. By running this program, based on the information that’s already known, the program also eliminates infinite of route until it finally finds out the optimal route.
  Information about unexpected events, needs to include things like the 3D - coordinates, lasting time, and possibility of occurrence etc.

round 2: for the round 2 of the project, I plan to combine my distance calculating project with a pygame similiar to asteroid. I will first put images of planets on the game screen, and have a small triangle representing the location of the user. Then when user input the name of the planet, the program will not only calculate the distance between planets, but also, the small trigangle will automatically move the image of the project.

Test:
1. run the program, see if the quittable screen will pop up.
2. run the program.if if there is images of planet,
3. examine if the result comes out is correct.
3. if there is error, start dubugging.

Revisions to plan:
because of only limited options of destinations are provided, user might input some locations that are not included in the codes, so, I use elif argument let the program to re-ask for location when use input somewhere that’s not included.
In addition to that, I also provide multiple choices for the journey plan, for example, you can go to planet Mars first, then go another planet that you want to, and then, the program will help you calculate the lengths of both routes.

Next Step: 
I want to combine my project with Pygame. The Pygame should be like the game asteroid. I will put different images of planets on the game screen. and user's location will be represented by a triangle. when the user input a destination, the triangle will automatically move to the corresponding image of the planet.

test plan:
1. the locations of the images of planets are indicated by coordinates.
2. Import Pygame.
3. download images of planets from internet.
4. run the program, see if the quittable screen will pop up.
5.input the coordinates, see if the triangle will move to the image of the corresponding planet.

Final Project Update 5/27/2018:

Concept: I want to design a program for the purpose of spaceship navigation, the inspiration is from the TV show Star Trek where gigantic spaceships can move to any location in the universe in the blink of an eye. I want to optimize the route so that the spaceship can move even faster. The thing that's original in my mind is that I want to make a map of solar system first, and map out the route of the ship by hand before the space ship starts flying.

Current State: I have imported the images of spaceship, Mars, Pavos, and Venus on a white background map, where you can move the spaceship around using keyboard. The issue of it is that it can't calculate and map out the optimal route, because you can only use keyboard to move the ship. The way my code works is easy, you just use "up" "down" "left" and "right" keys to move the spaceship around freely. And for the second model file "Star Trek Future Model 2.py", user could move the spaceship around by simply clicking the map, and the trace of the spaceship's movement is also shown on the map.

Future Possibility: my project now is still pretty sketchy - literally. If I can work on this as a profession in the future, I think I will need to create a 3D Model of the universe first, and import all the data of the planets and celestial bodies that are known, such as location, size etc. And then, based on the already known data, I can use certain algorithm that I developed to calculate the optimal route.

Near Future Plan: In the near future, I want to combine the characteristics of my "project 3.py" with those of "Star Trek Future Model 2.py" so that the user could map out the route by simply clicking the map, and with 2D images of different planets, user knows where to avoid to click, thus making a better route.
