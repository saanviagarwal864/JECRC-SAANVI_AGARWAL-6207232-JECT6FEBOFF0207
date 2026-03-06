## functions on string


# s = 'Python'
# print(s.lower())

# result = s.upper()
# print(result)

# s = 'JECRC'
# print(s.strip('C'))

# print(' Python '.rstrip())
# print(' Python '.lstrip())

# print(s.index('t'))

# strs = 'I LOVE PYTHON'
# print(strs.split())


# str1 = 'I-LOVE-PYTHON'
# print(str1.split('-'))

# list_of_strs = strs.split()
# print(list_of_strs)

# ## join

# print(' '.join(list_of_strs))

# print('-'.join(list_of_strs))

s = 'Hello World'

# print(s.startswith('H', 2, 5))
# print(s.startswith('H'))
# print(s.endswith('l', 2, 5))
# print(s.endswith('l'))


# str1 = '123ab'
# print(str1.isdigit())

# str2 = 'abcAb'
# print(str2.islower())

# print(str2.isalpha())


# functions for list data type
'''
1.append
2.insert
3. extend
4.pop
5.remove
6.clear
7.sort
8.reverse
9.index
10.count
'''

# l = [1, 2, 3]
# l.append(4)
# print(l)

## insert function string.insert(indexx, value)

# l.insert(3, 5)
# print(l)

## extend

# l2 = [13, 24]


# l.extend(l2)
# print(l)

## pop()

# l.pop()
# print(l)

# l.pop(2)
# print(l)

# l.pop(10)
# print(l)


## remove()
# first occurence remove


# l.remove(24)
# print(l)

# l.remove()
# print(l)

# l.remove(12)
# print(l)


## sort() and reverse()

## sort() -- sort in ascending order and return none i.e no new collection will be returned


# l = [12, 1, 3 ,45, 6]
# # print(l.sort())
# print(l)

# l.sort(reverse = True)
# print(l)
## if reverse is true then descending order , if false then ascending


# l = [1, 3, 4 ,2, 5,4]
# l.reverse()   ## reverse will always reverse the list not sort it 
# print(l)

# print(l.index(2))# will give indexof value
# # print(l.index(10)) ## error

# print(l.count(4))
# print(l.count(12)) # will not return error  instead gave count = 0

# clear will remove all the items in the list 

# l.clear()
# print(l)



## functions for tuple data types
'''
1.index
2. count
'''
# tpl = (1,2, 2, 3, 5)
# print(tpl.count(2))
# print(tpl.index(3))

# same as index and count in list



## Functions for set data type
'''
add
remove
discard
pop : randomly 
clear
union
intersection
difference 


'''

# s= {1, 2, True, False, 0, 3+9j}
# print(s)

# ## add() add element in set randomly + no effect is element is already present
# s.add(100)
# print(s)

# value = 2
# s.add(value) ## it adds the value but set will remove it if it's already present so that's why it throws no error
# print(s)

# # s.add([12, 13]) ## throws error as mutable collection is getting added
# # print(s)

# s.add((12, 13))
# print(s)

#  remove() -- remove an element from set, it must be present. if not it throws an error 
# s.remove(3+9j)
# print(s)

# s.remove(True)
# print(s)

# s.remove(10)  //throws keyerror
# print(s)

# ## discard() -- similar to remove but it does not raise an exception when an element is missing from the set
# # s.discard(1)
# # print(s)

# # s.discard(10) ## no error 
# # print(s)


# ## pop() - randomly pop out values from set
# # print(s)
# # s.pop()
# # print(s)
# # s.pop()
# # print(s)


# ## clear() -- discard all the element and return an empty set


# ## union - concate the sets, return a new set
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# # s3 = s1.union(s2)
# # print(s3)

# # s = s1.union(s2, s3)
# # print(s)

# # s4 = {5, 6, 7}
# # s5 = s1.union(s2, s, s3, s4)
# # print(s5)


# # s1.union({1, 2, 3}, {5, 6, 7}, {7, 8, 9})
# # print(s1)

# ## intersection - wil return the common elements
# # print(s1.intersection(s2))  ## {2,3}

# ## difference -- all the uncommon elements in set 1

# # print(s1.difference(s2)) ## {1}

# ## symmetric_difference - return a set with elements in either the set or other but not both  (remove intersect elements)

# # print(s1.symmetric_difference(s2))  ## {1, 4}




# ## functions for dictionary 
# '''
# 1.get
# 2.pop
# 3.popitem
# 4.clear
# 5.update
# 6.keys
# 7.values

# '''

# ## get(key) -- return the value of key if key is in dict, else default

# # d = {1:11, 2:22, (1, 2, 3):(1, 2, 3)}
# # print(d)

# # print(d.get(1))

# # print(d.get('1')) ## will not throw error

# # print(d[1])  ## can have this method too 

# # print(d[(1, 2, 3)])


# ## var_name.pop(key_name) -- if key exist remove otherwise raises a keyerror

# user = {
#     'username' : 'user123',
#     'password' : '*****',
#     'location' : 'IN'
# }

# # print(user)

# # print(user.pop('location'))
# # print(user)

# # user.pop('location') ## again doing this will show error as location key does not exist
# # print(user)

# ## popitem() -- remove and return a (key, value) pair as a tuple, LIFO

# # print(user.popitem())
# # print(user)

# # print(user.popitem())
# # print(user)

# # print(user.popitem())
# # print(user)

# # print(user.popitem())  ## dictionary is empty so it will throw error


# ## clear -- will remove all the elements

# ## update() -- will update values, pass a dictionary inside of it 

# # user['password'] = '123' 
# # print(user)

# # user.update({'password' : '12345678'})
# # print(user)

# # user.update({'password' : '*****', 'is_logged_in' : True})
# # print(user)

# ## keys -- will return all the keys
# print(user.keys())

# ## values -- will return all values

# print(user.values())

# ## items -- will return a list of key value pairs

# print(user.items()) 

'''
output --

dict_keys(['username', 'password', 'location'])
dict_values(['user123', '*****', 'IN'])
dict_items([('username', 'user123'), ('password', '*****'), ('location', 'IN')])

'''
