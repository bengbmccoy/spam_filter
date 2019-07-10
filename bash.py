'''
This is the first version of the spam filter, this will all be moved to a
proper file name structure once it is working

Written by: Ben McCoy, Jul 2019

'''

import pandas as pd
import numpy as np
import os
from collections import Counter

def main():

    print('hello my dudes')

    freq_df = init_df()
    # print(freq_df)

    # file = 'inbox_training'
    files = ['spam_training', 'inbox_training']
    for training_file in files:
        text = get_words(training_file)
        freq_dict = dict(count_freq(text))
        freq_df = update_df(freq_df, freq_dict, training_file)

    freq_df = freq_df.fillna(0)
    # print(freq_df)
    print(freq_df.to_string())

    # calc_lr(freq_df)

def calc_lr(freq_df):

    for index, row in freq_df.iterrows():
        pass

def update_df(freq_df, freq_dict, training_file):

    column = training_file.split('_')[0] + '_freq'

    for key, value in freq_dict.items():
        freq_df.loc[key, column] = value

    return freq_df

def count_freq(text):

    unique_words = (list(text.split()))
    counts = Counter(unique_words)
    return counts

def get_words(file):

    text = ''
    fnames = (os.listdir(file))
    for name in fnames:
        name = str(file) + '/' + str(name)
        f = open(name,'r')
        text = text + str(f.read())

    return text

def init_df():
    freq_df = pd.DataFrame(np.nan, index=[], columns=['inbox_freq', 'inbox_lr', 'spam_freq', 'spam_lr'])
    return freq_df

main()
