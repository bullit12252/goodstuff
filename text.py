import matplotlib.pyplot as plt
import matplotlib
from scipy.interpolate import interp1d
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
import datetime


#global parameters, which are used to store filenames and some data
global parameter
global sourcefile
global corrfuncfile
global minlambda
global maxlambda




#main functions

def reading_the_file(sourcefile):

    f = open(sourcefile, 'r')
    thewholetext = f.readlines()
    x = []
    y = []
    for i in thewholetext:
        x.append(float(i[:i.find('\t')].replace(",",".")))
        y.append(float(i[i.find('\t'):i.find('\n')+1].replace(",",".")))
    return x, y
   
    
def drawing_all(sourcefile):
    matplotlib.use('TkAgg')
    xaxes, yaxes = reading_the_file(sourcefile)
    plt.plot(xaxes, yaxes)
    plt.axis([380, 800, 0, 60000])
    #plt.xticks([]) 
    #plt.yticks([])
    plt.show()
    
def calculating_integral():
    global sourcefile, minlambda, maxlambda
    x, y = reading_the_file(sourcefile)
    minimum = min(y)
    new_y = []
    new_x = []
    integral = 0
    for i in range(len(x)):
        if x[i] >= minlambda and x[i] <= maxlambda:
            new_x.append(x[i])
            new_y.append(y[i]-minimum)
    print(new_y)
    for i in range(len(new_x)-1):
        integral += (new_x[i+1] - new_x[i])* new_y[i]
    return(integral)

def choose_file(parameter):
    global sourcefile
    sourcefile = askopenfilename()
    chs_src.configure(text = sourcefile)
def choose_correlation_function(parameter):
    global corrfuncfile
    corrfuncfile = askopenfilename()
    chs_calfunc.configure(text = corrfuncfile)
def calibrate():
    global sourcefile
    etalonspectrum = askopenfilename()
    xsrc, ysrc = reading_the_file(sourcefile)
    xeta, yeta = reading_the_file(etalonspectrum)
    xcorr = []
    ycorr = []
    name = str(datetime.datetime.now())[11:19] + '.txt'
    f = open(name, 'w')
    for i  in range(len(xsrc)):
        xcorr.append(xeta[i]/xsrc[i])
        ycorr.append(yeta[i]/ysrc[i])
        f.writeline(xeta[i]/xsrc[i] + '\t' + yeta[i]/ysrc[i] + '\n')
    f.close()
    

#btn functions
def close(event):
    root.destroy()

def draw(event):
    global sourcefile
    drawing_all(sourcefile)
def chfile(event):
    choose_file(parameter)
def chcorr(event):
    choose_correlation_function(parameter)
def set_lambda(event):
    global minlambda, maxlambda, sourcefile
    minlambdalab.configure(text = minlambdain.get())
    maxlambdalab.configure(text = maxlambdain.get())
    minlambda = int(minlambdain.get())
    maxlambda = int(maxlambdain.get())
    minlambdalab.configure(text = minlambdain.get())
    maxlambdalab.configure(text = maxlambdain.get())
    integral.configure(text = "значение равно " + str(calculating_integral()))
def clbr(event):
    print('zaglushka')
def clclt(event):
    calculating_integral()

parameter = 1



# GUI
root = Tk()
prog_name=Label(root,text='Зуку',font='Elephant')

#Root
root.title('Dictionary')
root.minsize(width=1000,height=305)
root.maxsize(width=1000,height=305)

#Entries
minlambdain=Entry(root, width = 11,bd = 5)
maxlambdain=Entry(root, width = 11,bd = 5)
time = Entry(root, width = 11, bd = 5)


#Labels
minlambdalab = Label(root,text='Min lambda')
maxlambdalab = Label(root, text = 'Max lambda')
timeword = Label(root,text='Integration time')
integral = Label(root,text='Lambda')
chs_src = Label(root,text='No file chosen')
chs_calfunc = Label(root,text='No file chosen')
minlambdaval = Label(root,text='-')
maxlambdaval = Label(root,text='-')
timeval = Label(root,text='-')
name = Label(root,text='Lab 208', font = 'Elephant')



#Buttons
btn_exit=Button(root,text='Exit',width=12,height=1, bg = "lightblue")
btn_draw=Button(root,text='Draw',width=12,height=1, bg = "lightblue")
btn_chfile=Button(root,text='Change file',width=50,height=1, bg = "lightblue")
btn_enter=Button(root,text='Enter',width=39,height=1, bg = "lightblue")
btn_chcorr = Button(root,text='Change corr func',width=50,height=1, bg = "lightblue")
btn_calibrate = Button(root,text='Calibrate',width=50,height=1, bg = "lightblue")
btn_calculate = Button(root,text='Calculate',width=12,height=1, bg = "lightblue")
btn_nothing = Button(root,text='blank',width=12,height=1, bg = "lightblue")



#Bindings of buttons
btn_exit.bind('<Button-1>', close)
btn_draw.bind('<Button-1>', draw)
btn_chfile.bind('<Button-1>', chfile)
btn_enter.bind ('<Button-1>', set_lambda)
btn_chcorr.bind('<Button-1>', chcorr)
btn_calibrate.bind('<Button-1>', clbr)
btn_calculate.bind('<Button-1>', clclt)

minlambdalab.grid(row = 1, column = 1)
maxlambdalab.grid(row = 2, column = 1)
timeword.grid(row = 3, column = 1)

minlambdain.grid(row = 1, column = 2)
maxlambdain.grid(row = 2, column = 2)
time.grid(row = 3, column = 2)
btn_exit.grid(row = 10,column = 10)
btn_draw.grid(row = 5,column = 1)
btn_chfile.grid(row = 1, column = 0)
btn_enter.grid(row = 4, column = 1, columnspan = 3)
integral.grid(row = 6, column = 1)
name.grid(row = 0, column = 0, columnspan = 5)
chs_src.grid(row = 2, column = 0)
btn_chcorr.grid(row = 3, column = 0)
chs_calfunc.grid(row = 4, column = 0)
btn_calibrate.grid(row = 5, column = 0)
btn_calculate.grid(row = 5, column = 2)
minlambdaval.grid(row = 1, column = 3)
maxlambdaval.grid(row = 2, column = 3)
timeval.grid(row = 3, column = 3)
btn_nothing.grid(row = 5, column = 3)



root.mainloop()


