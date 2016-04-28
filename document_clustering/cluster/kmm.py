import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import v_measure_score
from document_clustering.normalize.mds import normalize
from document_clustering.visualization.plotter import Plotter


class Kmm:
    num_clusters = 0
    clusters = None
    categories = None
    centroid = None
    vectorizer = None
    output_dir = ''
    df = None
    normalized_df = None

    def __init__(self, parsed_data, vectorizer, num_clusters, output_dir):
        print "kxh132430_final_project Algorithm:".ljust(30) + "KMean\n"
        urls = parsed_data[0]
        names = parsed_data[1]
        descriptions = parsed_data[2]
        self.categories = parsed_data[3]
        self.vectorizer = vectorizer
        self.num_clusters = num_clusters
        # self.kmm = KMeans(n_clusters=num_clusters)
        # print '[cluster num = %i]' % num_clusters
        kmm = KMeans(n_clusters=num_clusters, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)
        tfidf_matrix = self.vectorizer.tfidf_matrix_()
        kmm.fit(tfidf_matrix)
        self.centroid = kmm.cluster_centers_
        self.clusters = kmm.labels_.tolist()
        self.df = self.generate_data_frame(urls, names, descriptions)
        self.normalized_df = self.generate_normalized_data_frame(names)
        self.output_dir = output_dir

    def get_cluster_labels(self):
        return self.clusters

    def generate_data_frame(self, urls, names, descriptions):
        pages = {'url': urls, 'name': names, 'description': descriptions, 'cluster': self.clusters}
        frame = pd.DataFrame(pages, index=[self.clusters], columns=['name', 'description', 'cluster'])
        return frame

    def generate_normalized_data_frame(self, names):
        dist = self.vectorizer.dist_()
        xs, ys = normalize(dist)
        frame = pd.DataFrame(dict(x=xs, y=ys, label=self.clusters, name=names))
        return frame

    def display(self, show_top_words=False):
        frame = self.df
        if show_top_words:
            vocab_frame = self.vectorizer.vocab_frame_()
            terms = self.vectorizer.terms_()
            #sort cluster centers by proximity to centroid
            order_centroids = self.centroid.argsort()[:, ::-1]
            print("Top terms per cluster:")
            print

        for i in range(self.num_clusters):
            if show_top_words:
                print ("Cluster %d top words:" % i)
                for ind in order_centroids[i, :6]: #replace 6 with n words per cluster
                    print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'))
                print
                print
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

    def plot(self, file_format='html'):
        plotter = Plotter(self.output_dir)
        plotter.set_palette(self.num_clusters)
        if file_format == 'html':
            plotter.plot_html(self.normalized_df)
        elif file_format == 'png':
            plotter.plot_png(self.normalized_df)
        else:
            print 'Unsupported format!!!'

