from code4 import cal_save_likelihoods

#vehicle
vehicles = ['sedan', 'jeep', 'pickup', 'minibus', 'bus', 'truck']

data = [[18, 16, 4, 0],
        [3, 2, 1, 0],
        [4, 14, 6, 0],
        [18, 34, 13, 2],
        [9, 4, 11, 1],
        [26, 55, 44, 8]]

save_name = 'vehicle_likelihoods.csv'
cal_save_likelihoods(index=vehicles,
                     data=data,
                     save_name=save_name)

#sex
sex = ['man', 'woman']

data = [[73, 121, 78, 11],
        [5, 4, 1, 0]]

save_name = 'sex_likelihoods.csv'
cal_save_likelihoods(index=sex,
                     data=data,
                     save_name=save_name)

#road
roads = ['st_flat', 'st_des', 'st_asc', 'cuv_flat', 'cuv_des', 'cuv_asc']

data = [[30, 54, 32, 5],
        [17, 40, 24, 3],
        [9, 10, 9, 1],
        [6, 10, 2, 0],
        [11, 7, 9, 2],
        [5, 4, 3, 0]]

save_name = 'road_likelihoods.csv'
cal_save_likelihoods(index=roads,
                     data=data,
                     save_name=save_name)

#road surface
surfaces = ['dry', 'wet', 'sandy']

data = [[61, 99, 66, 10],
        [17, 25, 13, 1],
        [0, 1, 0, 0]]

save_name = 'surface_likelihoods.csv'
cal_save_likelihoods(index=surfaces,
                     data=data,
                     save_name=save_name)