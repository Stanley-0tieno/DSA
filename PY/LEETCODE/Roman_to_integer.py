def Solution(x):
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    # prev_value = 0
    
    # for char in reversed(x):
    #     value = roman_map[char]
    #     if value < prev_value:
    #         total -= value

    #     else :
    #         total += value

    # print(total)

    for i in range(len(x)):
        value = roman_map[x[i]]

        if i + 1 < len(x):
            next_value = roman_map[x[i+1]]

            if value < next_value:
                total -= value

            else:
                total += value
        else:
            total += value

        print(total)


Solution("X")