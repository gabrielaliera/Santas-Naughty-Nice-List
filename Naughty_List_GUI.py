#This application creates a database system for children in the Naughty List

#==================================IMPORTS============================================

#import
from tkinter import *

#We need the followinf for message boxes
import tkinter.messagebox as mb
#We need the following for Treeview
import tkinter.ttk as ttk

#We need the following for icons
from PIL import ImageTk,Image

#import the Database class that was created in Naughty_List_Tkinter_create_database python file
from Naughty_List_Tkinter_create_database import Database


#==================================CALL DATABASE AND CREATE WINDOW============================================

#create a path a vairable
path="C:/Users/Owner/Desktop/CRUD_TKINTER_PROJECT_GABRIELA/"

#Create an object of Database class that we created in Tkinter_create_database_Gaby python file
db = Database(path+"THE_NAUGHTY_LIST.db")

#Create window object
root =Tk()
#Add a title to the window
root.title("North Pole Enterprise Inc.")
#Set the size of the window
root.geometry("815x630+351+174")

#Changing the icon of the window
root.iconbitmap(path+"icons/tree.ico")

#Upload image on window
load=Image.open(path+'icons/Santa.ico')
render=ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.image =render
img.place(x=570,y=30)


#Create label widget for the title
lblTitle = Label(root, 
                 text="***The Naughty List***",
                 font=("Helvetica", 16),
                 fg='white',
                 bg='green',
                 relief=RIDGE)


#==================================BUTTON METHODS============================================


#Delcare the functions that will be called in the command / For the different events

def register_student():
    if validate_entry() & validate_number() == True:
    #Call the insert method of the database class providing wtih values that are entered
        auto_capitalize()
        db.insert(entChildID.get(),
                  entFName.get(),
                  entLName.get(),
                  entCity.get(),
                  state_selected.get(),
                  entContactNo.get(),
                  behavior_selected.get())
    #Call the method clear_form() to clear all fields in the form
        clear_form()
    #Call the method load_student_data() to update list from database
        load_student_data()
    #Display message box to confirm registrataion
        mb.showinfo(title= "North Pole Enterprise Inc.",message='Child Successfully Registered')
    


#Will be called when update button clicked
def update_student_data():
    if validate_entry() & validate_number() == True:
        MsgBox = mb.askquestion(title='Update Record',message='Do you want to update selected child record?', icon='warning')
        if MsgBox == 'yes':
    #call the insert method of the database class providing it with the values that user entered
            auto_capitalize()
            db.update(entChildID.get(),
                      entFName.get(),
                      entLName.get(),
                      entCity.get(),
                      state_selected.get(),
                      entContactNo.get(),
                      behavior_selected.get())
    #Call method clear_form() that will clear all fields in the form
            clear_form()
    #Call the method load_student_data() to update list from database
            load_student_data()
    #Display message box to confirm registrataion
            mb.showinfo(title= "North Pole Enterprise Inc.",message='Record Successfully Updated')
    



#Will be called on when delete button clicked
def delete_student_data():
    #Validate entry and confirm delete action with a message box
    if validate_entry() == True:
        MsgBox = mb.askquestion(title='Delect Record',message='Are you sure! You want to delete selected child record?', icon='warning')
        if MsgBox == 'yes':
            db.remove(entChildID.get())
        #call the function clear_form
            clear_form()
        #call the function load_student_data() to update the list from database
            load_student_data()
        #Display message box to confirm delete record
            mb.showinfo(title= "North Pole Enterprise Inc.",message='Record Deleted Successfully')
   
#==================================VALIDATE METHODS============================================

#Will validate that entries contain information, if blank will display box and focus cursor to blank entry box
def validate_entry():
    #Validate Entry Widgets
    if entChildID.get() == "":
        mb.showinfo("Information", "Please Enter Child ID")
        entChildID.focus_set()
        validated = False
    elif entFName.get() == "":
        mb.showinfo("Information", "Please Enter First Name")
        entFName.focus_set()
        validated = False
    elif entLName.get() == "":
        mb.showinfo("Information", "Please Enter Last Name")
        entLName.focus_set()
        validated = False
    elif entCity.get() == "":
        mb.showinfo("Information", "Please Enter City")
        entCity.focus_set()
        validated = False
    elif state_selected.get() == "":
        mb.showinfo("Information","Please Enter State")
        validated = False
    elif entContactNo.get() == "":
        mb.showinfo("Information","Please Enter Contact Number")
        entContactNo.focus_set()
        validated = False
    else:
        validated = True
    
    return validated

