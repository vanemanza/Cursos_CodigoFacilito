# coding: utf-8
a = pd.Series(np.arange(4))
a
a = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'])
a
a = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'], dtype=np.float32)
a
a['a']
a[0]
a.name = 'numeros'
a
a.index
a.index.values
a.index.values = 'indices'
a.index.values
a.index.tolist()
a.index.name = 'indices'
a
b = a *10
b
b[ b>15]
b[(b>15) 
b[(b > 15) & (b != 0) ]
