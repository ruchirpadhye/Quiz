from tkinter import *
from tkinter import ttk
import sqlite3 as sql
class CapitalQuiz:
    def __init__(self,root):
        #==== all StringVars =========

        self.roll_number=StringVar()
        self.name=StringVar()

        #==== Main Root (window) ======

        self.root = root
        self.root.geometry("1200x740")
        self.welcome_frame=Frame(self.root,bg="white",bd=0)
        self.main_frame=Frame(self.root,bg="white",bd=0)
        self.welcome_frame.pack(fill=BOTH,expand=1)

        #===== Welcome frame contents =====

        Label(self.welcome_frame,bg="black",fg="white",text="Capital Quiz",font=("arial",30)).pack(side=TOP,fill=X)
        Label(self.welcome_frame,bg="white",fg="black",text="Welcome to the Capital Quiz. This quiz contains 10 questions.",font=("arial",20)).place(x=30,y=70)
        Label(self.welcome_frame,bg="white",fg="black",text="Please enter your name and roll number. The time limit is 10 minutes.",font=("arial",20)).place(x=30,y=110)
        Label(self.welcome_frame,bg="white",fg="black",text="All the best !!!",font=("impact",30)).place(x=30,y=200)
        Label(self.welcome_frame,bg="white",fg="black",text="Roll Number",font=("arial",15)).place(x=30,y=350)
        Label(self.welcome_frame,bg="white",fg="black",text="Name",font=("arial",15)).place(x=30,y=420)

        #=== Entry ====

        ttk.Entry(self.welcome_frame,textvariable=self.roll_number,font=("arial",15)).place(x=150,y=350,width=250)
        ttk.Entry(self.welcome_frame,textvariable=self.name,font=("arial",15)).place(x=150,y=420,width=250)

        #=== Buttons ====
        
        self.start_button=Button(self.welcome_frame,command=self.database_check,bg="black",activebackground="black",fg="white",activeforeground="white",cursor="hand2",text="Start Quiz",state="disabled",font=("arial",20))
        self.start_button.place(x=30,y=490)

        #=== trace the input===
        
        self.roll_number.trace("w",self.check_validity)
        self.name.trace("w",self.check_validity)
    
    #== Clear the Label ====

    def clear_label(self):
        self.done_lbl.destroy()
    
    #=== Loads the Main Screen

    def main_screen(self):
        self.welcome_frame.pack_forget()
        self.lable=Label(self.root,fg="black",bg="white",text="Questions",font=("arial",30))
        self.lable.pack(side=TOP,fill=X,pady=10)
        self.b1_next=Button(self.root,bg="black",activebackground="black",fg="white",activeforeground="white",font=("arial",12,"bold"),text="Next →",command=self.next_page,cursor="hand2")
        self.b1_next.place(x=20,y=20,relx=0.9,rely=0)
        self.b2_next=Button(self.root,bg="black",activebackground="black",fg="white",activeforeground="white",font=("arial",12,"bold"),text="Next →",command=self.next_page2,cursor="hand2")
        self.b2_previous=Button(self.root,bg="black",activebackground="black",fg="white",activeforeground="white",font=("arial",12,"bold"),text="Previous ←",command=self.previous_page2,cursor="hand2")
        
        
        self.b1_previous=Button(self.root,bg="black",activebackground="black",fg="white",activeforeground="white",font=("arial",12,"bold"),text="Previous ←",command=self.previous_page,cursor="hand2")
        
        self.lbl = Label(self.root,font=("arial",20),text="",bg="white",fg="black")
        self.lbl.place(x=10,y=10)
        self.main_frame=Frame(self.root,bg="white",bd=0)
        self.main_frame2=Frame(self.root,bg="white",bd=0)
        self.main_frame4=Frame(self.root,bg="white",bd=0)
        self.main_frame3=Frame(self.root,bg="white",bd=0)
        self.main_frame5=Frame(self.root,bg="white",bd=0)
        self.b1_submit=Button(self.main_frame3,bg="black",command=self.submit_check,activebackground="black",fg="white",activeforeground="white",font=("arial",15,"bold"),text="Submit Quiz",cursor="hand2")
        self.b1_submit.place(x=10,y=400,relx=0.45)
        
        self.main_frame.pack(fill=BOTH,expand=1)
        

        
        
        self.which_page=1
        self.temp1=0
        frame1=Frame(self.main_frame,bg="light grey",height=180)
        frame1.pack(side=TOP,fill=X)
        frame2=Frame(self.main_frame,bg="light grey",height=180)
        frame2.pack(side=TOP,fill=X)
        frame3=Frame(self.main_frame,bg="light grey",height=180)
        frame3.pack(side=TOP,fill=X)
        frame4=Frame(self.main_frame,bg="light grey",height=180)
        frame4.pack(side=TOP,fill=X)
        frame5=Frame(self.main_frame2,bg="light grey",height=180)
        frame5.pack(side=TOP,fill=X)
        frame6=Frame(self.main_frame2,bg="light grey",height=180)
        frame6.pack(side=TOP,fill=X)
        frame7=Frame(self.main_frame2,bg="light grey",height=180)
        frame7.pack(side=TOP,fill=X)
        frame8=Frame(self.main_frame2,bg="light grey",height=180)
        frame8.pack(side=TOP,fill=X)
        frame9=Frame(self.main_frame3,bg="light grey",height=180)
        frame9.pack(side=TOP,fill=X)
        frame10=Frame(self.main_frame3,bg="light grey",height=180)
        frame10.pack(side=TOP,fill=X)
        self.not_attemp_1=[]
        self.not_attemp_2=[]
        self.not_attemp_3=[]
        self.temp=0
        Label(frame1,bg="black",fg="white",text="Q1",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame1,bg="black",fg="white",text="What is the capital of India?",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        self.capital_one=StringVar()
        self.capital_one.set("hellow")
        Radiobutton(frame1,bg="light grey",text="Washington DC",font=("arial",12),variable=self.capital_one,value="Washington DC").place(x=50,y=50)
        Radiobutton(frame1,bg="light grey",text="London",font=("arial",12),variable=self.capital_one,value="London").place(x=50,y=80)
        Radiobutton(frame1,bg="light grey",text="Delhi",font=("arial",12),variable=self.capital_one,value="Delhi").place(x=50,y=110)
        Radiobutton(frame1,bg="light grey",text="Tokyo",font=("arial",12),variable=self.capital_one,value="Tokyo").place(x=50,y=140)
        

        Label(frame2,bg="black",fg="white",text="Q2",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame2,bg="black",fg="white",text="What is the capital of Russia?",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        #Label(self.Questions, text = "Q2.  What is the capital of Russia?",font=("arial",12,"bold")).place(x=10,y=200)
        self.capital_two=StringVar()
        self.capital_two.set("hellow")
        Radiobutton(frame2,bg="light grey",text="Mumbai",font=("arial",12),variable=self.capital_two,value="Mumbai").place(x=50,y=50)
        Radiobutton(frame2,bg="light grey",text="Islamabad",font=("arial",12),variable=self.capital_two,value="Islamabad").place(x=50,y=80)
        Radiobutton(frame2,bg="light grey",text="Moscow",font=("arial",12),variable=self.capital_two,value="Moscow").place(x=50,y=110)
        Radiobutton(frame2,bg="light grey",text="Tokyo",font=("arial",12),variable=self.capital_two,value="Tokyo").place(x=50,y=140)

        Label(frame3,bg="black",fg="white",text="Q3",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame3,bg="black",fg="white",text="Wellington is the capital of which country?",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        self.capital_three=StringVar()
        self.capital_three.set("hellow")
        Radiobutton(frame3,bg="light grey",text="Pakistan",font=("arial",12),variable=self.capital_three,value="Pakistan").place(x=50,y=50)
        Radiobutton(frame3,bg="light grey",text="New Zealand",font=("arial",12),variable=self.capital_three,value="New Zealand").place(x=50,y=80)
        Radiobutton(frame3,bg="light grey",text="Japan",font=("arial",12),variable=self.capital_three,value="Japan").place(x=50,y=110)
        Radiobutton(frame3,bg="light grey",text="Canada",font=("arial",12),variable=self.capital_three,value="Canada").place(x=50,y=140)

        Label(frame4,bg="black",fg="white",text="Q4",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame4,bg="black",fg="white",text="State the capital of Myanmar.",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        self.capital_four=StringVar()
        self.capital_four.set("hellow")
        Radiobutton(frame4,bg="light grey",text="Cape Town",font=("arial",12),variable=self.capital_four,value="Cape Town").place(x=50,y=50)
        Radiobutton(frame4,bg="light grey",text="Islamabad",font=("arial",12),variable=self.capital_four,value="Islamabad").place(x=50,y=80)
        Radiobutton(frame4,bg="light grey",text="Burma",font=("arial",12),variable=self.capital_four,value="Burma").place(x=50,y=110)
        Radiobutton(frame4,bg="light grey",text="Beijing",font=("arial",12),variable=self.capital_four,value="Beijing").place(x=50,y=140)

        Label(frame5,bg="black",fg="white",text="Q5",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame5,bg="black",fg="white",text="Which country doesn't have a capital?",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        self.capital_five=StringVar()
        self.capital_five.set("hellow")
        Radiobutton(frame5,bg="light grey",text="Nauru",font=("arial",12),variable=self.capital_five,value="Nauru").place(x=50,y=50)
        Radiobutton(frame5,bg="light grey",text="Cuba",font=("arial",12),variable=self.capital_five,value="Cuba").place(x=50,y=80)
        Radiobutton(frame5,bg="light grey",text="Panama",font=("arial",12),variable=self.capital_five,value="Panama").place(x=50,y=110)
        Radiobutton(frame5,bg="light grey",text="Jamaica",font=("arial",12),variable=self.capital_five,value="Jamaica").place(x=50,y=140)

        Label(frame6,bg="black",fg="white",text="Q6",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame6,bg="black",fg="white",text="Which country's capital is Buenos Aires?",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        #Label(self.Questions, text = "Q2.  What is the capital of Russia?",font=("arial",12,"bold")).place(x=10,y=200)
        self.capital_six=StringVar()
        self.capital_six.set("hellow")
        Radiobutton(frame6,bg="light grey",text="Argentina",font=("arial",12),variable=self.capital_six,value="Argentina").place(x=50,y=50)
        Radiobutton(frame6,bg="light grey",text="Chile",font=("arial",12),variable=self.capital_six,value="Chile").place(x=50,y=80)
        Radiobutton(frame6,bg="light grey",text="Taiwan",font=("arial",12),variable=self.capital_six,value="Taiwan").place(x=50,y=110)
        Radiobutton(frame6,bg="light grey",text="Uruguay",font=("arial",12),variable=self.capital_six,value="Uruguay").place(x=50,y=140)

        Label(frame7,bg="black",fg="white",text="Q7",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame7,bg="black",fg="white",text="What is the capital of Algeria?",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        self.capital_seven=StringVar()
        self.capital_seven.set("hellow")
        Radiobutton(frame7,bg="light grey",text="Dhaka",font=("arial",12),variable=self.capital_seven,value="Dhaka").place(x=50,y=50)
        Radiobutton(frame7,bg="light grey",text="Algiers",font=("arial",12),variable=self.capital_seven,value="Algiers").place(x=50,y=80)
        Radiobutton(frame7,bg="light grey",text="Rabat",font=("arial",12),variable=self.capital_seven,value="Rabat").place(x=50,y=110)
        Radiobutton(frame7,bg="light grey",text="Cairo",font=("arial",12),variable=self.capital_seven,value="Cairo").place(x=50,y=140)

        Label(frame8,bg="black",fg="white",text="Q8",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame8,bg="black",fg="white",text="State the capital of Mexico.",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        self.capital_eight=StringVar()
        self.capital_eight.set("hellow")
        Radiobutton(frame8,bg="light grey",text="Mexico City",font=("arial",12),variable=self.capital_eight,value="Mexico City").place(x=50,y=50)
        Radiobutton(frame8,bg="light grey",text="Cancún",font=("arial",12),variable=self.capital_eight,value="Cancún").place(x=50,y=80)
        Radiobutton(frame8,bg="light grey",text="Oaxaca",font=("arial",12),variable=self.capital_eight,value="Oaxaca").place(x=50,y=110)
        Radiobutton(frame8,bg="light grey",text="San Miguel de Allende",font=("arial",12),variable=self.capital_eight,value="San Miguel de Allende").place(x=50,y=140)

        Label(frame9,bg="black",fg="white",text="Q9",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame9,bg="black",fg="white",text="What is the capital of Chile?",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        self.capital_nine=StringVar()
        self.capital_nine.set("hellow")
        Radiobutton(frame9,bg="light grey",text="Montevideo",font=("arial",12),variable=self.capital_nine,value="Montevideo").place(x=50,y=50)
        Radiobutton(frame9,bg="light grey",text="Santiago",font=("arial",12),variable=self.capital_nine,value="Santiago").place(x=50,y=80)
        Radiobutton(frame9,bg="light grey",text="Lima",font=("arial",12),variable=self.capital_nine,value="Lima").place(x=50,y=110)
        Radiobutton(frame9,bg="light grey",text="Quito",font=("arial",12),variable=self.capital_nine,value="Quito").place(x=50,y=140)

        Label(frame10,bg="black",fg="white",text="Q10",anchor="n",font=("arial",12,"bold")).place(x=0,y=0,width=30,height=180)
        Label(frame10,bg="black",fg="white",text="What is the capital of North Korea?",anchor="nw",padx=10,font=("arial",12,"bold")).place(x=30,y=0,relwidth=1,height=30)
        #Label(self.Questions, text = "Q2.  What is the capital of Russia?",font=("arial",12,"bold")).place(x=10,y=200)
        self.capital_ten=StringVar()
        self.capital_ten.set("hellow")
        Radiobutton(frame10,bg="light grey",text="Nairobi",font=("arial",12),variable=self.capital_ten,value="Nairobi").place(x=50,y=50)
        Radiobutton(frame10,bg="light grey",text="Oslo",font=("arial",12),variable=self.capital_ten,value="Oslo").place(x=50,y=80)
        Radiobutton(frame10,bg="light grey",text="Jakarta",font=("arial",12),variable=self.capital_ten,value="Jakarta").place(x=50,y=110)
        Radiobutton(frame10,bg="light grey",text="Pyongyang",font=("arial",12),variable=self.capital_ten,value="Pyongyang").place(x=50,y=140)


        #Label(self.main_frame2,fg="black",bg="white",text="Questions",font=("arial",30)).pack(side=TOP,fill=X,pady=10)
        
        self.timesss()
        
    def submit_check(self):
        self.main_frame3.pack_forget()
        self.main_frame4.pack(fill=BOTH,expand=1)
        self.b2_previous.place_forget()
        Label(self.main_frame4,fg="black",bg="white",text="Questions not attempted",font=("arial",22)).place(x=0,y=50,relx=0.4)
        
        if self.capital_one.get()=="hellow":
            self.not_attemp_1.append("Q1")
        if self.capital_two.get()=="hellow":
            self.not_attemp_1.append("Q2")
        if self.capital_three.get()=="hellow":
            self.not_attemp_1.append("Q3")
        if self.capital_four.get()=="hellow":
            self.not_attemp_1.append("Q4")
        if self.capital_five.get()=="hellow":
            self.not_attemp_2.append("Q5")
        if self.capital_six.get()=="hellow":
            self.not_attemp_2.append("Q6")
        if self.capital_seven.get()=="hellow":
            self.not_attemp_2.append("Q7")
        if self.capital_eight.get()=="hellow":
            self.not_attemp_2.append("Q8")
        if self.capital_nine.get()=="hellow":
            self.not_attemp_3.append("Q9")
        if self.capital_ten.get()=="hellow":
            self.not_attemp_3.append("Q10")
        f=str(self.not_attemp_1).replace("'","").replace("[","").replace("]","")
        f2=str(self.not_attemp_2).replace("'","").replace("[","").replace("]","")
        f3=str(self.not_attemp_3).replace("'","").replace("[","").replace("]","")
        Label(self.main_frame4,fg="black",bg="white",text=f"Page 1 - {f}",font=("arial",22)).place(x=0,y=130,relx=0.25)
        Label(self.main_frame4,fg="black",bg="white",text=f"Page 2 - {f2}",font=("arial",22)).place(x=0,y=180,relx=0.25)
        Label(self.main_frame4,fg="black",bg="white",text=f"Page 3 - {f3}",font=("arial",22)).place(x=0,y=230,relx=0.25)
        self.b2_submit=Button(self.main_frame4,bg="black",command=self.submit_quiz,activebackground="black",fg="white",activeforeground="white",font=("arial",15,"bold"),text="Submit Quiz",cursor="hand2")
        self.b2_submit.place(x=10,y=300,relx=0.40)
        self.b1_back=Button(self.main_frame4,bg="black",command=self.previous_page3,activebackground="black",fg="white",activeforeground="white",font=("arial",15,"bold"),text="Go Back",cursor="hand2")
        self.b1_back.place(x=10,y=300,relx=0.52)
    def timesss(self):
        self.temp+=1
        if self.temp==60:
            self.temp1+=1
            self.temp=0
        else:
            pass
        if self.temp1==10:
            self.root.destroy()
        else:
            self.lbl.config(text=f"Time Elapsed  {self.temp1}:{self.temp}")
            self.root.after("1000",self.timesss)

        
        
    def previous_page3(self):
        self.which_page=3
        self.not_attemp_1.clear()
        self.not_attemp_2.clear()
        self.not_attemp_3.clear()
        #if self.which_page==2:
        for widget in self.main_frame4.winfo_children():
            widget.place_forget()
        self.main_frame4.pack_forget()
        self.b2_next.place_forget()
        self.b1_previous.place_forget()
        self.b2_previous.place(x=20,y=20,relx=0.9,rely=0)
        self.main_frame3.pack(fill=BOTH,expand=1)
    def previous_page(self):
        self.which_page=1
        #if self.which_page==2:
        self.main_frame2.pack_forget()
        self.b1_previous.place_forget()
        self.b2_next.place_forget()
        
        self.b1_next.place(x=20,y=20,relx=0.9,rely=0)
        self.main_frame.pack(fill=BOTH,expand=1)
    def next_page2(self):
        self.which_page=3
        #if self.which_page==2:
        self.main_frame2.pack_forget()
        self.b2_next.place_forget()
        self.b1_previous.place_forget()
        self.b2_previous.place(x=20,y=20,relx=0.9,rely=0)
        self.main_frame3.pack(fill=BOTH,expand=1)
    def previous_page2(self):
        self.which_page=2
        #if self.which_page==2:
        self.main_frame3.pack_forget()
        self.b2_previous.place_forget()
        self.b2_next.place(x=20,y=20,relx=0.9,rely=0)
        self.b1_previous.place(x=20,y=20,relx=0.81,rely=0)
        self.main_frame2.pack(fill=BOTH,expand=1)
 
    def next_page(self):
        self.which_page=2
        #if self.which_page==2:
        self.main_frame.pack_forget()
        self.b1_next.place_forget()
        self.b2_next.place(x=20,y=20,relx=0.9,rely=0)
        self.b1_previous.place(x=20,y=20,relx=0.81,rely=0)
        self.main_frame2.pack(fill=BOTH,expand=1)

    #==== Inserts the marks into database and shows the calculation of marks

    def submit_quiz(self):
        points=0
        if self.capital_one.get()=="Delhi":
            points+=1
        if self.capital_two.get()=="Moscow":
            points+=1
        if self.capital_three.get()=="New Zealand":
            points+=1
        if self.capital_four.get()=="Burma":
            points+=1
        if self.capital_five.get()=="Nauru":
            points+=1
        if self.capital_six.get()=="Argentina":
            points+=1
        if self.capital_seven.get()=="Algiers":
            points+=1
        if self.capital_eight.get()=="Mexico City":
            points+=1
        if self.capital_nine.get()=="Santiago":
            points+=1
        if self.capital_ten.get()=="Pyongyang":
            points+=1
        self.capital_one.set("hellow")
        self.capital_two.set("hellow")
        self.capital_three.set("hellow")
        self.capital_four.set("hellow")
        self.capital_five.set("hellow")
        self.capital_six.set("hellow")
        self.capital_seven.set("hellow")
        self.capital_eight.set("hellow")
        self.capital_nine.set("hellow")
        self.capital_ten.set("hellow")
        self.conn = sql.connect("student_quiz.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""INSERT INTO marks
              (points, name)
              VALUES (?, ?) """, (points,self.name.get()))
        self.conn.commit()
        for widget in self.main_frame4.winfo_children():
            widget.place_forget()
        self.main_frame4.pack_forget()
        self.main_frame5.pack(fill=BOTH,expand=1)
        Label(self.main_frame5,fg="black",bg="white",text=f"You got {points} marks out of 10.",font=("arial",22)).place(x=0,y=200,relx=0.3)
        Label(self.main_frame5,fg="black",bg="white",text="Thank you for participating in the quiz.",font=("arial",22)).place(x=0,y=250,relx=0.3)
        Label(self.main_frame5,fg="black",bg="white",text="You will return to the main panel in 5 seconds.",font=("arial",22)).place(x=0,y=350,relx=0.3)
        self.root.after("5000",self.return_to_main_)
        #self.main_screen()
    #=== Check if user has attempted the quiz else brings the main page
    
    def return_to_main_(self):
        for widget in self.main_frame5.winfo_children():
            widget.destroy()
        self.lbl.destroy()
        self.lable.destroy()
        self.main_frame5.pack_forget()
        self.welcome_frame.pack(fill=BOTH,expand=1)
    def database_check(self):
        self.conn = sql.connect("student_quiz.db")
        self.cursor = self.conn.cursor()
        self.create_table()
        data = self.cursor.execute("""select * from tbl_student where _roll = ? and name = ?""",(self.roll_number.get(),self.name.get())).fetchall()
        print(data)
        if data!=[]:
            self.done_lbl=Label(self.welcome_frame,bg="white",fg="red",text="This student has already attempted the quiz.",font=("arial",15))
            self.done_lbl.place(x=430,y=350)
            self.root.after("1500",self.clear_label)
        else:
            self.cursor.execute("""INSERT INTO tbl_student
              (_roll, name)
              VALUES (?, ?) """, (self.roll_number.get(),self.name.get()))
            self.conn.commit()
            self.main_screen()

    #==== Function to Create table if it doesn't exist

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_student (
              _roll text,
              name text
            )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS marks (
              points text,
              name text
            )""")

    #==== This Checks if both the entries are filled. If no then the button is disabled else it is enabled.
        
    def check_validity(self,*args):
        
        if self.roll_number.get() and self.name.get():
            self.start_button.config(state="normal")
        else:
            self.start_button.config(state="disabled")

        
root=Tk()
objects=CapitalQuiz(root)
root.mainloop()
