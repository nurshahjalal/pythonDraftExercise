'''
problem :
Given a string of odd length greater 7, return a string made of the middle three chars of a given String
'''


def rtn_middle_char(random_string, len_of_string):
    string_len = len(random_string) - len_of_string
    half_string_len = int(string_len / 2)
    desire_string = random_string[half_string_len: half_string_len + len_of_string]
    print(desire_string)


r_string = "policeNurpolice"
rtn_middle_char(r_string, 3)


'''
 Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
'''


def add_in_middle(s1, s2):
    s1_len = int(len(s1)/2)
    new_string = s1[0:s1_len] + s2 + s1[s1_len:]
    print(new_string)

add_in_middle("policepolice", "Nur")
s1 = "Ault"
s2 = "Kelly"
add_in_middle(s1, s2)


'''
Arrange string characters such that lowercase letters should come first
Given an input string with the combination of the lower and upper case arrange characters in such a way that all 
lowercase letters should come first
'''

rand_string = "AdFBaTreMUngT"
new_lower_string = []
new_upper_string = []
for i in rand_string:
    if i.islower():
        new_lower_string.append(i)
    else:
        new_upper_string.append(i)
new_lower_string.extend(new_upper_string)
print("".join(new_lower_string))


'''
Count all lower case, upper case, digits, and special symbols from a given string

'''

str1 = "P@#yn26at^&i5ve"
def count_all_chars(str):
    count = {"lower": 0, "upper": 0, "digit": 0, "symbols": 0}
    for i in str:
        if i.islower():
            count["lower"] = count["lower"] + 1
        elif i.isupper() :
            count["upper"] =count["upper"] +1
        elif i.isdigit():
            count["digit"] = count["digit"] + 1
        else:
            count["symbols"] = count["symbols"] + 1
    count.update()
    print(f"Lower Letter: {count['lower']} \n Upper Letter: {count['upper']} \n "
          f"Digits: {count['digit']} \n special Symbols: {count['symbols']} \n ")

count_all_chars(str1)


'''
create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 and second 
last char of s2, and so on. Any leftover chars go at the end of the result.
'''

x1 = "ABC"
x2 = "XYZ"
outcome = "AZBYCX"

def mixed_string(x1, x2):
    new_string = ""
    i=1
    for x in x1:
        new_string = new_string+x + x2[-i]
        i+=1



mixed_string(x1, x2)


def mixString(s1, s2):
    s2 = s2[::-1]
    lengthS1 = len(s1)
    lengthS2 = len(s2)
    length = lengthS1 if lengthS1 > lengthS2 else lengthS2
    resultString = ""
    for i in range(length):
        if (i < lengthS1):
            resultString = resultString + s1[i]
        if (i < lengthS2):
            resultString = resultString + s2[i]

    print(resultString)

mixString(x1, x2)

'''
Find s1 character is present in s2
'''

s1 = "Sun"
s2 = "CumberSumnation"

def find_if(s1, s2):
    for i in s1:
        if i in s2:
            continue
        else:
            raise Exception(F"{i} Not found in {s2}")

find_if(s1, s2)
#find_if("Lamb", "LaLaLandBang")

def times_of_occurance(s1, s2):
    pass

s1= "USA"
s2 = "USA is awsome, I love USA, usa economy is best"
print(s2.count(s1))


'''
Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
Given:
'''

str1 = "English = 78 Science = 83 Math = 68 History = 65"
additon =0
for i in str1.split(" "):
    if i.isnumeric():
        additon =additon+int(i)
        continue

print(additon)


'''
Given an input string, count occurrences of all characters within a string
'''

str1 = "Apple"
count_dict = dict()

for char in str1:
    count_dict[char]=str1.count(char )
print(count_dict)

'''
reverse a string
'''
reg_string = "Lovely"
reversed_string = reg_string[::-1]
another_way_reverse = "".join(list(reversed(reg_string)))
print(reversed_string)






