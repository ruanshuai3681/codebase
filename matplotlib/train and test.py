import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
data_x=np.random.seed(2)
data_x=np.random.normal(3, 1, 1000)
data_y=np.random.normal(500, 10, 1000)/data_x

train_x=data_x[:800]
train_y=data_y[:800]

test_x=data_x[800:]
test_y=data_y[800:]

plt.scatter(train_x,train_y)

myfuc=np.poly1d(np.polyfit(train_x, train_y, 4))

fit_x=np.linspace(0,6,1000)
fit_plot=myfuc(fit_x)
plt.plot(fit_x, fit_plot)

plt.show()

train_r2=r2_score(train_y, myfuc(train_x))
print(train_r2)

test_r2=r2_score(test_y, myfuc(test_x))
print(test_r2)
