from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

#################################################

##               ##
## START OF VIEW ##
##               ##

class View:
	def __init__(self):
		self.build_window()
	def build_window(self):
		#Fonts
		FONT1 = 'Bahnschrift SemiBold'
		FONT2 = 'Bahnschrift SemiLight'

		#Colours
		BG = 'white'
		PRIMARY = '#45a0f5'

		class Data:
			def __init__(self):
				pass
			def find(self, directory):
				self.directory = directory
				with open(directory, 'r') as file:
					content = file.read().splitlines()
					file.close()
				data=[]
				for line in content:
					data.append(float(line))
				return data
			def find_date(self, directory):
				self.directory = directory
				with open(directory, 'r') as file:
					content = file.read().splitlines()
					file.close()
				data=[]
				for line in content:
					data.append(line)
				return data
		
		
		get_data = Data()

		data_fields = ['UpperArm', 'LowerArm', 'UpperLeg', 'LowerLeg', 'Chest', 'Shoulder']

		fig, ax = plt.subplots()
		ax.grid(b=None, which='major', axis='both')
		fig.canvas.set_window_title('MyMuscle | View Progress')

		ax.set_xlabel('Date Measured')
		ax.set_ylabel('Growth (cm)')

		days = get_data.find_date(f'data/dates.txt')

		for item in data_fields:
			growth = get_data.find(f'data/{item.lower()}_data.txt')
			ax.plot(days, growth, label=item)

		ax.legend()
		plt.show()

##             ##
## END OF VIEW ##
##             ##

###########################################################################

##              ##
## START OF ADD ##
##              ##

class Add:
	def __init__(self):
		top = Toplevel()
		self.top = top
		

		self.build_window()
	def submit_date(self):
		date = self.get_date_entry.get()
		if date == '':
			messagebox.showerror('Error', 'Please Enter A Date')
		else:
			entry1 = self.entry1.get()
			entry2 = self.entry2.get()
			entry3 = self.entry3.get()
			entry4 = self.entry4.get()
			entry5 = self.entry5.get()
			entry6 = self.entry6.get()

			with open('data/dates.txt', 'a') as file:
				file.write(str('\n' + date))
				file.close()

			with open('data/chest_data.txt', 'a') as file:
				file.write(str('\n' + entry1))
				file.close()

			with open('data/shoulder_data.txt', 'a') as file:
				file.write(str('\n' + entry2))
				file.close()

			with open('data/upperarm_data.txt', 'a') as file:
				file.write(str('\n' + entry3))
				file.close()

			with open('data/lowerarm_data.txt', 'a') as file:
				file.write(str('\n' + entry4))
				file.close()

			with open('data/upperleg_data.txt', 'a') as file:
				file.write(str('\n' + entry5))
				file.close()

			with open('data/lowerleg_data.txt', 'a') as file:
				file.write(str('\n' + entry6))
				file.close()




	def submit(self):
		entry1 = self.entry1.get()
		entry2 = self.entry2.get()
		entry3 = self.entry3.get()
		entry4 = self.entry4.get()
		entry5 = self.entry5.get()
		entry6 = self.entry6.get()
		
		#Fonts
		FONT1 = 'Bahnschrift SemiBold'
		FONT2 = 'Bahnschrift SemiLight'

		#Colours
		BG = 'white'
		PRIMARY = '#45a0f5'

		date_window=Toplevel()
		self.date_window = date_window
		date_window.configure(bg='white')
		date_window.geometry('200x150')

		get_date_label = Label(date_window, text='Enter Date', fg=PRIMARY, bg=BG, font=(FONT1, 17))
		get_date_label.pack()

		self.get_date_entry = Entry(date_window, fg=BG, bg=PRIMARY, font=(FONT1, 15), width=10, relief='flat')
		self.get_date_entry.pack(pady=15)

		get_date_button = Button(date_window, text='Enter', fg=BG, bg=PRIMARY, font=(FONT1, 15), width=10, relief='flat',
			command=self.submit_date)
		get_date_button.pack(pady=15)

		date_window.mainloop()

	def check_data(self, event=None):
			entry1 = self.entry1.get()
			entry2 = self.entry2.get()
			entry3 = self.entry3.get()
			entry4 = self.entry4.get()
			entry5 = self.entry5.get()
			entry6 = self.entry6.get()

			if len(entry1) == 0 or len(entry2) == 0 or len(entry3) == 0 or len(entry4) == 0 or len(entry5) == 0 or len(entry6) == 0:
				messagebox.showerror('Error', 'Please Fill In All Fields')

			else:
				self.submit()
				

	def build_window(self):
		top = self.top

		top.bind('<Return>', self.check_data)

		#Fonts
		FONT1 = 'Bahnschrift SemiBold'
		FONT2 = 'Bahnschrift SemiLight'

		#Colours
		BG = 'white'
		PRIMARY = '#45a0f5'

		top.geometry('310x400')
		top.configure(bg='white')
		top.title('MyMuscle | Add Progress')

		title_label = Label(top, text='MyMuscle', fg=PRIMARY, bg=BG, font=(FONT1, 35))
		title_label.place(relx=0.15)

		subtitle_label = Label(top, text='Add Progress', fg='black', bg=BG, font=('calibri', 10))
		subtitle_label.place(rely=0.16, relx=0.38)

		data_frame = Frame(top, bg=PRIMARY, bd=0)
		data_frame.place(relx=0.08, rely=0.22, relwidth=0.85, relheight=0.62)

		submit_button = Button(top, text='Submit', bd=0, relief='flat', font=(FONT1, 12, 'bold'), bg=PRIMARY, fg=BG,
			command=self.check_data)
		submit_button.place(relx=0.35, rely=0.87, relheight=0.1, relwidth=0.3)

		#chest
		entry1_label = Label(data_frame, text='Chest', fg=BG, bg=PRIMARY, font=('calibri', 10, 'bold'))
		entry1_label.pack()

		self.entry1 = Entry(data_frame, fg=PRIMARY, bg=BG, font=('calibri', 10), relief='flat', width=5)
		self.entry1.pack()

		#shoulders
		entry2_label = Label(data_frame, text='Shoulder To Shoulder', fg=BG, bg=PRIMARY, font=('calibri', 10, 'bold'))
		entry2_label.pack()

		self.entry2 = Entry(data_frame, fg=PRIMARY, bg=BG, font=('calibri', 10), relief='flat', width=5)
		self.entry2.pack()

		#upper arm
		entry3_label = Label(data_frame, text='Upper Arm', fg=BG, bg=PRIMARY, font=('calibri', 10, 'bold'))
		entry3_label.pack()

		self.entry3 = Entry(data_frame, fg=PRIMARY, bg=BG, font=('calibri', 10), relief='flat', width=5)
		self.entry3.pack()

		#lower arm
		entry4_label = Label(data_frame, text='Lower Arm', fg=BG, bg=PRIMARY, font=('calibri', 10, 'bold'))
		entry4_label.pack()

		self.entry4 = Entry(data_frame, fg=PRIMARY, bg=BG, font=('calibri', 10), relief='flat', width=5)
		self.entry4.pack()

		#upper leg
		entry5_label = Label(data_frame, text='Upper Leg', fg=BG, bg=PRIMARY, font=('calibri', 10, 'bold'))
		entry5_label.pack()

		self.entry5 = Entry(data_frame, fg=PRIMARY, bg=BG, font=('calibri', 10), relief='flat', width=5)
		self.entry5.pack()

		#lower leg
		entry6_label = Label(data_frame, text='Lower Leg', fg=BG, bg=PRIMARY, font=('calibri', 10, 'bold'))
		entry6_label.pack()

		self.entry6 = Entry(data_frame, fg=PRIMARY, bg=BG, font=('calibri', 10), relief='flat', width=5)
		self.entry6.pack()

		top.mainloop()


