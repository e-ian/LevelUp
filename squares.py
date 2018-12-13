"""question 5"""

def num_squares():
    squares = []
    for number in range(1, 21):
        squares.append(number**2)
    print(squares[0:5])

num_squares()