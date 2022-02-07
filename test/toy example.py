from ACLS.RGD_bindings import RGD
import numpy as np
Y = np.array([1, 3])
X = np.array([[1, 2], [3, 4]])
tau=2
iter=100
eta_0=1e-3
alpha=2
print(RGD(X.T,Y,tau,iter,eta_0,alpha))
