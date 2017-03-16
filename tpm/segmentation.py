from copy import deepcopy
from datetime import timedelta
from tpm.data_model import Trajectory
from sklearn.cluster import dbscan

from tpm.util.dist import calc_pdist_matrix


def split_by_time(trajectory, split_delta=timedelta(hours=2)):
    trajectory = deepcopy(trajectory)
    trajectories = list()
    last_datetime = None
    re_trajectory = Trajectory()

    for point in trajectory:
        if last_datetime is None:
            last_datetime = point.datetime

        if point.datetime - last_datetime > split_delta:
            trajectories.append(re_trajectory)
            re_trajectory = Trajectory()

        re_trajectory.append(deepcopy(point))
        last_datetime = point.datetime

    trajectories.append(re_trajectory)

    return trajectories


def split_by_staypoint(trajectory):
    assert trajectory.staypoints is not None
    trajectories = list()
    splits = list()
    for key in trajectory.staypoints:
        points = trajectory.staypoints[key]
        splits.append(points[int(len(points) / 2)])

    prev_split = 0
    for split in splits:
        trajectories.append(Trajectory(trajectory.points[prev_split:split]))
        prev_split = split

    trajectories.append(Trajectory(trajectory.points[prev_split:]))

    return trajectories




