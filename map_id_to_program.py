from __future__ import division
import argparse
import numpy as np
import csv

class mapping:
    def __init__(self):
        self.meta_data = np.empty([25258,6],dtype='str')
        with open('metadata.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in spamreader:
                self.meta_data[i, :] = row
                i += 1

    def programs_to_data(list_of_ids):
        lists = []
        for i in range(0, len(list_of_ids)):
            if list_of_ids == self.meta_data[0][i]:
                lists.append({'title':self.meta_data[1]
                            , 'genre':self.meta_data[2]
                            , 'sub-genre':self.meta_data[3]
                            , 'tags':self.meta_data[4]
                            , 'synopsis':self.meta_data[5]})
        return lists

def main():
    mapp = mapping()

if __name__ == '__main__':
   main()
