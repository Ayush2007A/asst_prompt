# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:29:09 2021

@author: moghe
"""
def asc():
    from PIL import Image
    path=input('...:img-path> ')
    def ascii(imgpath,output_file="ascii.txt"):
        # pass the image as command line argument
        image_path = imgpath
        img = Image.open(image_path)
    
        # resize the image
        width, height = img.size
        aspect_ratio = height/width
        new_width = 80
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))
        # new size of image
        # print(img.size)
    
        # convert image to greyscale format
        img = img.convert('L')
    
        pixels = img.getdata()
    
        # replace each pixel with a character from array
        chars = ["~","`","^","1","@","$","%","*","!",":","."]
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
    
        # split string of chars into multiple strings of length equal to new width and create a list
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
    
        # write to a text file.
        with open(output_file, "w") as f:
            f.write(ascii_image)
        return ascii_image
    print(ascii(path))

import keyboard
import os
import sys
import signal
import pyautogui
import sys, random, argparse
global pyautogui
from sympy import *
from colorama import Fore, Back, Style
sys.tracebacklimit=None
def set_variables(variables):
    return symbols(variables)
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("{int}")
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("{float input}")
        except ValueError:
            print("{string}")
def getFactor(expression):
    '''do factorization in python'''
    try:print(factor(expression))
    except:print('Error')
def solve_expr(expression):
    '''solve a algebraic expression'''
    try:print('{',expand(expression),'}')
    except:
        print('Not able to solve the expression')
def download_from_youtube(url,path):
    '''download youtube videos to a path'''
    print('Downloading your request\n')
    import pytube  
    from pytube import YouTube  
    video_url = url  
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.first()  
    video.download(path)
    print('Your video is saved to',path)
tokens = (
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN',
    )

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        t[0] = 0

def p_error(t):
    pass

import ply.yacc as yacc
parser = yacc.yacc()


def cls():
    import subprocess as sp
    sp.call('cls', shell=True)
cls()
print("A")
cls()
print('As')
cls()
print('Ass')
cls()
print('Asst')
cls()
print('Asst ')
cls()
print('Asst p')
cls()
print('Asst pr')
cls()
print('Asst pro')
cls()
print('Asst prom')
cls()
print('Asst promp')
cls()
print('Asst prompt')
cls()
print('Asst prompt:')
cls()
print('Asst prompt: Y')
cls()
print('Asst prompt: Yo')
cls()
print('Asst prompt: You')
cls()
print('Asst prompt: Your')
cls()
print('Asst prompt: Your ')
cls()
print('Asst prompt: Your a')
cls()
print('Asst prompt: Your as')
cls()
print('Asst prompt: Your ass')
cls()
print('Asst prompt: Your assi')
cls()
print('Asst prompt: Your assis')
cls()
print('Asst prompt: Your assist')
cls()
print('Asst prompt: Your assista')
cls()
print('Asst prompt: Your assistan')
cls()
print('Asst prompt: Your assistant\n')
import time
time.sleep(2)
def keyboardInterruptHandler(signal, frame):
    print(("\nKeyboardInterrupt".format(signal)))
    while True:
        main()
signal.signal(signal.SIGINT, keyboardInterruptHandler)
def call_ip(website):
    '''call the ip address of your url'''
    import socket
    url=website
    print(socket.gethostbyname(url))
def inspect(address):
    '''inspect a address'''
    try:
        import requests
        req = requests.get(address)
        print(req.text)
    except:
        print('Unable to get the code please check your url')
def main():
    code=input('asst--> ')
    parser.parse(code)
    if 'press' in code:
        string = code
        word = 'press'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        try:keyboard.send(out)
        except:print('unable to press key')
    if 'type' in code:
        string = code
        word = 'type'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        print(out)
    if 'python install' in code:
        string = code
        word = 'python install'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        print('Installing',out,'using pip')
        import time
        time.sleep(3)
        import pip
        pip.main(['install',out])
        print('successfully installed',out)
    if 'delete' in code:
        string = code
        word = 'delete'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        import os
        try:
            os.system('del '+out)
        except:
            print('unable to delete the required please check the syntax and path')
    if '[' and ']' in code:
        print(code)
    if 'bin' in code:
        string = code
        word = 'bin'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        out=(int(out))
        try:print(bin(out))
        except:print('invalid syntax')
    if code == 'exit':
        sys.exit()
    if 'shutdown' in code:
        os.system('shutdown /s')
    if 'clickon{' in code:
        xx=int(input('...: x> '))
        yy=int(input('...: y> '))
        clk=int(input('...: clicks> '))
        import pyautogui
        pyautogui.click(x=xx,y=yy,clicks=clk)
    if code=='position-pointer':
        import pyautogui
        print(pyautogui.position())
    if '@' in code:
        string = code
        word = '@'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        print(set(out))
    if code=='{':
        while code!='}':
            code=input('...: ')
    if 'ip' in code:
        string = code
        word = 'ip'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        try:
            call_ip(out)
        except:print('invalid address')
    if 'inspect' in code:
        string = code
        word = 'inspect'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        inspect(out)
    if 'open' in code:
        string = code
        word = 'open'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        import os
        os.system('start '+out)
    if 'solve' in code:
        string = code
        word = 'solve'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=set_variables(['a',
 'b',
 'c',
 'd',
 'e',
 'f',
 'g',
 'h',
 'i',
 'j',
 'k',
 'l',
 'm',
 'n',
 'o',
 'p',
 'q',
 'r',
 's',
 't',
 'u',
 'v',
 'w',
 'x',
 'y',
 'z'])
        solve_expr(out)
    if 'factor' in code:
        string = code
        word = 'factor'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=set_variables(['a',
 'b',
 'c',
 'd',
 'e',
 'f',
 'g',
 'h',
 'i',
 'j',
 'k',
 'l',
 'm',
 'n',
 'o',
 'p',
 'q',
 'r',
 's',
 't',
 'u',
 'v',
 'w',
 'x',
 'y',
 'z'])
        getFactor(out)
    if code=='cls':
        import subprocess as sp
        sp.call('cls', shell=True)
    if 'typeof' in code:
        string = code
        word = 'typeof'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        print(),check_user_input(out)
    if 'set-path' in code:
        string = code
        word = 'set-path'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        global path
        path=out
    if 'youton' in code:
        string = code
        word = 'youton'
        word_list = string.split()
        nout=(' '.join([i for i in word_list if i not in word]))
        download_from_youtube(nout, path)
    if 'set-char' in code:
        string=code
        word='set-char'
        word_list=string.split()
        g=(''.join([i for i in word if i not in word]))
        newg=g
        cork=newg.split()
    def ascii(imgpath,output_file="ascii.txt"):
        # pass the image as command line argument
        image_path = imgpath
        img = Image.open(image_path)
    
        # resize the image
        width, height = img.size
        aspect_ratio = height/width
        new_width = 80
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))
        # new size of image
        # print(img.size)
    
        # convert image to greyscale format
        img = img.convert('L')
    
        pixels = img.getdata()
    
        # replace each pixel with a character from array
        chars = ["~","`","^","1","@","$","%","*","!",":","."]
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
    
        # split string of chars into multiple strings of length equal to new width and create a list
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
    
        # write to a text file.
        with open(output_file, "w") as f:
            f.write(ascii_image)
        return ascii_image
    if code == 'ascii':
        asc()
    if 'ascii-' in code:
        string = code
        word = 'ascii-'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        try:
            try:ascii(out)
            except:print('!')
        except:print('!')
    if 'length'in code:
        string = code
        word = 'length'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        print(len(out))
while True:
    try:
        main()
    except:
        print('ERROR:Restarting')
        import time
        time.sleep(2)
        cls()
        main()
