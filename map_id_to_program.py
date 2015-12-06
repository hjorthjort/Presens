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

    def programs_to_data(self, list_of_ids):
        lists = []
        for i in range(0, len(list_of_ids)):
            if self.meta_data[i][0] in list_of_ids:
                lists.append({'title':self.meta_data[i][1]
                            , 'genre':self.meta_data[i][2]
                            , 'sub-genre':self.meta_data[i][3]
                            , 'tags':self.meta_data[i][4]
                            , 'synopsis':self.meta_data[i][5]})
        return lists

def main():
    mapp = mapping()

if __name__ == '__main__':
   main()
