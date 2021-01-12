from Helth_Management_System import Helth_Management_System

print(
"""
*******HELP*******
  *NAME
  	Harry : 101
  	Rohan : 102
  	Hammad: 103

  * WORK
  	Diet   : 'd'
  	Workout: 'w'
  	Retrive: 'r'
"""
)

name = input('What is your NAME: ')
work = input('What WORK do your want \nme to do: ')
if work.lower() == 'd':
	work_done = input('What did you have in your meal: ')
	print('  Your meal has been saved!')
elif work.lower() == 'w':
	work_done = input('What workout you have done: ')
	print('  Your workout has been saved!')
elif work.lower() == 'r':
	work_done = ""
def current_time():
	import datetime
	time = datetime.datetime.now()
	return time

Helth_Management_System(name, current_time(),work, work_done).main()
