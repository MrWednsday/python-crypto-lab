binary = "01001111101001110010110001001101"

permutation = [
    16,7,20,21,29,12,28,17,
    1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,
    19,13,30,6,22,11,4,25
]

output = ""
for i in permutation:
    output += binary[i - 1]

print(output)