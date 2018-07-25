# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:48:55 2018

@author: SH
"""

# This script allows the user to select a csv file using the file dialog box for data import

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
dataset = pd.read_csv(filename)