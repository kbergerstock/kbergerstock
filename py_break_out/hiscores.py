# a module to handle the high scores of a game
# k.r.bergerstock @ oct 2020

import const
from os import path
import arcade
from arcade import color

class Hiscores():
    def __init__(self, file_name):
        # create the hi score table
        self.file_name = file_name
        self.hi_scores = []
        
        
    def create(self):
        if path.isfile(self.file_name):
            return self.read()
        else:
            for i in range(1, 11):
                self.hi_scores.append([i,'AAA',369 - i*i])
            return self.write()    


    def write(self):
        try:
            with open(self.file_name, 'wt') as file:
                for item in self.hi_scores:
                    file.write('{},{},{}\n'.format(item[0],item[1],item[2]))    
            return True     
        except IOError:
            return False


    def read(self):
        try:
            self.hi_scores = []
            with open(self.file_name) as file:
                for line in file:
                    row = line.rstrip().split(',')
                    self.hi_scores.append([int(row[0]),row[1],int(row[2])])
            return True 
        except IOError:
            return False

           
    def check(self, score):
        return True if score > self.hi_scores[9][2] else False
       

    def update(self, initials, score):
        tmp = []
        if score <= self.hi_scores[9][2]:
            return
        else:
            one_shot = True
            for item in self.hi_scores:
                if one_shot:
                    if item[2] > score:
                        pass
                    else:
                        tmp.append([0,initials,score])   
                        one_shot = False
                tmp.append(item)
        
        for i in range(10):
            tmp[i][0] = i + 1
        self.hi_scores = tmp[0:10]
    
    def get(self):
        return self.hi_scores
            