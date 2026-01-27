#Question-1 - completed
print("Question#1")
Numbers = [10,501,22,37,100,999,87,351]
Even_number = []
Odd_number = []
for i in Numbers:
    if i % 2 == 0:
        Even_number.append(i)
    else:
        Odd_number.append(i)
print("Even Numbers : ",Even_number)
print("Odd Numbers : ",Odd_number)

#Question- 2
print("\n")
print("Question#2")
Numbers = [10,501,22,37,100,999,87,351]
prime_numbers = []
for i in Numbers:
    a = 0
    for j in range(1,i):
        if i % j == 0:
            a+=1
    if a == 1:
        prime_numbers.append(i)
print("Count of Prime number:", len(prime_numbers))
print(prime_numbers)



#Question-3
print("\n")
print("Question#3")
Numb_List = [10,501,22,37,100,999,87,351]
happy_numbers = []

for i in Numb_List:
    seen = set()
    temp = i

    while temp != 1 and temp not in seen:
        seen.add(temp)
        temp = sum(int(i_digit) ** 2 for i_digit in str(temp))

    if temp == 1:
        happy_numbers.append(i)
print("Happy numbers in the list are: ", happy_numbers)
print("Count of the Happy Numbers: ",len(happy_numbers))

#Question-4
print("\n")
print("Question#4")
Integer_number = int(input('Enter an integer number more than 3 digit: '))
first_number = int(str(Integer_number)[0])
last_number = int(str(Integer_number)[-1])
print("Sum : " + str(first_number + last_number))

#Question-5
print("\n")
print("Question#5")
coins = [1,2,5,10]
exp_amount = 10
attempt = 0
for i in range(len(coins)):
    for j in range(len(coins)):
        for k in range(len(coins)):
            for l in range(len(coins)):
                sum_coins = coins[i]+coins[j]+coins[k]+coins[l]
                #print(sum_coins)
                if sum_coins == exp_amount:
                    print("Sum of : ",+coins[i],coins[j],coins[k],coins[l], "is equal to " ,+exp_amount)
                    attempt += 1
                    break

#Question-6
print("\n")
print("Question#6")
list_1 = ['Apple','Banana','Cherry','Coimbatore','Chennai']
list_2 = ['Chennai','Banana','dragon fruit','Salem','Coimbatore']
list_3 = ['Coimbatore','Movies','Banana','Family','Chennai']
# print(list_1)
# print(list_2)
# print(list_3)
attempt = 0
for i in range(0,len(list_1)):
    for j in range(0,len(list_2)):
        for k in range(0,len(list_3)):
            if list_1[i] == list_2[j] == list_3[k]:
                print(list_1[i])
                attempt += 1

#Question-7
print("\n")
print("Question#7")
numbers = [1,6,5,4,1,6,8]
def non_repeating(numbs):
    for i in numbs:
        if numbs.count(i) == 1:
            return i
    return None
result = non_repeating(numbers)

print("Non - repeating first number is :", result)



#Question-8
print("\n")
print("Question#8")
numb = [5,8,9,4,3,7]

numb.sort()
print(numb)
print("Minimum number in a list:",+int(numb[0]))

#Question-9
print("\n")
print("Question#9")
list_num = [10,20,30,9]
value_exp  = 59
attempt = 0
for i in range(len(list_num)):
    for j in range(i+1,len(list_num)):
        for k in range(j+1,len(list_num)):
            check_value = list_num[i] + list_num[j] + list_num[k]
            #print(check_value)
            if check_value == value_exp:
                print("Sum of ", +list_num[i], list_num[j], list_num[k] , "is equal to 59")
                attempt += 1
                break
if attempt == 0:
    print("No triplet found with sum")

#Question-10
print("\n")
print("Question#10")
numb_sum = [4,2,-3,1,6]
sum_list = []
attempt = 0

for i in range(len(numb_sum)):
    for j in range(i+1,len(numb_sum)):
        sum_value = numb_sum[i] + numb_sum[j]
        if sum_value == 0:
            sum_list.append((numb_sum[i],numb_sum[j]))
            attempt += 1

if attempt > 0:
    print("Sum to Zero list :", sum_list)
else:
    print("No zero sum value found")
