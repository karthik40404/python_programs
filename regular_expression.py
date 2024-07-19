import re
a='welcome'
print(re.sub('w','W',a))
print(re.sub('welcome','python',a))
b=re.split('l',a)
print(b)
c='hello world'
print(re.split('',c))
print(re.findall('e',a))
print(re.findall('e',c))
print(len(re.findall('e',a)))

d='thank0 you'
print(re.search('y',d))
if re.search('o',d):
    print('yes')
else:
    print('no')

print(re.search('[0-9]',d))




# e='abcd'
# print(re.search('a',e))
# print(re.search('d',e))
# print(re.search('c.',e))
# print(re.search('d.',e))
# print(re.search('a..',e))
# print(re.search('d.',e))
# print(re.search('b.*',e))
# print(re.search('d.*',e))
# print(re.search('b.+',e))
# print(re.search('d.+',e))
# print(re.search('d.?',e))
# print(re.search('b.?',e))

