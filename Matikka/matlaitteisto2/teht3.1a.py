#teht 3: 1a)

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 8, 100)
y = x**2-4*x+3


ax=plt.subplot()

ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# samat mittasuhteet
ax.set_aspect('equal')

# x-akselin säätöä
ax.set_xticks(np.arange(-5, 8, 1))


# Y:lle rajat, että kuvaajat näkyvät fiksummin
plt.ylim([-5, 14])

# label tarvitsee tuon legend():n
plt.plot(x, y, label="$a) y = x^2-4x+3$")
plt.legend()
plt.show()