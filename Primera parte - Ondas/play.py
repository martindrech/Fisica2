# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:26:55 2022

@author: Martin
"""
import sounddevice as sd
import numpy as np
import pylab as plt
import time
from scipy import signal


def generador_de_senhal(frecuencia, duracion, amplitud, fs=44100):
    """
    Genera una señal de forma seniodal, de rampa, con una dada frecuencia y duracion.
    """
    cantidad_de_periodos = duracion*frecuencia
    puntos_por_periodo = int(fs/frecuencia)
    puntos_totales = puntos_por_periodo*cantidad_de_periodos
           
    tiempo = np.linspace(0, duracion, puntos_totales)
    data = amplitud*np.sin(2*np.pi*frecuencia*tiempo)
    return tiempo, data
    
def play_tone(frecuencia, duracion, amplitud=1, fs=44100, wait=True):
    """
    Esta función tiene como output un tono de una cierta duración y frecuencia.
    """
        
    tiempo, data = generador_de_senhal(frecuencia, duracion, amplitud,fs)   
    sd.play(data, fs)
    
    if wait:
        time.sleep(duracion)
        
    return data

def play_two(frecuencia, df, duracion = 5, amplitud = 1, fs=44100):
    """
    Esta función tiene como output un tono de una cierta duración y frecuencia, al que se le suma 
    uno de igual duracion pero frecuencia corrida en df.
    """
        
    cantidad_de_periodos = duracion*frecuencia
    puntos_por_periodo = int(fs/frecuencia)
    puntos_totales = puntos_por_periodo*cantidad_de_periodos
    
    tiempo = np.linspace(0, duracion, puntos_totales)

    data = amplitud* ( np.sin(2*np.pi*frecuencia*tiempo) + np.sin(2*np.pi*(frecuencia+df)*tiempo) )
    sd.play(data, fs)
    
    
def record(duracion, fs=192000):
    """
    Graba la entrada de microfono por el tiempo especificado
    """
    #sd.default.samplerate = fs #frecuencia de muestreo
    sd.default.channels = 1 #1 porque la entrada es una sola
    
    grabacion = sd.rec(frames = fs*duracion, blocking = True)
    return grabacion

