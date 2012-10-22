# !/bin/python
from __future__ import division
import sys
import random

"""
The script is rewritten C as Python.
====================================================
"""

for i in range(NPATH+1):
	cash_flow[i]=payoff(stock[i][tmax], pexe)

for t in range(NPATH,0,-1):i
	for n in range(NPATH+1)
		cash_flow[n]=discount
		basis_func(stock[n][t], func_value)
		for k in range(ORDER+1):
			matrix[n][k]=func_value[k]
			save[n][t]=func_value[k]
		matrix[n][ORDER+1]=cash_flow[n]
	householder(matrix, reg_coef, NPATH, ORDER+1)
	for n in range(NPATH+1):
		exerval = payoff(stock[n][t])
		if (exerval>0):
			contval=0
			for k in range(ORDER+1):
				contval+=reg_coef[k]*save[n][k]
			if (exerval > contval):
				cash_flow[n]=exerval

average #when time=0, discounted cash_flow's average
price = max(average, exerval) # when t=0
