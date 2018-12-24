# -*- coding:utf-8 -*-
import numpy as np


studenttype = np.dtype({
    'names':['name', 'chinese', 'english', 'math', 'total'],
    'formats':['S32', 'i', 'i', 'i', 'i']})

scores = np.array([("Zhang Fei", 66, 65, 30, 0), ("Guan Yu", 95, 85, 98, 0),
("Zhang Yu", 93, 92, 96, 0), ("Huang Zhong", 90, 88, 77, 0),
("Dian Wei", 80, 90, 90, 0)],dtype=studenttype)

print('{:10s}'.format(''),end='')
print('{:8s}'.format('Max'),end='')
print('{:8s}'.format('Min'),end='')
print('{:8s}'.format('Mean'),end='')
print('{:8s}'.format('Std'),end='')
print('{:8s}'.format('var'))
for name in studenttype.names:
    if name not in ['name', 'total']:
        print('{:8s}'.format(name),end='')
        print('{:8.2f}'.format(np.amax(scores[:][name])),end='')
        print('{:8.2f}'.format(np.amin(scores[:][name])),end='')
        print('{:8.2f}'.format(np.mean(scores[:][name])),end='')
        print('{:8.2f}'.format(np.std(scores[:][name])),end='')
        print('{:8.2f}'.format(np.var(scores[:][name])))

scores[:]['total'] = scores[:]['chinese'] + scores[:]['english'] + scores[:]['math'] 
ranks = np.sort(scores, order='total')
print('The rank of those five students is:')
for rank in ranks:
    for col in rank:
        print(col,end='\t')
    print('')