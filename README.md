# spam_filter
A simple spam filter based on the Bayes Classification

This project will use a simple naive bayes classification to determine which
keywords are frequently recurring in spam emails, so that future emails can
be classified as spam or not spam.

This project will require:
- spam training data, stored in a folder as .txt files
- non-spam training data, stored in a folder as .txt files
- a keywords frequency and likelihood ratio dataframe to be updated over time

The scripts will do the following:
- use training data to determine the likelihood ratio of all keywords
- use the likelihood ratio dataframe to determine if a target email is likely
spam or not spam
