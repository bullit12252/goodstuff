
#Программа - словарь с графическим интерфейсом


#Functions
def find(event):
    defins.delete(0.0,END)
    term=None
    defin=None
    term=terms.get()
    term=term.strip()
    term=term.capitalize()
    k=len(term)
    matches_list=[]
    j=0
    first = ''
    second = ''
    if k<=4:
        first = term
        second = term
    else:
        first = term[:3]
        second = term[k-4:]
    if term in DS.keys():
        defins.delete(0.0,END)
        defins.insert(0.0,DS[term.capitalize()])
    else:
        for key in DS.keys():
            count = 0
            if (first in key) or (second in key):
                for letter in term:
                    if letter in key:
                        count += 1
                if count >= k*0.9:
                    matches_list.append(key)
                    j += 1
        if j == 0:
            console.configure(text = 'Nothing was found')
            defins.delete(0.0,END)
        elif term == '':
            console.configure(text = 'Enter the term, please.')
        else:
            for hh in matches_list:
                defins.insert(0.0, hh + '\n')
            co = "No such term in database, similar words found:" + str(j)
            console.configure(text = co )
def add(event):
    term=None
    defin=None
    term=terms.get()
    term=term.strip()
    defin=defins.get(0.0,END)
    defin=defin.strip()
    if term.capitalize() in DS.keys():
        console.configure(text='Such term already exists!')
    elif term == '':
        console.configure(text='Enter the term please!!')
    else:
        if defin !='':
            DS[term.capitalize()]=defin.capitalize()
            update(DS)
            check1(term)
            defins.delete(0.0,END)
            terms.delete(0,END)
            console.configure(text='Success!')
            show_check()
        else:
            console.configure(text='Enter the definition please!')
def remove(event):
    term=terms.get()
    if term.capitalize() in DS.keys():
        del DS[term.capitalize()]
        update(DS)
        console.configure(text='Success!')
        clear(event)
    elif term == '':
        console.configure(text='Enter the term please!')
    else:
        console.configure(text='Such term doesn\'t exist!')
def edit(event):
    term=terms.get()
    defin=defins.get(0.0,END)
    defin=defin.strip()
    if term.capitalize() in DS.keys():
        if defin != '':
            DS[term.capitalize()]=defin.capitalize()
            update(DS)
            console.configure(text='Success!')
        else:
            console.configure(text='Enter the definition please!')
    elif term == '':
        console.configure(text='Enter the term please!')
    else:
        console.configure(text='Such term doesn\'t exist!')
def show_terms(event):
    defins.delete(0.0,END)
    for definition in DS.keys():
        defins.insert(0.0,definition+'\n')
def clear(event):
    defins.delete(0.0,END)
    terms.delete(0,END)
    console.configure(text='Fields were cleared!')
def update(DS):
    t=open('terms.txt','w')
    d=open('definitions.txt','w')
    for term in DS:
        t.write(term+'\n')
        d.write(DS[term]+'\n')
    t.close()
    d.close()
def add_check_then(event):
    check_file=open('check_then.txt','r')
    file_terms=open('terms.txt','r')
    check=check_file.readlines()
    terms1=file_terms.readlines()
    file_terms.close()
    check_file.close()
    table=terms.get()
    table.strip()
    table.capitalize()
    table+='\n'
    if table.capitalize() in check:
        console.configure(text='This term is already in list!')
    elif table.capitalize() in terms1:
        console.configure(text='This term is already in dictionary!')
    elif table == '\n':
        console.configure(text='Please, enter the term!')
    else:
        check_then2=open('check_then.txt','a')
        check_then2.write(table.capitalize())
        console.configure(text='Success!')
        terms.delete(0,END)
        check_then2.close()
        show_check()
def check1(term):
    check_file=open('check_then.txt','r')
    l=check_file.readlines()
    check_file.close()
    term+='\n'
    if term.capitalize() in l:
        l.remove(term.capitalize())
        checkk=open('check_then.txt','w')
        checkk.writelines(l)
        checkk.close()
def show_check():
    file=open('check_then.txt','r')
    lis=file.readlines()
    m=''
    for i in lis:
        m+=i
    check_then.configure(text=m)
