import numpy as np
import pandas as pd




from numpy.random import randn



df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc', 'def', 'ghi', 'xyz']})
print(df.head())
print(df['col2'].nunique())
print(df['col2'].value_counts())
print(df[df['col1']>2])





from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
print(df.to_sql('my_table',engine))