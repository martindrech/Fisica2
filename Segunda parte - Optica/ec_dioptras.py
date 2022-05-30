# -*- coding: utf-8 -*-
"""
Created on Fri May 27 16:03:49 2022

@author: Martin
"""

import matplotlib.pyplot as plt
import numpy as np


#%%

R = 5
n1 = 1
n2 = 1.33

def si(so):
    """
    Devuelve el la distancia imagen dada la distancia del objeto de una dioptra 
    esferica de radio R e indices n1 y n2.
    """
    return ((n2-n1)/(R*n2) - n1/(n2*so))**(-1)

print(si(35))
#%%
plt.figure(1)
plt.clf()

s_objetos = np.linspace(1, 30, 2000)
s_imagenes = si(s_objetos)
plt.plot(s_objetos, s_imagenes, '.')
plt.ylabel('$s_i$ [cm]', size = 20)
plt.xlabel('$s_o$ [cm]', size = 20)
plt.title(f'$R$ = {R} cm, $n_1$ = {n1}, $n_2$ = {n2}')

plt.ylim(-500, 500)

#dibujo lineas punteadas en las asintotas, osea en fo y fi. 
plt.vlines(n1*R/(n2-n1), np.min(s_imagenes), np.max(s_imagenes), color = 'k', linestyle = 'dashed')
plt.hlines(n2*R/(n2-n1), np.min(s_objetos), np.max(s_objetos), color = 'k', linestyle = 'dashed')

plt.tight_layout()