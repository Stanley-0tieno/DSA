num = [4, 5, 0, 4, 6]
target = 8

def Solution(num, target):
    hashmap = {}

    for i, n in enumerate(num):
        compliment = target - n
        if compliment in hashmap:
            print(hashmap[compliment], i)
            break
        hashmap[n] = i

Solution(num, target)


