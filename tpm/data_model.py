# radius of earth in meters
R = 6378137


class Point(object):
    def __init__(self, lat, lon, datetime):
        self.lat = lat
        self.lon = lon
        self.datetime = datetime

    def __str__(self):
        return '{},{},{}'.format(self.lat, self.lon, self.datetime)


class Trajectory(object):
    def __init__(self, points=list()):
        self.points = points
        self.staypoints = None

    def __iter__(self):
        return self.points.__iter__()

    def __getitem__(self, item):
        return self.points[item]

    def __str__(self):
        return str(len(self.points))

    def __len__(self):
        return len(self.points)

    def append(self, point):
        self.points.append(point)

    def concat(self, trajectory):
        self.points.extend(trajectory.points)
