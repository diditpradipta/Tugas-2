# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from cmath import exp, pi
import matplotlib.pyplot as plt
import numpy as np

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    genap = fft(x[0::2])
    ganjil = fft(x[1::2])
    q = [exp(-2j * pi * k / N) * ganjil[k] for k in range(N//2)]
    return [(genap[k] + q[k]) for k in range(N//2)] + [(genap[k] - q[k]) for k in range(N//2)]

def generate_signal(t, A, width):
    return [1 if -width * A < i < width * A else 0 for i in t]

def plot_signal_and_fft(signal, title):
    output = fft(signal)
    output_oneside = output[:n//2]
    
    plt.plot(t, signal)
    plt.title(title + ' Signal')
    plt.show()

    plt.plot(f, output_oneside)
    plt.title('FFT of ' + title)
    plt.show()

A = 4
t_interval = 8 * A
n = 512
t = [i * t_interval / n for i in range(-n//2, n//2)]
f = list(range(n//2))

plot_signal_and_fft(generate_signal(t, A, 0.5), 'Signal 1 (A/2)')
plot_signal_and_fft(generate_signal(t, A, 1), 'Signal 2 (A)')
plot_signal_and_fft(generate_signal(t, A, 3), 'Signal 3 (3A)')