# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:09:03 2020

@author: anne smal
"""
import random 
import datetime

class Human :
  
    def __init__ (self, name, bd=None) :
        self._name = name
        if bd :
            self._birthday = bd
        else :
            self._birthday = datetime.date.today()
        self._gender = random.choice('MF')

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name
        
    """
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        self._age = new_age
    """
    
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender
        
    @property
    def birthday(self):
        return self._birthday
    
    def say(self, message) :
        print(self._name, ":", message)
        
        

    
    @property
    def age(self):
        today = datetime.datetime.now()
        age = today.year - self._birthday.year
        
        if (today.month<self._birthday.month) or (today.month == self._birthday.month and today.day<self._birthday.day):
            age -= 1
            
        return age    
        
        
if __name__=="__main__" :
    bd = datetime.date(2000, 2, 21)
    bob = Human("Bob",bd)    
    bob.say("I am " + str(bob.age) + " years old")


