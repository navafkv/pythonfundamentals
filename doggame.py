#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Dog:
    """A simple attempt to model a dog"""
    def __init__(self,name,age):
        """Initializing name and age attributes"""
        self.name= name
        self.age= age
        print('This worked!')
        
    def sit(self):
        """Simulate a dog in response to a sit command"""
        print(f"{self.name} is now sitting")
        
    def roll_over(self):
        """Simulate a dog in response to a rollover command"""
        print(f"{self.name} is now rolling over")

