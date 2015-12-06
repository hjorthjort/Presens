from __future__ import division
import argparse
import numpy as np
from alchemy import alchemy
from twitter_trends import twitter

class trend_filtering:
    def __init__(self):
        self.al_object = alchemy()
        self.tw_object = twitter()

    def prioritise_on_trends(self, metadata_list, trends_list):
        priority_list = []
        trending_concepts = self.get_trending_concepts()
        for i in range(0, metadata_list[:,0].size):
            metadata_concepts = self.get_metadata_concepts(metadata[i,:])
            for k in range(0, len(metadata_concepts))
                for j in range(0, len(trending_concepts)):
                    if metadata_concepts[k] == trending_concepts[j]:
                        priority_list.append(metadata_list[i,:])
        return priority_list

    def get_metadata_concepts(self, metadata):
        concepts = []
        concepts.append(self.al_object.find_keywords(". ".joint(metadata)))
        return concepts

    def get_trending_concepts(self):
        concepts = []
        for trend in self.tw_object.get_trends():
            tweets = self.tw_object.get_tweets(trend)
            concepts.append(self.al_object.find_keywords(". ".join(tweets)))
        return concepts
