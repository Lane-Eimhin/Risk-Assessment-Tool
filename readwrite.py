from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Risk Assessment')
root.iconbitmap('C:/gui/RAexamplelogo.png')
root.geometry("500x450")

def open_docx():
	#Read only is 'r', Read and Write 'r+', Write Only 'w', Write and Read 'w+', Append Only 'a', Append and Read 'a+'
	text_file = filedialog.askopenfilename(initialdir= "C:/gui/docx", title= "Open docx File", filetypes=(("Docx Files", "*.txt"), ))
	text_file = open(text_file, 'r')
	#read the file once its open
	text= text_file.read()

	my_text.insert(END, text)
	text_file.close()

def save_docx():
	text_file = filedialog.askopenfilename(initialdir= "C:/gui/docx", title= "Open docx File", filetypes=(("Docx Files", "*.txt"), ))
	text_file = open(text_file, 'w')
	text_file.write(my_text.get(1.0, END))

my_text = Text(root, width=40, height=10, font=("Helvetica", "16"))
my_text.pack(pady=20)

open_text = Button(root, text="Open your docx file", command=open_docx)
open_text.pack(pady=20)

save_button = Button(root, text="Save File", command= save_docx)
save_button.pack(pady=20)
root.mainloop()