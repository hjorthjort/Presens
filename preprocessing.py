from __future__ import division
import argparse
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import requests

class preprocessing:
    def __init__(self):
        self.id_time_map = None

    def day(self, timestamp):
        return dt.date.fromtimestamp(timestamp).weekday()

    def time(self, timestamp):
        return dt.datetime.fromtimestamp(timestamp).hour

    def weather(self, timestamp):
        return np.random.choice(np.arange(10))

    def gen_id_time_map(self):
        self.id_time_map = np.loadtxt('learned_actions.csv', delimiter=',', dtype='|S36,int',usecols=(1, 3), skiprows=1, unpack=True)

    def get_programs(self):
        return self.id_time_map[0]

    def get_data(self):
        if self.id_time_map == None:
            self.gen_id_time_map()
        data_set = np.empty([self.id_time_map[1].shape[0], 3])
        for i in range(0, data_set[:,0].size):
            data_set[i,0] = self.day(self.id_time_map[1][i])
            data_set[i,1] = self.time(self.id_time_map[1][i])
            data_set[i,2] = self.weather(self.id_time_map[1][i])
        return data_set
