from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Password Manager")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg="white")



##################################VARIABLES#############################################
records = []
m = 0


##################################FUNCTIONS#############################################

#-----------------------------Add Record Function---------------------------------------
def add_record():
    global m
    m+=1
    app_name = application_name_ent.get()
    url = url_ent.get()
    email_id = email_id_ent.get()
    password = password_ent.get()
    record = f" {m}: App Name: {app_name}, URL: {url}, Email Id: {email_id}, Password: {password}"
    records.append(record)
    messagebox.showinfo("Record Added", "Record has been added successfully!")
    show_record()  # update the label with the new record


#--------------------------------Show Record Function-------------------------------------
def show_record():
    record_lbl.config(text="\n".join(records))
    hide_record_btn = Button(root, text="Hide Records", bg='gray', fg='black', font=('Segoe UI', 12), command=hide_record)
    hide_record_btn.place(x=201, y=116, width=160, height=27)


#---------------------------------Hide Record Function---------------------------------------
def hide_record():
    record_lbl.config(text="")
    show_record_btn = Button(root, text="Show Records", bg='gray', fg='black', font=('Segoe UI', 12), command=show_record)
    show_record_btn.place(x=201, y=116, width=160, height=27)


#---------------------------------Delete Record Function---------------------------------------
def delete_record():
    global m
    m-=1
    try:
        index = int(delete_record_ent.get()) - 1
        records.pop(index)
        messagebox.showinfo("Record Deleted", "Record has been deleted successfully!")
        show_record()  # update the label with the updated records list
    except IndexError:
        messagebox.showerror("Error", "Invalid record index")
    except ValueError:
        messagebox.showerror("Error", "Invalid record index")


#--------------------------------Edit Record Function------------------------------------------
def edit_record():
    try:
        index = int(edit_box.get()) - 1
        app_name = application_name_ent.get()
        url = url_ent.get()
        email_id = email_id_ent.get()
        password = password_ent.get()
        record = f"App Name: {app_name}, URL: {url}, Email Id: {email_id}, Password: {password}"
        records[index] = record
        messagebox.showinfo("Record Updated", "Record has been updated successfully!")
        show_record()  # update the label with the updated records list
    except IndexError:
        messagebox.showerror("Error", "Invalid record index")
    except ValueError:
        messagebox.showerror("Error", "Invalid record index")



##########################################LABELS#######################################################
application_name_lbl = Label(text="Application Name", fg='black', bg='white', font=('Segoe UI', 12))
application_name_lbl.place(x=39, y=4)

url_lbl = Label(text="URL", fg='black', bg='white', font=('Segoe UI', 12))
url_lbl.place(x=77, y=30)

email_id_lbl = Label(text="Email Id", fg='black', bg='white', font=('Segoe UI', 12))
email_id_lbl.place(x=67, y=56)

password_lbl = Label(text="Password", fg='black', bg='white', font=('Segoe UI', 12))
password_lbl.place(x=63, y=82)

record_lbl = Label(text="", bg='light gray',fg='black',font=('Segoe UI', 12), wraplength=580)
record_lbl.place(x=10, y=240, width=580, height=130)



##############################################BUTTONS#############################################################
add_record_btn = Button(root, text="Add Record", bg='green', fg='black', font=('Segoe UI', 12), command=add_record)
add_record_btn.place(x=16, y=116, width=145, height=27)

edit_record_btn = Button(root, text="Edit Record", bg='orange', fg='black', font=('Segoe UI', 12), command=edit_record)
edit_record_btn.place(x=16, y=154, width=145, height=27)

delete_record_btn = Button(root, text="Delete Record", bg='red', fg='black', font=('Segoe UI', 12), command=delete_record)
delete_record_btn.place(x=16, y=192, width=145, height=27)

show_record_btn = Button(root, text="Show Records", bg='gray', fg='black', font=('Segoe UI', 12), command=show_record)
show_record_btn.place(x=201, y=116, width=160, height=27)

hide_record_btn = Button(root, text="Hide Records", bg='gray', fg='black', font=('Segoe UI', 12), command=hide_record)



#######################################################ENTRY BOX########################################################
application_name_ent = Entry(bg='white', font=('Segoe UI', 12))
application_name_ent.place(x=191, y=4, width=180)

url_ent = Entry(bg='white', font=('Segoe UI', 12))
url_ent.place(x=191, y=30, width=180)

email_id_ent = Entry(bg='white', font=('Segoe UI', 12))
email_id_ent.place(x=191, y=56, width=180)

password_ent = Entry(bg='white', font=('Segoe UI', 12))
password_ent.place(x=191, y=82, width=180)

edit_box = Entry(bg='white', font=('Segoe UI', 12))
edit_box.place(x=191, y=154, width=180)

delete_record_ent = Entry(bg='white', font=('Segoe UI', 12))
delete_record_ent.place(x=191, y=192, width=180)

#################################IMAGE######################################
img = PhotoImage(file='Program manager img.png')
Label(root,image=img,border=0,bg='white',width=189,height=210).place(x=390,y=8)
 

root.mainloop()
