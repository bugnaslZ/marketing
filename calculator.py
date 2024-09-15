from tkinter import *
win = Tk()
win.geometry('250x280')
win.config(bg='blue')
equation = ''
def show(value):
    global equation
    equation += value
    lbl_mohasli.config(text=equation)
def calculate():
    global equation
    result = ''
    if equation != '':
        try:
            result = eval(equation)
        except:
            result = 'erorr'
        lbl_mohasli.config(text=result)

def clear():
    global equation
    equation = ""
    lbl_mohasli.config(text=equation)


lbl_calculator = Label(win,text='calculator',bg='blue',fg='lightblue',font='impact')
lbl_calculator.place(x=87,y=1)

lbl_mohasli = Label(win,text='',bg='blue',fg='white',font='impact 20')
lbl_mohasli.place(x=103,y=30)
btn_9 = Button(win,text='9',fg='blue',font='impact',width=4,command=lambda:show('9')) 
btn_9.place(x=10,y=80)
btn_8 = Button(win,text='8',fg='blue',font='impact',width=4,command=lambda:show('8')) 
btn_8.place(x=65,y=80)
btn_7 = Button(win,text='7',fg='blue',font='impact',width=4,command=lambda:show('7')) 
btn_7.place(x=120,y=80)
btn_6 = Button(win,text='6',fg='blue',font='impact',width=4,command=lambda:show('6')) 
btn_6.place(x=10,y=130)
btn_5 = Button(win,text='5',fg='blue',font='impact',width=4,command=lambda:show('5')) 
btn_5.place(x=65,y=130)
btn_4 = Button(win,text='4',fg='blue',font='impact',width=4,command=lambda:show('4')) 
btn_4.place(x=120,y=130)
btn_3 = Button(win,text='3',fg='blue',font='impact',width=4,command=lambda:show('3')) 
btn_3.place(x=10,y=180)
btn_2 = Button(win,text='2',fg='blue',font='impact',width=4,command=lambda:show('2')) 
btn_2.place(x=65,y=180)
btn_1 = Button(win,text='1',fg='blue',font='impact',width=4,command=lambda:show('1')) 
btn_1.place(x=120,y=180)
btn_0 = Button(win,text='0',fg='blue',font='impact',width=4,command=lambda:show('0')) 
btn_0.place(x=65,y=230)
btn_zarb =  Button(win,text='X',fg='red',font='impact',width=5,command=lambda:show('*')) 
btn_zarb.place(x=175,y=80)
btn_taghsim = Button(win,text='%',fg='red',font='impact',width=5,command=lambda:show('%'))
btn_taghsim.place(x=175,y=130)
btn_jame = Button(win,text='+',fg='red',font='impact',width=5,command=lambda:show('+'))
btn_jame.place(x=175,y=180)
btn_menha =Button(win,text='-',fg='red',font='impact',width=5,command=lambda:show('-'))
btn_menha.place(x=175,y=230)
btn_clear = Button(win,text='c',fg='red',font='impact',width=4,command=clear)
btn_clear.place(x=10,y=230)
btn_mosavi =Button(win,text='=',fg='red',font='impact',width=4,command=calculate)
btn_mosavi.place(x=120,y=230)











win.mainloop()