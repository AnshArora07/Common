from tkinter import *
import math
import numpy as np
from numpy import *
import matplotlib.pyplot as plot

def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")


def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)


def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)
def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)
    
def trig_asin():
    global calc_operator
    result = str(math.asin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)
    
def trig_acos():
    global calc_operator
    result = str(math.acos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)
    
def trig_atan():
    global calc_operator
    result = str(math.atan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)
    
def trig_acot():
    global calc_operator
    result = str(1/math.atan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)
def third_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)
    def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    


def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)


def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op 

sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '*10**'
try:
    print("0/0")
except:
    print("ERROR")


tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth = 5, bg='#BBB', justify='right').grid(columnspan=5, padx = 10, pady = 15)

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}
button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}


abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda:button_click('abs(')).grid(row=1, column=0, sticky="nsew")

modulo = Button(tk_calc, button_params, text='mod',
                command=lambda:button_click('%')).grid(row=1, column=1, sticky="nsew")

int_div = Button(tk_calc, button_params, text='div',
                 command=lambda:button_click('//')).grid(row=1, column=2, sticky="nsew")

factorial_button = Button(tk_calc, button_params, text='x!',
                   command=fact_func).grid(row=1, column=3, sticky="nsew")

eulers_num = Button(tk_calc, button_params, text='e',
                    command=lambda:button_click(str(math.exp(1)))).grid(row=1, column=4, sticky="nsew")


sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin).grid(row=2, column=0, sticky="nsew")

cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos).grid(row=2, column=1, sticky="nsew")

tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan).grid(row=2, column=2, sticky="nsew")

cotangent = Button(tk_calc, button_params, text='cot',
             command=trig_cot).grid(row=2, column=3, sticky="nsew")
 
pi_num = Button(tk_calc, button_params, text='π',
                command=lambda:button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")

asine = Button(tk_calc, button_params, text='asin',
             command=trig_asin).grid(row=3, column=0, sticky="nsew")

acosine = Button(tk_calc, button_params, text='acos',
             command=trig_acos).grid(row=3, column=1, sticky="nsew")

atangent = Button(tk_calc, button_params, text='atan',
             command=trig_atan).grid(row=3, column=2, sticky="nsew")

acotangent = Button(tk_calc, button_params, text='acot',
             command=trig_acot).grid(row=3, column=3, sticky="nsew")

x_division = Button(tk_calc, button_params, text='1/x',
             command=lambda:button_click('1/')).grid(row=3, column=4, sticky="nsew")
