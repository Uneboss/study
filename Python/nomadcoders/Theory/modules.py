# modules
from math import ceil, fabs
print(ceil(1.3)) # 올림
print(fabs(-1.2)) # 절대값

from math import fsum as cutty_sum
print(cutty_sum([1,2,3,4,5]))
# can't use name "fsum" anymore

from calculator import plus, minus
print(plus(1,3), minus(3,1))
# print() can get infinite arguments
