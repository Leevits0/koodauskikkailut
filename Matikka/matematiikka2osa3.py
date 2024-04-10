from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure(figsize=(6.4*3, 4.8*3))  # Luodaan yksi kuvaaja

# Luodaan ensimmäinen alakuvio
ax1 = plt.subplot(211)  # 2 riviä, 1 sarake, ensimmäinen alakuvio
ymp = patches.Circle((0, 0), radius=1, fill=0)
ax1.add_patch(ymp)

ax1.spines['left'].set_position('center')
ax1.spines['bottom'].set_position('center')
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

ax1.axis('equal')

plt.xticks(np.arange(-3*np.pi, 4*np.pi, np.pi), [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$'])
plt.yticks(np.arange(-1, 2, 1))

pii = np.pi
pist_xy = np.array([pii, pii/2, 3*pii/4, pii/6, 2*pii/3, 5*pii/6, pii, 3*pii/2])
nim = np.array([1, 2, 4, 6, 3, 6, 1, 2])
varit = np.array(['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow'])

text = [r'$\pi$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\frac{\pi}{6}$', r'$\frac{2\pi}{3}$', r'$\frac{5\pi}{6}$', r'$\pi$', r'$\frac{3\pi}{2}$']

x = np.cos(pist_xy / nim)
y = np.sin(pist_xy / nim)

plt.scatter(x, y, color=varit, marker='X')

for i in range(len(pist_xy)):
    plt.annotate(text[i],
                 xy=(np.cos(pist_xy[i] / nim[i]), np.sin(pist_xy[i] / nim[i])), xycoords='data',
                 xytext=(+30, +5), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.legend(text, loc='upper right')


# Luodaan toinen alakuvio
ax2 = plt.subplot(212)  # 2 riviä, 1 sarake, toinen alakuvio
X = np.linspace(-3*np.pi, 3*np.pi, 1000, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color='blue', linestyle='-', label='Cosine')
plt.plot(X, S, color='red', linestyle='--', label='Sine')

plt.xticks([-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi],
           [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$'])
plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$1$'])

plt.legend()

plt.show()
