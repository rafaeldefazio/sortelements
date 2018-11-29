#coding: utf8
import csv



def ler(pathPassos, pathArray):
	global arrayI
	global passos

	# abre arquivos
	fp = open(pathPassos, 'r')
	fa = open(pathArray, 'r')


	# arrays vazias
	passos = []
	arrayI = []

	# lê passos
	ler = csv.reader(fp)
	for linha in ler:
	    passos = passos + [[int(linha[0]), int(linha[1])]]
	fp.close()

	# lê array original
	ler = csv.reader(fa)
	for linha in ler:
		arrayI = arrayI + [int(linha[0])]
	fa.close()
