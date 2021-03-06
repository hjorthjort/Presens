from __future__ import division
import argparse
import numpy as np
from preprocessing import preprocessing
from sklearn import cluster

class kmeansclutering:
    def __init__(self, data_matrix, program_ids):
        self.rows = data_matrix.shape[0]
        self.cols = data_matrix.shape[1]
        clusters = int(self.rows/10000)
        iterations = int(self.rows/100000)
        self.kmeans = cluster.KMeans(n_clusters=clusters, max_iter=iterations, init='k-means++', precompute_distances='auto')
        self.program_ids = program_ids
        self.clusters = self.kmeans.fit_predict(data_matrix)

    def get_recommendation_cluster(self, datapoint):
        cluster = self.kmeans.predict(datapoint)
        program_id_list = []
        for i in range(0, self.clusters.size):
            if self.clusters[i] == cluster:
                program_id_list.append(self.program_ids[i])
        return program_id_list
