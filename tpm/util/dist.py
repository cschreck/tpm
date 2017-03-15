from math import sin
from math import asin
from math import cos
from math import radians
from math import sqrt
from tpm.data_model import R


def haversine_distance(p1, p2):
    lat_rad1 = radians(p1.lat)
    lon_rad1 = radians(p1.lon)
    lat_rad2 = radians(p2.lat)
    lon_rad2 = radians(p2.lon)
    return 2*R * asin(sqrt(sin((lat_rad2-lat_rad1)/2)**2 + cos(lat_rad1)*cos(lat_rad2)*(sin((lon_rad2-lon_rad1)/2)**2)))


def calc_pdist_matrix(trajectory):
    return [[haversine_distance(p1, p2)for p2 in trajectory] for p1 in trajectory]

