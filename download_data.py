# -*- coding: utf-8 -*-

''' Download data from DFRLab's S3 bucket

This script will create a folder called data and store in it
the csv files.
'''

# import modules
import os
import urllib.request as req

# create data folder
if not os.path.exists('./data/'):
    os.mkdir('./data/')

# download data from DFRLab's S3 bucket
datasets = [
    'https://dfrlab.s3-us-west-2.amazonaws.com/datafest-tbilisi/data/indonesia_022020_users_csv_hashed.csv',
    'https://dfrlab.s3-us-west-2.amazonaws.com/datafest-tbilisi/data/indonesia_022020_tweets_csv_hashed.csv'
]

# log
print ('')
print (' downloading csv files into data folder...')

for d in datasets:
    filename = d.split('/')[-1]
    path = f'./data/{filename}'
    req.urlretrieve(d, path)

print (' done!')
