from __future__ import division
import argparse
import numpy as np
from weather import getWeather
from date_time import weekday, hour_of_day

class preprocessing:
    def __init__(self):
        self.id_time_map = None

    # Generate a matrix with timestamp and programid from a file
    def gen_id_time_map(self):
        self.id_time_map = np.loadtxt('learned_actions.csv', delimiter=',', dtype='|S36,int',usecols=(1, 3), skiprows=1, unpack=True)

    # Return the programid array
    def get_programs(self):
        return self.id_time_map[0]

    # Returns a matrix with cols: [Weekday, Hour of day, Weather] to run in a clustering algorithm
    def get_data(self):
        if self.id_time_map == None:
            self.gen_id_time_map()
        data_set = np.empty([self.id_time_map[1].shape[0], 3])
        for i in range(0, data_set[:,0].size):
            data_set[i,0] = weekday(self.id_time_map[1][i])
            data_set[i,1] = hour_of_day(self.id_time_map[1][i])
            data_set[i,2] = getWeather(self.id_time_map[1][i],'London')
        return data_set
