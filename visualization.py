"""Clustering visualization."""

import os
import time

from plotly import graph_objs
import plotly.plotly as plot


class Plot(object):
    def __init__(self, clusters, num_clusters):
        self.num_clusters = num_clusters
        self.clusters = clusters
        plot.sign_in(os.environ['name'], os.environ['key'])
        self.layout = graph_objs.Layout(xaxis=graph_objs.XAxis(autorange=True),
                             yaxis=graph_objs.YAxis(autorange=True))

    def visualize(self, delay):
        tokens = os.environ['tokens'].split()
        streams = map(plot.Stream, tokens)
        scatters = [graph_objs.Scatter(
            x=[],
            y=[],
            mode='markers',
            stream={'token': "{}".format(t)},
            name="cluster #{}".format(i)) for i, t in enumerate(tokens)]
        data = graph_objs.Data(scatters)
        fig = graph_objs.Figure(data=data, layout=self.layout)
        unique_url = plot.plot(fig, filename='clusters')

        for s in streams:
            s.open()
        for cls in self.clusters:
            norm_points = [zip(('x', 'y'), zip(*cl.points)) for cl in cls]
            for cl_points, stream in zip(map(dict, norm_points), streams[1:]):
                time.sleep(delay)
                streams[0].write(zip(('x', 'y'), zip(*[i.centroid for i in cls])),
                        self.layout)
                stream.write(cl_points, self.layout)
