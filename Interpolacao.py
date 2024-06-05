import numpy as np
import matplotlib.pyplot as plt

class TrigInterp:
    def __init__(self, x, dx):
        self.Q = len(x) # Número de pontos
        self.dx = dx # Distância entre os pontos
        self.c = np.fft.rfft(x) # É um vetor de coeficientes

    def interp(self, x):
        y = self.c[0].real / 2 # Coeficiente para k = 0
        Q = self.Q # Número de pontos
        P = Q * self.dx # Período
        N = len(self.c) # Número de coeficientes
        for k in range(1, N):
            c = self.c[k]
            y += c.real * np.cos(2 * np.pi * k * x / P) - c.imag * np.sin(2 * np.pi * k * x / P)

        return 2 * y / Q
    #
    # def __call__(self, x):
    #     return self.interp(x)

def main():
    # Inicializar n de pontos, distancia entre pontos e os pontos a serem interpolados para criar o objeto
    # interpolar os pontos usando o método interp
    # plotar os pontos e a interpolação


    num_pontos = 5
    intervalos = 1.0 # Comprimento do intervalo
    pontos = [1,2,3,-1,4]
    x0 = np.linspace(0, intervalos, num_pontos + 1)[:-1]

    trig_interp = TrigInterp(pontos, intervalos / num_pontos)# Interpolação
    x = np.arange(0, intervalos, 0.01)# Pontos para plotar
    y = trig_interp.interp(x) # Valores interpolados

    print(trig_interp.c)
    plt.plot(x, y, "k:", label="Interpolado")
    plt.plot(x0, pontos, "ro", label="Pontos")
    plt.legend()
    plt.show()

def triginterp(t, y):
    N = len(t)

    def tau(x):
        denom = np.where(N % 2 == 1, N * np.sin(np.pi * x / 2), N * np.tan(np.pi * x / 2))
        return np.where(x == 0, 1.0, np.sin(N * np.pi * x / 2) / denom)

    def interpolant(x):
        return sum(y[k] * tau(x - t[k]) for k in range(len(y)))

    return interpolant

# toriginal = [-1,-0.5,0,0.5,1]
# y = [3,0,1,0,4]
# N = len(toriginal)
# n = (N - 1) // 2
# t = 2 * np.arange(-n, n + 1) / N
# f = triginterp(t, y) # F é a função interpolante
# x = np.linspace(-1, 1, 100)
# plt.plot(x, f(x))
# plt.plot(toriginal, y, "bo")
# plt.plot(t, y, "ro")
# plt.legend(["Interpolacao", "Pontos originais", "Pontos corrigidos"])
# plt.show()



# f = lambda x: np.exp(np.sin(np.pi*x)-2*np.cos(np.pi*x))
# N = 7
# n = (N - 1) // 2
# t = 2 * np.arange(-n, n + 1) / N
# print(t)
# y = f(t)
# px = triginterp(t, y)
# x = np.linspace(-1, 1, 200)
# fi = triginterp(t, y)
# plt.plot(x,px(x), label="Interpolacao", color="black")
# plt.plot(x, f(x), label="funcao")
# plt.plot(t, y, "ro", label="Pontos")
# plt.show()

def interpolar(f,N):
    n = (N - 1) // 2
    t = 2 * np.arange(-n, n + 1) / N
    y = f(t)
    return triginterp(t, y), t, y



# f = lambda x: np.exp(np.sin(np.pi*x)-2*np.cos(np.pi*x))
# N = 7
# fi, t,y = interpolar(f,N)
# x = np.linspace(-1, 1, 200)
# plt.plot(x,fi(x), label="Interpolacao", color="black")
# plt.plot(x, f(x), label="funcao")
# plt.plot(t, y, "ro", label="Pontos")
# plt.legend()
# plt.show()
#
#
# f = lambda x: np.exp(np.cos(np.pi*x)-5*np.sinc(np.pi*x))
# N = 3
# fi , t , y = interpolar(f,N)
# print(t)
# x = np.linspace(-1, 1, 200)
# plt.plot(x,fi(x), label="Interpolacao", color="black")
# plt.plot(x, f(x), label="funcao")
# plt.plot(t, y, "ro", label="Pontos")
# plt.legend()
# plt.show()

# x = [-0.6666, 0, 0.6666] # t = 2 * np.arange(-n, n + 1) / N onde N = 3 e n = N - 1 // 2
# pontos = x
# y = [6, 2, 0]
# f = triginterp(x, y)
# x = np.linspace(-1, 1, 200)
# plt.plot(x, f(x))
# plt.plot(pontos, [6, 2, 0], "ro")
# plt.show()
#
