import itertools

times = ['morning', 'noon', 'afternoon', 'night']
days = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun']
vehicles = ['sedan', 'jeep', 'pickup', 'minibus', 'bus', 'truck']
sexes = ['man', 'woman']
roads = ['st_flat', 'st_des', 'st_asc', 'cuv_flat', 'cuv_des', 'cuv_asc']
surfaces = ['dry', 'wet', 'sandy']

evidences = list(itertools.product(times, days, vehicles,
                                   sexes, roads, surfaces))
print(evidences)

