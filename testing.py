input = ["pierwszeFalse", "oko", "akilkutuklika"]

temp = input[0].split()

print(temp)
temp = False

A = [3, 5, 15, 30, 300]
B = ["A", "B", "C", "D", "E"]

for i in range(1, 10000):
    for x in range(len(A)-1, 0, -1):
        if i % A[x] == 0:
            print(B[x])
            temp = True
        elif x == 0 and temp == False:
            print(i)
        temp = False
