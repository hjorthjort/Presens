from __future__ import division
import argparse
import numpy as np
import csv

def programs_to_data(self, list_of_ids, meta_data):
    lists = []
    for i in range(0, len(list_of_ids)):
        if meta_data[i][0] in list_of_ids:
            lists.append({'programid':meta_data[i][0]
                        , 'title':meta_data[i][1]
                        , 'genre':meta_data[i][2]
                        , 'sub-genre':meta_data[i][3]
                        , 'tags':meta_data[i][4]
                        , 'synopsis':meta_data[i][5]})
    return lists
