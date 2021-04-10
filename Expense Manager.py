from tkinter import *
import tkinter.messagebox as tmsg

#--------============== front page ================---------#

def first():

    def getval():
        print(f"{nameval.get(), passsval.get()}")
        next_page()

    root = Tk()
    root.geometry('578x311')  # (widthxhieght)
    root.minsize(200, 250)  # (width, hieght)
    root.maxsize(750, 600)  # (width, hieght)
    root.title("Akash's GUI")

    f = Frame(root, bg="light green", borderwidth=6, relief=SUNKEN, pady=10, padx=65)
    f.grid()

    Label(f, text="Golmal Khatabook", bg="light grey", fg="black", padx=45, pady=10, font="comicsansms 16 bold",
          borderwidth=5, relief=RIDGE).grid(row=0, column=1)
    Label(f, text="Welcome to Golmal Khatabook", bg="pink", fg="red", padx=40, font="comicsansms 10 bold",
          borderwidth=4, relief=SUNKEN).grid(row=1, column=1, padx=15, pady=10)

    name = Label(f, text="Username -> ", font="comicsansms 12", padx=10, pady=3, borderwidth=3, relief=RAISED,
                 fg="blue", bg="sky blue")
    passs = Label(f, text="Password -> ", font="comicsansms 12", padx=11, pady=3, borderwidth=3, relief=RAISED,
                  fg="blue", bg="sky blue")

    name.grid(row=2, column=0, pady=3)
    passs.grid(row=3, column=0)

    nameval = StringVar()
    passsval = StringVar()

    nameentry = Entry(f, textvariable=nameval)
    passsentry = Entry(f, textvariable=passsval)

    nameentry.grid(row=2, column=1)
    passsentry.grid(row=3, column=1)

    Button(f, text="Log In", font="arial 11 bold", padx=5, pady=1, borderwidth=5, relief=RAISED, command=getval).grid(
        row=4, column=1, pady=20)

    Button(f, text="Not a user? Register Here", font="arial 10 bold", padx=5, pady=1, borderwidth=5, relief=RAISED,
           command=reg).grid(row=5, column=1)

    root.mainloop()

def reg():
    def regval():
        print (f"{ nameval.get(), emailval.get(), userval.get(), passsval.get(), tncval.get()}")
        z = tmsg.showinfo("Registraion Status", "Registration Successful !!!")

    root = Tk()
    root.geometry('620x340')  # (widthxhieght)
    root.minsize(200, 250)  # (width, hieght)
    root.maxsize(700, 700)  # (width, hieght)
    root.title("Registration Window")

    f1 = Frame(root, bg="light green", borderwidth=6, relief=SUNKEN, pady=10, padx=65)
    f1.grid()

    Label(f1, text="Golmal Khatabook", bg="light grey", fg="black", padx=45, pady=10, font="comicsansms 16 bold",
          borderwidth=5, relief=RIDGE).grid(row=0, column=1, pady=10)

    name = Label(f1, text="Name -> ", font="comicsansms 12", padx=38, pady=3, borderwidth=3, relief=RAISED, fg="blue",
                 bg="sky blue")
    email = Label(f1, text="Email id -> ", font="comicsansms 12", padx=30, pady=3, borderwidth=3, relief=RAISED,
                  fg="blue", bg="sky blue")
    user = Label(f1, text="Username -> ", font="comicsansms 12", padx=24, pady=3, borderwidth=3, relief=RAISED,
                 fg="blue", bg="sky blue")
    passs = Label(f1, text="Set Password -> ", font="comicsansms 12", padx=10, pady=3, borderwidth=3, relief=RAISED,
                  fg="blue", bg="sky blue")

    name.grid(row=1, column=0, padx=20)
    user.grid(row=3, column=0, padx=20)
    email.grid(row=2, column=0, padx=20)
    passs.grid(row=4, column=0, padx=20)

    nameval = StringVar()
    userval = StringVar()
    emailval = StringVar()
    passsval = StringVar()
    tncval = IntVar()

    nameentry = Entry(f1, textvariable=nameval)
    userentry = Entry(f1, textvariable=userval)
    emailentry = Entry(f1, textvariable=emailval)
    passsentry = Entry(f1, textvariable=passsval)

    nameentry.grid(row=1, column=1, )
    userentry.grid(row=3, column=1)
    emailentry.grid(row=2, column=1)
    passsentry.grid(row=4, column=1)

    # ---------------------Check Button--------------------------------------------------------

    tnc = Checkbutton(f1, text="I have read all Terms and conditions.", font="comicsansms 10", padx=26, pady=3,
                      borderwidth=3, relief=RAISED, fg="black", bg="light grey", variable=tncval)
    tnc.grid(row=5, column=1, pady=13)

    # ----------------------------Submit Button---------------------------------------------------------------

    Button(f1, text="Sign Up", font="elephant 12 bold", padx=5, pady=5, borderwidth=5, relief=RAISED,
           command=regval).grid(row=6, column=1)
    root.mainloop()

