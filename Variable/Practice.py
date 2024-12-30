a = [10, 20, 30]
b = a
b = 100

print(b)
print(a)
print(type(b))
print(type(a))

a = [10, 20, 30]
b = a
b[1] = [100]
print(b)

lst = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for i in lst:
    lst.remove(i)
print(lst)

a = [1, 2, 3, 4]
print(a[1])
print(len(a))
print(a[-1])
print()

lst = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for i in lst:
    lst.pop(len(lst)-1)
print(lst)

lst = [2, 1, 3, 2, 3, 1]
for i in lst:
    lst.pop(i)
print(lst)

nums = {1:10, 2:20, 3:30}
for i in nums:
    nums[i] = nums[i]+2
print(nums)
print(nums.values())
print(nums.keys())
print(nums.items())
print(nums.pop(i))
print(nums)

a = 5
b = 3
c = 4
d = 2
print(a*b+c/d)

nums1 = {1:10, 2:20, 3:30}
nums2 = {}
for i in nums1:
    nums2[nums1[i]] = i
print(nums2)

nums1 = {1:10, 2:20, 3:30}
nums2 = {}
for i in nums1:
    nums2[nums1[i]] = nums1[i]+2
print(nums2)

a = "1010"
b = a[-1::-1]
print(b[1])

a = [10, 20, 30]
b = a
b.append(40)
print(b)
b.pop(1)
print(b)

st = 'aaabbbbccccc'
d = {}. fromkeys(st,0)
for i in st:
    d[i] = d[i] + 1
print(d)

st = '12233344444'
d = {}. fromkeys(st, 0)
for i in st:
    d[i] = d[i]+1
print(d[i])

n1 = ['a', 'b','c','d']
n2 = [1,2,3,4]
d = {}
for x,y in zip(n1, n2):
    d[x] = y
print(d)

a = ["1,2,3,4"]
for i in a:
    print(a)
    print(i)
a = [1, 2, 3,4]
while i in a:
    print(a)

nums1 = {1:10, 2:20, 3:30}
nums2 = {}
for i in nums1:
    if i%2 == 1:
        nums2[nums1[i]] = i
    else:
        nums2[i] = nums1[i]
print(nums2)

nums1 = {10:1, 20:2, 30:3}
nums2 = {}
for i in nums1:
    if i%2 == 1:
        nums2[nums1[i]] = i
    else:
        nums2[i] = nums1[i]
print(nums2)

str = 'ABcd'
for i in str:
    print(i.swapcase(), end='')


s = {5,4, 5, 6, 3, 6, 2}
for i in list(s):
    s.discard(i)
print(s)

for i in range(6):
    if i == 4:
        break
    print(i)

list_1 = ["2", 2, 3, "ab",5]
del list_1[2]
print(list_1)

nums = [2, 4, 'a', 'b', True, 10]
for i in nums:
    nums.pop()
print(nums)

a = [0,1,2,3,5]
a.append(4)
print(a)

x = [0,1,2,3,4,5]
print(x[::-1])

import calendar
year = 2024
month = 2
print(calendar.month(year,month))

import calendar
year = 2024
month = 12
print(calendar.month(year,month))

import calendar
year = 2025
month = 2
print(calendar.month(year,month))






