"""question 3"""
def binary_num():
    x = input().split(",")
    binary_inputs = []
    for number in x:
        try:
            x = int(number, 2)
        except ValueError:
            print(" Input binary numbers only!!!")
        else: 
            if x%5 == 0:
                binary_inputs.append(number)
    print(','.join(binary_inputs))
binary_num()