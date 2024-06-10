import pandas as pd
import numpy as np


# Constructing DataFrame from a dictionary:
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
df


# Constructing DataFrame from a dictionary including Series:
d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
pd.DataFrame(data=d, index=[0, 1, 2, 3])


# Constructing DataFrame from numpy ndarray:
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                    columns=['a', 'b', 'c'])
df2


# Constructing DataFrame from Series/DataFrame:
ser = pd.Series([1, 2, 3], index=["a", "b", "c"])
df = pd.DataFrame(data=ser, index=["a", "c"])
df


# The index of a DataFrame is a series of labels that identify each row.
# Check index of a DataFrame:
df.index


# Replace index of a DataFrame:
df.index = [100, 200]
df.index


# The column labels of the DataFrame.
# Check columns of DataFrame:
df.columns


# This returns a Series with the data type of each column:
df.dtypes


# Print a concise summary of a DataFrame.
# With details
df.info(verbose=True)


# Without details
df.info(verbose=False)


# Return a subset of the DataFrame’s columns based on the column dtypes.
df = pd.DataFrame({'a': [1, 2] * 3,
                'b': [True, False] * 3,
                'c': [1.0, 2.0] * 3})
df.select_dtypes(exclude=['int64'])


# Only the values in the DataFrame will be returned, the axes labels will be removed.
df.values


# It has the row axis labels and column axis labels as the only members. 
# They are returned in that order.
df.axes


# Return an int representing the number of axes / array dimensions.
# Return 1 if Series. Otherwise return 2 if DataFrame:
s = pd.Series({'a': 1, 'b': 2, 'c': 3})
s.ndim


# Return an int representing the number of elements in this object.
# Return the number of rows if Series. 
# Otherwise return the number of rows times number of columns if DataFrame.
df.size


# Return a tuple representing the dimensionality of the DataFrame.
df.shape


# Return the memory usage of each column in bytes.
# The memory usage can optionally include the contribution of the index and elements of object dtype:
df.memory_usage()


# Indicator whether Series/DataFrame is empty:
df_empty = pd.DataFrame({'A' : []})
df_empty














