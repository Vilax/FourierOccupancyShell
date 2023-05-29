import numpy as np

def loadDirections():
    return np.array([[0, 0],
                   [5.65487, 1.10715],
                   [0.628319, 1.10715],
                   [3.14159, 1.10715],
                   [4.39823, 1.10715],
                   [1.88496, 1.10715],
                   [5.65487, 0.553575],
                   [0.628319, 0.553575],
                   [0, 1.01722],
                   [5.02655, 1.01722],
                   [5.96903, 1.5708],
                   [5.34071, 1.5708],
                   [1.25664, 1.01722],
                   [0.314159, 1.5708],
                   [0.942478, 1.5708],
                   [1.5708, 1.5708],
                   [3.76991, 1.01721],
                   [2.51327, 1.01721],
                   [3.14159, 0.553584],
                   [4.39823, 0.553584],
                   [1.88496, 0.553584],
                   [6.04558, 0.761782],
                   [1.01903, 0.761782],
                   [4.78894, 0.761782],
                   [0, 1.5708],
                   [1.25664, 1.5708],
                   [5.02655, 1.5708],
                   [3.93977, 1.29076],
                   [2.68313, 1.29076],
                   [3.76991, 0.463647],
                   [2.51327, 0.463647],
                   [0, 0.463648],
                   [1.25664, 0.463648],
                   [5.02655, 0.463648],
                   [6.11332, 1.29076],
                   [1.08678, 1.29076],
                   [4.85669, 1.29076],
                   [3.60005, 1.29076],
                   [2.34341, 1.29076],
                   [3.53231, 0.761784],
                   [2.27567, 0.761784],
                   [0.237606, 0.761782],
                   [1.49424, 0.761782],
                   [5.26415, 0.761782],
                   [0.169861, 1.29076],
                   [1.4265, 1.29076],
                   [5.19641, 1.29076],
                   [0.628319, 1.5708],
                   [5.65487, 1.5708],
                   [4.00752, 0.761784],
                   [2.75088, 0.761784],
                   [5.65487, 0.276787],
                   [0.628319, 0.276787],
                   [5.96088, 1.04058],
                   [5.34886, 1.04058],
                   [5.82077, 1.3362],
                   [5.48896, 1.3362],
                   [0.934327, 1.04058],
                   [0.462413, 1.3362],
                   [0.794224, 1.3362],
                   [3.4476, 1.04058],
                   [2.83558, 1.04058],
                   [3.14159, 0.830358],
                   [4.70424, 1.04058],
                   [4.39823, 0.830358],
                   [1.88496, 0.830358],
                   [5.65487, 0.830361],
                   [0.628319, 0.830361],
                   [0.32231, 1.04058],
                   [2.97569, 1.33619],
                   [2.05086, 1.33619],
                   [3.3075, 1.33619],
                   [4.23232, 1.33619],
                   [4.56414, 1.33619],
                   [1.71905, 1.33619],
                   [4.09222, 1.04058],
                   [2.19096, 1.04058],
                   [3.14159, 0.276792],
                   [4.39823, 0.276792],
                   [1.57895, 1.04058],
                   [1.88496, 0.276792],
                   [0, 0.747561],
                   [1.25664, 0.747561],
                   [5.02655, 0.747561],
                   [0.08324, 1.43028],
                   [1.33988, 1.43028],
                   [5.10979, 1.43028],
                   [3.85315, 1.43028],
                   [2.59651, 1.43028],
                   [3.91421, 0.609539],
                   [2.65757, 0.609539],
                   [0.235874, 0.354602],
                   [1.49251, 0.354602],
                   [5.26242, 0.354602],
                   [6.04122, 1.16462],
                   [1.01467, 1.16462],
                   [4.78458, 1.16462],
                   [3.45289, 1.31083],
                   [4.70953, 1.31083],
                   [2.19626, 1.31083],
                   [3.48525, 0.900747],
                   [2.22861, 0.900747],
                   [5.84358, 0.786482],
                   [0.81703, 0.786482],
                   [3.05979, 1.45309],
                   [4.31643, 1.45309],
                   [1.80316, 1.45309],
                   [4.01188, 1.16462],
                   [2.75524, 1.16462],
                   [3.53404, 0.354599],
                   [2.2774, 0.354599],
                   [0.284665, 0.900749],
                   [1.5413, 0.900749],
                   [5.31121, 0.900749],
                   [0.317018, 1.31082],
                   [5.34357, 1.31082],
                   [0.710117, 1.45309],
                   [5.73667, 1.45309],
                   [4.20952, 0.78648],
                   [1.69624, 0.78648],
                   [2.95288, 0.78648],
                   [6.13889, 0.609544],
                   [1.11234, 0.609544],
                   [4.88225, 0.609544],
                   [6.19995, 1.43028],
                   [1.1734, 1.43028],
                   [4.94331, 1.43028],
                   [3.76991, 1.28688],
                   [2.51327, 1.28688],
                   [3.62561, 0.609539],
                   [2.36898, 0.609539],
                   [6.04731, 0.354602],
                   [1.02076, 0.354602],
                   [4.79067, 0.354602],
                   [5.96617, 1.31082],
                   [0.939619, 1.31082],
                   [3.52794, 1.16462],
                   [2.27131, 1.16462],
                   [3.3303, 0.78648],
                   [4.58694, 0.78648],
                   [2.07367, 0.78648],
                   [5.99852, 0.900749],
                   [0.971972, 0.900749],
                   [4.74188, 0.900749],
                   [3.22339, 1.45309],
                   [4.48003, 1.45309],
                   [1.96675, 1.45309],
                   [4.08693, 1.31083],
                   [1.57366, 1.31083],
                   [2.83029, 1.31083],
                   [4.00579, 0.354599],
                   [2.74915, 0.354599],
                   [0.439607, 0.786482],
                   [5.46615, 0.786482],
                   [0.241967, 1.16462],
                   [1.4986, 1.16462],
                   [5.26852, 1.16462],
                   [0.54652, 1.45309],
                   [5.57307, 1.45309],
                   [4.05458, 0.900747],
                   [2.79794, 0.900747],
                   [0.144299, 0.609544],
                   [1.40094, 0.609544],
                   [5.17085, 0.609544],
                   [0, 1.28688],
                   [1.25664, 1.28688],
                   [5.02655, 1.28688],
                   [3.68667, 1.43028],
                   [2.43003, 1.43028],
                   [3.76991, 0.747559],
                   [2.51327, 0.747559],
                   [0, 0.225901],
                   [1.25664, 0.225901],
                   [5.02655, 0.225901],
                   [5.88662, 1.18754],
                   [0.860074, 1.18754],
                   [3.37335, 1.18754],
                   [4.62998, 1.18754],
                   [2.11671, 1.18754],
                   [3.30659, 0.929877],
                   [4.56323, 0.929877],
                   [2.04995, 0.929877],
                   [5.81987, 0.929882],
                   [0.793317, 0.929882],
                   [3.14159, 1.33305],
                   [4.39823, 1.33305],
                   [1.88496, 1.33305],
                   [4.16647, 1.18754],
                   [1.6532, 1.18754],
                   [2.90984, 1.18754],
                   [3.76991, 0.225898],
                   [2.51327, 0.225898],
                   [0.46332, 0.929882],
                   [5.48987, 0.929882],
                   [0.396563, 1.18754],
                   [5.42311, 1.18754],
                   [0.628319, 1.33305],
                   [5.65487, 1.33305],
                   [4.23323, 0.929877],
                   [1.71996, 0.929877],
                   [2.97659, 0.929877],
                   [5.87698, 0.648584],
                   [0.850436, 0.648584],
                   [6.12611, 1.5708],
                   [1.09956, 1.5708],
                   [4.86947, 1.5708],
                   [3.86003, 1.15265],
                   [2.60339, 1.15265],
                   [3.42954, 0.487697],
                   [4.68617, 0.487697],
                   [2.1729, 0.487697],
                   [5.94281, 0.487696],
                   [0.916263, 0.487696],
                   [6.03974, 1.43042],
                   [1.01319, 1.43042],
                   [4.7831, 1.43042],
                   [3.67979, 1.15265],
                   [2.42316, 1.15265],
                   [3.36371, 0.648582],
                   [4.62035, 0.648582],
                   [2.10707, 0.648582],
                   [0.106374, 0.886078],
                   [1.36301, 0.886078],
                   [5.13292, 0.886078],
                   [0.243446, 1.43042],
                   [1.50008, 1.43042],
                   [5.26999, 1.43042],
                   [0.785398, 1.5708],
                   [5.81195, 1.5708],
                   [4.17611, 0.648582],
                   [1.66284, 0.648582],
                   [2.91948, 0.648582],
                   [5.65487, 0.138394],
                   [0.628319, 0.138394],
                   [5.80509, 1.06893],
                   [5.50465, 1.06893],
                   [5.7413, 1.22057],
                   [5.56843, 1.22057],
                   [0.778537, 1.06893],
                   [0.541885, 1.22057],
                   [0.714752, 1.22057],
                   [3.29181, 1.06893],
                   [2.99137, 1.06893],
                   [3.14159, 0.968762],
                   [4.54845, 1.06893],
                   [4.39823, 0.968762],
                   [1.88496, 0.968762],
                   [5.65487, 0.691967],
                   [0.628319, 0.691967],
                   [0.162298, 1.02312],
                   [4.86425, 1.02312],
                   [2.90053, 1.45318],
                   [2.12602, 1.45318],
                   [1.41894, 1.02312],
                   [3.38266, 1.45318],
                   [4.15717, 1.45318],
                   [4.63929, 1.45318],
                   [1.64389, 1.45318],
                   [3.93221, 1.02313],
                   [2.35098, 1.02313],
                   [3.14159, 0.415179],
                   [4.39823, 0.415179],
                   [1.88496, 0.415179],
                   [6.17681, 0.886078],
                   [1.15026, 0.886078],
                   [4.92017, 0.886078],
                   [0.15708, 1.5708],
                   [1.41372, 1.5708],
                   [5.18363, 1.5708],
                   [4.01336, 1.43042],
                   [2.75672, 1.43042],
                   [4.11029, 0.487697],
                   [1.59701, 0.487697],
                   [2.85365, 0.487697],
                   [0.340374, 0.487696],
                   [5.36692, 0.487696],
                   [6.19307, 1.15266],
                   [1.16652, 1.15266],
                   [4.93643, 1.15266],
                   [3.52647, 1.43042],
                   [2.26983, 1.43042],
                   [3.66354, 0.886069],
                   [2.4069, 0.886069],
                   [0.406201, 0.648584],
                   [5.43275, 0.648584],
                   [0.0901183, 1.15266],
                   [1.34676, 1.15266],
                   [5.11667, 1.15266],
                   [0.471239, 1.5708],
                   [5.49779, 1.5708],
                   [3.87629, 0.886069],
                   [2.61965, 0.886069],
                   [5.65487, 0.415181],
                   [0.628319, 0.415181],
                   [6.12089, 1.02312],
                   [5.18885, 1.02312],
                   [5.89593, 1.45318],
                   [5.4138, 1.45318],
                   [1.09434, 1.02312],
                   [0.387255, 1.45318],
                   [0.869382, 1.45318],
                   [3.60761, 1.02313],
                   [2.67557, 1.02313],
                   [3.14159, 0.691971],
                   [4.39823, 0.691971],
                   [1.88496, 0.691971],
                   [5.65487, 0.968755],
                   [0.628319, 0.968755],
                   [0.4781, 1.06893],
                   [3.05516, 1.22056],
                   [1.97139, 1.22056],
                   [3.22803, 1.22056],
                   [4.3118, 1.22056],
                   [4.48466, 1.22056],
                   [1.79852, 1.22056],
                   [4.24801, 1.06893],
                   [2.03517, 1.06893],
                   [3.14159, 0.138387],
                   [4.39823, 0.138387],
                   [1.73474, 1.06893],
                   [1.88496, 0.138387]])