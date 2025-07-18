a = 6

while (a > 0):
    if(a<2):
        break 
        continue
    print(a)
    a -= 1 

for x in ['khang', 'tiến']:
    print(x)
for x in range(10):
    print(x)
for x in range(2,10):
    print(x)
for x in range(2,-10,-1):
    print(x)



# nhập 1 số và in ra tất cả các số nguyên tố nhỏ hơn số vừa nhập
n = int(input("Nhập một số: "))

for i in range(2, n):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)