from __future__ import division
import argparse
import numpy as np
from alchemy import alchemy
from twitter_trends import twitter
import csv

class trend_filtering:
    def __init__(self):
        self.al_object = alchemy()
        self.tw_object = twitter()
        self.meta_data = np.empty([25258,6],dtype='|S1000')
        with open('metadata.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in spamreader:
                self.meta_data[i, :] = row
                i += 1

        self.meta_data_concepts = []
        iter = 10 #self.meta_data[:,0].size
        for i in range(0, iter):
            s = " ";
            seq = (self.meta_data[i][0], self.meta_data[i][1], self.meta_data[i][2], self.meta_data[i][3], self.meta_data[i][4], self.meta_data[i][5])
            self.meta_data_concepts.append(self.al_object.find_keywords(s.join(seq)))

    def get_trending_programids(self):
        trend_list = []
        trending_concepts = self.get_trending_concepts()
        for i in range(0, len(self.meta_data_concepts)):
            for j in range(0, len(trending_concepts)):
                if trending_concepts[j] == self.meta_data_concepts[i]:
                    trend_list.append(self.meta_data[i,0])
        return trend_list

    def get_trending_concepts(self):
        concepts = []
        for trend in self.tw_object.get_trends():
            tweets = self.tw_object.get_tweets(trend)
            concepts.append(self.al_object.find_keywords(". ".join(tweets)))
        print concepts
        return concepts

    def get_meta_data(self):
        return self.meta_data