#Validate that number entries only in parent's mobile
def validate_number():
    try:
        int(entContactNo.get())
        return True
    except ValueError:
        mb.showwarning(title='North Pole Entreprise Inc',message='Error: Phone Number entry is not a number')
        entContactNo.focus_set()

#Allows for only digits to be entered in ChildID entry
def onlyNum(entry):
    if entry.isdigit():
        number = True
    elif entry == '':
        number = True
    else:
        number = False

    return number

#Capitalize the first letter of each word on entry widgets
def auto_capitalize():
    ftext = FName_Text.get()
    ltext = LName_Text.get()
    ctext = City_Text.get()

    if " " in ftext:
        fpart = ftext.split(" ")
        FcapitalizeParts = [letter.capitalize() for letter in fpart]
        FcapitalizeWord = " ".join(FcapitalizeParts)
        FName_Text.set(FcapitalizeWord)
    else:
        FName_Text.set(FName_Text.get().capitalize())
        
    if " " in ltext:
        lpart = ltext.split(" ")
        LcapitalizeParts = [letter.capitalize() for letter in lpart]
        LcapitalizeWord = " ".join(LcapitalizeParts)
        LName_Text.set(LcapitalizeWord)
    else:
        LName_Text.set(LName_Text.get().capitalize())

    if " " in ctext:
        cpart = ctext.split(" ")
        CcapitalizeParts = [letter.capitalize() for letter in cpart]
        CcapitalizeWord = " ".join(CcapitalizeParts)
        City_Text.set(CcapitalizeWord)
    else:
        City_Text.set(City_Text.get().capitalize()) 
 

#================================== METHODS============================================


#Will be called in the commands of different buttons like register, update ,delete 
def clear_form():
#all character from index 0 to the end of entry will be deleted
    entChildID.delete(0,END)
    entFName.delete(0,END)
    entLName.delete(0,END)
    entCity.delete(0,END)
    state_selected.set(stateList[0])
    entContactNo.delete(0,END)
    behavior_selected.set("Naughty")

#Will be called when register, update, delete or insert records
def load_student_data():
    
    for row in tvChild.get_children():
        tvChild.delete(row)
    for row in db.fetch():
        ChildID = row[1]
        First_Name =row[2]
        Last_Name =row[3]
        City =row[4]
        State= row[5]
        Phone_Number= row[6]
        Behavior = row[7]
        tvChild.insert("",'end',text=ChildID,value=(ChildID, First_Name, Last_Name, City, State, Phone_Number, Behavior))


#Will call when exit button is clicked and a message box with display to confirm action
def exit():
    MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application?',icon='warning')
    if MsgBox == 'yes':
        #add close connection
        root.destroy()


def show_search_record():
    clear_form()
    userID = entSearch.get()
    
    if userID == "":
        mb.showwarning(title='Missing Information', message="Please Enter ChildID")  
        entSearch.focus_set()  
        return
    try:
        if entSearch.get().isdigit() == False:
            raise ValueError("Invalid Child ID.")
    
        values = db.searchID(userID)
    
        if not values:
            mb.showinfo(title='No Result Found',message='No ChildID Record Found')
            entSearch.focus_set()
        else:
            entChildID.insert(0,values[0][1])
            entFName.insert(0,values[0][2])
            entLName.insert(0,values[0][3])
            entCity.insert(0,values[0][4])
            state_selected.set(values[0][5])
            entContactNo.insert(0,values[0][6])
            behavior_selected.set(values[0][7])
    except ValueError as excpt:
        print(excpt)
        mb.showwarning(title='Error',message='Error: Child ID must be a number')
        entSearch.focus_set()
      

