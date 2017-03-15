from tpm.util.dist import calc_pdist_matrix
from sklearn.cluster import dbscan



def density_based_staypoint_detection(trajectory):
    pdist_matrix = calc_pdist_matrix(trajectory)
    clusters = dbscan(pdist_matrix, eps=3, min_samples=10, metric='precomputed')[1]
    for cluster in clusters:
        pass
