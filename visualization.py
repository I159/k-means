"""Clustering visualization."""

import os
import time

from plotly import graph_objs
import plotly.plotly as plot


class DynamicPlot(object):
    def __init__(self, clusters):
        self.clusters = clusters
        plot.sign_in(os.environ['name'], os.environ['key'])
        self.layout = graph_objs.Layout(
                title="K-means clustering computation result.",
                xaxis=graph_objs.XAxis(autorange=True),
                yaxis=graph_objs.YAxis(autorange=True),
                legend=graph_objs.Legend(yref='paper'))

    def visualize(self, delay):
        tokens = os.environ['tokens'].split()
        streams = map(plot.Stream, tokens)
        scatters = [graph_objs.Scatter(
            x=[],
            y=[],
            mode='markers',
            stream={'token': "{}".format(t)},
            name="cluster #{}".format(i)) for i, t in enumerate(tokens[1:])]
        scatters.insert(0, graph_objs.Scatter(
            x=[],
            y=[],
            mode='markers',
            stream={'token': tokens[0]},
            name="centroids"))

        data = graph_objs.Data(scatters)
        fig = graph_objs.Figure(data=data, layout=self.layout)
        unique_url = plot.plot(fig, filename='clusters')

        for s in streams:
            s.open()
        for cls in self.clusters:
            norm_points = [zip(('x', 'y'), zip(*cl.points)) for cl in cls]
            for cl_points, stream in zip(map(dict, norm_points), streams[1:]):
                time.sleep(delay)
                streams[0].write(
                        zip(('x', 'y'), zip(*[i.centroid for i in cls])),
                        self.layout)
                stream.write(cl_points, self.layout)


class StaticPlot(object):
    def __init__(self, clusters):
        self.clusters = clusters
        plot.sign_in(os.environ['name'], os.environ['key'])
        self.layout = graph_objs.Layout(
                title="K-means clustering computation result.",
                xaxis=graph_objs.XAxis(autorange=True),
                yaxis=graph_objs.YAxis(autorange=True))

    def make_scatter(self, name, x, y):
        return graph_objs.Scatter(x=x, y=y, mode='markers', name=name)

    def make_centroids_scatter(self, x, y):
        text = ['cluster #{}'.format(i) for i in range(len(x))]
        return graph_objs.Scatter(
                text=text,
                x=x,
                y=y,
                mode='markers',
                name='centroids',
                marker=graph_objs.Marker(size=10))

    def visualize(self):
        norm_points = [zip(*cl.points) for cl in self.clusters]
        scatters = [self.make_scatter(
            'cluster #{}'.format(i), *v) for i, v in enumerate(norm_points)]
        centroids = zip(*[i.centroid for i in self.clusters])
        scatters.append(self.make_centroids_scatter(*centroids))

        data = graph_objs.Data(scatters)
        fig = graph_objs.Figure(data=data, layout=self.layout)
        plot.plot(fig)
        plot.image.save_as({'data': data}, 'k-means.png')
