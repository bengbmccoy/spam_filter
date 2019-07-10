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

    # freq_df = freq_df.fillna(0)
    # print(freq_df)
    # print(freq_df.to_string())

    lr_df = calc_lr(freq_df)
    lr_df = lr_df.fillna(0.0001)
    # print(lr_df)

    assessment_text = get_words('assessment')
    assessment_dict = dict(count_freq(assessment_text))
    # print(assessment_dict)

    assess_inbox_lr = 1
    assess_spam_lr = 1

    for key, value in assessment_dict.items():
        try:
            assess_inbox_lr = assess_inbox_lr * (lr_df.at[key, 'inbox_lr'])
        except:
            pass
        try:
            assess_spam_lr = assess_spam_lr * (lr_df.at[key, 'spam_lr'])
        except:
            pass

    # print(assess_inbox_lr)
    # print(assess_spam_lr)

    posterior_odds = assess_inbox_lr/assess_spam_lr

    print(posterior_odds)

def calc_lr(freq_df):

    inbox_count = freq_df['inbox_freq'].sum()
    spam_count = freq_df['spam_freq'].sum()
    for index, row in freq_df.iterrows():
        if row['inbox_freq'] > 0:
            freq_df.set_value(index, 'inbox_lr', row['inbox_freq']/inbox_count)
        if row['spam_freq'] > 0:
            freq_df.set_value(index, 'spam_lr', row['spam_freq']/spam_count)

    return freq_df

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
