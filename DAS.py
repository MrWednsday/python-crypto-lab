messageBinary = "0011000100110001001100010011000100110001001100010011000100110001"
keyBinary = "0011000100110001001100010011000100110001001100010011000100110001"

messageBinary = "0011000000110000001100000011000000110000001100000011000000110000"
keyBinary = "0011000000110000001100000011000000110000001100000011000000110000"

initialPermList = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7]

expansionList = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,21,1]

keyTransformList = [
    57,49,41,33,25,17,9,1,
    58,50,42,34,26,18,10,2,
    59,51,43,35,27,19,11,3,
    60,52,44,36,63,55,47,39,
    31,23,15,7,62,54,46,38,
    30,22,14,6,61,53,45,37,
    29,21,13,5,28,20,12,4
]

keyShortList = [
    14,17,11,24,1,5,3,28,
    15,6,21,10,23,19,12,4,
    26,8,16,7,27,20,13,2,
    41,52,31,37,47,55,30,40,
    51,45,33,48,44,49,39,56,
    34,53,46,42,50,36,29,32
]

initialPem = ""
for i in initialPermList:
    initialPem += messageBinary[i - 1]

print("Initial permutation")
print(initialPem)


rightSideOfInitialPerm = initialPem[32:]
leftSideOfInitialPerm = initialPem[0:32]

print("Right side of initial perm")
print(rightSideOfInitialPerm)

print("Left side of initial perm")
print(leftSideOfInitialPerm)

expandedRightSide = ""
for i in expansionList:
    expandedRightSide += initialPem[i - 1]

print("Expanded right side")
print(expandedRightSide)

keyShort = ""
for i in keyTransformList:
    keyShort += keyBinary[i - 1]

print("Key 56bit")
print(keyShort)

keyShortLeft = keyShort[0:28]
keyShortRight = keyShort[28:]

print("Key 56bit left side")
print(keyShortLeft)
print("Key 56bit right side")
print(keyShortRight)


print("Key left side rotate left 1")
keyShortLeftRotate = keyShortLeft[1:] + keyShortLeft[0]
print(keyShortLeftRotate)
print("Key right side rotate left 1")
keyShortRightRotate = keyShortRight[1:] + keyShortRight[0]
print(keyShortRightRotate)

keyRotatedCombined = keyShortLeftRotate + keyShortRightRotate

print("Combined key")
print(keyRotatedCombined)

keyOutput = ""
for i in keyShortList:
    keyOutput += keyRotatedCombined[i - 1]


print("Key short output")
print(keyOutput)

expandedRightSide
keyOutput

xOr = ""
for i in range(len(expandedRightSide)):
    xOr += str((int(expandedRightSide[i]) ^ int(keyOutput[i])))

print("xOr")
print(xOr)