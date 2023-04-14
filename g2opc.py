#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script to convert a file with point charges in Gaussian format
to a point charge file in ORCA format 

Created on Fri Apr 14 07:36:39 2023

@author: borowski
"""
import sys, os

### Seting the file names                                                  ###
sys_argv_len = len(sys.argv)
if sys_argv_len > 1:
    inp_f_name = sys.argv[1]
else:
    inp_f_name = None
if sys_argv_len > 2:
    output_fname = sys.argv[2]
else:
    output_fname = None

if not os.path.isfile(inp_f_name):
    print("Input file (with Gaussian point charges) not found \n")
    sys.exit(1)

### reading the Gaussian pc file ###
inp_f = open(inp_f_name, 'r')

n_lines = 0
X = []
Y = []
Z = []
Q = []

for line in inp_f:
    s_line = line.split()
    if len(s_line) == 4:
        n_lines += 1
        X.append(s_line[0])
        Y.append(s_line[1])
        Z.append(s_line[2])
        Q.append(s_line[3])
        
inp_f.close()

### writing output ORCA point charge file ###
if output_fname != None:
    out_f = open(output_fname, 'w')
    out_f.write(str(n_lines) + '\n')
else:
    print(str(n_lines))
    
if output_fname != None:
    for i in range(n_lines):
        line2write = Q[i] + '\t' + X[i] + '\t' + Y[i] + '\t' + Z[i] + '\n'
        out_f.write(line2write)
    out_f.close()
else:
    for i in range(n_lines):
        line2write = Q[i] + '\t' + X[i] + '\t' + Y[i] + '\t' + Z[i]
        print(line2write)


 