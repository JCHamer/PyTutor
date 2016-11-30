import random, sys, time

typing_speed = 100

def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10.0/typing_speed)

def print_code(str):
	print('\x1b[7;33;40m' + str + '\x1b[0m');

print_slow("Welcome to Python Tutor!\n");
print_slow("Python is very friendly and can help you solve lots of problems!\n\n");

print_slow("You can start running python commands by opening a new ");
print_slow("terminal and typing ");
print_code("\"python\"");
print_slow("Why don't you go do that now\n\n");

time.sleep(10);

print_slow("Now you've got a personal python interpretor that will run the commands ");
print_slow("you type and remember any variables that you store\n\n");

time.sleep(.5);

print_slow("If ever you want to leave the python interpretor, just type ");
print_code("\"exit()\"");

time.sleep(1);

print_slow("\nLet's start by learning about variables - ");
print_slow("But first, what is a variable?\nA variable is a memory box ");
print_slow("where the computer holds onto some piece of information. For example, a number. ");
print_slow("Variables are reffered to by a unique name, like x, y, num1, or other descriptors.\n");

time.sleep(1);

print_slow("In order to store a variable, simply type a name for it and set it equal to some value. ");
print_slow("Try typing:\n");

print_code("\"x = 8\"");
x = 8;

time.sleep(3);

print_slow("\nNow the computer will remember that x is equal to 8 for us.\n");
print_slow("If you want to see what the value of your variable is, you can call print on it. ");
print_slow("The print function will print out the value of a variable. ");
print_slow("Why don't you go ahead and try it now. Type ");
print_code("\"print(x)\"");

time.sleep(5);

print_slow("\n\nOne of the most essential tools of computer science is basic arithmetic. ");
print_slow("Addition, subtraction, multiplication, and division - as you prboably ");
print_slow("know, these operations are represtented by +, -, *, and /\n\n");

time.sleep(3);

print_slow("You can perform these operation on numbers yourself or on variables ");
print_slow("that you've already stored in the computer.\n");

print_slow("\nWhat do you get when you try ");
print_code("\"x*27\"");
result = int(input());

while result != 216:
	print_slow("Oops, it looks like you may have had some issues.\n");
	print_slow("Make sure that x = 8 and then try again: ");
	result = int(input());

print_slow("By now, you've got multiplication down, now play around with the other operations!\n\n");

#Add in pow and sqrt?

print("At this point you should have all the skills that you need in order to solve for x in your equations! Feel free to scroll back and look at the different tips for python, play around some more with the interpreter, solve some math problems, or raise your hand if you need help!");