def check():
    pass

def add():
    r = Tk()
    r.geometry('345x567')  # (widthxhieght)
    r.minsize(345, 567)  # (width, hieght)
    r.maxsize(345, 567)  # (width, hieght)
    r.title("Add txn GUI")

    def addval():
        print(f"{var.get(), var2.get(), var3.get(), amount_val.get(), date_val.get(), rem_val.get()}")
    # -----------------------------------------------------------------

    f2 = Frame(r, bg="light green", borderwidth=6, relief=SUNKEN, pady=10, padx=65)
    f2.grid()
    Label(f2, text="Select ", font="comicsansms 12", padx=5, pady=3, borderwidth=2, relief=SUNKEN, fg="black",
          bg="light grey").grid(row=0, column=0, padx=20, pady=5)
    var = StringVar()
    var.set(1)
    a = Radiobutton(f2, text="Debit", variable=var, value="Debit", padx=3).grid(row=0, column=1, padx=20)
    a = Radiobutton(f2, text="Credit", variable=var, value="Credit").grid(row=1, column=1)

    # -------------------------------------------------------------------------

    f3 = Frame(r, bg="yellow", borderwidth=6, relief=SUNKEN, pady=10, padx=54)
    f3.grid()
    Label(f3, text="Mode ", font="comicsansms 12", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",
          bg="light grey").grid(row=3, column=0, padx=10, pady=5)
    var2 = StringVar()
    var2.set(1)
    b = Radiobutton(f3, text="UPI", variable=var2, value="UPI", padx=24).grid(row=3, column=1, padx=20)
    b = Radiobutton(f3, text="Net Banking", variable=var2, value="Net Banking").grid(row=4, column=1, pady=3)
    b = Radiobutton(f3, text="Cash", variable=var2, value="Cash", padx=21).grid(row=5, column=1, pady=5)

    # ===========================================----------

    f4 = Frame(r, bg="cyan", borderwidth=6, relief=SUNKEN, pady=6, padx=55)
    f4.grid()
    Label(f4, text="spent on ", font="comicsansms 12", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",
          bg="light grey").grid(row=6, column=0, padx=5, pady=7)
    var3 = StringVar()
    var3.set(1)
    c = Radiobutton(f4, text="Food", variable=var3, value="Food", padx=15).grid(row=6, column=1, padx=20)
    c = Radiobutton(f4, text="Travel", variable=var3, value="Travel", padx=12).grid(row=7, column=1)
    c = Radiobutton(f4, text="Other", variable=var3, value="Other", padx=12).grid(row=8, column=1, pady=8)

    # ===================-----------------------------------

    f5 = Frame(r, bg="red", borderwidth=6, relief=SUNKEN, pady=10, padx=10)
    f5.grid()

    Label(f5, text="Amount ", font="comicsansms 12", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",
          bg="light grey").grid(row=9, column=0, padx=10, pady=10)
    amount_val = StringVar()
    amountentry = Entry(f5, textvariable=amount_val)
    amountentry.grid(row=9, column=1)

    Label(f5, text="Date (YYYY-MM-DD)", font="comicsansms 12", padx=10, pady=3, borderwidth=2, relief=SUNKEN,
          fg="black", bg="light grey").grid(row=10, column=0, padx=10, pady=5)
    date_val = StringVar()
    dateentry = Entry(f5, textvariable=date_val)
    dateentry.grid(row=10, column=1)

    Label(f5, text="Remarks ", font="comicsansms 12", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",
          bg="light grey").grid(row=11, column=0, padx=10, pady=5)
    rem_val = StringVar()
    rementry = Entry(f5, textvariable=rem_val)
    rementry.grid(row=11, column=1)

    Button(f5, text="Submit", font="elephant 12 bold", padx=5, pady=1, borderwidth=5, relief=RAISED,
           command=addval).grid(row=12, column=1, pady=2)

    r.mainloop()
#----------------------------------------------------------------------

