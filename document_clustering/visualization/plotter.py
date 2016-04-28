import os
import matplotlib.pyplot as plt
import mpld3
from document_clustering.visualization.toptoolbar import TopToolbar


class Plotter:
    colors = [(0, '#1b9e77'), (1, '#d95f02'), (2, '#7570b3'), (3, '#e7298a'), (4, '#ffb400'), (5, '#ffff00'), (6, '#000000')]
    names = [(0, 'A'),(1, 'B'),(2, 'C'),(3, 'D'),(4, 'E'),(5, 'F'),(6, 'G')]
    cluster_colors = {}
    cluster_names = {}
    output_dir = ''

    def __init__(self, output_dir):
        self.output_dir = output_dir

    def set_palette(self, k):
        self.cluster_colors = dict(self.colors[:k])
        self.cluster_names = dict(self.names[:k])

    def plot_png(self, data_frame):
        # #group by cluster
        groups = data_frame.groupby('label')

        # set up plot
        fig, ax = plt.subplots(figsize=(17, 9)) # set size
        ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling

        #iterate through groups to layer the plot
        #note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
        for name, group in groups:
            ax.plot(group.x, group.y, marker='o', linestyle='', ms=12,
                    label=self.cluster_names[name], color=self.cluster_colors[name],
                    mec='none')
            ax.set_aspect('auto')
            ax.tick_params(\
                axis= 'x',          # changes apply to the x-axis
                which='both',      # both major and minor ticks are affected
                bottom='off',      # ticks along the bottom edge are off
                top='off',         # ticks along the top edge are off
                labelbottom='off')
            ax.tick_params(\
                axis= 'y',         # changes apply to the y-axis
                which='both',      # both major and minor ticks are affected
                left='off',      # ticks along the bottom edge are off
                top='off',         # ticks along the top edge are off
                labelleft='off')

        ax.legend(numpoints=1)  #show legend with only 1 point

        #add label in x,y position with the label as the film title
        for i in range(len(data_frame)):
            ax.text(data_frame.ix[i]['x'], data_frame.ix[i]['y'], data_frame.ix[i]['name'], size=8)

        # plt.savefig(self.dir_name + 'clusters_small_noaxes.png', dpi=200)
        plt.show() #show the plot
        plt.close()

    def plot_html(self, data_frame):
        #group by cluster
        groups = data_frame.groupby('label')

        #define custom css to format the font and to remove the axis labeling
        css = """
        text.mpld3-text, div.mpld3-tooltip {
          font-family:Arial, Helvetica, sans-serif;
        }

        g.mpld3-xaxis, g.mpld3-yaxis {
        display: none; }

        svg.mpld3-figure {
        margin-left: -10px;}
        """

        # Plot 14 6
        fig, ax = plt.subplots(figsize=(10,6)) #set plot size
        ax.margins(0.03) # Optional, just adds 5% padding to the autoscaling

        #iterate through groups to layer the plot
        #note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
        for name, group in groups:
            points = ax.plot(group.x, group.y, marker='o', linestyle='', ms=12,
                             label=self.cluster_names[name], mec='none',
                             color=self.cluster_colors[name])
            ax.set_aspect('auto')
            labels = [i for i in group.name]

            #set tooltip using points, labels and the already defined 'css'
            tooltip = mpld3.plugins.PointHTMLTooltip(points[0], labels, voffset=10, hoffset=10, css=css)
            #connect tooltip to fig
            mpld3.plugins.connect(fig, tooltip, TopToolbar())

            #set tick marks as blank
            ax.axes.get_xaxis().set_ticks([])
            ax.axes.get_yaxis().set_ticks([])

            #set axis as blank
            ax.axes.get_xaxis().set_visible(False)
            ax.axes.get_yaxis().set_visible(False)

        ax.legend(numpoints=1) #show legend with only one dot

        html = mpld3.fig_to_html(fig)

        out_file = os.path.join(self.output_dir, 'index.html')

        with open(out_file, 'w') as file_:
            file_.write(html)

        plt.close()

    def plot_dendrogram(self, dendrogram):

        fig, ax = plt.subplots(figsize=(18, 24)) # set size 15, 20
        ax = dendrogram;

        plt.tick_params(\
            axis= 'x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelbottom='off')

        #uncomment below to save figure
        # plt.savefig(self.dir_name + 'ward_clusters.png', dpi=200) #save figure as ward_clusters

        plt.show()
        plt.close()
