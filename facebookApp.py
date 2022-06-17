from tkinter import*
import sqlite3
from tkinter import ttk,messagebox
root=Tk()


cen=sqlite3.connect('facebook.db')


# c=cen.cursor()
# c.execute(''' Create table user(
#     firstName text,
#     lastName text,
#     age text,
#     adress text,
#     city text,
#     Zipcode text,
#     password text,
#     gender text
# )
# ''')

fb=Label(root,text='FACEBOOK',fg='blue',font=20)
fb.grid(row=0,column=0,columnspan=2)

#commands
def submit():
    conn= sqlite3.connect('facebook.db')

    c=conn.cursor()
    c.execute('''insert into user values(:firstName, :lastName,:age,:adress,:city,:Zipcode,:password,:gender)''',{'firstName':firstname.get(),'lastName':lastname.get(),'age':age.get(), 'adress':address.get(),'city':city.get(),'Zipcode':zipcode.get(),'password':password.get(),'gender':gender.get()}
    )
    messagebox.showinfo('success','Inserted sucessfully')
    
    conn.commit()
    conn.close()




def show():
    conn= sqlite3.connect('facebook.db')

    c=conn.cursor()
    c.execute('select *,oid from user')
    messagebox.showinfo('success','showed')
    record=c.fetchall()
    print(record)
    print_record=''
    for record in record:
        print_record+=str(record[0])+'  '+str(record[1])+''+'\t'+str(record[8])+'\n'

    show_record=Label(root,text=print_record)
    show_record.grid(row=14,column=0,columnspan=2,padx=1)
    conn.commit()
    conn.close()



def delete():
    conn= sqlite3.connect('facebook.db')

    c=conn.cursor()
    c.execute('delete from user where oid ='+delete_entry.get())
    print('success','deleted')
    conn.commit()
    conn.close()
def update():
    conn= sqlite3.connect('facebook.db')
    rec=delete_entry.get()
    c=conn.cursor()
    c.execute('''UPDATE user SET
                firstName=:firstName,
                lastName=:lastName,
                age =:age,
                adress =:adress,
                city =:city,
                Zipcode =:Zipcode,
                password =:password,
                gender =:gender
                WHERE oid= :oid''',
            {'firstName':firstname_edit.get(),
            'lastName':lastname_edit.get(),
            'age':age_edit.get(),
            'adress':address_edit.get(),
            'city':city_edit.get(),
            'Zipcode':zipcode_edit.get(),
            'password':password_edit.get(),
            'gender':gender_edit.get(),
            'oid':rec
            }
        )
    conn.commit()
    conn.close()
    editor.destroy()






def edit():
    global editor 
    editor=Toplevel()
    editor.title('Update data')
    editor.geometry('300x400')

    conn=sqlite3.connect('facebook.db')
    c=conn.cursor()
    rec=delete_entry.get()
    c.execute("select * from user where oid="+rec)
    records=c.fetchall()
    print(records)

    global firstname_edit
    global lastname_edit
    global age_edit
    global address_edit
    global city_edit
    global zipcode_edit
    global password_edit
    global gender_edit

    firstname_edit= Entry(editor, width=30)
    firstname_edit.grid(row=1,column=1,padx=20,pady=5)

    lastname_edit=Entry(editor,width=30)
    lastname_edit.grid(row=2,column=1,pady=5)

    age_edit=Entry(editor,width=30)
    age_edit.grid(row=3,column=1,pady=5)

    address_edit=Entry(editor,width=30)
    address_edit.grid(row=4,column=1,pady=5)

    city_edit=Entry(editor,width=30)
    city_edit.grid(row=5,column=1,pady=5)

    zipcode_edit=Entry(editor,width=30)
    zipcode_edit.grid(row=6,column=1,pady=5)

    password_edit=Entry(editor,width=30)
    password_edit.grid(row=7,column=1,pady=5)

    gender_edit=Entry(editor,width=30)
    gender_edit.grid(row=8,column=1,pady=5)

    fnamelabel= Label(editor,text="firstname")
    fnamelabel.grid(row=1,column=0)

    lastnamelabel= Label(editor,text="lastname")
    lastnamelabel.grid(row=2,column=0)

    agelabel= Label(editor,text="age")
    agelabel.grid(row=3,column=0)

    addresslabel= Label(editor,text="address")
    addresslabel.grid(row=4,column=0)

    citylabel= Label(editor,text="city")
    citylabel.grid(row=5,column=0)

    zipcodelabel= Label(editor,text="zipcode")
    zipcodelabel.grid(row=6,column=0)

    passwordlabel= Label(editor,text="password")
    passwordlabel.grid(row=7,column=0)

    genderlabel= Label(editor,text="gender")
    genderlabel.grid(row=8,column=0)

    sub_btn=Button(editor,text='Submit',command=update)
    sub_btn.grid(row=9,column=0,columnspan=2)
    for record in records:
        firstname_edit.insert(0,record[0])
        lastname_edit.insert(0,record[1])
        age_edit.insert(0,record[2])
        address_edit.insert(0,record[3])
        city_edit.insert(0,record[4])
        zipcode_edit.insert(0,record[5])
        password_edit.insert(0,record[6])
        gender_edit.insert(0,record[7])


    conn.commit()
    conn.close()




firstname= Entry(root, width=30)
firstname.grid(row=1,column=1,padx=20,pady=5)

lastname=Entry(root,width=30)
lastname.grid(row=2,column=1,pady=5)

age=Entry(root,width=30)
age.grid(row=3,column=1,pady=5)

address=Entry(root,width=30)
address.grid(row=4,column=1,pady=5)

city=Entry(root,width=30)
city.grid(row=5,column=1,pady=5)

zipcode=Entry(root,width=30)
zipcode.grid(row=6,column=1,pady=5)

password=Entry(root,width=30)
password.grid(row=7,column=1,pady=5)

gender=Entry(root,width=30)
gender.grid(row=8,column=1,pady=5)

fnamelabel= Label(root,text="firstname")
fnamelabel.grid(row=1,column=0)

lastnamelabel= Label(root,text="lastname")
lastnamelabel.grid(row=2,column=0)

agelabel= Label(root,text="age")
agelabel.grid(row=3,column=0)

addresslabel= Label(root,text="address")
addresslabel.grid(row=4,column=0)

citylabel= Label(root,text="city")
citylabel.grid(row=5,column=0)

zipcodelabel= Label(root,text="zipcode")
zipcodelabel.grid(row=6,column=0)

passwordlabel= Label(root,text="password")
passwordlabel.grid(row=7,column=0)

genderlabel= Label(root,text="gender")
genderlabel.grid(row=8,column=0)

deletelabel= Label(root,text="delete")
deletelabel.grid(row=10,column=0)

sub_btn=Button(root,text='Submit',command=submit)
sub_btn.grid(row=9,column=0,columnspan=2)

delete_entry=Entry(root,width=30)
delete_entry.grid(row=10,column=1,pady=5)


sub_btn=Button(root,text='delete',command=delete)
sub_btn.grid(row=11,column=0,columnspan=2)
sub_btn=Button(root,text='show',command=show)
sub_btn.grid(row=12,column=0,columnspan=2)
sub_btn=Button(root,text='edit',command=edit)
sub_btn.grid(row=13,column=0,columnspan=2)



cen.commit()
cen.close()

root.mainloop()
