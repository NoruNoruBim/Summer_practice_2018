from sklearn.linear_model import Perceptron
import numpy as np


base = []
with open("base.txt", 'r') as file:
	for line in file:
		line = line.split()
		if float(line[-1]) != 3:
			base += [line]
for i in range(len(base)):
	for j in range(len(base[i])):
		base[i][j] = float(base[i][j])
base = np.array(base)
#print(base)


X_train = np.array(base[ : len(base) * 0.8, : -1])
y_train = np.array(base[ : len(base) * 0.8, -1 : ]).ravel()

X_test = np.array(base[len(base) * 0.8 : , : -1])
y_test = np.array(base[len(base) * 0.8 : , -1 : ]).ravel()

#print(y_train)
#print(y_test)

ppn = Perceptron(n_iter = 30, eta0 = 0.1, random_state = 0)
ppn.fit(X_train, y_train)

errors = ppn.predict(X_test) - y_test

good = 0
for i in range(len(errors)):
	if errors[i] == 0:
		good += 1
print(good / float(len(errors)))
