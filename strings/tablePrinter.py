#TABLE PRINT


def printTable(table):
    for i in range(len(table)):
        for x in table:
            col_width = len(max(x, key=len))
            print(x[i].rjust(col_width + 2, ' '), end='')
        print()


tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


printTable(tableData)



# ! Make the zombie dice simulator
