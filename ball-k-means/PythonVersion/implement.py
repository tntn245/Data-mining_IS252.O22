from win_ball_kmeans_python import ball_k_means

if __name__ == '__main__':
    dataset_address = "D:\\Data mining\\data+centers\\dataset\\Codrna.csv"
    clf = ball_k_means(isDouble=1)
    m = clf.fit(dataset_address, 5, True, True, -1, "D:\\Data mining\\data+centers\\centroids\\Codrna4.csv")