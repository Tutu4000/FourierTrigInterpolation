import numpy as np
import matplotlib
import matplotlib.pyplot as plt


plt.style.use('fast')
matplotlib.use('tkagg')

def interpolacao_trig(pontos):
    N = len(pontos)
    fourier = np.fft.fft([p[1] for p in pontos])
    fourier = fourier/N
    print(fourier)
    def interpolante(x):
        soma = 0
        for i in range(N):
            soma += fourier[i] * np.exp(1j * i * x)
        return soma
    return interpolante

def interpolacao_trig_corrigida(pontos):
    N = len(pontos)
    fourier = np.fft.fft([p[1] for p in pontos])
    fourier = fourier/N
    if N % 2 == 0:
        def interpolante(x):
            m = N // 2 # N = 2m
            soma = 0
            for i in range (-m, m):
                soma += fourier[i] * np.exp(1j * i * x)
            return soma
    else:
        def interpolante(x):
            m = (N - 1) // 2 # N = 2m + 1
            soma = 0
            for i in range(-m, m+1):
                soma += fourier[i] * np.exp(1j * i * x)

            return soma
    return interpolante

def intervalos(N):
    step = 2*np.pi/N
    return [(i*step) for i in range(N)]



#Definindo os pontos:
pontos = [(0, 0), (2*np.pi/5, 3), (4*np.pi/5, 0), (6*np.pi/5, -3), (8*np.pi/5, 0)]
pontos2 = [(0,0), (2*np.pi/5, 3*np.pi/4), (4*np.pi/5,np.pi), (6*np.pi/5, 3*np.pi/4), (8*np.pi/5,3)]
pontos3 = [(0,0), (2*np.pi/8, 3), (4*np.pi/8,0), (6*np.pi/8, -3), (8*np.pi/8,0), (10*np.pi/8,3), (12*np.pi/8,0), (14*np.pi/8,-3)]
pontos4 = [(0,0), (4*np.pi/4, 3), (8*np.pi/4,0)]

x,y = zip(*pontos)
for xi, yi in zip(x, y):
    plt.axhline(y=yi, xmin=0, xmax=xi, linestyle='--', alpha = 0.2)
    plt.axvline(x=xi, ymin=0, ymax=yi, linestyle='--', alpha = 0.2)
plt.scatter(x, y, label="Pontos originais")



#Função interpoladora calculada manualmente



#plotando a funcao interpoladora
x = np.linspace(0, np.pi*2, 200)

# Calculando a interpolacao trigonometrica e plotando
fic = interpolacao_trig_corrigida(pontos)
fic = np.array([fic(xi) for xi in x])
plt.plot(x,fic, label="Interpolacao com correcao")

fi = interpolacao_trig(pontos)
fi = np.array([fi(xi) for xi in x])
plt.plot(x,fi, label="Interpolacao sem correcao")

plt.legend()
plt.show()