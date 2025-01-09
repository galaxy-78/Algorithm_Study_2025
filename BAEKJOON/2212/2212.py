# N=10
# K=5
# spot=[20, 3, 14, 6, 7, 8, 18, 10, 12, 15]

N = int(input()); K = int(input()); spot = list(map(int, input().split()))
spot.sort()

result = []
for i in range(N-1):
    result.append(spot[i+1]-spot[i])
result.sort()

sum = 0
for i in range(0, len(result)-K+1):
    sum += result[i]

print(sum)
