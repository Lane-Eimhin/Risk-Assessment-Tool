from tkinter import *

window=Tk()
window.title("Risk Assessment Questions")
window.iconbitmap('C:/gui/RAexamplelogo.ico')
window.geometry('600x600')


#Questions:
question1 =Label(window,text='How many attacks do you experience in a year?', fg='blue', font=('Arial',14))
question1.grid(row=0,column=0,padx=0,pady=0, sticky=W)

question2 =Label(window,text='How many times do you perfrom backups in a year?', fg='blue', font=('Arial',14))
question2.grid(row=2,column=0,padx=0,pady=0, sticky=W)

question3 =Label(window,text='How many employees do you have?', fg='blue', font=('Arial',14))
question3.grid(row=4,column=0,padx=0,pady=0, sticky=W)

question4 =Label(window,text='How many clients do you service?', fg='blue', font=('Arial',14))
question4.grid(row=6,column=0,padx=0,pady=0, sticky=W)

question5 =Label(window,text='How many end points are on your network?', fg='blue', font=('Arial',14))
question5.grid(row=8,column=0,padx=0,pady=0, sticky=W)

question6 =Label(window,text='How many end user devices?', fg='blue', font=('Arial',14))
question6.grid(row=10,column=0,padx=0,pady=0, sticky=W)

question6 =Label(window,text='Number of phishing emails received in a year?', fg='blue', font=('Arial',14))
question6.grid(row=12,column=0,padx=0,pady=0, sticky=W)


#Answers:

ans1=IntVar()
ans2=IntVar()
ans3=IntVar()
ans4=IntVar()
ans5=IntVar()
ans6=IntVar()
ans7=IntVar()

answers1=Entry(window, textvariable=ans1, fg='black', font=('Arial',14))
answers1.grid(row=1, column=0, sticky=W)

answers2=Entry(window, textvariable=ans2, fg='black', font=('Arial',14))
answers2.grid(row=3, column=0, sticky=W)

answers3=Entry(window, textvariable=ans3, fg='black', font=('Arial',14))
answers3.grid(row=5, column=0, sticky=W)

answers4=Entry(window, textvariable=ans4, fg='black', font=('Arial',14))
answers4.grid(row=7, column=0, sticky=W)

answers5=Entry(window, textvariable=ans5, fg='black', font=('Arial',14))
answers5.grid(row=9, column=0, sticky=W)

answers6=Entry(window, textvariable=ans6, fg='black', font=('Arial',14))
answers6.grid(row=11, column=0, sticky=W)

answers7=Entry(window, textvariable=ans7, fg='black', font=('Arial',14))
answers7.grid(row=13, column=0, sticky=W)


#functions

def assessfunction():
	riskvalue=IntVar()
	riskvalue = 0 

	riskans1=IntVar()
	riskans1 =  70

	riskans2=IntVar()
	riskvalue = 50

	riskans3=IntVar()
	riskvalue = 0 

	riskans4=IntVar()
	riskvalue = 0 

	riskans5=IntVar()
	riskvalue = 0 

	riskans6=IntVar()
	riskvalue = 0 

	riskans7=IntVar()
	riskvalue = 0 

	emptylabel.config(text = 'Running Assessment ')
	
	if ans1 > riskans1:
		riskvalue+= 5

	if ans2 < riskans2:
		riskvalue+= 5

	if riskvalue > 100:
		print('High Risk')



runbutton=Button(window, command=assessfunction,text='Run Assessment', fg='blue', font=('Arial',14))
runbutton.grid(row=14,column=0,sticky=W)

emptylabel=Label(window, fg='blue', font=('Arial',14))
emptylabel.grid(row=15, column=0,sticky=W)

window.mainloop()