# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:10:49 2018

@author: s3856366
"""

import win32com.client as win32
import psutil
import os
import subprocess

def send_notification():
    outlook = win32.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0x0)
    mail.To = 'Stephanie.Hosang@scotiabank.com; Stephanie.Hosang@scotiabank.com'
    mail.Cc='Stephanie.Hosang@scotiabank.com'
    mail.Subject = 'Pending QC Report - Awaiting Case Transitions'
    mail.body = "Please note that the Case Transitions file has not yet been updated. \nAutomated script run has been terminated. \n\nScript will need to be run manually once file is received."
    mail.send
    print('Notification email sent!')
    
send_notification()


