# -*- coding: utf-8 -*-
"""F1_score_evaluation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16mKRLdJsz-uvkNHgsPR9xABMKkUrZS7H
"""

# from google.colab import drive
# drive.mount('/content/drive')

from sklearn.metrics import f1_score
import numpy as np
import pandas as pd
import sys


def getF1(filename):
    try:
        y_true = pd.read_csv(f'api/submissions/target_with_us.csv', index_col = None, header = None)

        y_pred = pd.read_csv(f'media/{filename}', index_col = None, header = None)

        return (f1_score(y_true, y_pred, average='weighted'))
    except:
        return ("ERROR")
