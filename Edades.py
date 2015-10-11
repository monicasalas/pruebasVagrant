# -*- coding: utf-8 -*-

'''
Created on 04/09/2015

@author: Mono
'''
#from doctest import DocTest


def suma(num1, num2):
        """
        Además de ser comentarios se pueden utilizar para hacer pruebas sencillas
        >>> suma(5,3)
        8
        """
        
        return num1+num2
if __name__=="__main__":
    import doctest
    doctest.testmod()
