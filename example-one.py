# This is a sample Python script.
import array
import math

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

f = open('input', 'r').read()


def countEven():
    count = 0
    for line in f.splitlines():
        for value in line.split(" "):
            if int(value) % 2 == 0:
                count += 1
    return count


print(f"Có bao nhiêu số chẵn: {countEven()}")


def countOdd():
    count = 0
    for line in f.splitlines():
        for value in line.split(" "):
            if int(value) % 2 != 0:
                count += 1
    return count


print(f"Có bao nhiêu số lẽ: {countOdd()}")


def prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = False
            break
    else:
        return True


def countPrime():
    count = 0
    for line in f.splitlines():
        for value in line.split(" "):
            if prime(int(value)):
                count += 1
    return count


print(f"Có bao nhiêu số nguyên tố: {countPrime()}")


def countAppear():
    count = {}

    for line in f.splitlines():
        for value in line.split(" "):
            if count.get(value):
                count[value] += 1
            else:
                count[value] = 1

    maxValue = 0
    appear = None

    for key in count.keys():
        if count[key] > maxValue:
            maxValue = count[key]
            appear = key

    return appear


print(f"Số xuất hiện nhiều nhất: {countAppear()}")
