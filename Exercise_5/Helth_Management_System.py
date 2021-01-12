class Helth_Management_System:
	"""This class has all requirements for the program"""
	
	def __init__(self,name,time,work,work_done=""):
		self.work_done = work_done
		self.name = int(name)
		self.time = str(time)
		self.work = work
	
	def main(self):
		x = '['+self.time[:-7]+']' #This is time
		file_hrd='harry_diet.txt'
		file_hrw='harry_exercise.txt'

		file_hdd='hammad_diet.txt'
		file_hdw='hammad_exercise.txt'
		
		file_rd='rohan_diet.txt'
		file_rw='rohan_exercise.txt'
				
		if self.name == 101:
			if self.work.lower() == 'd':
				with open(file_hrd, "a") as storage:
					storage.write(x + ' ' + self.work_done + '\n')
			elif self.work.lower() == 'w':
				with open(file_hrw, "a") as storage:
					storage.write(x + ' ' + self.work_done + '\n')
			elif self.work.lower() == 'r':
				with open(file_hrd) as storage:
					print('\tHarry Diet History: \n' + storage.read())
				with open(file_hrw) as storage:
					print('\n\tHarry Workout Done: \n' + storage.read())

		elif self.name == 102:
			if self.work.lower() == 'd':
				with open(file_hdd, "a") as storage:
					storage.write(x + ' ' + self.work_done + '\n')
			elif self.work.lower() == 'w':
				with open(file_hdw, "a") as storage:
					storage.write(x + ' ' + self.work_done + '\n')
			else:
				with open(file_hdd) as storage:
					print('\tHammad Diet History: \n' + storage.read())
				with open(file_hdw) as storage:
					print('\n\tHammad Workout Done: \n' + storage.read())

		elif self.name == 103:
			if self.work.lower() == 'd':
				with open(file_rd, "a") as storage:
					storage.write(x + ' ' + self.work_done + '\n')
			elif self.work.lower() == 'w':
				with open(file_rw, "a") as storage:
					storage.write(x + ' ' + self.work_done + '\n')
			else:
				with open(file_rd) as storage:
					print('\tRohan Diet History: \n' + storage.read())
				with open(file_rw) as storage:
					print('\n\tRohan Workout Done: \n' + storage.read())
