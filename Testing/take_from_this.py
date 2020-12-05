from tkinter import *
import time as tm
from datetime import date
import Database
import list
Today = date.today()


def add_new():
    root = Tk()
    root.title('test for database')
    #root.geometry("1350x900+0+0")
    root.configure(background="powder blue")

    phone = StringVar(root)
    name = StringVar(root)
    age = StringVar(root)
    sex = StringVar(root)
    status = StringVar(root)
    fam = StringVar(root)
    job = StringVar(root)
    diseases = StringVar(root)
    habits = StringVar(root)
    allergy = StringVar(root)
    # mid = StringVar(root)
    # surgery = StringVar(root)
    # treatment = StringVar(root)
    #
    # note = StringVar(root)
    # phy = StringVar(root)

    #=================================================================================================


    def exit_a():
        root.destroy()


    def submit():
        if(len(name.get())!=0):
            Database.Add_newRec(Date.get(),name.get(),age.get(),fam.get(),job.get(),mid.get(),surgery.get(),note.get(),phy.get(),treatment.get())
            #Database.Add_newRec(Date.get(),PhoneN.get(),name.get(),age_entry.get(),sex.get(),status.get(),fam_entery.get(),job_e.get(),diseases1.get(),diseases2.get(),diseases3.get(),habits1.get(),habits2.get(),allergy,mid.get(),surgery.get(),note.get(),phy.get(),treatment.get())
        # print(diseases1.get())

        # clear the data
        '''
        PhoneN.delete(0, END)
        f_name.delete(0, END)
        l_name.delete(0, END)
        age.delete(0, END)
        Var.set("----")
        Var2.set("----")
        fam.delete(0, END)
        job.delete(0, END)
        Allergy1.delete(0, END)
        #   description.delete(0, END)
        #    description1.delete(0, END)
        #    description2.delete(0, END)
        hab.deselect()
        '''

    def check1():
        alle_la = Label(frame, text='mid/الدواء')
        alle_la.grid(row=12, column=1, sticky=E)
        Allergy1 = Entry(frame, width=20,textvariable=allergy)
        Allergy1.grid(row=12, column=2)

    # ==================================================frames=======================================================
    titleframe = LabelFrame(root, bd=2, padx=50, pady=8, bg="Light Blue", relief=RIDGE)
    titleframe.pack(side=TOP)
    title = Label(titleframe, bg="Light Blue", fg="Dark red", font=('arial', 47, 'bold'),
                  text="العيادة التخصصية لطب الطوارئ والإسعاف")
    title.grid(row=0, column=0)
    title1 = Label(titleframe, bg="Light Blue", fg="Dark Blue", font=('arial', 20, 'bold'), text="Dr.Essam Khalil")
    title1.grid(row=1, column=0)
    frame = LabelFrame(root, text="Patient Record/سجل المريض", padx=50, pady=20, relief=RIDGE)
    frame.pack(padx=5, pady=10, )
    Buttonframe = LabelFrame(root, width=100, height=60, padx=5, pady=8, relief=RIDGE)
    Buttonframe.pack(side=BOTTOM, anchor=S)
    # time
    time_lable = Label(root, bg="powder blue", font='ariel 30', text=tm.strftime('%H:%M'))
    time_lable.place(x=10, y=10)

    # =================================================Lable==============================================

    date_lable = Label(frame, text="Date/التاريخ\n")
    date_lable.grid(row=1, column=0, sticky=W)
    PhoneN_lable = Label(frame, text="phone Number/رقم التلفون\n")
    PhoneN_lable.grid(row=2, column=0, sticky=W)
    f_name_lable = Label(frame, text="Name/الاسم \n")
    f_name_lable.grid(row=3, column=0, sticky=W)
    # l_name_lable = Label(frame, text="Last Name/الكنية\n")
    # l_name_lable.grid(row=4, column=0, sticky=W)
    Age_lable = Label(frame, text="Age/العمر\n")
    Age_lable.grid(row=5, column=0, sticky=W)
    Sex_lable = Label(frame, text="Sex/الجنس\n")
    Sex_lable.grid(row=6, column=0, sticky=W)
    status_lable = Label(frame, text="status/الحالة\n")
    status_lable.grid(row=7, column=0, sticky=W)
    fam_lable = Label(frame, text="number of family members/عدد افراد العائلي\n")
    fam_lable.grid(row=8, column=0, sticky=W)
    Job_lable = Label(frame, text="Job/الوظيفة\n")
    Job_lable.grid(row=9, column=0, sticky=W)
    disesase_lable = Label(frame, text="chronic diseases/الأمراض المزمنة\n")
    disesase_lable.grid(row=10, column=0, sticky=W)
    hab_lable = Label(frame, text="Habits/العادات\n")
    hab_lable.grid(row=11, column=0, sticky=W)
    Allergy_lable = Label(frame, text="Allergy/حساسية تجاه الادوية\n")
    Allergy_lable.grid(row=12, column=0, sticky=W)
    medic_lable = Label(frame, text="midc/الادوية المستخدمة\n")
    medic_lable.grid(row=14, column=0, sticky=W)
    Surgery_lable = Label(frame, text="Surgery/عمليات جراحية \n")
    Surgery_lable.grid(row=14, column=1, sticky=W)
    note_lable = Label(frame, text="Note/ملاحظة\n")
    note_lable.grid(row=14, column=2, sticky=W)
    description_lable = Label(frame, text="physical examination /فصح السريري والتشخيص")
    description_lable.grid(row=16, column=0, columnspan=2, sticky=W)
    sol_lable = Label(frame, text="Treatment/العلاج")
    sol_lable.grid(row=18, column=0, sticky=W)

    # ========================================================Entry====================================================

    Date = Entry(frame)
    Date.insert(END, Today)
    Date.grid(row=1, column=1, padx=20)
    PhoneN = Entry(frame,textvariable=phone, width=30)
    PhoneN.grid(row=2, column=1, padx=20)
    name1 = Entry(frame,textvariable=name, width=30)
    name1.grid(row=3, column=1, padx=20)
    # l_name = Entry(frame, width=30)
    # l_name.grid(row=4, column=1)
    age_entry = Entry(frame, width=30,textvariable=age)
    age_entry.grid(row=5, column=1)
    fam_entery = Entry(frame, width=10,textvariable=fam)
    fam_entery.grid(row=8, column=1,)
    job_e = Entry(frame, width=30,textvariable=job)
    job_e.grid(row=9, column=1)

    # =========================dropes and checkbox ====================================

    # var = StringVar(frame)
    # var2 = StringVar(frame)
    status.set("------")
    sex.set("------")
    drop_s = OptionMenu(frame,sex,"Male/ذكر","Female/أنثى")
    drop_s.grid(row=6,column=1)
    drop_stat = OptionMenu(frame,status,"Married/متزوج\ة","Single/أعزب")
    drop_stat.grid(row=7,column=1)

    diseases1 = StringVar()
    dise1= Checkbutton(frame, text='Blood Pressure/الضغط', variable=diseases1)
    dise1.deselect()
    dise1.grid(row=10, column=1, sticky=W)

    diseases2 = StringVar()
    dise2= Checkbutton(frame, text='DM/السكري', variable=diseases2)
    dise2.deselect()
    dise2.grid(row=10, column=2, sticky=W)

    diseases3 = StringVar()
    dise3= Checkbutton(frame, text='Asthma/الربو', variable=diseases3)
    dise3.deselect()
    dise3.grid(row=10, column=3, sticky=W)
    #---------------------------------------------------------------------
    # diseases = dict()
    # dis = ['Blood Pressure/الضغط', 'DM/السكري', 'Asthma/الربو']
    # roow = [1, 2, 3, 4]
    # for i, j in zip(dis, roow):
    #     diseases[i] = StringVar()
    #     dise = Checkbutton(frame, text=i, variable=diseases[i])
    #     dise.deselect()
    #     dise.grid(row=10, column=j, sticky=W)
    #---------------------------------------------------------------------

    habits1 = StringVar()
    hab1 = Checkbutton(frame, text='smoker/مدخن', variable=habits1)
    hab1.deselect()
    hab1.grid(row=11, column=1, sticky=W)

    habits2 = StringVar()
    hab2 = Checkbutton(frame, text='smoker/مدخن', variable=habits2)
    hab2.deselect()
    hab2.grid(row=11, column=2, sticky=W)
    #---------------------------------------------------------------------
    # habits = dict()
    # dis1 = ['smoker/مدخن', 'alcoholic/كحولي',]
    # roow = [1, 2, 3]
    # for i, j in zip(dis1, roow):
    #     habits[i] = StringVar()
    #     hab = Checkbutton(frame, text=i, variable=habits[i])
    #     hab.deselect()
    #     hab.grid(row=11, column=j, sticky=W)
    #--------------------------------------------------------------------

    var5 = IntVar()
    allergy_entry = Checkbutton(frame, text='yes/نعم', variable=var5, command=check1)
    allergy_entry.grid(row=12, column=1, sticky=W)
    allergy_entry.deselect()

    # ==================================Text entry ========================================

    mid = Text(frame, width=30, height=3, background="white")
    mid.grid(row=15, column=0, columnspan=2,sticky=W)
    note = Text(frame, width=30, height=3, background="white")
    note.grid(row=15, column=2, columnspan=2, pady=10, padx=10,sticky=W)
    surgery = Text(frame, width=30, height=3, background="white",)
    surgery.grid(row=15, column=1,pady=10, padx=10,sticky=W)
    phy = Text(frame, width=55, height=5, background="white")
    phy.grid(row=17, column=0, columnspan=2, sticky=W)
    treatment = Text(frame, width=55, height=5, background="white",)
    treatment.grid(row=19, column=0, columnspan=2,sticky=W)
    # ===================================button==============================================
    submit_B = Button(Buttonframe, text="save/حفظ", command=submit)
    submit_B.grid(row=0, column=0, pady=10, padx=10, ipadx=100)

    submit_B = Button(Buttonframe, text="Exit/إغلاق", command=exit_a)
    submit_B.grid(row=0, column=1, pady=10, padx=10, ipadx=100)
