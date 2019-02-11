# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:10:49 2018

@author: SH
"""

import win32com.client as win32
import psutil
import os
import subprocess

def send_notification():
    outlook = win32.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0x0)
    mail.To = 'email@email.com; email@email.com'
    mail.Cc='email@email.com'
    mail.Subject = 'Subject'
    mail.body = "Message Here. \nMessage Here."
    mail.send
    print('Notification email sent!')
    
send_notification()


