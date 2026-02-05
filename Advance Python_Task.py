#Question:1
print('Question:1')
People_list = [{'name': 'Gokila','age':25},
               {'name':'Nandhini','age': 18},
               {'name':'Rishani','age': 15},
               {'name':'Prakash','age': 50},
               {'name':'Vellai','age': 35},
               {'name':'Viyan','age': 10},
               {'name':'Mohana','age': 40},
               ]

adults = filter(lambda a: a['age'] >= 18, People_list)
adult_name = list(map(lambda p:p['name'], adults))
print(adult_name)

#Question:2
print('\nQuestion:2')
from functools import reduce

numb = list(map(int,input("Enter any 3 to 7 numbers in a list with comma separator to check product value:"). split(',')))

product_value = reduce(lambda a,b : a*b, numb)
print(product_value)

#Question:3
print('\nQuestion:3')
number_list = list(map(int,input("Enter any 5 to 10 numbers in a list with comma separator to check even number and square of even numbers: "). split(',')))

even_numb = lambda x: x % 2 == 0
even_numbers = [x for x in number_list if even_numb(x)]
square_even_numb = [x*2 for x in number_list if even_numb(x)]
print("Even numbers in the list:",even_numbers)
print("Square of the even numbers: ",square_even_numb)

#Question:4
print('\nQuestion:4')
data = 'Check data variable value is integer'

check_value = lambda x: x.isdigit()
print(check_value(data))

#Question:5
print('\nQuestion:5')
import datetime

date_value = datetime.datetime.now()
print(date_value)

year_month_day = lambda a:(a.year,a.month,a.day)
print('Year : ',year_month_day(date_value)[0])
print('Month : ',year_month_day(date_value)[1])
print('Day : ',year_month_day(date_value)[2])

#Question:6
print('\nQuestion:6')
fibonacci_number = (int(input('Enter any integer value for fibonacci series: ')))
fib_series = lambda n :[0,1] + [0 for _ in range(n-2)] if n > 1 else[0] if n ==1 else[]

def generate_fib(n):
    seq = fib_series(n)
    for i in range(2,n):
        seq[i] = seq[i-1] + seq[i-2]
    return seq

print(generate_fib(fibonacci_number))