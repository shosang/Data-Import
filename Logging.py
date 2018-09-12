# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:38:19 2018

@author: SH
"""

import logging
import os

dirpath=os.getcwd()

def main():

    logging.basicConfig(filename=os.path.join(dirpath, 'update.log'), 
                        format='%(asctime)s - %(message)s', 
                        datefmt='%Y-%m-%d %I:%M:%S %p', 
                        level=logging.INFO)
             
    logging.info(os.getlogin() + ' - update started')

    logging.info(os.getlogin() + ' - update completed')

## ----------------------------------------------------------------------------

if __name__ == '__main__':
    main()