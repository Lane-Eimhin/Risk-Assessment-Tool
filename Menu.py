from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.title('Quantitive Risk Assessment Tool')
root.iconbitmap('C:/gui/RAexamplelogo.ico')
root.geometry('600x600')


#setting dimensions
min_width = 50
max_width = 200

#increasing width of the frame
cur_width = min_width 
expanded = False

def expand():
	global cur_width, expanded
	cur_width += 10 #increase width by 10
	rep = root.after(5,expand) #repeat ever 5 ms
	frame.config(width=cur_width)#changes width to the new size
	if cur_width >= max_width:
		expanded = True #frame is expanded
		root.after_cancel(rep) #stop repeating the function
		fill()

def contract():
	global cur_width, expanded
	cur_width -= 10 #reduce width by 10
	rep = root.after(5,contract) #repeat ever 5 ms
	frame.config(width=cur_width)#changes width to the new size
	if cur_width <= max_width:
		expanded = False #frame is contracted
		root.after_cancel(rep) #stop repeating the function
		fill()

def fill():
	if expanded: #If the frame is expanded show a text and remove the image
		info_b.config(text='information',image = '',font=(0,21))
		home_b.config(text='Dashboard',image = '',font=(0,21))
		add_b.config(text='Add Session',image = '',font=(0,21))
		save_b.config(text='Save Session',image = '',font=(0,21))

	else: #bring the images back
		info_b.config(image=info, font=(0,21))
		home_b.config(image=home, font=(0,21))
		add_b.config(image=AddSession, font=(0,21))
		save_b.config(image=SaveSession, font=(0,21))

#defining the images to be shown and resize them

#info = PhotoImage(file='c:/gui/info.png')
#home = PhotoImage(file='c:/gui/home.png')
#AddSession = PhotoImage(file='c:/gui/AddSession.png')
#SaveSession = PhotoImage(file='c:/gui/SaveSession.png')

info = ImageTk.PhotoImage(Image.open('c:/gui/info.png').resize((40,40),Image.ANTIALIAS))
home = ImageTk.PhotoImage(Image.open('c:/gui/home.png').resize((40,40),Image.ANTIALIAS))
AddSession = ImageTk.PhotoImage(Image.open('c:/gui/AddSession.png').resize((40,40),Image.ANTIALIAS))
SaveSession = ImageTk.PhotoImage(Image.open('c:/gui/SaveSession.png').resize((40,40),Image.ANTIALIAS))

root.update() #For the width to get updated
frame = Frame(root,bg='#ADD8E6',width=50,height=root.winfo_height())
frame.grid(row=0,column=0)

#making the button with the icon.
info_b = Button(frame, image=info, bg= '#ADD8E6',relief='flat')
home_b = Button(frame, image=home, bg= '#ADD8E6',relief='flat')
add_b = Button(frame, image=AddSession, bg= '#ADD8E6',relief='flat')
save_b = Button(frame, image=SaveSession, bg= '#ADD8E6',relief='flat')

#Put them on the frame
info_b.grid(row=0,column=0,pady=10)
home_b.grid(row=2,column=0,pady=20)
add_b.grid(row=3,column=0,pady=30)
save_b.grid(row=4,column=0)

#bind to frame if entered or left.
frame.bind('<Enter>',lambda e: expand())
frame.bind('<Leave>',lambda e: contract())

frame.grid_propagate(False)

root.mainloop()