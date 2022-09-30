import random
import string

#losowy ciąg znaków
source = string.ascii_letters + string.digits
result_str = ''.join((random.choice(source) for i in range(100)))
print(result_str)
