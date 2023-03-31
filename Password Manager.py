from tkinter import *
from tkinter import messagebox
import ast
try:
    root =Tk()
    root.title('Login and Signup Page')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)










    #################################FUNCTIONS####################################################

    #--------------------------------Main Program------------------------------------------------#
    def password_manager():
        root = Tk()
        root.title("Password Manager")
        root.geometry("600x400")
        root.resizable(False, False)
        root.configure(bg="white")



        ##################################VARIABLES#############################################
        records = []
        global m
        m = 0



        ##################################FUNCTIONS#############################################

        #-----------------------------Add Record Function---------------------------------------
        def add_record():
            global m
            m +=1
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
        
    #####################################################################################################








    #######################################################################################################
    #----------------------------Sign Up------------------------------------------------#
    def signup_command():
        window=Tk()
        window.title("SignUp")
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        def signup ():
            username=user.get()
            password=code.get()
            confirm_password=confirm_code.get()

            if password==confirm_password:
                try:
                    file=open('datasheet.txt','r+')
                    d=file.read()
                    r=ast.literal_eval(d)

                    dict2={username:password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    file=open('datasheet.txt','w')
                    w=file.write(str(r))

                    messagebox.showinfo('Signup','Succesful sign up')
                except:
                    file=open('datasheet.txt','w')
                    pp=str({'Username' : 'password'})
                    file.write(pp)
                    file.close()

            else:
                messagebox.showerror('Invaid',"Both Password should match")


        #------------------------------Destroy Window------------------------------#
        def sign():
            window.destroy()

        #########################################FRAME#########################################
        frame=Frame(window,width=350,height=390,bg='#fff')
        frame.place(x=480,y=50)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)


        ##########################################HEADINGS###########################################
        heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
        heading.place(x=100,y=5)



        ##########################################BUTTONS#####################################################
        Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)


        signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
        signin.place(x=200,y=340)



        ##########################################LABELS##############################################################
        label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label.place(x=90,y=340)



        ############################################USER INPUT#######################################################

        #--------------------------------------------USERNAME------------------------------------------------------#
        user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        user.place(x=30,y=80)
        user.insert(0, 'Username')
        

        #--------------------------------------------PASSWORD-------------------------------------------------------#

        code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        code.place(x=30,y=150)
        code.insert(0, 'Password')
        


        #-------------------------------------------CONFIRM CODE---------------------------------------------------#

        confirm_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        confirm_code.place(x=30,y=220)
        confirm_code.insert(0, 'Confirm Password')
        





        window.mainloop()
    ###################################################################################################################################################################









    #################################################################################################################################################
    #-------------------------------Sign in------------------------------------------------------#
    def signin():
        username=user.get()
        password=code.get()

        file=open('datasheet.txt','r')
        d=file.read()
        r=ast.literal_eval(d)
        file.close()

        if username in r.keys() and password==r[username]:
            screen=Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg="white")
            screen.destroy()
            root.destroy()
            password_manager()
            screen.mainloop()
            
        else:
            messagebox.showerror('Invalid','invalid username or password')




    #####################################IMAGE######################################################################
    img = PhotoImage(file='login.png')
    Label(root,image=img,bg='white').place(x=50,y=50)



    ################################################FRAME###############################################################
    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)



    ###################################################HEADINGS###########################################################
    heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)



    #################################################BUTTON#######################################################################
    Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)


    sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
    sign_up.place(x=215,y=270)



    #####################################################LABEL########################################################################

    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=270)



    ######################################################USER INPUT#####################################################################################
    #--------------------------------------------USERNAME---------------------------------------------------------------------------#
    user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')


    #---------------------------------------------PASSWORD----------------------------------------------------------------------------#

    code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    #############################################################################################################################################
    root.mainloop()

except NameError:
    messagebox