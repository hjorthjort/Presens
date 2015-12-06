from preprocessing import preprocessing
from kmeansclustering import kmeansclutering
from trend_filtering import trend_filtering

class recommendations:
    def __init__(self):
        print "Reached init"
        preproc = preprocessing()
        self.trend_filter = trend_filtering()
        print "did stuff 1"
        self.in_data = preproc.get_data()
        print "did stuff 2"
        self.program_map = preproc.get_programs()
        print "did stuff 3"
        self.kmeans = kmeansclutering(self.in_data, self.program_map)
        print "Done with init"

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
