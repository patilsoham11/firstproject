# python tkinter tutorial
# tee-kinter , tk-inter , kinter 

# starter code
# import tkinter            # --->1st way use tkinter module
# form tkinter import *       # yaa peksh 1st better--->2nd way use tkinter but only write .Tk() constructor write
import tkinter as tk         # 3rd use of tkinter NO write tkinter only write tk.
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('GUI app')

# create Labels
# widgets --> label, buttons, radio buttons - (tk) made pan ahe
# & ajun ek submodule ahe (ttk) ha disayala tk paksha better ahe
# tkk module mde sarv ahe(for check python OFL-PYTHON 3.764-BIT-OFL-LIB-tkinter-__inti__.py-edit with IDLE. )
# from tkinter import ttk for ttk module.
name_label = ttk.Label(win, text='Enter your name :')    
# window var lebel ahe pan win var location nahi sangitalo
# for window lebel set 2 mothods use
# 1.pack =.pack()
# 2.grid =.grid(row =0, column=0) --> pack peksha better .grid()
name_label.grid(row=0, column=0,sticky =tk.W)

email_label = ttk.Label(win, text='Enter your email :') 
email_label.grid(row=1, column=0,sticky =tk.W)

age_label = ttk.Label(win, text='Enter your age :') 
age_label.grid(row=2, column=0,sticky =tk.W)

gender_label = ttk.Label(win, text='select your gender :') 
gender_label.grid(row=3, column=0,sticky =tk.W)

# create user entrybox(user store data)
name_var =tk.StringVar()
name_entrybox =ttk.Entry(win, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var =tk.StringVar()
email_entrybox =ttk.Entry(win, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var =tk.StringVar()
age_entrybox =ttk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

# create user combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14, textvariable=gender_var, state = 'readonly')
gender_combobox['values']= ('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

# radio button
# students, teacher
usertype = tk.StringVar()
radiobtn1 =ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=4, column=0)

radiobtn2 =ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column=1)

# check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='check if you want to subscribe to our newsletter ', variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)

# # create user Submit button(& user data store file.txt)
# def user_data():
#     username = name_var.get()
#     userage = age_var.get()
#     useremail = email_var.get()
#     print(f'{username} is {userage} years old, {useremail}')
#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     if checkbtn_var.get() == 0:
#         subscribed = 'No'
#     else:
#         subscribed = 'Yes'
#     print(user_gender, user_type, subscribed)

#     with open('file.txt', 'a') as f:
#         f.write(f'{username},{userage},{useremail},{user_gender},{user_type}, {subscribed}\n')

    # name_entrybox.delete(0,tk.END)
    # age_entrybox.delete(0,tk.END)
    # email_entrybox.delete(0,tk.END)
    # # For Colour change 
    # name_label.configure(foreground='#B388ff')        #---> apan yaa made colours use karu shaktot(Blur,red,yellow)
    # # apan yaa google(google colour picker)varun hexa value use ne.

    # # for submit_button colour change
    # submit_button.configure(foreground='Blue')

# User input Data write to CSV files
def action():
    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    user_type = usertype.get()
    user_gender = gender_var.get()
    if checkbtn_var.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'

    with open('files.csv', 'a',newline='') as f:
        dict_writer =DictWriter(f,fieldnames=['username','userage','user email address','user type','user gender','subcribed'])
        if os.stat('files.csv').st_size==0:
            dict_writer.writeheader()

        dict_writer.writerow({
            'username' : username,
            'user email address' :useremail,
            'userage' : userage,
            'user type' : user_type,
            'user gender' : user_gender,
            'subcribed' : subscribed
        })
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='#B388ff')  


submit_button = tk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=0)


win.mainloop()