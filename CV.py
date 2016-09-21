#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.grid_search import GridSearchCV

if __name__ == "__main__":
    N = 50
    np.random.seed(0)
    x = np.sort(np.random.uniform(0, 6, N), axis=0)
    y = 2*np.sin(x) + 0.1*np.random.randn(N)
    x = x.reshape(-1, 1)
    print 'x=\n', x
    print 'y=\n', y

    model = svm.SVR(kernel='rbf', gamma=0.1)
    c_can = np.logspace(-2, 2, 10)
    gamma_can = np.logspace(-2, 2, 10)
    svr = GridSearchCV(model, param_grid={'C': c_can, 'gamma': gamma_can}, cv=5)
    svr.fit(x, y)
    print '验证参数: \n', svr.best_params_

    x_test = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
    y_hat = svr.predict(x_test)
    # 支撑向量
    sp = svr.best_estimator_.support_
    plt.scatter(x[sp], y[sp], s=120, c='r', marker='*', label='Support Vectors')
    plt.plot(x_test, y_hat, 'r-', linewidth=2, label='RBF Kernel')
    plt.plot(x, y, 'go', markersize=5)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()




