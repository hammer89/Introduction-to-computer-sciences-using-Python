# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 00:14:16 2018

@author: MEKO
"""
        
broj = int(input('Insert an integer: '))
root = 0
i = 0
if broj == 0:
    print('power: any number')
    print('root: ', + root)
elif broj == 1:
    print('root: any number')
    print('power: 0')    
elif broj < 0:
    while root >= broj:
        root -= 1
        pwr = 5
        while pwr > 1:
            if root**pwr == broj:
                print('Root: ', root)
                print('Power: ', pwr)
                i += 1
                break
            pwr -= 1   
elif broj > 0:
  while root <= broj:
      root += 1
      pwr = 5
      while pwr > 1:
         if root**pwr == broj:
            print('Root: ', root)
            print('Power: ', pwr)
            i += 1
            break
         pwr -= 1  
if i == 0:
    print('Nema kombinacija takvih brojeva!')