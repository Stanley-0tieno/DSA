num = [2, 7, 11, 15 ]
target = 9

def Solution(num, target):
    hashmap = {}

    for i, n in enumerate(num):
        compliment = target - n
        if compliment in hashmap:
            print(hashmap[compliment], i)
            break
        hashmap[n] = i


Solution(num, target)