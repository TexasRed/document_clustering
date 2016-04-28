import pandas as pd
from sklearn.metrics import v_measure_score
from scipy.cluster.hierarchy import ward, dendrogram, fcluster
from document_clustering.visualization.plotter import Plotter


class Hac:

    linkage_matrix = None
    num_clusters = 0
    clusters = None
    categories = None
    dendrogram = None
    df = None
    output_dir = ''

    def __init__(self, parsed_data, vectorizer, num_clusters, output_dir):
        print "kxh132430_final_project Algorithm:".ljust(30) + "HAC\n"
        urls = parsed_data[0]
        names = parsed_data[1]
        descriptions = parsed_data[2]
        self.categories = parsed_data[3]
        self.linkage_matrix = ward(vectorizer.dist_()) #define the linkage_matrix using ward kxh132430_final_project pre-computed distances
        self.dendrogram = dendrogram(self.linkage_matrix, orientation="left", labels=names)
        self.num_clusters = num_clusters
        clusters = fcluster(self.linkage_matrix_(), self.num_clusters, criterion='maxclust')
        clusters[:] = [x - 1 for x in clusters]
        self.clusters = clusters
        self.df = self.generate_data_frame(urls, names, descriptions)
        self.output_dir = output_dir

    def generate_data_frame(self, urls, names, descriptions):
        pages = {'url': urls, 'name': names, 'description': descriptions, 'cluster': self.clusters}
        frame = pd.DataFrame(pages, index=[self.clusters], columns=['name', 'description', 'cluster'])
        return frame

    def linkage_matrix_(self):
        return self.linkage_matrix

    def dendrogram_(self):
        return self.dendrogram

    def clusters_(self):
        return self.clusters

    def display(self):
        frame = self.df
        for i in range(self.num_clusters):
            print("Cluster %d title:" % i)
            for title in frame.ix[i]['name'].values.tolist():
                print(' %s,' % title)
            print
            print
        print 'Documents in each cluster:'
        print 'cid count'
        print self.df['cluster'].value_counts().sort_index()
        print
        v_score = v_measure_score(labels_true=self.categories, labels_pred=self.clusters)
        print 'The v_measure score is: %s' % v_score

    def plot(self):
        plotter = Plotter(self.output_dir)
        plotter.plot_dendrogram(self.dendrogram)
