# Task Illidan
data = [int(i) for i in input().split()]
values = [int(j) for j in input().split()]


def illidan(data, values):
    min_dif = abs(data[1] - (values[0]+values[1]+values[2]))
    min_list = values[:3]
    for i in range(len(values)):
        for j in range((len(values))):
            for l in range((len(values))):
                if i != j and i != l and j != l:

                    sort = [values[i], values[j], values[l]]
                    sort.sort()
                    if abs(data[1] - (sort[0]+sort[1]+sort[2])) < min_dif:
                        min_dif = abs(data[1] - (sort[0]+sort[1]+sort[2]))
                        min_list = []
                        for value in sort:
                            min_list.append(value)
    return min_list


min_list = illidan(data, values)

print(' '.join([str(x) for x in min_list]))


