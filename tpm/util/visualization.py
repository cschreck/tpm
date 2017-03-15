import folium


def visualize_trajectory(trajectory, clusters=None):
    map_lat, map_lon = trajectory[0].lat, trajectory[1].lon
    map_osm = folium.Map(location=[map_lat, map_lon])

    for i, p in enumerate(trajectory):
        tup = (p.lat, p.lon)
        if clusters is not None and clusters[i] >= 0:
            marker = folium.Marker(tup, icon=folium.Icon(color='green'))
            map_osm.add_children(marker)
        else:
            marker = folium.Marker(tup)
            map_osm.add_children(marker)

    return map_osm