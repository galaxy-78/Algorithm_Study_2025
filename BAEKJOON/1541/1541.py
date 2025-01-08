def minus_split_string(input_string):
    return input_string.split('-')

def plus_split_string(input_string):
    return input_string.split('+')

input_string = input()
result_1 = minus_split_string(input_string)
result_2 = []

sum_all = 0
cnt = 0
for i in result_1:
    result_2 = plus_split_string(i)
    sum_one = 0
    cnt += 1
    for j in result_2:
        sum_one += int(j)
        if cnt == 1:
            sum_all = sum_one
    if cnt != 1:
        sum_all -= sum_one

print(sum_all)
