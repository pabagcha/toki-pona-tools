from random import *
from pathlib import Path
import argparse

with open(Path('grammar/GramaticaTokiPona2adaptadogenerador.txt'), encoding='UTF8') as fil: rules = fil.readlines()
rules = [y.strip() for y in rules]

parser = argparse.ArgumentParser(description="Toki Pona sentence generator.\n The sentences generated probably do not make sense but are grammatically correct.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--number", type=int,required=False,default="1", help="number of generated sentences")
flags = parser.parse_args()
def EsTerminal(frase=''):
    words = x.strip().split(' ')
    for w in words:
        if w.isupper():
            return False
    return True

def expand (palabra, frase):
    for r in rules:
        partes = r.split("=")
        if partes[0].strip() == palabra.strip():
            opciones = partes[1].split("|")
            if opciones[0].strip() == "λ": 
                eleccion = randint(0,(len(opciones)-1)*3)
                if eleccion >= len(opciones): eleccion =0
            elif palabra.strip() == 'SN' or  palabra.strip() =='SUJ' or  palabra.strip() =='SUJLI' or palabra.strip() =='PREDSINCC': 
                eleccion = randint(0,(len(opciones)-1)*3)
                if eleccion >= len(opciones): eleccion =0
            else: eleccion = randint(0,len(opciones)-1)
            
            return frase.replace(palabra, opciones[eleccion].strip(),1)


def format(frase):
    if frase.find("λ") >= 0: frase=frase.replace("λ","")
    frase=" ".join(frase.split()).strip()
    frase=frase.replace(" ,",",")
    if  frase[-1] == '?' : frase=frase.replace(" ?","?")
    elif frase[-1] == '!' :frase=frase.replace(" !","!")
    else: frase = frase+"."
    return frase

             
for i in range(flags.number):
    x="S"
    while not EsTerminal(x):
        words = x.strip().split(' ')
        for w in words:
            if w!="" and w.isupper():
                x = expand(w,x)
                break
    
    print(format(x))   




