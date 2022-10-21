#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Description: Code to compute the scoring of the Green Index 3.0 (utilities)


Author: Alfonso Caiazzo (HEDERA Sustainable Solutions)
Copyright: e-MFP Green Inclusive and Climate-Smart Finance AG
License: CC-BY-4.0
Terms of use: reproduction possible, use the following sentence to acknowledge the original sources:
    "This code is part of thee digital solutions for the Green Index 3.0. It has been developed by Alfonso Caiazzo (HEDERA)"
Version: 2022.09-1.0
Released: September 1st, 2022

"""

###############################################################################
# Return a dictionary with all indicators organized per standard and practice
###############################################################################
def full_GI():
    all_indicators = indicator_to_score()
    GI= dict()
    GI = {
          0: {
              1: [a for a in all_indicators if a.find('GI_0_1')>=0],
              2:[a for a in all_indicators if a.find('GI_0_2')>=0],
              },
          1: {
              1: [a for a in all_indicators if a.find('GI_1_1')>=0],
              2:[a for a in all_indicators if a.find('GI_1_2')>=0],
              },
          2: {
              1: [a for a in all_indicators if a.find('GI_2_1')>=0],
              2:[a for a in all_indicators if a.find('GI_2_2')>=0],
              },
          3: {
              1: [a for a in all_indicators if a.find('GI_3_1')>=0],
              2:[a for a in all_indicators if a.find('GI_3_2')>=0],
              }
          }
    return GI

###############################################################################
# Evaluate selected indicator
###############################################################################
def evaluate_indicators(df):
    
    indicators = []
    for s in full_GI().keys(): # standards
        for p in full_GI()[s].keys(): # practices
            for i in full_GI()[s][p]: # indicators
                indicators.append(i[10:])
                
                
    indicators_score = dict()
    for i in indicators:
        indicators_score[i] = 0
    for index,row in df.iterrows():  
        for i in indicators:
            indicators_score[i] += indicator_to_score('indicator_'+i,row)/len(df)
    
    return indicators_score


###############################################################################
# Associate a score to each available indicator
###############################################################################
def indicator_to_score(argument=None,r=None):
    
    switcher = {
        # ----------------------------
        # Section 0.1
        'indicator_GI_0_1_1': GI_0_1_1,
        'indicator_GI_0_1_2': GI_0_1_2,
        'indicator_GI_0_1_3': GI_0_1_3,
        'indicator_GI_0_1_4': GI_0_1_4,
        'indicator_GI_0_1_5': GI_0_1_5,
        'indicator_GI_0_1_6': GI_0_1_6,
        
        # ----------------------------
        # Section 0.2
        'indicator_GI_0_2_1': GI_0_2_1,
        'indicator_GI_0_2_2': GI_0_2_2,
        'indicator_GI_0_2_3': GI_0_2_3,
        'indicator_GI_0_2_4': GI_0_2_4,
        'indicator_GI_0_2_5': GI_0_2_5,
        'indicator_GI_0_2_6': GI_0_2_6,
        'indicator_GI_0_2_7': GI_0_2_7,
        'indicator_GI_0_2_8': GI_0_2_8,
        'indicator_GI_0_2_9': GI_0_2_9,
        'indicator_GI_0_2_10': GI_0_2_10,
        'indicator_GI_0_2_11': GI_0_2_11,
        'indicator_GI_0_2_12': GI_0_2_12,
        'indicator_GI_0_2_13': GI_0_2_13,
        
        # ----------------------------
        # Section 1.1
        'indicator_GI_1_1_1': GI_1_1_1,
        'indicator_GI_1_1_2': GI_1_1_2,
        'indicator_GI_1_1_3': GI_1_1_3,
        'indicator_GI_1_1_4': GI_1_1_4,
        'indicator_GI_1_1_5': GI_1_1_5,
        'indicator_GI_1_1_6': GI_1_1_6,
        'indicator_GI_1_1_7': GI_1_1_7,
        'indicator_GI_1_1_8': GI_1_1_8,
        'indicator_GI_1_1_9': GI_1_1_9,
        'indicator_GI_1_1_10': GI_1_1_10,
        
        # ----------------------------
        # Section  1.2
        'indicator_GI_1_2_1': GI_1_2_1,
        'indicator_GI_1_2_2': GI_1_2_2,
        'indicator_GI_1_2_3': GI_1_2_3,
        'indicator_GI_1_2_4': GI_1_2_4, 
        
        # ----------------------------
        # Section 2.1
        'indicator_GI_2_1_1': GI_2_1_1,
        'indicator_GI_2_1_2': GI_2_1_2,
        'indicator_GI_2_1_3': GI_2_1_3,
        'indicator_GI_2_1_4': GI_2_1_4,
        'indicator_GI_2_1_5': GI_2_1_5,
        'indicator_GI_2_1_6': GI_2_1_6,
        'indicator_GI_2_1_7': GI_2_1_7,
        'indicator_GI_2_1_8': GI_2_1_8,
        'indicator_GI_2_1_9': GI_2_1_9,
        'indicator_GI_2_1_10': GI_2_1_10,
        
        # ----------------------------
        # Section  2.2
        'indicator_GI_2_2_1': GI_2_2_1,
        'indicator_GI_2_2_2': GI_2_2_2,
        'indicator_GI_2_2_3': GI_2_2_3,
        'indicator_GI_2_2_4': GI_2_2_4,
        'indicator_GI_2_2_5': GI_2_2_5,
        'indicator_GI_2_2_6': GI_2_2_6,
        
        
        # ----------------------------
        # Section  3.1
        'indicator_GI_3_1_1': GI_3_1_1,
        'indicator_GI_3_1_2': GI_3_1_2,
        'indicator_GI_3_1_3': GI_3_1_3,
        'indicator_GI_3_1_4': GI_3_1_4,
        'indicator_GI_3_1_5': GI_3_1_5,
        'indicator_GI_3_1_6': GI_3_1_6,
        'indicator_GI_3_1_7': GI_3_1_7,
        'indicator_GI_3_1_8': GI_3_1_8,
        'indicator_GI_3_1_9': GI_3_1_9,
        'indicator_GI_3_1_10': GI_3_1_10,
        'indicator_GI_3_1_11': GI_3_1_11,
        'indicator_GI_3_1_12': GI_3_1_12,
        'indicator_GI_3_1_13': GI_3_1_13,
        'indicator_GI_3_1_14': GI_3_1_14,
        'indicator_GI_3_1_15': GI_3_1_15,
        'indicator_GI_3_1_16': GI_3_1_16,
        'indicator_GI_3_1_17': GI_3_1_17,
        'indicator_GI_3_1_18': GI_3_1_18,
        'indicator_GI_3_1_19': GI_3_1_19,
        'indicator_GI_3_1_20': GI_3_1_20,
        'indicator_GI_3_1_21': GI_3_1_21,
        'indicator_GI_3_1_22': GI_3_1_22,
        'indicator_GI_3_1_23': GI_3_1_23,
        'indicator_GI_3_1_24': GI_3_1_24,
        'indicator_GI_3_1_25': GI_3_1_25,
        
        # ----------------------------
        # Section  3.2
        'indicator_GI_3_2_1': GI_3_2_1,
        'indicator_GI_3_2_2': GI_3_2_2,
        'indicator_GI_3_2_3': GI_3_2_3,
        'indicator_GI_3_2_4': GI_3_2_4,
        
        
    }
    
    if argument==None:
        return switcher.keys()
    else:
        # Get the function from switcher dictionary
        indicator_score = switcher.get(argument, lambda: "Invalid indicator " + argument)
        # Execute the function
        return indicator_score(r)
    





              

###########################################################################
# SINGLE INDICATORS - GI 0.1
###########################################################################
def GI_0_1_1(r):
    x = r['indicator_GI_0_1_1']
    if type(x)==str:
        if x=='none':
            return 0
        else:
            if len(x.split(" "))>1:
                return 100
            else:
                return 50
    else:
        return 0 
    
    
# 100% if at least 2 multiple choice answers are ticked, 
# or if at least 2 details are answered" partially", 
# or if 1 multiple choices is ticked and one detail is answered "partially
def GI_0_1_2(r):
    count = 0
    for j in ['a','b','c','d']:
        x = r['indicator_GI_0_1_2_' + j]
        if type(x)==str and x=='yes':
            count += 1
            
    for j in ['e','f','g']:
        x = r['indicator_GI_0_1_2_' + j]
        if type(x)==str and x!='no':
            count += 1
        
    
    if count>1:
        return 100
    elif count==1:
        return 50
    else:
        return 0

def GI_0_1_3(r):
    return indicator_with_details(r,name='indicator_GI_0_1_3')


def GI_0_1_4(r):
    count = 0
    for j in ['a','b','c','d','e']:
        x = r['indicator_GI_0_1_4_' + j]
        if type(x)==str and x=='yes':
            count += 1
    if count > 1:
        return 100
    elif count == 1:
        return 50
    else:
        return 0 

def GI_0_1_5(r):
    return indicator_with_details(r,name='indicator_GI_0_1_5')

def GI_0_1_6(r):
    x = r['indicator_GI_0_1_6']
    if type(x)==str:
        return yes_no_partially(x)
    else:
        return 0
    

###############################################################################
# SINGLE INDICATORS - GI 0.2
###############################################################################
def GI_0_2_1(r):
    return indicator_with_details(r,name='indicator_GI_0_2_1')

def GI_0_2_2(r):
    return indicator_with_details(r,name='indicator_GI_0_2_2')

# CHECK THE NEW IMPLEMENTATION
def GI_0_2_3(r):
    x = r['indicator_GI_0_2_3']
    if type(x)==str:
        if x=='none':
            return 0
        elif len(x.split(' '))==1:
            return 50
        elif len(x.split(' '))>1:
            return 100
    else:
        return 0

def GI_0_2_4(r):
    return indicator_with_details(r,name='indicator_GI_0_2_4')

def GI_0_2_5(r):
    x = r['indicator_GI_0_2_5']
    if type(x)==str:
        return yes_no_partially(x)
    else:
        return 0

def GI_0_2_6(r):
    return indicator_with_details(r,name='indicator_GI_0_2_6')

def GI_0_2_7(r):
    x = r['indicator_GI_0_2_7']
    if type(x)==str:
        return yes_no_partially(x)
    else:
        return 0

def GI_0_2_8(r):
    return indicator_with_details(r,name='indicator_GI_0_2_8')

def GI_0_2_9(r):
    return indicator_with_details(r,name='indicator_GI_0_2_9')

def GI_0_2_10(r):
    return indicator_with_details(r,name='indicator_GI_0_2_10')

def GI_0_2_11(r):
    return indicator_with_details(r,name='indicator_GI_0_2_11')


# 100% if at least 1 multiple choice answers is ticked in "adverse environmental impact (Minimum frequency: annually): " 
# and 
# at least 1 multiple choice answers is ticked in "Vulnerability (Minimum frequency: annually)." 
# 50% if one or more multiple choices answers are ticked in "adverse environmental impact (Minimum frequency: annually): " 
# but no multilple choices answers is ticked in "Vulnerability (Minimum frequency: annually)."

# or if one or more multiple choices answers are ticked in "Vulnerability (Minimum frequency: annually) "
#  but no multilple choices answers is ticked in "adverse environmental impact (Minimum frequency: annually)."
def GI_0_2_12(r):
    a = 0
    b = 0
    x = r['indicator_GI_0_2_12_details']
    if type(x)==str:
        a = 1
    y = r['indicator_GI_0_2_12_b_details']
    if type(y)==str:
        b = 1
    return a*50 + b*50 
    

def GI_0_2_13(r):
    return indicator_with_details(r,name='indicator_GI_0_2_13')

###############################################################################
# SINGLE INDICATORS - GI 1.1
###############################################################################
def GI_1_1_1(r):
    return simple_details(r['indicator_GI_1_1_1'])

def GI_1_1_2(r):
    return simple_details(r['indicator_GI_1_1_2'])

def GI_1_1_3(r):
    return simple_details(r['indicator_GI_1_1_3'])

def GI_1_1_4(r):
    return simple_details(r['indicator_GI_1_1_4'])

def GI_1_1_5(r):
    return simple_details(r['indicator_GI_1_1_5'])

def GI_1_1_6(r):
    return simple_details(r['indicator_GI_1_1_6'])

def GI_1_1_7(r):
    return indicator_with_details(r,name='indicator_GI_1_1_7')

def GI_1_1_8(r):
    return simple_details(r['indicator_GI_1_1_8'])

def GI_1_1_9(r):
    return simple_details(r['indicator_GI_1_1_9'])

def GI_1_1_10(r):
    return simple_details(r['indicator_GI_1_1_10'])
#indicator_with_details(r,name='indicator_GI_1_1_10')

    

###############################################################################
# SINGLE INDICATORS - GI 1.2
###############################################################################
def GI_1_2_1(r):
    return indicator_with_details(r,name='indicator_GI_1_2_1')

def GI_1_2_2(r):
    return indicator_with_details(r,name='indicator_GI_1_2_2')

def GI_1_2_3(r):
    return indicator_with_details(r,name='indicator_GI_1_2_3')



# row['indicator_GI_1_2_4'] == 'none -> 0
# row['indicator_GI_1_2_4'] != 'none' & len['indicator_GI_1_2_4_details'] <=1 -> 50
# row['indicator_GI_1_2_4'] != 'none' 0 & len['indicator_GI_1_2_4_details'] >1 -> 10
def GI_1_2_4(r):
    partially = 1
    x = r['indicator_GI_1_2_4']
    if type(x)==str:
        if x=='none':
            return 0
        else:
            y = r['indicator_GI_1_2_4_details']
            if type(y)==str:
                if len(y.split(" "))>partially:
                    return 100
                else:
                    return 50
            else:
                return 0
    else:
        return 0


###############################################################################
# SINGLE INDICATORS - GI 2.1
###############################################################################
def GI_2_1_1(r):
    return indicator_with_details(r,name='indicator_GI_2_1_1')

def GI_2_1_2(r):
    return indicator_with_details(r,name='indicator_GI_2_1_2')

def GI_2_1_3(r):
    return indicator_with_details(r,name='indicator_GI_2_1_3')

def GI_2_1_4(r):
    return indicator_with_details(r,name='indicator_GI_2_1_4')

def GI_2_1_5(r):
    return indicator_with_details(r,name='indicator_GI_2_1_5')

def GI_2_1_6(r):
    return indicator_with_details(r,name='indicator_GI_2_1_6')

def GI_2_1_7(r):
    return simple_details(r['indicator_GI_2_1_7'])

def GI_2_1_8(r):
    x = r['indicator_GI_2_1_8']
    if type(x)==str:
        return yes_no_partially(x)
    else:
        return 0

def GI_2_1_9(r):
    x = r['indicator_GI_2_1_9']
    if type(x)==str:
        return yes_no_partially(x)
    else:
        return 0
    

def GI_2_1_10(r):
    x = r['indicator_GI_2_1_10']
    if type(x)==str:
        return yes_no_partially(x)
    else:
        return 0
    
    
###############################################################################
# SINGLE INDICATORS - GI 2.2
###############################################################################
def GI_2_2_1(r):
    return indicator_with_details(r,name='indicator_GI_2_2_1')

def GI_2_2_2(r):
    return indicator_with_details(r,name='indicator_GI_2_2_2')

def GI_2_2_3(r):
    a = r['indicator_GI_2_2_3_a']
    n_a = len(a.split(" ")) if type(a)==str else 0
    if a == 'none':
        n_a = 0
    b = r['indicator_GI_2_2_3_b']
    n_b = len(b.split(" ")) if type(b)==str else 0
    if b == 'none':
        n_b = 0
    if n_a + n_b >1 :
        return 100
    elif n_a + n_b == 1:
        return 50
    else:
        return 0
    

def GI_2_2_4(r):
    x = r['indicator_GI_2_2_4']
    if type(x)==str:
        return yes_no_partially(x)
    else:
        return 0

def GI_2_2_5(r):
    x = r['indicator_GI_2_2_5']
    if type(x)==str:
        if x=='no':
            return 0
        
        else:
            y = r['indicator_GI_2_2_5_details']
            if type(y)==str:
                y = y.split(" ")
                if 'inside' in y:
                    return 100
                else:
                    return 50
            else:
                return 0
            
    else:
        return 0

def GI_2_2_6(r):
    partially = 1
    x = r['indicator_GI_2_2_6']
    if type(x)==str:
        
        if x=='none':
            return 0
        
        else:
        
            a = r['indicator_GI_2_2_6_details_a']
            b = r['indicator_GI_2_2_6_details_b']
            
            if type(a)==str and type(b)==str:
                if len(b.split(" "))==partially:
                    return 50
                elif len(b.split(" "))>partially:
                        return 100
                
            else:
                return 0
    
    # -- type(x) != str      
    else:
        return 0

    
###############################################################################
# SINGLE INDICATORS - GI 3.1
###############################################################################
def GI_3_1_1(r):
    x = r['indicator_GI_3_1_1_a_details']
    y = r['indicator_GI_3_1_1_b_details']
    c_x = len(x.split(" ")) if type(x)==str else 0
    c_y = len(y.split(" ")) if type(y)==str else 0
    if c_x + c_y > 1:
        return 100
    elif c_x + c_y == 1:
        return 50
    else:
        return 0
    

def GI_3_1_2(r):
    x = r['indicator_GI_3_1_2']
    if type(x)==str:
        v = x.split(" ")
        if 'loan_products' in v:
            y = r['indicator_GI_3_1_2_details']
            if type(y)==str and len(y.split(" "))>1:
                if ('paygo' in v) or ('leasing' in v):
                    return 100
                else:
                    return 50
            else:
                return 50
        else:
            return 0
    else:
        return 0
    
    
    

def GI_3_1_3(r):
    return indicator_with_details(r,name='indicator_GI_3_1_3')

def GI_3_1_4(r):
    return indicator_with_details(r,name='indicator_GI_3_1_4')

def GI_3_1_5(r):
    return simple_details(r['indicator_GI_3_1_5_details'])

def GI_3_1_6(r):
    x = r['indicator_GI_3_1_6']
    if type(x)==str:
        v = x.split(" ")
        if 'loan_products' in v:
            y = r['indicator_GI_3_1_6_details']
            if type(y)==str and len(y.split(" "))>1:
                return 100
            else:
                return 50
        else:
            return 0
    else:
        return 0

def GI_3_1_7(r):
    return indicator_with_details(r,name='indicator_GI_3_1_7')

def GI_3_1_8(r):
    return indicator_with_details(r,name='indicator_GI_3_1_8')

def GI_3_1_9(r):
    return simple_details(r['indicator_GI_3_1_9_details'])

def GI_3_1_10(r):
    x = r['indicator_GI_3_1_10']
    if type(x)==str:
        v = x.split(" ")
        if 'loan_products' in v:
            y = r['indicator_GI_3_1_10_details']
            if type(y)==str and len(y.split(" "))>1:
                if ('paygo' in v) or ('leasing' in v):
                    return 100
                else:
                    return 50
            else:
                return 50
        else:
            return 0
    else:
        return 0
    
def GI_3_1_11(r):
    return indicator_with_details(r,name='indicator_GI_3_1_11')

def GI_3_1_12(r):
    return indicator_with_details(r,name='indicator_GI_3_1_12')

def GI_3_1_13(r):
    return simple_details(r['indicator_GI_3_1_13_details'])

def GI_3_1_14(r):
    x = r['indicator_GI_3_1_14']
    if type(x)==str:
        v = x.split(" ")
        if 'loan_products' in v:
            y = r['indicator_GI_3_1_14_details']
            if type(y)==str and len(y.split(" "))>1:
                if ('paygo' in v) or ('leasing' in v):
                    return 100
                else:
                    return 50
            else:
                return 50
        else:
            return 0
    else:
        return 0

def GI_3_1_15(r):
    return indicator_with_details(r,name='indicator_GI_3_1_15')

def GI_3_1_16(r):
    return indicator_with_details(r,name='indicator_GI_3_1_16')

def GI_3_1_17(r):
    return simple_details(r['indicator_GI_3_1_17'])

def GI_3_1_18(r):
    return indicator_with_details(r,name='indicator_GI_3_1_18')


def GI_3_1_19(r):
    
    x = r['indicator_GI_3_1_19']
    if type(x)==str:

        if 'dedicated' in x.split(' '):
            y = r['indicator_GI_3_1_19_details']
            if type(y)==str and len(y.split(' '))>1:
                return 100
            else:
                return 50
        else:
            return 0

    else:
        return 0

def GI_3_1_20(r):
    return indicator_with_details(r,name='indicator_GI_3_1_20')

def GI_3_1_21(r):
    return indicator_with_details(r,name='indicator_GI_3_1_21')

def GI_3_1_22(r):
    return indicator_with_details(r,name='indicator_GI_3_1_22')

def GI_3_1_23(r):
    return indicator_with_details(r,name='indicator_GI_3_1_23_a')

def GI_3_1_24(r):
    return indicator_with_details(r,name='indicator_GI_3_1_24')

def GI_3_1_25(r):
    return indicator_with_details(r,name='indicator_GI_3_1_25')

    

###############################################################################
# SINGLE INDICATORS - GI 3.2
###############################################################################
def GI_3_2_1(r):
    return simple_details(r['indicator_GI_3_2_1'])

def GI_3_2_2(r):
    x = r['indicator_GI_3_2_2_a_details']
    y = r['indicator_GI_3_2_2_b_details']
    c_x = len(x.split(" ")) if type(x)==str else 0
    c_y = len(y.split(" ")) if type(y)==str else 0
    if c_x + c_y > 1:
        return 100
    elif c_x + c_y == 1:
        return 50
    else:
        return 0

def GI_3_2_3(r):
    return simple_details(r['indicator_GI_3_2_3'])

def GI_3_2_4(r):
    return simple_details(r['indicator_GI_3_2_4'])


    
#####################################################
# useful functions
#####################################################
# input: string ('yes','partially','no')
# return 100,50,0
def yes_no_partially(x):
    if x=='yes':
        return 100
    elif x=='no':
        return 0
    else:
        return 50

# input: multiple selection answer
# if nan -> 0
# if 'none' -> 0
# if count <= partially -> 50
# if count > partially -> 100
def simple_details(x,partially=1):
    if type(x)==str:
        if x=='none':
            return 0
        else:
            if len(x.split(" ")) <= partially:
                return 50
            else:
                return 100
    else:
        return 0
    
# Evaluation of indicators with a follow-up 'details' question
# input: row and name of the variable
# if row[name]='no' -> 0
# if row[name] = 'yes' -> if n_detais > partially ->  100, else 50
def indicator_with_details(r,name,partially=1):
    x = r[name]
    if type(x)==str:
        if x=='no':
            return 0
        else:
            y = r[name+'_details']
            if type(y)==str:
                if len(y.split(" "))>partially:
                    return 100
                else:
                    return 50
            else:
                return 0
    else:
        return 0
    


