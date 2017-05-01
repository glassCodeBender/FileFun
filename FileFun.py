
# -*- coding: utf-8 -*-
"""
@Author: glassCodeBender

Program Purpose:
    
        This program will be used as my base file import and export program.

"""
import os
import sys

class FileFun(object):

    def __init__(self, file1 = '', file2 = ''):
       self.file = file1 
       self.extraFile = file2 
       
    """ Getter Methods """   
    def getFile1(self):
        return self.file
    def getFile2(self):
        return self.extraFile
    
    """ Program reads the file line by line """
    def readFileByLine(self):        

        file1 = self.extraFile # take the String passed to the Class and place it in a variable.
        
        """ open file """
        if os.path.exists( file1 ):
            try:
                txtFile = open(file1)
            except IOError:
                print("Could not read file " + file1)
                
        """ read file line by line and place each line in a list. """     
        for f in txtFile:
            try:
                lineList = f.readlines()
            except IOError:
                print("Could not read file " + file1)
        txtFile.close()
        return lineList
    """ END readFileByLine() method """

""" THIS METHOD IS UNNECESSARY """
"""
    def import_ufile(self):
        if os.path.exists(argv[1]):
            try:
                fusers = open(argv[1])
            except IOError:
                print("Could not read file " + argv[1])                

        for f in fusers:
            try:
                user_list = f.readlines()
            except IOError:
                print("Could not read file " + argv[1])
        fusers.close()
        return user_list
   """ 
# read a combination of each username and password in to see if one matches


# need a command to close files and exit programs if we have success


# read the next 50 lines (this assumes we only read first 50 lines)

"""
 create a if __name__ = __main__ command at the end that will determine what happens
 if the program is run from another program. 

"""
"""
with open(pfile_string) as f:
    for i in range(50):
        f.next()
    for line in f:
        pass_list2 = f.readlines()
"""     
