from math import radians
# radius of earth in meters
R = 6378137


class Point(object):
    def __init__(self, lat, lon, datetime):
        self.lat = lat
        self.lon = lon
        self.datetime = datetime

    def __str__(self):
        return '{},{},{}'.format(self.lat, self.lon, self.datetime)

    def get_location(self):
        return [self.lat, self.lon]

    def get_location_in_rad(self):
        return [radians(self.lat), radians(self.lon)]


class Trajectory(object):
    def __init__(self, points=None):
        if points is None:
            self.points = list()
        else:
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

    def get_points_as_location_in_rad(self):
        return [point.get_location_in_rad() for point in self.points]

    @staticmethod
    def convert_locations_in_rad(points):
        return [point.get_location_in_rad() for point in points]
