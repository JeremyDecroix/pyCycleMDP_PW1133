import numpy as np

from pycycle.maps.map_data import MapData


"""Python version of axi-3_2.map Compressor map from NPSS"""
AXI3_2 = MapData()

# Map design point values
AXI3_2.defaults = {}
AXI3_2.defaults['alphaMap'] = 0.0
AXI3_2.defaults['NcMap'] = 1.00
AXI3_2.defaults['PRmap'] = 3.2000
AXI3_2.defaults['RlineMap'] = 2.000
AXI3_2.RlineStall = 1.0


AXI3_2.alphaMap = np.array([0.000, 90.000])
AXI3_2.NcMap = np.array(
    [0.400, 0.500, 0.600, 0.700, 0.800, 0.900, 0.950, 1.000, 1.050, 1.100])
AXI3_2.RlineMap = np.array(
    [1.000, 1.200, 1.400, 1.600, 1.800, 2.000, 2.200, 2.400, 2.600])

AXI3_2.WcMap = np.array([[[6.656, 7.378, 8.080, 8.763, 9.423, 10.060, 10.673,
                           11.260, 11.820],
                          [9.491, 10.188, 10.860, 11.505, 12.122,
                              12.710, 13.268, 13.796, 14.293],
                          [11.897, 12.714, 13.487, 14.214, 14.893,
                              15.524, 16.105, 16.637, 17.120],
                          [14.089, 15.192, 16.204, 17.124, 17.948,
                              18.676, 19.309, 19.847, 20.292],
                          [16.714, 18.186, 19.490, 20.622, 21.579,
                              22.364, 22.981, 23.436, 23.738],
                          [18.858, 21.035, 22.884, 24.398, 25.579,
                              26.436, 26.987, 27.254, 27.290],
                          [22.503, 24.231, 25.678, 26.847, 27.744,
                              28.379, 28.768, 28.930, 28.937],
                          [27.711, 28.362, 28.914, 29.368, 29.729,
                              30.000, 30.184, 30.286, 30.312],
                          [29.904, 30.161, 30.384, 30.572, 30.727,
                              30.850, 30.941, 31.002, 31.033],
                          [30.985, 31.102, 31.204, 31.291, 31.363, 31.421,
                           31.465, 31.495, 31.512]],
                         [[10.501, 11.535, 12.510, 13.422, 14.269, 15.048,
                           15.758, 16.398, 16.967],
                          [15.757, 16.712, 17.588, 18.381, 19.093,
                              19.722, 20.270, 20.737, 21.126],
                          [18.067, 19.097, 20.022, 20.840, 21.553,
                              22.161, 22.666, 23.072, 23.381],
                          [19.344, 20.666, 21.825, 22.818, 23.648,
                              24.318, 24.833, 25.199, 25.425],
                          [20.464, 22.123, 23.542, 24.720, 25.661,
                              26.370, 26.859, 27.142, 27.235],
                          [21.010, 23.199, 25.025, 26.483, 27.581,
                              28.334, 28.764, 28.898, 28.898],
                          [23.582, 25.289, 26.704, 27.830, 28.674,
                              29.249, 29.575, 29.669, 29.669],
                          [27.711, 28.362, 28.914, 29.368, 29.729,
                              30.000, 30.184, 30.286, 30.312],
                          [29.904, 30.161, 30.384, 30.572, 30.727,
                              30.850, 30.941, 31.002, 31.033],
                          [30.985, 31.102, 31.204, 31.291, 31.363, 31.421, 31.465, 31.495, 31.512]]])

AXI3_2.effMap = np.array([[[.6351, .6886, .7311, .7604, .7732, .7656, .7301, .6566, .5323],
                           [.6976, .7385, .7706, .7924, .8017, .7961, .7710, .7203, .6373],
                           [.7060, .7522, .7890, .8149, .8276, .8243, .8001, .7484, .6620],
                           [.6777, .7390, .7891, .8257, .8458, .8455, .8181, .7540, .6423],
                           [.6433, .7197, .7828, .8299, .8572, .8601, .8299, .7548, .6202],
                           [.5603, .6639, .7506, .8167, .8568, .8639, .8252, .7220, .5303],
                           [.6258, .7084, .7766, .8276, .8576, .8619, .8317, .7553, .6187],
                           [.7730, .8037, .8276, .8442, .8523, .8510, .8382, .8115, .7689],
                           [.8181, .8289, .8367, .8414, .8427, .8404, .8337, .8223, .8055],
                           [.8238, .8280, .8307, .8318, .8312, .8289, .8246, .8180, .8091]],
                          [[.6421, .7081, .7620, .8011, .8220, .8199, .7862, .7088, .5724],
                           [.7200, .7689, .8083, .8365, .8515, .8505, .8290, .7807, .6989],
                           [.7234, .7737, .8143, .8436, .8595, .8595, .8390, .7920, .7124],
                           [.6836, .7479, .8005, .8391, .8612, .8630, .8383, .7787, .6749],
                           [.6399, .7185, .7834, .8318, .8601, .8639, .8346, .7611, .6298],
                           [.5576, .6616, .7486, .8147, .8548, .8619, .8237, .7222, .5347],
                           [.6217, .7040, .7719, .8225, .8521, .8560, .8257, .7496, .6143],
                           [.7730, .8037, .8276, .8442, .8523, .8510, .8382, .8115, .7689],
                           [.8181, .8289, .8367, .8414, .8427, .8404, .8337, .8223, .8055],
                           [.8238, .8280, .8307, .8318, .8312, .8289, .8246, .8180, .8091]]])

