from  collections import Counter

randomWord = "Aabcsdddeerrtttdaaa"
frequent = Counter(randomWord)
print(frequent)

for k in frequent:
    print(frequent[k], k)

names = ['abul', 'babul', 'kabul', 'chulbul', 'abul', 'Babul', 'Nupur', 'nupur', 'kabul', 'abul', 'babul', 'kabul', \
        'chulbul', 'abul', 'Babul', 'Nupur', 'nupur', 'kabul', 'Kabita']


print(Counter(names).most_common(1))
# most_common_words= [word for word, word_count in Counter(names).most_common(1)]
# print(most_common_words)


for name in Counter(names).most_common(1):
    print(name[0])


# find fist duplicate in a list

dup_names = ['abul', 'babul', 'kabul', 'chulbul', 'abul', 'Babul', 'Nupur', 'nupur', 'kabul', 'abul', 'babul', 'kabul', \
        'chulbul', 'abul', 'Babul', 'Nupur', 'nupur', 'kabul', 'Kabita']

'''
abul = 4
babul = 2
kabul = 4
Babul = 2
chulbul = 2
nupur = 2
Nupur = 2
Kabita = 1
'''

# set_ = set()
#
# for item in dup_names:
#     if item in set_:
#         return item
#     set_.add(item)
# return None

dup_word = set()

for item in dup_names:
    if item in dup_word:
        print(f'First Duplicate word is { item}')
        break
    dup_word.add(item)


#
# def firstDuplicate(a):
#     set_ = {}
#     for item in a:
#         if item in set_:
#             return item
#         set_.add(item)
#     return None
#
# print(firstDuplicate(dup_names))

# find all duplicate in a list

dup_word = set()
dup_list = []
for item in dup_names:
    if item in dup_word:
        dup_list.append(item)
    dup_word.add(item)
print(Counter(dup_list))
print(set(dup_list))

unique_list = []
for x in dup_names:
    if dup_names.count(x) > 1:
        unique_list.append(x)

print(list(enumerate(set(unique_list))))


