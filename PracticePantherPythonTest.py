#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np


df = pd.read_csv('Migration_Interview_Data (Python).csv')


#remove dupes
df = df.drop_duplicates()


#adding contact to column names
df.columns = ['Contact: ' + col for col in df.columns]


#proper letter casing for names 
df['Contact: First Name'] = df['Contact: First Name'].str.title()
df['Contact: Last Name'] = df['Contact: Last Name'].str.title()


#making date format mm/dd/yyyy
df['Contact: Date of Birth'] = pd.to_datetime(df['Contact: Date of Birth'], dayfirst=True)
df['Contact: Date of Birth'] = df['Contact: Date of Birth'].dt.strftime('%m/%d/%Y')


#creating unique ID's per row 
df['Contact: ID'] = np.arange(1, len(df) + 1)


#assigning full name to abbrev. names and empty/na cells
assigned_map = {
    'GM': 'Gabe Michel',
    'AA': 'Aaron Artsen',
    'BL': 'Bond Liver',
    'IC': 'Individual Contributor',
    'TM': 'Tim Mint'
}

df['Contact: Assigned'] = df['Contact: Assigned'].map(assigned_map)
df['Contact: Assigned'] = df['Contact: Assigned'].fillna('Gabe Michel')


#exporting finished transformation to csv
df.to_csv('python_test_transformed_contacts.csv', index=False)


