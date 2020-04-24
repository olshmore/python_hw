class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        return str('\n'.join([' '.join([str(el) for el in row]) for row in self.rows]))

    def __add__(self, other):
        other = Matrix(other)
        # return str('\n'.join([' '.join([str(el) for el in row])for row in other.rows]))
        s1, s2, s3 = [], [], []
        for row in self.rows:
            for el in row:
                s1.append(el)
        for row in other.rows:
            for el in row:
                s2.append(el)
        if len(s1) == len(s2):
            for i in range(len(s1)):
                s3.append(s1[i] + s2[i])
            return s3
        else:
            return 'Матрицы не одинакового размера'


new_matrix = Matrix(([1, 1, 1], [1, 1, 1], [1, 1, 1]))

print(new_matrix)

print(new_matrix + ([1, 1, 1], [2, 2, 2], [2, 2, 2]))