#Will be use in tree view
def show_selected_record(child):
    clear_form()
    for selection in tvChild.selection():
        item= tvChild.item(selection)
        global child_id
        child_id,first_name, last_name,city,state,contact_no, behavior = item["values"][0:7]
        entChildID.insert(0,child_id)
        entFName.insert(0, first_name)
        entLName.insert(0, last_name)
        entCity.insert(0, city)
        state_selected.set(state)
        entContactNo.insert(0, contact_no)
        behavior_selected.set(behavior)
    return child_id

#==================================LABEL WIDGET=======================================

#Create label widgets for each field
lblChildID = Label(root, text= 'Child ID:',font=('Helvetica',10))
lblFName = Label(root, text='First Name:', font=('Helvetica',10))
lblLName = Label(root, text='Last Name:', font=('Helvetica',10))
lblContactNo = Label(root, text= "Parent's Mobile:", font=('Helvetica',10))
lblCity = Label(root, text='City:', font=('Helvetica',10))
lblState = Label(root, text='State:', font=('Helvetica',10))

lblBehavior = Label(root, text="Behavior:", font=("Helvetica",10))

#Create label for select and search
lblSelect = Label(root, text='Please select one record below to update or delete', font=('Helvetica',10))
lblSearch= Label(root,text="Enter Child ID:", font=('Helvetica',10))

#==================================ENTRY WIDGET=====================================

FName_Text = StringVar()
LName_Text = StringVar()
City_Text = StringVar()

#Create entry widgets
entChildID=Entry(root)
entFName=Entry(root, textvariable= FName_Text )
entLName=Entry(root, textvariable= LName_Text)
entContactNo=Entry(root)
entCity=Entry(root, textvariable= City_Text)


#Register onlyNum function and configure ChildID entry to only accept numbers
reg= root.register(onlyNum)
entChildID.config(validate='key',validatecommand=(reg,'%P'))

#Create entry widget for the search
entSearch = Entry(root)

#==================================DROP DOWN WIDGET=====================================

stateList=["","AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
           "HI", "ID", "IL", "IN","IA", "KS", "KY", "LA", "ME", "MD",
           "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV","NH", "NJ",
           "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
           "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY" ]

#Define the selected variable for our drop down list of states 
state_selected=StringVar(root)

#set the default value for the option menu to the first item in the list 
state_selected.set(stateList[0])

#create an OptionMenu widget -drop down list for the state
stateOp=OptionMenu(root,state_selected,*stateList)

#==================================BUTTONS WIDGET=====================================

#Create button
btn_register = Button(root,text="Register",font=('Helvetica',11),bg='green',fg='white',
                      relief=RAISED, command=register_student)

btn_update =   Button(root,text="Update",font=('Helvetica',11),bg='green',fg='white',
                      relief=RAISED, command= update_student_data)

btn_delete =   Button(root,text="Delete",font=('Helvetica',11),bg='red',fg='white',
                      relief=RAISED, activebackground='green', command= delete_student_data)

btn_clear =    Button(root,text="Clear",font=('Helvetica',11), bg='green',fg='white',
                      relief=RAISED, command=clear_form)

btn_show_all = Button(root,text="Show All",font=('Helvetica',11),bg='green',fg='white',
                      relief=RAISED, command=load_student_data)

btn_search =   Button(root, text="Search", font=('Helvetica',11),bg='green',fg='white',
                      relief=RAISED, command=show_search_record)

btn_exit =     Button(root,text="Exit",font=('Helvetica',11), bg='green',fg='white',
                      relief=RAISED, command=exit)


#==================================RADIO BUTTON WIDGET=====================================

behavior_selected= StringVar()
behavior_selected.set("Naughty")

naughtyRB = Radiobutton(root,text="Naughty", variable=behavior_selected, value="Naughty")
vnaughtyRB = Radiobutton(root,text="Very Naughty", variable=behavior_selected, value="Very Naughty")
enaughtyRB = Radiobutton(root,text="Extremely Naughty", variable=behavior_selected, value="Extremely Naughty", fg='red')

#==================================TREEVIEW WIDGET=====================================

#specift a tuple columns
columns =("#1","#2","#3","#4","#5","#6","#7")


