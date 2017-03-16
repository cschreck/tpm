from datetime import timedelta
from copy import deepcopy

from tpm.util.dist import haversine_distance
from tpm.data_model import Trajectory, Point

import numpy as np


def mean_filter(trajectory, window_size=5):
    trajectory = deepcopy(trajectory)
    points = []
    for i in range(window_size, len(trajectory)):
        mean_lat = np.mean([trajectory[j].lat for j in range(i - window_size, i)])
        mean_lon = np.mean([trajectory[j].lon for j in range(i - window_size, i)])
        points.append(Point(mean_lat, mean_lon, trajectory[i].datetime))

    return Trajectory(points)


def median_filter(trajectory, window_size=5):
    trajectory = deepcopy(trajectory)
    points = []
    for i in range(window_size, len(trajectory)):
        median_lat = np.median([trajectory[j].lat for j in range(i - window_size, i)])
        median_lon = np.median([trajectory[j].lon for j in range(i - window_size, i)])
        points.append(Point(median_lat, median_lon, trajectory[i].datetime))

    return Trajectory(points)


def distance_duplication_filter(trajectory, distance_threshold=1):
    trajectory = deepcopy(trajectory)
    idxs = list()
    for i in range(len(trajectory) - 1):
        if haversine_distance(trajectory[i], trajectory[i + 1]) < distance_threshold:
            idxs.append(i + 1)

    for i in reversed(idxs):
        del trajectory.points[i]

    return trajectory


def time_duplication_filter(trajectory, time_threshold=timedelta(seconds=1)):
    trajectory = deepcopy(trajectory)
    idxs = list()
    for i in range(len(trajectory) - 1):
        if trajectory[i + 1].datetime - trajectory[i].datetime < time_threshold:
            idxs.append(i + 1)

    for i in reversed(idxs):
        del trajectory.points[i]

    return trajectory


def speed_filter_abs(trajectory, speed_threshold=70, in_kmh=False):
    trajectory = deepcopy(trajectory)
    idxs = list()
    if in_kmh:
        speed_threshold /= 3.6

    for i in range(len(trajectory) - 1):
        dist_diff = haversine_distance(trajectory[i], trajectory[i + 1])
        time_diff = trajectory[i + 1].datetime - trajectory[i].datetime
        speed = dist_diff / time_diff.total_seconds()

        if speed > speed_threshold:
            idxs.append(i + 1)

    for i in reversed(idxs):
        del trajectory.points[i]

    return trajectory


def speed_filter_avg(trajectory, speed_threshold, window_size=5, in_kmh=False):
    trajectory = deepcopy(trajectory)
    idxs = list()
    dists = [haversine_distance(p1, p2) for p1, p2 in
               zip(trajectory[0:len(trajectory) - 1], trajectory[1:len(trajectory)])]
    seconds = [(p2.datetime - p1.datetime).total_seconds() for p1, p2 in
               zip(trajectory[0:len(trajectory) - 1], trajectory[1:len(trajectory)])]

    speed = np.divide(dists, seconds)

    if in_kmh:
        speed *= 3.6

    for i in range(window_size, len(trajectory)):
        if np.abs(np.mean(speed[i - window_size:window_size]) - speed[i]) > speed_threshold:
            idxs.append(i)

    reversed(idxs)
    for idx in idxs:
        del trajectory.points[idx]

    return trajectory
