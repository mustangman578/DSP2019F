# If you go beyond the range, for example with int8, you get don't get the right values and it responds with negative values.

import numpy as np

print(np.int8(1233))
print(np.iinfo(np.int16))
print(np.iinfo(np.int32))

'''
-47
Machine parameters for int16
---------------------------------------------------------------
min = -32768
max = 32767
---------------------------------------------------------------

Machine parameters for int32
---------------------------------------------------------------
min = -2147483648
max = 2147483647
---------------------------------------------------------------

'''
