from math import sin
from math import asin
from math import cos
from math import radians
from math import sqrt
from math import atan2
from math import degrees
from tpm.data_model import R
from tpm.data_model import Trajectory
from sklearn.neighbors import DistanceMetric

import numpy as np

haversine = DistanceMetric.get_metric('haversine')


def haversine_distance(p1, p2):
    lat_rad1 = radians(p1.lat)
    lon_rad1 = radians(p1.lon)
    lat_rad2 = radians(p2.lat)
    lon_rad2 = radians(p2.lon)
    return 2*R * asin(sqrt(sin((lat_rad2-lat_rad1)/2)**2 + cos(lat_rad1)*cos(lat_rad2)*(sin((lon_rad2-lon_rad1)/2)**2)))


def fast_haversine_distance(p1,p2):
    dist = haversine.pairwise([p1, p2])[0][1]
    return R * dist


def calc_pdist_matrix(trajectory):
    locations = Trajectory.convert_locations_in_rad(trajectory)
    dists = haversine.pairwise(locations)
    return R * dists


def blocked_pdist_matrix(trajectory, window_size=15):
    length = len(trajectory)
    dist = np.zeros((length, length))
    locations = trajectory.get_points_as_location_in_rad()

    for i in range(0, length):
        p1 = locations[i]
        for j in range(i - window_size, i + window_size):
            if j < 0 or j >= length or i == j:
                continue
            p2 = locations[j]
            dist[i][j] = fast_haversine_distance(p1, p2)

    return dist


def calc_heading(p1, p2):
    lat1 = radians(p1.lat)
    lon1 = radians(p1.lon)
    lat2 = radians(p2.lat)
    lon2 = radians(p2.lon)

    bearing = atan2(cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(lon2 - lon1), sin(lon2 - lon1) * cos(lat2))
    bearing = degrees(bearing)
    bearing = (bearing + 360) % 360

    return bearing