#Create the Trreviwq widget
tvChild = ttk.Treeview(root,
                         show="headings",
                         height="5", columns=columns)

#specify the heading the corresponding columns
tvChild.heading('#1',text="ChildID",anchor='center')
tvChild.column('#1',width=60,anchor='center', stretch=False)

tvChild.heading('#2',text="FirstName",anchor='center')
tvChild.column('#2',width=60,anchor='center', stretch=True)

tvChild.heading('#3',text="LastName",anchor='center')
tvChild.column('#3',width=60,anchor='center', stretch=True)

tvChild.heading('#4',text="City",anchor='center')
tvChild.column('#4',width=60,anchor='center', stretch=True)

tvChild.heading('#5',text="State",anchor='center')
tvChild.column('#5',width=60,anchor='center', stretch=True)

tvChild.heading('#6',text="Phone Number",anchor='center')
tvChild.column('#6',width=60,anchor='center', stretch=True)

tvChild.heading('#7',text="Behavior",anchor='center')
tvChild.column('#7',width=60,anchor='center', stretch=True)


##Add scroll bar
vsb= ttk.Scrollbar(root, orient=VERTICAL,
                   command=tvChild.yview)

#place the vsd
vsb.place(x=40 + 640 +1, y=275, height= 180 +20)

#Configure the treeview to use the vsd for y axis scroll bar
tvChild.configure(yscroll=vsb.set)

#Create the horizontal scrollbar
hsb = ttk.Scrollbar(root,orient=HORIZONTAL,
                    command=tvChild.xview)
#place the hsb
hsb.place(x=40,y=275+200+1,width=620 +20)

#Configure the treeview to use the hsb for x axis scroll bar
tvChild.configure(xscroll=hsb.set)

#Style Treeview
style =ttk.Style()
style.theme_use('clam')

##bind the treeview to the function show_selected_record
tvChild.bind("<<TreeviewSelect>>",show_selected_record)


#==================================PLACE LABEL WIDGET=====================================

#Place the labels

lblTitle.place(x=250,y=15,height=27,width=300)

lblChildID.place(x=24,y=60,height=23,width=100)
lblFName.place(x=15,y=90,height=23,width=100)
lblLName.place(x=15,y=120,height=23,width=100)

lblContactNo.place(x=310,y=60,height=23,width=104)
lblCity.place(x=360,y=90,height=23,width=65)
lblState.place(x=355,y=120,height=23,width=71)

lblBehavior.place(x=35,y=150,height=23,width=71)

lblSelect.place(x=150, y=225, height=23, width=400)
lblSearch.place(x=174,y=510,height=23,width=134)

#==================================PLACE ENTRY WIDGET=====================================
#Place entry widgets
entChildID.place(x=120,y=62,height=21,width=186)
entFName.place(x=120,y=92,height=21,width=186)
entLName.place(x=120,y=120,height=21,width=186)

entContactNo.place(x=415,y=62,height=21,width=186)
entCity.place(x=415,y=92,height=21,width=186)
stateOp.place(x=415,y=122,height=21,width=186)

entSearch.place(x=310, y=510, height=21, width=186)

#==================================PLACE BUTTONS WIDGET=====================================
#Place the button widgets
btn_register.place(x=90,y=185,height=25,width=76)
btn_update.place(x=170,y=185,height=25,width=76)
btn_delete.place(x=260,y=185,height=25,width=76)
btn_clear.place(x=348,y=185,height=25,width=76)
btn_show_all.place(x=430,y=185,height=25,width=76)

btn_search.place(x=498,y=510,height=26,width=76)
btn_exit.place(x=320,y=550,height=31,width=60)

#==================================RADIOBUTTONS WIDGET=====================================
#Place radio buttons
naughtyRB.place(x=115,y=150)
vnaughtyRB.place(x=200,y=150)
enaughtyRB.place(x=310,y=151)
#==================================PLACE TREEVIEW WIDGET=====================================

#Place the treeview widgets
tvChild.place(x=40,y=275,height=200,width=640)

#==================================MAIN LOOP=====================================

#Call load_student_data to always show records on treeview
load_student_data()


#Call the mainloop()
root.mainloop()