# -*- coding: utf-8 -*-
# Copyright (c) 2019 Benjamin Yao
import os
import platform
import time
import math
from decimal import *
from decimal import Decimal as dec
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def wait():
    if waitsetc == 2:
        wait = str(input("Press enter to continue..."))
        clear()
    if waitsetc == 1:
        clear()
        wait = str(input("Press enter to continue..."))
    if waitsetc == 0:
        wait = str(input("Press enter to exit..."))
def equation_edit():
    global equation_str
    global original_eq_str
    global eq_range_max
    global eq_range_min
    for x in range(1,len(str(original_eq_str)),1):
        equation_str = equation_str.replace("^","**")
        equation_str = equation_str.replace(")(", ")*(")
        equation_str = equation_str.replace("xx", "x*x")
        equation_str = equation_str.replace("0(", "0*(")
        equation_str = equation_str.replace("1(", "1*(")
        equation_str = equation_str.replace("2(", "2*(")
        equation_str = equation_str.replace("3(", "3*(")
        equation_str = equation_str.replace("4(", "4*(")
        equation_str = equation_str.replace("5(", "5*(")
        equation_str = equation_str.replace("6(", "6*(")
        equation_str = equation_str.replace("7(", "7*(")
        equation_str = equation_str.replace("8(", "8*(")
        equation_str = equation_str.replace("9(", "9*(")
        equation_str = equation_str.replace("0x", "0*x")
        equation_str = equation_str.replace("1x", "1*x")
        equation_str = equation_str.replace("2x", "2*x")
        equation_str = equation_str.replace("3x", "3*x")
        equation_str = equation_str.replace("4x", "4*x")
        equation_str = equation_str.replace("5x", "5*x")
        equation_str = equation_str.replace("6x", "6*x")
        equation_str = equation_str.replace("7x", "7*x")
        equation_str = equation_str.replace("8x", "8*x")
        equation_str = equation_str.replace("9x", "9*x")
        equation_str = equation_str.replace("x0", "x*0")
        equation_str = equation_str.replace("x1", "x*1")
        equation_str = equation_str.replace("x2", "x*2")
        equation_str = equation_str.replace("x3", "x*3")
        equation_str = equation_str.replace("x4", "x*4")
        equation_str = equation_str.replace("x5", "x*5")
        equation_str = equation_str.replace("x6", "x*6")
        equation_str = equation_str.replace("x7", "x*7")
        equation_str = equation_str.replace("x8", "x*8")
        equation_str = equation_str.replace("x9", "x*9")
        equation_str = equation_str.replace("x8", "x*8")
        equation_str = equation_str.replace("x9", "x*9")
        equation_str = equation_str.replace("abs", "m_f00q")
        equation_str = equation_str.replace("floor", "m_f01q")
        equation_str = equation_str.replace("ceil", "m_f02q")
        equation_str = equation_str.replace("factorial", "m_f03q")
        equation_str = equation_str.replace("x!" or "(x)!", "m_f03w")
        equation_str = equation_str.replace("gamma", "m_f04q")
        equation_str = equation_str.replace("sqrt", "m_f05q")
    for x in range(1,len(str(original_eq_str)),1):
        equation_str = equation_str.replace("m_f00q", "math.fabs")
        equation_str = equation_str.replace("m_f01q", "math.floor")
        equation_str = equation_str.replace("m_f02q", "math.ceil")
        equation_str = equation_str.replace("m_f03q", "math.gamma")
        equation_str = equation_str.replace("m_f03w", "math.gamma(x)")
        equation_str = equation_str.replace("m_f04q", "math.gamma")
        equation_str = equation_str.replace("m_f05q", "math.sqrt")
    for x in range(1,len(str(original_eq_str)),1):
        equation_str = equation_str.replace("arcsinh", "trig_f03")
        equation_str = equation_str.replace("arccosh", "trig_f13")
        equation_str = equation_str.replace("arctanh", "trig_f23")
        equation_str = equation_str.replace("arcsin", "trig_f01")
        equation_str = equation_str.replace("arccos", "trig_f11")
        equation_str = equation_str.replace("arctan", "trig_f21")
        equation_str = equation_str.replace("sinh", "trig_f02")
        equation_str = equation_str.replace("cosh", "trig_f12")
        equation_str = equation_str.replace("tanh", "trig_f22")
        equation_str = equation_str.replace("sin", "trig_f00")
        equation_str = equation_str.replace("cos", "trig_f10")
        equation_str = equation_str.replace("tan", "trig_f20")
    for x in range(1,len(str(original_eq_str)),1):
        equation_str = equation_str.replace("trig_f03", "math.asinh")
        equation_str = equation_str.replace("trig_f13", "math.acosh")
        equation_str = equation_str.replace("trig_f23", "math.atanh")
        equation_str = equation_str.replace("trig_f01", "math.asin")
        equation_str = equation_str.replace("trig_f11", "math.acos")
        equation_str = equation_str.replace("trig_f21", "math.atan")
        equation_str = equation_str.replace("trig_f02", "math.sinh")
        equation_str = equation_str.replace("trig_f12", "math.cosh")
        equation_str = equation_str.replace("trig_f22", "math.tanh")
        equation_str = equation_str.replace("trig_f00", "math.sin")
        equation_str = equation_str.replace("trig_f10", "math.cos")
        equation_str = equation_str.replace("trig_f20", "math.tan")
    if equation_str.count(".asin") and eq_range_max > 1:
        eq_range_max = 1
    if equation_str.count(".asin") and eq_range_min < -1:
        eq_range_min = -1
    equation_str = equation_str.replace("arccos", "math.acos")
    if equation_str.count(".acos") and eq_range_max > 1:
        eq_range_max = 1
    if equation_str.count(".acos") and eq_range_min < -1:
        eq_range_min = -1
    equation_str = equation_str.replace("arctan", "math.atan")
    if equation_str.count(".atan") and eq_range_max > 1:
        eq_range_max = 1
    if equation_str.count(".atan") and eq_range_min < -1:
        eq_range_min = -1
def solve():
    clear()
    global tstart
    global tend
    global x_var
    global y_var
    y_var = 0
    x_var = eq_range_min
    print("X","		   Y")
    tstart = time.perf_counter()
    while x_var <= eq_range_max:
        x = x_var
        try:
            eval(equation_str)
            y_var = dec(eval(equation_str))
            print(x_var,"		|",y_var)
            x_var += eq_res
        except:
            print(x_var,"		|","ERROR")
            x_var += eq_res
    tend = time.perf_counter()
def table():
    global tstart
    global tend
    global x_var
    global y_var
    global equation_str
    global original_eq_str
    global eq_range_max
    global eq_range_min
    global eq_res
    clear()
    getcontext().prec = 96
    equation_str = "0"
    eq_range_min = 0
    eq_range_max = 0
    eq_res = 1
    equation_str = str(input("Y="))
    eq_range_min = dec(input("Min X:"))
    eq_range_max = dec(input("Max X:"))
    eq_res = dec(input("Resolution:"))
    original_eq_str = equation_str
    clear()
    print("Preparing...")
    equation_edit()
    solve()
    print("\n")
    print(original_eq_str)
    print(equation_str)
    print("\n")
    print("Time", tend - tstart)
    print("\n")
clear()
print("1:Table")
option = int(input("Select Solver:"))
if option == 1:
    table()
else:
    clear()
    print("Invalid Option")
waitsetc = 0
wait()
clear()
# End of Program
