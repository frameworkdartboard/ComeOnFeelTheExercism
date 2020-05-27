class Matrix:

    
    def __init__(self, matrix_string):
        self.thematrix=[]
        matrix_lines = matrix_string.splitlines()
        for line in matrix_lines:
            row=map(int,line.split(' '))
            self.thematrix.append(list(row))

    def row(self, index):
        return(self.thematrix[index-1])

    def column(self, index):
        thecolumn=[]
        for row in self.thematrix:
            thecolumn.append(int(row[index-1]))
        return(thecolumn)

ddeebbugg=False

if ddeebbugg:
    foomat=Matrix("1 2 4\n3 0 3\n4 49 56")
    print("Matrix = 1 2 4 \\n3 0 3\\n4 49 56\n")
    print("foomat.row(1) = '%r' " % foomat.row(1))
    print("foomat.row(2) = '%r' " % foomat.row(2))
    print("foomat.row(3) = '%r' " % foomat.row(3))
    print("foomat.column(1) = '%r' " % foomat.column(1))
    print("foomat.column(2) = '%r' " % foomat.column(2))
    print("foomat.column(3) = '%r' " % foomat.column(3))