#teht 3: 1b)


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)
y = 1.5*x**2-3+7


ax=plt.subplot()

ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# samat mittasuhteet
ax.set_aspect('equal')

# x-akselin säätöä
ax.set_xticks(np.arange(-5, 5, 1))

# Y:lle rajat, että kuvaajat näkyvät fiksummin
plt.ylim([-2, 14])

# label tarvitsee tuon legend():n
plt.plot(x, y, label="$y = 1,5x^2-3x+7$")
plt.legend()

plt.show()