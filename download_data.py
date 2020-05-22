# -*- coding: utf-8 -*-

''' Download data from DFRLab's S3 bucket

This script will create a folder called data and store in it
the csv files.
'''

# import modules
import os

# create data folder
if not os.path.exists('./data/'):
    os.mkdir('./data/')

# download data from DFRLab's S3 bucket

