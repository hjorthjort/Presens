from preprocessing import preprocessing
from kmeansclustering import kmeansclutering
from trend_filtering import trend_filtering

class recommendations:
    def __init__(self):
        preproc = preprocessing()
        self.trend_filter = trend_filtering()
        self.in_data = preproc.get_data()
        self.program_map = preproc.get_programs()
        self.kmeans = kmeansclutering(in_data, program_map)

    def get_kmeans_recommendations(self, new_datapoint):
        recommended_program_ids = self.kmeans.get_recommendation_cluster(new_datapoint)
        return recommended_program_ids

    def get_trend_recommendations(self):
        list_of_trending_programs = self.trend_filter.prioritise_on_trends()
        return list_of_trending_programs

    def get_recommendations(self, new_datapoint):
        kmeans_recommendation = self.get_kmeans_recommendations(new_datapoint)
        trend_recommendation = self.get_trend_recommendations()
        return set(kmeans_recommendation).intersection(trend_filtering)

    def get_meta_data():
        return self.trend_filter.get_meta_data()    
