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

    @staticmethod
    def scatter(clid):
        return graph_objs.Scatter(x=[], y=[], mode='markers',
                                  name="cluster #{}".format(clid))

    def visualize(self):
        streams = map(plot.Stream, os.environ['tokens'].split())
        scatters = [graph_objs.Scatter(
            x=[],
            y=[],
            mode='markers',
            name="cluster #{}".format(i)) for i in range(self.num_clusters)]
        data = graph_objs.Data(scatters)
        fig = graph_objs.Figure(data=data, layout=self.layout)
        unique_url = plot.plot(fig, filename='clusters')

        for cls in self.clusters:
            # FIXME: separated stream for every plot
            norm_points = [zip(('x', 'y'), zip(*cl.points)) for cl in cls]
            for s in streams:
                s.open()
            for cl_points, stream in zip(map(dict, norm_points), streams):
                stream.write(cl_points)


#        data = graph_objs.Data(map(self.scatter, range(self.num_clusters)))
#        plot.plot(data)
#        import pdb; pdb.set_trace()
#        stream = plot.Stream(os.environ['token'])
#        stream.open()
#        for cls in self.clusters:
#            stream.write(
#                    (dict(zip(('x', 'y'), zip(*cl.points))) for cl in cls))
#        stream.close()
