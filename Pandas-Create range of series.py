
""" Write a function that takes start and end of a range returns a Pandas series object containing
numbers within that range.
In case the user does not pass start or end or both they should default to 1 and 10 respectively.
eg.
 range_series() -> Should Return a pandas series from 1 to 10
 range_series(5) -> Should Return a pandas series from 5 to 10
 range_series(5, 10) -> Should Return a pandas series from 5 to 10."""

import pandas as pd
class cs:
    def range_series(self,a=0,b=10):
        return pd.Series(range(a,b))
c=cs()
print(c.range_series())
print(c.range_series(5))
print(c.range_series(5,10))

