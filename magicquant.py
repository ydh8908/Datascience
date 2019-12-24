#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:38:11 2019

@author: donghyunyoo
"""

import pandas as pd

def magic_by_pd(file_path):
    per_data = pd.read_excel(file_path, sheet_name = 'PER', index_col=0)
    filtered_per = per_data[per_data['PER']>0]
    sorted_per=filtered_per.sort_values(by='PER')
    sorted_per['PER랭킹']=sorted_per['PER'].rank()
    roa_data = pd.read_excel(file_path, sheet_name='ROA', index_col=0)
    filtered_roa = roa_data.dropna()
    filtered_roa.columns=['ROA']
    sorted_roa = filtered_roa.sort_values(by='ROA', ascending =False)
    sorted_roa['ROA랭킹']=sorted_roa['ROA'].rank(ascending=False)
    total_df=pd.merge(sorted_per,sorted_roa, how='inner', left_index=True, right_index=True)
    total_df['종합랭킹']=(total_df['PER랭킹']+total_df['ROA랭킹']).rank(ascending=True)
    return total_df.sort_values(by='종합랭킹')