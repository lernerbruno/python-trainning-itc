def build_matrix(rows, cols):
    matrix = []
    for i in range(1,rows+1):
        row = []
        for j in range(1,cols+1):
            row += [i*j]
        matrix += [row]
    return matrix

if __name__ == '__main__':
    print(build_matrix(3,3))