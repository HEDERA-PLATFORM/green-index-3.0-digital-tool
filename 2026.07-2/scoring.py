#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Description: Code to compute the scoring of the Green Index 3.0

Usage: python scoring.py <inpuf_file.json>

The input file has the form:
    {
     'datafile': <file name with dataset>,
     'survey': <path to XLS form>,
     'select_column': <name of column to be used for selecting an audit>,
     'select_value': <value of column to be used for selecting an audit>,
     'output_base_folder': <output folder> [optional]
     
     }

Author: Alfonso Caiazzo (HEDERA Sustainable Solutions)
Copyright: e-MFP Green Inclusive and Climate-Smart Finance AG
License: CC-BY-4.0
Terms of use: reproduction possible, use the following sentence to acknowledge the original sources:
    "This code is part of thee digital solutions for the Green Index 3.0. It has been developed by Alfonso Caiazzo (HEDERA)"
Version: 2022.09-1.0
Released: September 1st, 2022

"""

import os
import pandas as pd
import json
import sys

from green_index import evaluate_indicators

###############################################################################
# I/O Class
###############################################################################
class InputParameters:
    def __init__(self,input_dict):
        
        # [REQUIRED] files to be used
        self.datafile = input_dict['datafile'] 
        
        # [REQUIRED] path to green index XLS Form
        self.survey = input_dict['survey']
        
        # [REQUIRED] Selection of the right audit
        self.select_column = input_dict['select_column']
        self.select_value = input_dict['select_value']

        # [OPTIONAL] output directory
        self.output_base_folder = (input_dict['output_base_folder']  
                                   if 'output_base_folder' in input_dict.keys() else './')
###############################################################################
       
        
        
if len(sys.argv)>1:
    
    ###########################################################################
    # read input
    ###########################################################################    
    input_file = sys.argv[1]
    print(" ** reading file: ", input_file)

    with open(input_file) as f:
        input_dict = json.load(f)
        
    io = InputParameters(input_dict)
    
    ###########################################################################
    # read dataframe & survey
    ###########################################################################
    print(" --[GREEN INDEX 3.0]--- READING DATAFILE: ", io.datafile)
    full_df = pd.read_csv(io.datafile)
    full_df.columns = [c[c.rfind("-")+1:] for c in full_df.columns]
    
    print(" --[GREEN INDEX 3.0]--- READING XLS FORM: ", io.survey)
    survey = pd.read_excel(io.survey,sheet_name='survey')
    choices = pd.read_excel(io.survey,sheet_name='choices')
    
    ###########################################################################
    # select institution
    ###########################################################################
    df = full_df.loc[full_df[ io.select_column ] == io.select_value ]
    
    
    ###########################################################################
    # evaluate score
    ###########################################################################
    print(" --[GREEN INDEX 3.0]--- EVALUATE SCORE ")
    indicators_score = evaluate_indicators(df)
    
    
    ###############################################################################
    # export to Excel
    ###############################################################################
    i_score_table = pd.DataFrame.from_dict({
        'Indicator': [i for i in indicators_score.keys()],
        'Score': [indicators_score[i] for i in indicators_score.keys()]
        })
    
    if not os.path.exists(io.output_dir):
        print(" ** ERROR: OUTPUT DIRECTORY DOES NOT EXIST **")
        print(" ** ERROR: I cannot save the output file. **")
    else:
        i_score_table.to_excel(io.output_dir + 'green_index_3.0_scores.xlsx')
        print(" --[GREEN INDEX 3.0]--- SAVED: ", io.output_dir + 'green_index_3.0_scores.xlsx')
    
else:
    print("** ERROR: You need to provide an input (JSON) file **")
    
    





          

