#!/usr/bin/python
#coding:utf-8
d1 = {'a1': 1, 'a2': 2, 'a3': 3}
d2 = {'a1': 10, 'a4':40, 'a5': 3}

s1 = set(d1.keys())
s2 = set(d2.keys())
#print s1 & s2

result = {}
for s in s1 & s2:
    result[s] = d2[s]

print result


common_keys = set(d1.keys()) & set(d2.keys())
common_values = set(d1.values()) & set(d2.values())

new_d1 = d1.copy()
new_d1.update(d2)

result = {}
for k, v in new_d1.items():
    if k not in common_keys and v not in common_values:
        result[k] = v
print result
