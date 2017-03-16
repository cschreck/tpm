import os
from dateutil import parser

from tpm.data_model import Point, Trajectory

import numpy as np

def read_geolife(subject_dir):
    files = os.listdir(subject_dir)
    files = sorted(files)
    trajectories = []
    for file in files:
        file_path = os.path.join(subject_dir, file)
        with open(file_path, 'r') as f:
            points = []
            for line in f.readlines()[6:]:
                lat, lon, _, _, _, date, time = line.split(',')
                point = Point(np.float32(lat), np.float32(lon), datetime=parser.parse("{} {}".format(date, time)))
                points.append(point)

            trajectories.append(Trajectory(points))

    return trajectories

