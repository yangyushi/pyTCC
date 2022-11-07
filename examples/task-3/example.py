import sys
sys.path.insert(0, "../../src")
import tcc
import numpy as np


"""
Generate ideal gas (random points)
Different frames may have different numbers
"""
n_frame = 10
configurations = []
for f in range(n_frame):
    num = np.random.randint(1000, 1500)
    coord = np.random.uniform(0, 20, (num, 3))
    configurations.append(coord)

"""
Find clusters in the gas
"""
otf = tcc.OTF()
box = [20, 20, 20]
otf.clusters_to_analyse = ['sp3a', 'sp4a', 'sp4b', 'sp4c']

otf(
    configurations, box,
    # TCC parameters
    rcutAA=1.8, clusts=False, raw=False,
    PBCs=True, analyse_all_clusters=False,
)


"""
Print the populations
"""
population = otf.population
print(population)
