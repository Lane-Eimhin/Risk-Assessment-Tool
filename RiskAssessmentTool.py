from tkinter import *
window=Tk()
window.title('Risk Assessment Tool')
window.iconbitmap('C:/gui/RAexamplelogo.ico')
window['bg']='light blue'
title=Label(window,text='RA Tool',font=('Arial',40), bg='light blue')
title.place(x=600, y=50)
labelComp=Label(window,text='Company Name =',font=('Arial',30), bg='light blue')
labelComp.place(x=150,y=250)
nameEntered=Entry(window,font=('Arial',30))
nameEntered.place(x=500,y=250)
worm=0
ransomware=0
sqli=0
trojan=0

def questions1():
    compName=nameEntered.get()
    quesNumb1=Label(window,text='Question 1:',font=('Arial',40), bg='light blue')
    quesNumb1.place(x=570, y=20)
    question1=Label(window,text='How many users do you have?',font=('Arial',30), bg='light blue')
    question1.place(x=499,y=100)

    def worm2():
        global worm
        worm +=1
        labelw2=Label(window)
        labelw2.pack()
        labelw2.after(10,questions2)

    def ransomware2():
        global ransomware
        ransomware +=1
        labelr2=Label(window)
        labelr2.pack()
        labelr2.after(10,questions2)

    def questions2():

        quesNumb2=Label(window,text='Question 2',font=('Arial',40), bg='light blue')
        quesNumb2.place(x=570, y=20)
        question2=Label(window,text='How often do you perfom scans',font=('Arial',30), bg='light blue')
        question2.place(x=499,y=100)

        def trojan3():

            global trojan
            trojan +=1
            labelt3=Label(window)
            labelt3.pack()
            labelt3.after(10,questions3)

        def ransomware3():
            global ransomware
            ransomware +=1
            labelr3 = Label(window)
            labelr3.pack()
            labelr3.after(10,questions3)

        def questions3():
            
            quesNumb3=Label(window,text='Question 3',font=('Arial',40), bg='light blue')
            quesNumb3.place(x=570, y=20)
            question3=Label(window,text='Do you backup regularly?',font=('Arial',30), bg='light blue')
            question3.place(x=499,y=100)

            def worm4():

                global worm
                worm +=1
                labelw4=Label(window)
                labelw4.pack()
                labelw4.after(10,questions4)

            def questions4():

                quesNumb4=Label(window,text='Question 4',font=('Arial',40), bg='light blue')
                quesNumb4.place(x=570, y=20)
                question4=Label(window,text='In what range is your income',font=('Arial',30), bg='light blue')
                question4.place(x=499,y=100)

                def ransomware5():

                    global ransomware
                    ransomware +=1
                    labelr5=Label(window)
                    labelr5.pack()
                    labelr5.after(10,questions5)

                def sqli5():

                    global sqli
                    sqli +=1
                    labels5=Label(window)
                    labels5.pack()
                    labels5.after(10,questions5)

                def questions5():

                    quesNumb5=Label(window,text='Question 5',font=('Arial',40), bg='light blue')
                    quesNumb5.place(x=570, y=20)
                    question5=Label(window,text='Do you implement website download restrictions?',font=('Arial',30), bg='light blue')
                    question5.place(x=290,y=100)

                    def ransomware6():

                        global ransomware
                        ransomware +=1
                        labelr6=Label(window)
                        labelr6.pack()
                        labelr6.after(10,questions6)

                    def sqli6():

                        global sqli
                        sqli +=1
                        labels6=Label(window)
                        labels6.pack()
                        labels6.after(10,questions6)

                    def questions6():

                        quesNumb6=Label(window,text='Question 6',font=('Arial',40), bg='light blue')
                        quesNumb6.place(x=570, y=20)
                        question6=Label(window,text='Do you utilise anti-virus?',font=('Arial',30), bg='light blue')
                        question6.place(x=420,y=100)

                        def worm7():

                            global worm
                            worm +=1
                            labelw7=Label(window)
                            labelw7.pack()
                            labelw7.after(10,questions7)

                        def sqli7():

                            global sqli
                            sqli +=1
                            labels7=Label(window)
                            labels7.pack()
                            labels7.after(10,questions7)

                        def questions7():

                            quesNumb7=Label(window,text='Question 7',font=('Arial',40), bg='light blue')
                            quesNumb7.place(x=570, y=20)
                            question7=Label(window,text='How consistently do you update hardware?',font=('Arial',30), bg='light blue')
                            question7.place(x=400,y=100)

                            def trojan8():
                    
                                global trojan
                                trojan +=1
                                labelt8=Label(window)
                                labelt8.pack()
                                labelt8.after(10,questions8)
                            
                            def sqli8():
                    
                                global worm
                                worm +=1
                                labelw8=Label(window)
                                labelw8.pack()
                                labelw8.after(10,questions8)
                            
                            def questions8():

                                quesNumb8=Label(window,text='Question 8',font=('Arial',40), bg='light blue')
                                quesNumb8.place(x=570, y=20)
                                question8=Label(window,text='Do you implement email download restrictions?',font=('Arial',30), bg='light blue')
                                question8.place(x=400,y=100)


                                def worm9():
                    
                                    global worm
                                    worm +=1
                                    labelw9=Label(window)
                                    labelw9.pack()
                                    labelw9.after(10,questions9)
                            
                                def questions9():

                                    quesNumb9=Label(window,text='Question 9',font=('Arial',40), bg='light blue')
                                    quesNumb9.place(x=570, y=20)
                                    question9=Label(window,text='Do you recieve frequent scam emails?',font=('Arial',30), bg='light blue')
                                    question9.place(x=450,y=100)

                                    def trojan10():
                    
                                        global trojan
                                        trojan +=1
                                        labelt10=Label(window)
                                        labelt10.pack()
                                        labelt10.after(10,questions10)
                            
                                    def questions10():

                                        quesNumb10=Label(window,text='Question 10',font=('Arial',40), bg='light blue')
                                        quesNumb10.place(x=570, y=20)
                                        question10=Label(window,text='Where do you devote the least amount of security?',font=('Arial',30), bg='light blue')
                                        question10.place(x=350,y=100)

                                        def trojanF():
                    
                                            global trojan
                                            trojan +=1
                                            labelt10=Label(window)
                                            labelt10.pack()
                                            labelt10.after(10,final)

                                        def sqliF():
                    
                                            global sqli
                                            sqli +=1
                                            labelt10=Label(window)
                                            labelt10.pack()
                                            labelt10.after(10,final)

                                        def wormF():
                    
                                            global worm
                                            worm +=1
                                            labelt10=Label(window)
                                            labelt10.pack()
                                            labelt10.after(10,final)

                                        def ransomwareF():
                    
                                            global ransomware
                                            ransomware +=1
                                            labelt10=Label(window)
                                            labelt10.pack()
                                            labelt10.after(10,final)

                                        def final():
                                            if worm > sqli and worm > trojan and worm > ransomware:
                                                label_N=Label(window,text=compName,font=('Arial',15), bg='light blue')
                                                label_N.place(x=400,y=150)
                                                label_P=Label(window,text=':You are at risk of a worm attack',font=('Arial',11), bg='light blue')
                                                label_P.place(x=500,y=150)
                                                label_P=Label(window,text='When suffering from a worm it can result in massive losses due to it’s highly infectious spreading\n methods. Preventing worms can be helped through limiting the reliance on the internet. Worms can \neasily spread through connections, the internet being no different as such limit website access and \n email downloads. Additionally keeping your system spread across various servers with few \nconnections can help slow the spread of a worm. In the event of a worm attack limit employee \nconnectivity to one another on the system as more employees means more targets and damages.',font=('Arial',9), bg='light blue')
                                                label_P.place(x=650,y=250, anchor="center")
                                            elif sqli > worm and sqli > trojan and sqli > ransomware:
                                                label_N=Label(window,text=compName,font=('Arial',15), bg='light blue')
                                                label_N.place(x=400,y=150)
                                                label_P=Label(window,text=':You are at risk of a sql injection',font=('Arial',11), bg='light blue')
                                                label_P.place(x=500,y=150)
                                                label_P=Label(window,text='The best way to avoid an SQL Injection is sanitisation of code. Implementing secure methods such as \nwhite lists, character escaping, parametered statements and utilising firewalls can help mitigate the \nthreat. Don’t leave database errors on the front end as it offers an “in” for attackers',font=('Arial',9), bg='light blue')
                                                label_P.place(x=650,y=250, anchor="center")
                                            elif trojan > sqli and trojan > worm and trojan > ransomware:
                                                label_N=Label(window,text=compName,font=('Arial',15), bg='light blue')
                                                label_N.place(x=400,y=150)
                                                label_P=Label(window,text=':You are risk of a Trojan attack.',font=('Arial',11), bg='light blue')
                                                label_P.place(x=500,y=150)
                                                label_P=Label(window,text='Trojans establish a backdoor for hackers to enter your system. Prevention begins with caution, don’t \ninstall any software from emails without confirming the sender is not malicious. If in a larger \ncompany you may need to implement restrictions on various websites and sources. As it is with \nmany cases of security keeping up to date and utilising an Anti-virus can vastly improve protection \nfrom a Trojan attack. If in the event these preventative measures are not enough you may need to \nrely on backups to restore systems to a safe state, as such regular backups are necessary.',font=('Arial',9), bg='light blue')
                                                label_P.place(x=650,y=250, anchor="center")
                                            elif ransomware > worm and ransomware > trojan and ransomware > sqli:
                                                label_N=Label(window,text=compName,font=('Arial',15), bg='light blue')
                                                label_N.place(x=400,y=150)
                                                label_P=Label(window,text=':You are at risk of a ransomware attack.',font=('Arial',11), bg='light blue')
                                                label_P.place(x=500,y=150)
                                                label_P=Label(window,text='Ransomware can be costly so prevention is very important. The best method to avoid ransomware is \nto not click unsolicited links. Ensure you are up to date in both software and hardware terms.\n Tracking background tasks can ensure you know what is running on your system \nand can help you understand if your in the process of being compromised. Backups are entirely \nnecessary to counter Ransomware, though the backup must be kept on another device from yours. \nBackups can completely bypass the threat ransomware can pose.',font=('Arial',9), bg='light blue')
                                                label_P.place(x=650,y=250, anchor="center")
                                            else:
                                                label_P=Label(window,text='An Error Occured.',font=('Arial',15), bg='light blue')
                                                label_P.place(x=590,y=250)


                                            def end():
                                                window.destroy()

                                            endButton=Button(window,height=1,width=10,text='Close',font=('Arial',30),command=end)
                                            endButton.place(x=500,y=390)

                                            quesNumb10.destroy()
                                            question10.destroy()
                                            choice101.destroy()
                                            choice102.destroy()
                                            choice103.destroy()
                                            choice104.destroy()

                                        choice101=Button(window,height=1,width=10,text='Passwords',font=('Arial',30),command=ransomwareF)
                                        choice101.place(x=400,y=200)
                                        choice102=Button(window,height=1,width=10,text='Whitelisting',font=('Arial',30),command=sqliF)
                                        choice102.place(x=800,y=200)
                                        choice103=Button(window,height=1,width=10,text='Emails',font=('Arial',30),command=wormF)
                                        choice103.place(x=400,y=300)
                                        choice104=Button(window,height=1,width=10,text='Downloads',font=('Arial',30),command=trojanF)
                                        choice104.place(x=800,y=300)

                                        quesNumb9.destroy()
                                        question9.destroy()
                                        choice91.destroy()
                                        choice92.destroy()

                                    choice91=Button(window,height=1,width=10,text='Yes',font=('Arial',30),command=trojan10)
                                    choice91.place(x=400,y=200)
                                    choice92=Button(window,height=1,width=10,text='No',font=('Arial',30),command=questions10)
                                    choice92.place(x=800,y=200)

                                    quesNumb8.destroy()
                                    question8.destroy()
                                    choice81.destroy()
                                    choice82.destroy()

                                choice81=Button(window,height=1,width=10,text='Yes',font=('Arial',30),command=questions9)
                                choice81.place(x=400,y=200)
                                choice82=Button(window,height=1,width=10,text='No',font=('Arial',30),command=worm9)
                                choice82.place(x=800,y=200)

                                quesNumb7.destroy()
                                question7.destroy()
                                choice71.destroy()
                                choice72.destroy()
                                choice73.destroy()

                            choice71=Button(window,height=1,width=10,text='Frequently',font=('Arial',30),command=questions8)
                            choice71.place(x=400,y=200)
                            choice72=Button(window,height=1,width=10,text='Infrequently',font=('Arial',30),command=trojan8)
                            choice72.place(x=800,y=200)
                            choice73=Button(window,height=1,width=10,text='Never',font=('Arial',30),command=sqli8)
                            choice73.place(x=600,y=300)


                            quesNumb6.destroy()
                            question6.destroy()
                            choice61.destroy()
                            choice62.destroy()
                            choice63.destroy()

                        choice61=Button(window,height=1,width=10,text='Yes',font=('Arial',30),command=questions7)
                        choice61.place(x=400,y=200)
                        choice62=Button(window,height=1,width=10,text='No',font=('Arial',30), command=worm7)
                        choice62.place(x=800,y=200)
                        choice63=Button(window,height=1,width=10,text='Somewhat',font=('Arial',30),command=sqli7)
                        choice63.place(x=600,y=300)

                        quesNumb5.destroy()
                        question5.destroy()
                        choice51.destroy()
                        choice52.destroy()
                        choice53.destroy()

                    choice51=Button(window,height=1,width=10,text='Yes',font=('Arial',30),command=questions6)
                    choice51.place(x=400,y=200)
                    choice52=Button(window,height=1,width=10,text='Some',font=('Arial',30),command=sqli6)
                    choice52.place(x=600,y=300)
                    choice53=Button(window,height=1,width=10,text='No',font=('Arial',30),command=ransomware6)
                    choice53.place(x=800,y=200)

                    quesNumb4.destroy()
                    question4.destroy()
                    choice41.destroy()
                    choice42.destroy()


                choice41=Button(window,height=1,width=10,text='<100,000',font=('Arial',30),command= ransomware5)
                choice41.place(x=400,y=200)
                choice42=Button(window,height=1,width=10,text='>100,000',font=('Arial',30),command= sqli5)
                choice42.place(x=800,y=200)

                quesNumb3.destroy()
                question3.destroy()
                choice31.destroy()
                choice32.destroy()
                choice33.destroy()
                choice34.destroy()


            choice31=Button(window,height=1,width=10,text='monthly',font=('Arial',30),command=questions4)
            choice31.place(x=400,y=200)
            choice32=Button(window,height=1,width=10,text='<6months',font=('Arial',30),command=worm4)
            choice32.place(x=800,y=200)
            choice34=Button(window,height=1,width=10,text='>6 months',font=('Arial',30),command=worm4)
            choice34.place(x=800,y=300)
            choice33=Button(window,height=1,width=10,text='Never',font=('Arial',30),command=worm4)
            choice33.place(x=400,y=300)

            quesNumb2.destroy()
            question2.destroy()
            choice21.destroy()
            choice22.destroy()
            choice23.destroy()
            choice24.destroy()

        choice21=Button(window,height=1,width=10,text='Daily',font=('Arial',30),command=questions3)
        choice21.place(x=400,y=200)
        choice22=Button(window,height=1,width=10,text='Weekly',font=('Arial',30),command=trojan3)
        choice22.place(x=800,y=200)
        choice23=Button(window,height=1,width=10,text='Monthly',font=('Arial',30),command=ransomware3)
        choice23.place(x=400,y=300)
        choice24=Button(window,height=1,width=10,text='Never',font=('Arial',30),command=ransomware3)
        choice24.place(x=800,y=300)

        quesNumb1.destroy()
        question1.destroy()
        choice1.destroy()
        choice2.destroy()
        choice3.destroy()
        choice4.destroy()

    choice1=Button(window,height=1,width=10,text='1000+',font=('Arial',30),command=ransomware2)
    choice1.place(x=400,y=200)
    choice2=Button(window,height=1,width=10,text='500-1000',font=('Arial',30),command=worm2)
    choice2.place(x=800,y=200)
    choice3=Button(window,height=1,width=10,text='250-500',font=('Arial',30),command=worm2)
    choice3.place(x=400,y=300)
    choice4=Button(window,height=1,width=10,text='0-250',font=('Arial',30),command=worm2)
    choice4.place(x=800,y=300)
    title.destroy()
    labelComp.destroy()
    nameEntered.destroy()
    button1.destroy()

button1=Button(window,height=1,width=10,text='Submit',font=('Arial',30),command=questions1)
button1.place(x=600,y=350)

window.mainloop()
