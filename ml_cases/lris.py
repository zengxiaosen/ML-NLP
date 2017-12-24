import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib as plt
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def iris_type(s):
    it = {'Iris-setosa': 0,'Iris-versicolor': 1,'Iris-virginica': 2}
    return it[s]

if __name__ == "__main__":
    path = 'iris.data'
    path_csv = 'iris.csv'

    f = file(path)
    x = []
    y = []
    for d in f:
        print d
        d = d.strip()
        if d:
            d = d.split(',')
            y.append(d[-1])
            x.append(map(float, d[:-1]))
            print x
            print y

    x = np.array(x)
    print x

    y = np.array(y)
    print y
    y[y == 'Iris-setosa'] = 0
    y[y == 'Iris-versicolor'] = 1
    y[y == 'Iris-virginica'] = 2

    print y
    y = y.astype(dtype=np.int)
    print y

    df = pd.read_csv(path_csv)
    x = df.values[:, :-1]
    y = df.values[:, -1]

    print x
    print y

    le = preprocessing.LabelEncoder()
    le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    print le.classes_
    y = le.transform(y)
    print y

    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    print data

    x, y = np.split(data, (4,), axis=1)
    print x
    print y

    x = x[:, :2]
    print x
    print y
    # x = StandardScaler().fit_transform(x)
    # logreg = LogisticRegression()
    # logreg.fit(x, y.ravel())
    logreg = Pipeline([('sc', StandardScaler()),
                       ('clf', LogisticRegression()) ])
    logreg.fit(x, y.ravel())

    N, M = 500, 500
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()
    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, M)
    x1, x2 = np.meshgrid(t1, t2)
    print x1
    x_test = np.stack((x1.flat, x2.flat), axis=1)
    print x_test

    y_hat = logreg.predict(x_test)
    y_hat = y_hat.reshape(x1.shape)
    plt.pcolormesh(x1, x2, y_hat, cmap=plt.cm.Spectral, alpha=0.6)
    plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', s=50, cmap=plt.cm.prism)
    plt.xlabel('Sepal lenght')
    plt.ylabel('Sepal width')
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.grid()
    plt.show()

    y_hat = logreg.predict(x)
    y = y.reshape(-1)
    result = y_hat == y
    print result
    c = np.count_nonzero(result)
    print c
    print 'Accuracy: %.2f%%' % (100 * float(c) / float(len(result)))




