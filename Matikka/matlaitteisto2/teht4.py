#teht 4
# tehtävän pallon lentorataa kuvaava paraabeli:

#teht 3: 1b)


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-100, 100, 100)
y = -0.0063*x**2+0.55*x


ax=plt.subplot()

ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# samat mittasuhteet
#ax.set_aspect('equal')

# x-akselin säätöä
ax.set_xticks(np.arange(-2, 100, 10))

# Y:lle rajat, että kuvaajat näkyvät fiksummin
plt.ylim([-4, 13])

# label tarvitsee tuon legend():n
plt.plot(x, y, label="$y = -0,0063x^2+0.55x$")
plt.legend()

plt.show()