# coding: utf-8

comp = 0
mov = 0

def comparacao(valor):
	global comp
	comp += valor

def movimentacao(valor):
	global mov
	mov += valor

def resetmetrics():
	global comp, mov
	comp = 0
	mov = 0