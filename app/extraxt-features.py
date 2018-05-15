import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def make_Dictionary(root_dir):
    all_words = []
    emails = [os.path.join(root_dir,f) for f in os.listdir(root_dir)]
    for mail in emails:
        with open(mail) as m:
            for line in m:
                words = line.split()
                all_words += words
    dictionary = Counter(all_words)

    list_to_remove = list(dictionary)

    for item in list_to_remove:
        if item.isalpha() == False:
            del dictionary
        elif len(item) == 1:
            del dictionary[item]
    
    dictionary = dictionary.most_common(3000)

    return directory


print('hola!')
make_Dictionary('.//test-mails//8-899msg1.txt')