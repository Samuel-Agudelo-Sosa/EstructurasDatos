def towers():
    l = [int(x) for x in input().split()]
    number_of_towers = 1
    max_height = 1
    acc = 1
    l.sort()
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            acc += 1
            if acc > max_height:
                max_height = acc
        else:
            number_of_towers += 1
    return (max_height, number_of_towers )

print(towers())

