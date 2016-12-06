import random, sys, time

typing_speed = 120

def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10.0/typing_speed)

def print_code(str):
	print('\n\x1b[7;33;40m\"' + str + '\"\x1b[0m\n');

print_slow("Welcome to Python Tutor!\n");
print_slow("Python is very friendly and can help you solve lots of problems!\n\n");

print_slow("You can start running python commands by opening a new ");
print_slow("terminal and typing ");
print_code("python");
print_slow("Why don't you go do that now\n\n");

time.sleep(10);

print_slow("Now you've got a personal python interpretor that will run the commands ");
print_slow("you type and remember any variables that you store\n\n");

time.sleep(.5);

print_slow("If ever you want to leave the python interpretor, just type ");
print_code("exit()");

time.sleep(1);

print_slow("Let's start by learning about variables - ");
print_slow("But first, what is a variable?\nA variable is a memory box ");
print_slow("where the computer holds onto some piece of information. For example, a number. ");
print_slow("Variables are reffered to by a unique name, like x, y, num1, or other descriptors.\n");

time.sleep(1);

print_slow("In order to store a variable, simply type a name for it and set it equal to some value. ");
print_slow("Try typing:\n");

print_code("x = 8");
x = 8;

time.sleep(3);

print_slow("\nNow the computer will remember that x is equal to 8 for us.\n");
print_slow("If you want to see what the value of your variable is, you can call print on it. ");
print_slow("The print function will print out the value of a variable. ");
print_slow("Why don't you go ahead and try it now. Type ");
print_code("print(x)");

time.sleep(5);

print_slow("\nOne of the most essential tools of computer science is basic arithmetic. ");
print_slow("Addition, subtraction, multiplication, and division - as you prboably ");
print_slow("know, these operations are represtented by +, -, *, and /\n\n");

time.sleep(3);

print_slow("You can perform these operation on numbers yourself or on variables ");
print_slow("that you've already stored in the computer.\n");

print_slow("\nWhat do you get when you try ");
print_code("x*27");
result = int(input());

while result != 216:
	print_slow("Oops, it looks like you may have had some issues.\n");
	print_slow("Make sure that x = 8 and then try again: ");
	result = int(input());

print_slow("By now, you've got multiplication down, now play around with the other operations!\n\n");

#Add in pow and sqrt?
time.sleep(1);

print_slow("You may also want to use exponents, in order to use exponents, ");
print_slow("instead of using ^, to get exponents, you use **, for example, ");
print_code("4**2");
print_slow("is 16\n\n");

print_slow("In order to take the sqrt of a number, first you need to run the command: ");
print_code("from math import sqrt");
print_slow("This tells python how to take the sqrt of a number. ");
print_slow("You can then take the squareroot by running ");
print_code("sqrt(16)");
print_slow("As you may have guessed, this will give you 4.\n\n");

print_slow("At this point you should have all the skills that you need in order to solve for x in your equations! Feel free to scroll back and look at the different tips for python, play around some more with the interpreter, or solve some math problems!");
print_slow("Now that you know some basic math, let's see if we can use it to draw and control turtles! Press enter to continue when you're ready.\n")
garbage = raw_input()
print_slow("\nLet's make a turtle! In order to tell your computer how to make a turtle, you have to type ")
print_code("import turtle")
print_slow(". Try it now! Press enter to continue when you're done.\n")
garbage = raw_input()
print_slow("\nSweet! Now let's make a new turtle. Think of a name for your turtle! You can name it whatever you want. I'm going to name mine Tina.\n")
print_slow("Once you've thought of a name for your turtle, you can create it! I'm going to create mine by typing ")
print_code("tina = turtle.Turtle()")
print_slow(" . This creates a Turtle OBJECT. An object is something that can be modified by different built-in commands. From now on, any time you see me use 'tina' in code, you should replace it with your turtle's name! Press enter to continue when you've created a turtle object.\n")
garbage = raw_input()
print_slow("\nNow, you should have seen a white screen pop up with an arrow in the middle. This arrow is your turtle! 'Tutorial,' you may be saying, 'what in the world are you talking about? This is an ARROW, not a TURTLE!'\n")
print_slow("You have to make it a turtle shape! This is an example of MODIFYING an object! To modify your turtle type in ")
print_code("tina.shape('turtle')")
time.sleep(5)
print_slow("\nNow your turtle should look like a turtle. Now it's time to draw!\n")
print_slow("Type in the following to move forward:\n")
print_code("tina.foward(100)")
time.sleep(5)
print_slow("This makes your turtle move 100 steps foward!\n")
print_slow("\nType in the following to make Tina turn right:\n")
print_code("tina.right(90)")
time.sleep(5)
print_slow("This makes your turtle turn 90 degrees right! Now that you know how to make your turtle turn right and go forward, you can make it draw a square. Give it a shot!\n")
print_slow("How can you make your turtle turn left?\n")
print_slow("Press enter when you're ready to make your turtle draw more shapes!\n")
garbage = raw_input()
print_slow("\nYou're now a turn-master! I guess you can call your turtle 'Tina Turner' now...\n")
print_slow("\nThat was a bad joke for old people! Sorry. Anyway, to make your turtle draw a circle, type \n")
print_code("tina.circle(50)")
time.sleep(5)
print_slow("What do you think that number means? Experiment with different numbers! Press enter when you're ready to continue.\n")
garbage = raw_input()
print_slow("\nNow let's draw a half circle! Type in:\n")
print_code("tina.circle(50,180)")
time.sleep(5)
print_slow("\nWhat do you think that second number means? Try experimenting with both numbers! Press enter when you want to continue.\n")
garbage = raw_input()
print_slow("Now let's try changing your turtle's color! Type in:\n")
print_code("tina.color('green')")
time.sleep(5)
print_slow("\nYour turtle should be green now! But what if you want to change the color of the pen your turtle draws with? Try this:\n")
print_code("tina.pencolor('blue')")
time.sleep(5)
print_slow("\nYou should now have a green turtle and a blue pen! Mess around with colors to find ones that you like! Press enter when you're ready to continue.\n")
garbage = raw_input()
print_slow("\nCongratulations! You've reached the end of this tutorial. But there's so much more you can do with turtles!!!\n")
print_slow("All of the commands we gave our turtle were called 'member functions'. Any turtle objects can access them! You can see a list of turtle member functions right here:\n")
print("docs.python.org/3.1/library/turtle.html#turtle-methods\n")
print_slow("Just click on each function to reveal how to use it!\n")
print_slow("Some good challenge activities might be:\n")
print("draw a stick figure!\ndraw an equilateral triangle!\nnow an isoceles one!\nchange the turtle's shape to a square!\nmove the turtle without using the pen!\n")
print_slow("Thanks for participating in the hour of code!\n")