def clear_console(event):
    console.configure(text='Waiting for input...')
def exit_1(event):
    global win
    win = Toplevel(root, relief = RAISED)
    win.title('Are you sure?')
    lab_sure = Label(win, text = 'Are you sure?')
    btn_yes = Button(win, text = 'Yes', width = 12, height = 1)
    btn_no = Button(win, text = 'No', width = 12, height = 1)
    btn_yes.bind('<Button-1>', exit_prog)
    btn_no.bind('<Button-1>', exit_win)
    lab_sure.grid(row = 0, column = 0)
    btn_yes.grid(row = 1, column = 0)
    btn_no.grid(row = 1, column =1)
def exit_prog(event):
    root.destroy()
def exit_win(event):
    win.destroy()
def clr_upper(event):
    terms.delete(0, END)
def clr_lower(event):
    defins.delete(0.0,END)
    


#Filling dictionary from files (then i should use access)
DS={}
file_t=open('terms.txt','r')
file_d=open('definitions.txt','r')
term_file=file_t.readlines()
def_file=file_d.readlines()
v=len(term_file)
for i in range(v):
    DS[term_file[i].strip()]=def_file[i].strip()
file_t.close()
file_d.close()



#creating widgets
from tkinter import *
root=Tk()
prog_name=Label(root,text='DICTIONARY v4 - Beta',font='Elephant')
terms=Entry(root,width=53,bd=5)
defins=Text(root,width=40,height=7,bd=5,wrap=WORD)
console=Label(root,text='Welcome')
check_then=Label(root)
check_title=Label(root,text='Check this terms later:')
btn_add=Button(root,text='Add',width=12,height=1, bg = "lightblue")
btn_remove=Button(root,text='Remove',width=12,height=1, bg = "lightblue")
btn_edit=Button(root,text='Edit',width=12,height=1, bg = "lightblue")
btn_show_terms=Button(root,text='Show terms',width=12,height=1, bg = "lightblue")
btn_check=Button(root,text='Check later',width=12,height=1, bg = "lightblue")
btn_exit=Button(root,text='Exit',width=12,height=1, bg = "lightblue")
btn_find=Button(root,text='Find',width=12,height=1, bg = "lightblue")
btn_clr_upper = Button(root, text = "Del", width = 3, height = 1, bg = "black", fg = 'white')
btn_clr_lower = Button(root, text = "Del", width = 3, height = 1, bg = "black", fg = 'white')
#safemode 
#var = IntVar()
#var.set(0)
#rad0 = Radiobutton(root,text="NSFW\n",
#         variable=var,value=0)
#rad1 = Radiobutton(root,text="SFW\n",
#          variable=var,value=1)
#btn_chng_sfmd=Button(root, text = "choose")
#############################################

show_check()
#Binding buttons
btn_add.bind('<Button-1>',add)
btn_remove.bind('<Button-1>',remove)
btn_edit.bind('<Button-1>',edit)
btn_exit.bind('<Button-1>',exit_1)
btn_show_terms.bind('<Button-1>',show_terms)
btn_check.bind('<Button-1>',add_check_then)
btn_find.bind('<Button-1>', find)
btn_clr_upper.bind("<Button-1>", clr_upper)
btn_clr_lower.bind("<Button-1>", clr_lower)
root.bind('<Key>',clear_console)
root.bind('<Delete>', clear)


#Accomodating widgets
root.title('Dictionary')
root.minsize(width=620,height=305)
root.maxsize(width=620,height=305)
prog_name.grid()
terms.grid()
defins.grid(row=2,column=0,rowspan=5)
btn_add.grid(row=2,column=2)
btn_remove.grid(row=4,column=2)
btn_edit.grid(row=3,column=2)
btn_show_terms.grid(row=5,column=2)
console.grid(column=0,row=8)
btn_check.grid(column=2,row=6)
btn_exit.grid(row=7, column =2)
btn_find.grid(row=1,column=2)
btn_clr_upper.grid(row = 1, column = 1)
btn_clr_lower.grid(row = 2, column = 1)
check_then.grid(column=3,row=1,rowspan=100,sticky=N,columnspan=100)
check_title.grid(row=0,column=3)



root.mainloop()










