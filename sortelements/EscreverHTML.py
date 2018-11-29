#coding: utf8
import LerShell
from copy import deepcopy as dp
import subprocess
from os import getcwd

def escreverShell():
    PATH = "output/shell"
    LerShell.ler("%s/shellSortPassos.csv" % PATH, "%s/array.csv" % PATH)
    arrayI = LerShell.arrayI
    arrayT = dp(arrayI)
    passos = LerShell.passos

    HTMLi = """<!DOCTYPE HTML>
    <html>

    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Shell Sort</title>
        <style type="text/css">
            span.numero{
                        cursor: default;
                    }
            
                    p{
                        text-align: center;
                    }
            
                    p.atual{
                        font-size: 2em;
                        color: grey;
                    }
        </style>

    </head>

    <body>

        <div class="container">
            <div class="row valign-wrapper">
                <div class="col s8 offset-s2 valign">
                    <h1>Shell Sort</h1>
                    <br/><br/>"""

    HTMLArrayInicial = '<h3><span class="badge">Array inicial</span>%s</h3><br/>' % arrayI
    HTMLloopCards = []


    for p in passos:
        gap = p[1] - p[0]
        card = """<div class="card light-grey darken-1">
                        <div class="card-content dark-grey-text">
                            <span class="card-title">Trocar elemento</span>
                            <p><span class="badge">Gap: %d</span><span class="waves-effect waves-light btn numero">%d</span> com <span class="waves-effect waves-light btn numero">%d</span></p>
                        </div>
                    </div>""" % (gap, arrayT[p[0]], arrayT[p[1]])

        arrayT[p[0]], arrayT[p[1]] = arrayT[p[1]], arrayT[p[0]]

        card = card + """
                    <div class="card light-grey darken-1">
                        <div class="card-content dark-grey-text">
                            <span class="card-title">Array atualizado</span>
                            <p class="atual">%s</</p>
                        </div>
                    </div>""" % arrayT

        HTMLloopCards = HTMLloopCards + [card]

    HTMLArrayFinal = """
                    <br/>
                    <h3><span class="badge">Array ordenada</span>%s</h3>
                </div>""" % arrayT

    HTMLf = '</div></div><script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script></body></html>'



    salvar = open("%s/shellSort.html" % PATH,"w")
    salvar.write(HTMLi)
    salvar.write(HTMLArrayInicial)
    for c in HTMLloopCards:
        salvar.write(c)
    salvar.write(HTMLArrayFinal)
    salvar.write(HTMLf)
    salvar.close() 
    #subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe', '-new-tab', '%s' % (getcwd() + "\\" + PATH.replace("/", "\\") + "\\shellSort.html")])

    