"""question 0"""
def grading_system():
    """function that handles the grading of student's marks"""
    
    marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]
    list1=[]
    list2=[]

    for value in marks:
        if value > 50:
            list1.append(value)
        elif value < 50:
            list2.append(value)
    for value in list1:
        if value >= 90 and value <= 100:
            print (str(value)+' '+'Excellent')   
        elif value >= 70 and value <= 89:
            print (str(value)+' '+'very good') 
        elif value >= 60 and value <= 69:
            print (str(value)+' '+'good')     
        else:
            print (str(value)+' '+'poor')          

    for value in list2:
        if value >= 40 and value <= 50:
            print (str(value)+' '+'poor')  
        elif value >= 20 and value <= 39:
            print (str(value)+' '+'very poor') 
        else:
            print (str(value)+' '+'repeat')

grading_system()