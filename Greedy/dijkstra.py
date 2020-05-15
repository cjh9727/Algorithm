file = input()
with open(file, "r") as f:
    data = [[int(i) for i in line.split()] for line in f.readlines()]

n = data[0][0]
matrix = [[9999 for col in range(n)] for row in range(n)]
for i in range(n):
    matrix[i][i] = 0
for i in range(1, len(data)) :
    first_num = data[i][0]
    second_num = data[i][1]
    weight = data[i][2]
    matrix[first_num-1][second_num-1] = weight


def solve(source):
    F = []
    for i in range(n):
        F.append(0)
    touch = []
    for i in range (n):
        touch.append(source)
    touch[source] = 0
    length = []
    for i in range(n) :
        length.append(matrix[source][i])
    length[source] = -1

    for i in range(n-1) :
        min = 9999
        for i in range(n) :
            if 0 <= length[i] < min :
                min = length[i]
                vnear = i
        t = touch[vnear]
        edge = matrix[t][vnear]
        F[vnear] = F[t] + edge

        for i in range(n) :
            if (length[vnear] + matrix[vnear][i]) < length[i] :
                length[i] = length[vnear] + matrix[vnear][i]
                touch[i] = vnear;

        length[vnear] = -1
    return F

    


