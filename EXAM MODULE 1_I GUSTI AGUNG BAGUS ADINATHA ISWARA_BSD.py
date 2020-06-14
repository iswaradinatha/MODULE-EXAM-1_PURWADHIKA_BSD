# 1. Create a function called Hashtag that generate hashtag which accepting string separated by space as presented in the below with following rules (15 Points):
def Hashtag(string):
    list_string = string.split()
    new_string = []
    for i in list_string:
        new_string.append(i.capitalize())
    
    str_new_string = ''.join(new_string)
    if len(str_new_string) >= 140 or len(str_new_string) == 0:
        print(False)
    else:
        print('#{}'.format(str_new_string))


Hashtag('dont worry be happy')

# 2. Write a function that accepts a list of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number (10 points).
def create_phone_number(number):
    first_format = f'{number[0]}{number[1]}{number[2]}'
    second_format = f'{number[3]}{number[4]}{number[5]}'
    third_format = f'{number[6]}{number[7]}{number[8]}{number[9]}'
    int_check = []
    for i in number:
        if type(i) == int:
            int_check.append(True)
        else:
            int_check.append(False)
    if False in int_check or len(number) != 10:
        print ('Invalid input')
    else:
        print (f'({first_format}) {second_format}-{third_format}')

number = [0,2,1,7,4,1,6,5,2,8]
create_phone_number(number)

# 3. You are given a list of integers. Your task is to sort odd numbers within the list in ascending order, and even numbers in descending order but keep all the odds or the evens number in the same index group (35 Points).
# Note that zero is an even number. If you have an empty list, you need to return it.
def sort_odd_even(num):
    for i in range (len(num)):
        for j in range(i+1,len(num)):
            if num[i] % 2 == 0 and num[j] % 2 == 0:
                if num[i] < num[j]:
                    temp = num[i]
                    num[i] = num[j]
                    num[j] = temp
            elif num[i] % 2 !=0 and num[j] %2 !=0:
                if num [i] > num[j]:
                    temp = num[i]
                    num[i] = num[j]
                    num[j] = temp
            elif num[i] == '':
                return num
    print(num)

num = [5,3,2,8,1,4]
sort_odd_even(num)
