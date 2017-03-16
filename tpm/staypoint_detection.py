from tpm.util.dist import calc_pdist_matrix
from sklearn.cluster import dbscan
from collections import defaultdict
from collections import Counter
import copy


def density_based_staypoint_detection(trajectory, window_size=20, lookforward=3):
    trajectory = copy.deepcopy(trajectory)
    mask = list()
    for i in range(window_size, len(trajectory) - window_size):
        pdist_matrix = calc_pdist_matrix(trajectory[i - window_size: i + window_size])
        clusters = dbscan(pdist_matrix, eps=4, min_samples=20, metric='precomputed')[1]
        if not Counter(clusters)[-1] == window_size * 2:
            mask.append(True)
        else:
            mask.append(False)

    for i in range(window_size):
        mask.insert(0, mask[0])
    mask.extend([mask[-1]] * window_size)

    clusters = defaultdict(list)
    cluster_id = 0
    clustered_idxs = [i for i, val in enumerate(mask) if val]
    for i, j in zip(clustered_idxs[:len(clustered_idxs) - 1], clustered_idxs[1:len(clustered_idxs)]):
        if j - i > lookforward:
            cluster_id += 1
        clusters[cluster_id].append(i)

    trajectory.staypoints = dict(clusters)
    return trajectory
