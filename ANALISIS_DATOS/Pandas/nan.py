# coding: utf-8
a = pd.Series([10,20,np.NaN, 40, np.NaN])
a
pd.isnull(a)
pd.notnull(a)
a.isnull()
a
a.dropna()
a
a.fillna(99)
a[ a.notnull() ]
