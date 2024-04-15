#practice exam 2
#question 1
'''def num_in_sequence(sequences):
    list=[]
    count=1
    previousnum=sequences[0]
    for i in sequences[1:]:
        if i==previousnum:
            count+=1
        else:
            list.append(count)
            count=1
        previousnum=i
    list.append(count)
    return list

print(num_in_sequence([2,2,4,4,4,2,2,1,3,5,5]))'''

'''def encode(password):
    evenlist=[string for string in password[0::2]]
    oddlist=[string for string in password[1::2]]
    finallist=[evenlist,oddlist]
    return finallist

print(encode("16024583"))'''

'''class Calculator:
    def __init__(self):
        self.value=0.0

    def add(self,val):
        self.value+=val

    def subtract(self,val):
        self.value-=val

    def multiply(self,val):
        self.value*=val

    def divide(self,val):
        self.value/=val

    def clear(self):
        self.value=0.0

    def get_value(self):
        return self.value

listlist=[1,1,2,4,8,9,1]
listlist[1:]=[1,1,1,1,5,8,8,6,2]
print(listlist)'''

'''def factorial(number):
    if number==1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(5))'''

'''def fibonacci(number):
    if number==0:
        return 0
    if number==1:
        return 1
    else:
        return fibonacci(number-2)+fibonacci(number-1)

print(fibonacci(5))'''

def reverse_string(string):
    # base case
    if (len(string) == 1):
        return string
    # recursive call
    else:
        return reverse_string(string[1:]) + string[0]


print(reverse_string("bruh"))

def nested_sum(nest):
    sum=0
    for i in nest:
        if type(i)==int:
            sum+=i
        if type(i)==list:
            sum+=nested_sum(i)
    return sum

print(nested_sum([[1, 2], [3, [4, [5, 6]]], [7, [8, [9, [10]]]]]))
