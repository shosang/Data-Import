# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:10:49 2018

@author: SH
"""

import win32com.client as win32

# Drafting and sending email notification to senders. You can add other senders’ email in the list
def send_notification():
    outlook = win32.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0x0)
    mail.To = 'sh@sh.com'
    mail.Cc='sh@sh.com'
    mail.Subject = 'Subject'
    mail.body = "Body. \nBody. \n\nThank you."
    mail.send
    print('Email sent!')
    
send_notification()


