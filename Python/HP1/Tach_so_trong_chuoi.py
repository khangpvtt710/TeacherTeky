# cách nhau bởi dấu cách
s = "12 45 78 3"
numbers = [int(x) for x in s.split()]
print(numbers)
# cách nhau bởi dấu phẩy
s = "12,45,78,3"
numbers = [int(x) for x in s.split(",")]
print(numbers)
# tách số trong chuỗi
import re
s = "Tôi có 12 con cá và 3 con mèo"
numbers = [int(x) for x in re.findall(r'\d+', s)]
print(numbers)
# tách từng số
s = "123456"
digits = [int(ch) for ch in s]
print(digits)