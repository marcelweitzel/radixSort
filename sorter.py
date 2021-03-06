import random
import math


def bucket_iteration(eingabe, stellenwert):
    output = [0]*len(eingabe)
    counts = [0]*10
    for number in eingabe:
        counts[get_Digit_from_right_to_left(number, stellenwert)] += 1
    sum = 0
    for i in range(len(counts)):
        counts[i] = sum = sum+counts[i]
    for number in eingabe[::-1]:
        digit = get_Digit_from_right_to_left(number, stellenwert)
        counts[digit] -= 1
        output[counts[digit]] = number
    return output


def get_Digit_from_right_to_left(number, zehner_stelle):
    reduction = math.floor(number/zehner_stelle)
    return reduction % 10


ARRAY_SIZE = int(input("How large should the random array be?\n"))
eingabe = [i for i in range(ARRAY_SIZE)]
random.shuffle(eingabe)
#eingabe = [277, 806, 681, 462, 787, 163, 284, 166, 905, 518, 263, 395, 988, 307, 779, 721]
print("this is the random array:\n", eingabe)
for i in range(math.ceil(math.log10(ARRAY_SIZE))):
    eingabe = bucket_iteration(eingabe, pow(10, i))
print("and this is its solved state:\n", eingabe)