##            ##
## END OF ADD ##
##            ##

###########################################

class OptionWindow:
	def __init__(self, root):
		self.build_window()

	def Button1_press(self):
		start_add_window = Add()

	def Button2_press(self):
		start_view_window = View()
		

	def build_window(self):
		#Fonts
		FONT1 = 'Bahnschrift SemiBold'
		FONT2 = 'Bahnschrift SemiLight'

		#Colours
		BG = 'white'
		PRIMARY = '#45a0f5'

		root.geometry('300x250')
		root.title('MyMuscle | Home ')

		root.configure(bg='white')
		root.iconbitmap('img/icon.ico')

		title_label = Label(root, text='MyMuscle', bg=BG, fg=PRIMARY, font=(FONT1, 25, 'bold'))
		title_label.pack()

		blue_frame = Frame(root, bg=PRIMARY, bd=0)
		blue_frame.place(relx=0.15, rely=0.25, relwidth=0.7, relheight=0.6)

		frame_title = Label(blue_frame, text='Select An Option:', bg=PRIMARY, fg=BG, font=(FONT2, 12))
		frame_title.place(relx=0.19)

		button1 = Button(blue_frame, text='Add Progress', bg=BG, fg=PRIMARY, relief='flat', font=(FONT2, 10), 
			command=self.Button1_press)
		button1.place(rely=0.4, relx=0.033)

		button2 = Button(blue_frame, text='View Progress', bg=BG, fg=PRIMARY, relief='flat', font=(FONT2, 10), 
			command=self.Button2_press)
		button2.place(rely=0.4, relx=0.5)


##############################

root=Tk()
newWindow = OptionWindow(root)
root.mainloop()


