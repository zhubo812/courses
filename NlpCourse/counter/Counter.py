'''
Created on Feb 23, 2019

@author: Jackie
'''

class Counter(object):
    '''
    classdocs
    '''
    dict

    def __init__(self, params):
        '''
        Constructor
        '''
        dict={}
    def add(self,k):
        dict[k]=dict[k]+1
        
    def addWithFreq(self,k,v):
        dict[k]=dict[k]+v
    
    def clear(self):
        dict= {}
    
    def getResult(self):
        return dict