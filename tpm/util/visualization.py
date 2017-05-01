import folium


def visualize_trajectory(trajectory):
    map_lat, map_lon = trajectory[0].lat, trajectory[0].lon
    map_osm = folium.Map(location=[map_lat, map_lon])

    for i, p in enumerate(trajectory):
        tup = (p.lat, p.lon)
        marker = folium.Marker(tup)
        map_osm.add_children(marker)

    return map_osm


def visualize_start_end_trajectory(trajectory):
    map_lat, map_lon = trajectory[0].lat, trajectory[0].lon
    map_osm = folium.Map(location=[map_lat, map_lon])

    p1 = trajectory[0]
    p2 = trajectory[-1]
    tup = (p1.lat, p1.lon)
    marker = folium.Marker(tup)
    map_osm.add_children(marker)
    tup = (p2.lat, p2.lon)
    marker = folium.Marker(tup)
    map_osm.add_children(marker)

    return map_osm


def visualize_start_end_trajectories(trajectories):
    map_lat, map_lon = trajectories[0][0].lat, trajectories[0][0].lon
    map_osm = folium.Map(location=[map_lat, map_lon])

    for trajectory in trajectories:
        p1 = trajectory[0]
        p2 = trajectory[-1]
        tup = (p1.lat, p1.lon)
        marker = folium.Marker(tup)
        map_osm.add_children(marker)
        tup = (p2.lat, p2.lon)
        marker = folium.Marker(tup)
        map_osm.add_children(marker)

    return map_osm