def view():
    import tkinter.messagebox as tmsg

    root = Tk()
    root.geometry('510x595')  # (widthxhieght)
    root.minsize(200, 250)  # (width, hieght)
    root.maxsize(750, 1000)  # (width, hieght)
    root.title("View txn GUI")

    def viewall():
        a = tmsg.showinfo("All txn ", "Loading All transaction ... ")
        print(a)

    def view5():
        a = tmsg.showinfo("Last 5 txn ", "Loading Last 5 transaction ... ")
        print(a)

    def date():
        print (f"From Date - : {from_date_val.get()}")
        print (f" To Date  - : {to_date_val.get()}")

    def credit():
        a = tmsg.showinfo("Credit txn ", "Loading all credited transaction ... ")
        print(a)

    def debit():
        b = tmsg.showinfo("Debit txn ", "Loading all debited transaction ... ")
        print(b)

    def upi():
        b = tmsg.showinfo("UPI txn ", "Loading all UPI transaction ... ")
        print(b)

    def nb():
        b = tmsg.showinfo("Net Banking txn ", "Loading all Net Banking transaction ... ")
        print(b)

    def cash():
        b = tmsg.showinfo("Cash txn ", "Loading all Cash transaction ... ")
        print(b)

    #--------------------------------------------------------------

    f2 = Frame(root, bg="light green", borderwidth=6, relief=SUNKEN, pady=5, padx=63)
    f2.grid()

    var1 = StringVar()
    var1.set(1)
    Label(f2, text="To View all transaction ->", font="comicsansms 12", padx=20, pady=3, borderwidth=2, relief=SUNKEN, fg="black",bg="light grey").grid(row=0, column=0, padx=10, pady=10)

    Button(f2, text="Click Here", font="elephant 12 bold", padx=5, pady=1, borderwidth=5, relief=RAISED,
        command=viewall).grid(row=0, column=1, pady=2)

    Label(f2, text="To view last 5 transactions ->", font="comicsansms 12", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",bg="light grey").grid(row=1, column=0, padx=10, pady=10)
    Button(f2, text="Click Here", font="elephant 12 bold", padx=5, pady=1, borderwidth=5, relief=RAISED,
        command=view5).grid(row=1, column=1, pady=2)

    #------------------------------------------------

    f3 = Frame(root, bg="yellow", borderwidth=6, relief=SUNKEN, pady=5, padx=40)
    f3.grid()

    Label(f3, text="To view transactions within Dates ->", font="comicsansms 12", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",bg="light grey").grid(row=2, column=0, padx=10, pady=5)

    Label(f3, text="From Date (YYYY-MM-DD) ->", font="comicsansms 10", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",bg="light grey").grid(row=3, column=0, padx=10, pady=2)
    Label(f3, text="To Date (YYYY-MM-DD) ->", font="comicsansms 10", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",bg="light grey").grid(row=4, column=0, padx=10, pady=2)


    from_date_val = StringVar()
    from_date_entry = Entry(f3, textvariable=from_date_val)
    from_date_entry.grid(row=3, column=1)

    to_date_val = StringVar()
    to_date_entry = Entry(f3, textvariable=to_date_val)
    to_date_entry.grid(row=4, column=1)

    Button(f3, text="Submit", font="arial 10 bold", padx=5, pady=1, borderwidth=5, relief=RAISED,
        command=date).grid(row=5, column=0, pady=5)

    #----------------------------------------------------

    f4 = Frame(root, bg="cyan", borderwidth=6, relief=SUNKEN, pady=8, padx=110)
    f4.grid()

    Label(f4, text="To view all transactions by Type ->", font="comicsansms 12", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",bg="light grey").grid(row=2, column=0, padx=10, pady=10)

    Button(f4, text="Credit",font = "comicsansms 10 italic", borderwidth=3, relief =RAISED, padx=10, command=credit).grid(row =6, column=0)
    Button(f4, text="Debit",font = "comicsansms 10 italic", borderwidth=3, relief =RAISED, padx=12, command=debit).grid(row =7, column=0, pady=2)

    #----------------------------------------------------------

    f5 = Frame(root, bg="red", borderwidth=6, relief=SUNKEN, pady=8, padx=105)
    f5.grid()

    Label(f5, text="To view all transactions by Mode ->", font="comicsansms 12", padx=10, pady=3, borderwidth=2, relief=SUNKEN, fg="black",bg="light grey").grid(row=6, column=0, padx=10, pady=10)

    Button(f5, text="UPI",font = "comicsansms 10 italic", borderwidth=3, relief =RAISED, padx=30, command=upi).grid(row =7, column=0)
    Button(f5, text="Net Banking",font = "comicsansms 10 italic", borderwidth=3, relief =RAISED, padx=5,command=nb).grid(row =8, column=0, pady=2)
    Button(f5, text="Cash",font = "comicsansms 10 italic", borderwidth=3, relief =RAISED, padx=27, command=cash).grid(row =9, column=0)


    root.mainloop()

#=============================second page ===============================

def next_page():
    root = Tk()
    root.geometry ('493x225')  # (widthxhieght)
    root.minsize(200, 100)  # (width, hieght)
    root.maxsize(750, 600)  # (width, hieght)

    f1 = Frame(root, bg="light Green", borderwidth=6, relief=SUNKEN)  # frame makes blocks in our GUI window
    f1.grid()

    Label(f1, text="What do you wish to do ?", font="comicsansms 12", padx=10, pady=3, borderwidth=3, relief=RAISED,fg="black", bg="light grey").grid(row=0, column=1, pady=20, padx=160)
    b1 = Button(f1, fg="red", text="Add Txn", padx=5, pady=5, borderwidth=5, relief=RAISED, command=add)
    b1.grid(row=1, column=1, padx=20)
    b2 = Button(f1, fg="red", text="View Txn", padx=5, pady=5, borderwidth=5, relief=RAISED, command=view)
    b2.grid(row=2, column=1, padx=20, pady=30)

    root.title("second page GUI")

first()