file = open("input.txt")
lines = file.readlines()

gam = 0
eps = 0

for i in range(len(lines[0])-1):
    zero = 0
    one = 0
    for line in lines:
        if int(line[i]) == 0:
            zero = zero + 1
        else:
            one = one + 1
    if one > zero:
        gam = gam + 2 ** (len(lines[0])-2-i)
    else:
        eps = eps + 2 ** (len(lines[0])-2-i)

print("gamma   :: " + str(gam))
print("epsilon :: " + str(eps))
print("result  :: " + str(gam * eps))