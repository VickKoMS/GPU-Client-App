from tkinter import *
from tkinter import Tk
from tkinter import ttk
from views import *
from tkinter import messagebox
#from tkcalendar import *

#colors
co0 = "#ffffff" #White
co1 = "#000000"
co2 = "#1100F0" 
co3 = "#999999"
co4 = "#FFFF00"

window = Tk ()
window.title ("")
window.geometry("490x700")
window.configure(background=co0)
window.resizable(width=False, height=False)


#frames
frame_up = Frame(window, width=484, height=40, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=484, height=180, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_between = Frame(window, width=484, height=40, bg=co2)
frame_between.grid(row=2, column=0, padx=0, pady=1)

frame_client = Frame(window, width=484, height=140, bg=co0)
frame_client.grid(row=3, column=0, padx=0, pady=1)

frame_table = Frame(window, width=484, height=300, bg=co3, relief="flat") # relif solved the problem with the table
frame_table.grid(row=4, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

#functions

def show():
    global tree
    
    list_header = ["Car Maker", "Model", "VIN", "Plate", "Year", 
                   "First Name", "Last Name", "IDNP", "Email"]
    
    demo_list = view()
    
    tree = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")
    
    vertical_bar = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    horizontal_bar = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
    
    tree.configure(yscrollcommand=vertical_bar.set, xscrollcommand=horizontal_bar.set)
    
    tree.grid(column=0, row=0, sticky=NSEW) # NSEW are coordinates
    vertical_bar.grid(column=1, row=0, sticky=NS)
    horizontal_bar.grid(column=0, row=1, sticky=EW)
    
    #tree head
    tree.heading(0, text="Car Maker", anchor=NW)
    tree.column(0, width=40, anchor=NW)
    
    tree.heading(1, text="Model", anchor=NW)
    tree.column(1, width=40, anchor=NW)
    
    tree.heading(2, text="VIN", anchor=NW)
    tree.column(2, width=40, anchor=NW)
    
    tree.heading(3, text="Plate", anchor=NW)
    tree.column(3, width=40, anchor=NW)
    
    tree.heading(4, text="Year", anchor=NW)
    tree.column(4, width=40, anchor=NW)
    
    tree.heading(5, text="First Name", anchor=NW)
    tree.column(5, width=90, anchor=NW)
    
    tree.heading(6, text="Last Name", anchor=NW)
    tree.column(6, width=90, anchor=NW)
    
    tree.heading(7, text="IDNP", anchor=NW)
    tree.column(7, width=40, anchor=NW)
    
    tree.heading(8, text="Email", anchor=NW)
    tree.column(8, width=40, anchor=NW)
    
    for item in demo_list:
        tree.insert("","end", values=item)
       
show()

def insert():
    Car_Maker = entry_maker.get()
    Model = entry_model.get()
    Vin = entry_vin.get()
    Plate = entry_plate.get()
    Year = entry_year.get()
    First_Name = entry_name.get()
    Last_Name = entry_last.get()
    Idnp = entry_idnp.get()
    Email = entry_email.get()
    
    data = [Car_Maker, Model, Vin, Plate, Year, 
            First_Name,Last_Name, Idnp, Email]
    
    if Car_Maker == "" or Model == "" or Vin == "" or Plate == "" or Year == "" or First_Name == "" or Last_Name == "" or Idnp == "" or Email == "":
        messagebox.showwarning("data", "Please fill in all fields!")
        
    else:
        add(data)
        messagebox.showinfo("data", "Data was added succesfully!")
        
        entry_maker.delete(0, "end")
        entry_model.delete(0, "end")
        entry_vin.delete(0, "end")
        entry_plate.delete(0, "end")
        entry_year.delete(0, "end")
        entry_name.delete(0, "end")
        entry_last.delete(0, "end")
        entry_idnp.delete(0, "end")
        entry_email.delete(0, "end")
        
        show()
 
def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary["values"]
        
        Car_Maker = str(tree_list[0])
        Model = str(tree_list[1]) 
        Vin = str(tree_list[2]) 
        Plate = str(tree_list[3]) 
        Year = str(tree_list[4]) 
        First_Name = str(tree_list[5]) 
        Last_Name = str(tree_list[6]) 
        Idnp = str(tree_list[7]) 
        Email = str(tree_list[8])
        
        entry_maker.insert(0, Car_Maker)
        entry_model.insert(0, Model)
        entry_vin.insert(0, Vin)
        entry_plate.insert(0, Plate)
        entry_year.insert(0, Year)
        entry_name.insert(0, First_Name)
        entry_last.insert(0, Last_Name)
        entry_idnp.insert(0, Idnp)
        entry_email.insert(0, Email)
        
        def confirm():
            new_car_maker = entry_maker.get()
            new_model = entry_model.get()
            new_vin = entry_vin.get()
            new_plate = entry_plate.get()
            new_year = entry_year.get()
            new_first_name = entry_name.get()
            new_last_name = entry_last.get()
            new_idnp = entry_idnp.get()
            new_email = entry_email.get()
            
            data = [new_vin, new_car_maker, new_model, new_vin, new_plate, new_year,
                    new_first_name, new_last_name, new_idnp, new_email]
            
            update(data)
            
            messagebox.showinfo("Success", "Data was updated successfully!")
            
            entry_maker.delete(0, "end")
            entry_model.delete(0, "end")
            entry_vin.delete(0, "end")
            entry_plate.delete(0, "end")
            entry_year.delete(0, "end")
            entry_name.delete(0, "end")
            entry_last.delete(0, "end")
            entry_idnp.delete(0, "end")
            entry_email.delete(0, "end")
            
            for widget in frame_table.winfo_children():
                widget.destroy()
            
        b_confirm.destroy()
            
        b_confirm = Button(frame_down, text="Confirm", width=8, height=1,  bg=co0, font="Ivy 8 bold", command=confirm)
        b_confirm.place(x=240, y=400)
            
        show(b_confirm)
       
    except IndexError:
        messagebox.showerror("Error", "Select one from the table!")    

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary["values"]
        tree_vin = str(tree_list[2])
        
        remove(tree_vin)
        
        messagebox.showinfo("Success", "Data has been deleted successfuly!")
        
        for widget in frame_table.winfo_children():
            widget.destroy()
            
        show()
        
    except IndexError:
        messagebox.showerror("Error", "Select one from the table!")

def to_search():
    vin = e_search.get()
    
    data = search(vin)
    
    def delete_command():
        tree.delete(*tree.get_children())
    
    delete_command()
    
    for item in data:
        tree.insert("", "end", values=item)
        
    e_search.delete(0, "end")   
    
                               
#frame_up widgets

app_name = Label(frame_up, text="CAR REGISTERING", height=1, font=('Verdana 17 bold'),bg=co2, fg=co0)
app_name.place(x=4, y=4)

#frame_between widgets
client_name = Label(frame_between, text=("CLIENT REGISTERING"), height=1, font=('Verdana 17 bold'),bg=co2, fg=co0)
client_name.place(x=4,y=4)
#frame_down widgets

#Car Maker
label_car_maker = Label(frame_down, text="Car Maker:", width=10, height=1, font=('Ivy 10 bold'), bg=co0, anchor=NW )
label_car_maker.place(x=5, y=20)
entry_maker = ttk.Combobox(frame_down, width=20)
entry_maker['values'] = ["Acura", "Alfa-Romeo", "Aston Martin", "Audi", "BMW", "Bentley", "Buick",
                      "Cadilac", "Chevrolet", "Chrysler", "Daewoo", "Daihatsu", "Dodge", "Eagle",
                      "Ferrari", "Fiat", "Fisker", "Ford", "Freighliner","GMC - General Motors Company",
                      "Genesis", "Geo", "Honda", "Hummer", "Hyundai", "Infinity", "Isuzu", "Jaguar",
                      "Jeep", "Kla", "Lamborghini", "Land Rover", "Lexus", "Lincoln", "Lotus", "Mazda",
                      "Maserati", "Maybach", "McLaren", "Mercedez-Benz", "Mercury", "Mini", "Mitsubishi",
                      "Nissan", "Oldsmobile", "Panoz", "Plymouth", "Polestar", "Pontiac", "Porsche", "Ram",
                      "Rivian", "Rolls_Royce", "Saab", "Saturn", "Smart", "Subaru", "Susuki", "Tesla", 
                      "Toyota", "Volkswagen", "Volvo"]
entry_maker.place(x=100, y=20)

#Model
label_model = Label(frame_down, text="Model:", width=10, height=1, font=('Ivy 10 bold'), bg=co0, anchor=NW)
label_model.place(x=5, y=50)
entry_model = Entry(frame_down, width=20, justify="left", highlightthickness=1, relief="solid")
entry_model.place(x=100, y=50)

#VIN Number
label_vin = Label(frame_down, text="VIN:", width=10, height=1, font=("Ivy 10 bold"), bg=co0, anchor=NW)
label_vin.place(x=5, y=80)
entry_vin = Entry(frame_down, width=20, justify="left", highlightthickness=1, relief="solid")
entry_vin.place(x=100, y=80)

#Plate Number
label_plate = Label(frame_down, text="Plate:", width=10, height=1, font=("Ivy 10 bold"), bg=co0, anchor=NW)
label_plate.place(x=5, y=110)
entry_plate = Entry(frame_down, width=20, justify="left", highlightthickness=1, relief="solid")
entry_plate.place(x=100, y=110)

#Color
label_color = Label(frame_down, text="Color:", width=10, height=1, font=("Ivy 10 bold"), bg=co0, anchor=NW)
label_color.place(x=5, y=140)
entry_color = Entry(frame_down, width=20, justify="left", highlightthickness=1, relief="solid")
entry_color.place(x=100, y=140)

#Year, to create a calendar for this
label_year = Label(frame_down, text="Year:", width=10, height=1, font=("Ivy 10 bold"), bg=co0, anchor=NW)
label_year.place(x=5, y=140)
entry_year = Entry(frame_down, width=20, justify="left", highlightthickness=1, relief="solid")
entry_year.place(x=100, y=140)

#----------------------------------------------------------------

#First Name in Frame Client
label_name = Label(frame_client, text="First Name:", width=10, height=1, font=("Ivy 10 bold"), bg=co0, anchor=NW)
label_name.place(x=5, y=10)
entry_name = Entry(frame_client, width=20, justify="left", highlightthickness=1, relief="solid")
entry_name.place(x=100, y=10)

#Last Name
label_last = Label(frame_client, text="Last Name:", width=10, height=1, font=("Ivy 10 bold"), bg=co0, anchor=NW)
label_last.place(x=5, y=40)
entry_last = Entry(frame_client, width=20, justify="left", highlightthickness=1, relief="solid")
entry_last.place(x=100, y=40)

#IDNP
label_idnp = Label(frame_client, text="IDNP:", width=10, height=1, font=("Ivy 10 bold"), bg=co0, anchor=NW)
label_idnp.place(x=5, y=70)
entry_idnp = Entry(frame_client, width=20, justify="left", highlightthickness=1, relief="solid")
entry_idnp.place(x=100, y=70)

#Date of Birth, We do not need it... Email is better
label_email = Label(frame_client, text="Email:", width=10, height=1, font=("Ivy 10 bold"), bg=co0, anchor=NW)
label_email.place(x=5, y=100)
entry_email = Entry(frame_client, width=20, justify="left", highlightthickness=1, relief="solid")
entry_email.place(x=100, y=100)

#-----------------------------------------------------------------

#Button
b_search = Button(frame_down, text="Search:", height=1,  bg=co0, font="Ivy 8 bold", command=to_search)
b_search.place(x=280, y=20)
e_search = Entry(frame_down, width=14, justify="left", font=("Ivy", 11), highlightthickness=1, relief="solid")
e_search.place(x=340, y=20)

b_add = Button(frame_down, text="Add", width=8, height=1,  bg=co0, font="Ivy 8 bold", command=insert)
b_add.place(x=270, y=70)

b_edit = Button(frame_down, text="Edit", width=8, height=1,  bg=co0, font="Ivy 8 bold", command=to_update)
b_edit.place(x=270, y=100)

b_delete = Button(frame_down, text="Delete", width=8, height=1,  bg=co0, font="Ivy 8 bold", command=to_remove)
b_delete.place(x=270, y=130)

b_view = Button(frame_down, text="View", width=8, height=1,  bg=co0, font="Ivy 8 bold", command=show)
b_view.place(x=370, y=70)


#--------------------------------------------------------------------



window.mainloop()

