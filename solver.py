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
    global eq_range_max
    global eq_range_min
    equation_str = equation_str.replace("^","**")
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
    equation_str = equation_str.replace("sinh" or "Sinh", "math.sinh")
    equation_str = equation_str.replace("cosh" or "Cosh", "math.cosh")
    equation_str = equation_str.replace("tanh" or "Tanh", "math.tanh")
    equation_str = equation_str.replace("arcsinh", "math.asinh")
    equation_str = equation_str.replace("arccosh", "math.acosh")
    equation_str = equation_str.replace("arctanh", "math.atanh")
    equation_str = equation_str.replace("arcsin", "math.asin")
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
    if equation_str.count("sin" or "Sin") > 1 + equation_str.count(".sin"):
        equation_str = equation_str.replace("sin" or "Sin", "math.sin")
    if equation_str.count("cos" or "Cos") > 1 + equation_str.count(".cos"):
        equation_str = equation_str.replace("cos" or "Cos", "math.cos")
    if equation_str.count("tan" or "Tan") > 1 + equation_str.count(".tan"):
       equation_str = equation_str.replace("tan" or "Tan", "math.tan")
    equation_str = equation_str.replace("abs", "math.abs")
    equation_str = equation_str.replace("floor", "math.floor")
    equation_str = equation_str.replace("ceil", "math.ceil")
    equation_str = equation_str.replace("factorial", "math.gamma")
def solve():
    clear()
    global x_var
    global y_var
    y_var = 0
    x_var = eq_range_min
    print("X","		   Y")
    while x_var <= eq_range_max:
        x = x_var
        y_var = eval(equation_str)
        print(x_var,"		|",y_var)
        x_var += eq_res
clear()
getcontext().prec = 32
equation_str = "0"
eq_range_min = 0
eq_range_max = 0
eq_res = 1
equation_str = str(input("Y="))
eq_range_min = dec(input("Min X:"))
eq_range_max = dec(input("Max X:"))
eq_res = dec(input("Resolution:"))
equation_edit()
solve()
waitsetc = 0
wait()