AXI3_2.PRmap = np.array([[[1.2111, 1.2157, 1.2145, 1.2078, 1.1954, 1.1775, 1.1539, 1.1246, 1.0898],
                          [1.3489, 1.3505, 1.3454, 1.3336, 1.3153,
                              1.2907, 1.2596, 1.2219, 1.1781],
                          [1.5300, 1.5360, 1.5306, 1.5139, 1.4861,
                              1.4477, 1.3986, 1.3389, 1.2696],
                          [1.7787, 1.8068, 1.8112, 1.7918, 1.7493,
                              1.6847, 1.5984, 1.4916, 1.3678],
                          [2.1243, 2.2036, 2.2368, 2.2224, 2.1611,
                              2.0556, 1.9080, 1.7227, 1.5092],
                          [2.4235, 2.6404, 2.7664, 2.7917, 2.7142,
                              2.5400, 2.2769, 1.9416, 1.5639],
                          [2.8688, 3.0534, 3.1474, 3.1445, 3.0451,
                              2.8555, 2.5827, 2.2406, 1.8550],
                          [3.5470, 3.5566, 3.5254, 3.4543, 3.3449,
                              3.2000, 3.0207, 2.8093, 2.5717],
                          [3.7752, 3.7298, 3.6683, 3.5912, 3.4994,
                              3.3935, 3.2737, 3.1402, 2.9944],
                          [3.8744, 3.8211, 3.7601, 3.6915, 3.6159, 3.5334, 3.4440, 3.3476, 3.2447]],
                         [[1.4770, 1.4966, 1.5005, 1.4884, 1.4607, 1.4180, 1.3603, 1.2879, 1.2028],
                          [1.9042, 1.9205, 1.9158, 1.8903, 1.8445,
                              1.7795, 1.6956, 1.5935, 1.4760],
                          [2.1812, 2.2081, 2.2062, 2.1756, 2.1170,
                              2.0322, 1.9216, 1.7871, 1.6327],
                          [2.3966, 2.4656, 2.4877, 2.4620, 2.3896,
                              2.2735, 2.1155, 1.9199, 1.6959],
                          [2.5861, 2.7183, 2.7803, 2.7686, 2.6839,
                              2.5309, 2.3141, 2.0425, 1.7336],
                          [2.6763, 2.9474, 3.1087, 3.1461, 3.0564,
                              2.8474, 2.5297, 2.1261, 1.6760],
                          [3.0338, 3.2416, 3.3490, 3.3485, 3.2401,
                              3.0314, 2.7305, 2.3538, 1.9309],
                          [3.5470, 3.5566, 3.5254, 3.4543, 3.3449,
                              3.2000, 3.0207, 2.8093, 2.5717],
                          [3.7752, 3.7298, 3.6683, 3.5912, 3.4994,
                              3.3935, 3.2737, 3.1402, 2.9944],
                          [3.8744, 3.8211, 3.7601, 3.6915, 3.6159, 3.5334, 3.4440, 3.3476, 3.2447]]])


AXI3_2.units = {}
AXI3_2.units['NcMap'] = 'rpm'
AXI3_2.units['WcMap'] = 'lbm/s'

AXI3_2.Npts = AXI3_2.NcMap.size

# format for new regular grid interpolator:

AXI3_2.param_data = []
AXI3_2.output_data = []

AXI3_2.param_data.append({'name': 'alphaMap', 'values': AXI3_2.alphaMap,
                          'default': 0, 'units': None})
AXI3_2.param_data.append({'name': 'NcMap', 'values': AXI3_2.NcMap,
                          'default': 1.0, 'units': 'rpm'})
AXI3_2.param_data.append({'name': 'RlineMap', 'values': AXI3_2.RlineMap,
                          'default': 2.0, 'units': None})

AXI3_2.output_data.append({'name': 'WcMap', 'values': AXI3_2.WcMap,
                           'default': np.mean(AXI3_2.WcMap), 'units': 'lbm/s'})
AXI3_2.output_data.append({'name': 'effMap', 'values': AXI3_2.effMap,
                           'default': np.mean(AXI3_2.effMap), 'units': None})
AXI3_2.output_data.append({'name': 'PRmap', 'values': AXI3_2.PRmap,
                           'default': np.mean(AXI3_2.PRmap), 'units': None})
