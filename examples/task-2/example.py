import sys
sys.path.insert(0, "../../src")
import tcc


"""
Specifying the folder for the tcc output as `tcc-output`
"""
parser = tcc.Parser("tcc-output")
parser.clear()  # remove existing folder named 'tcc-output'


"""
Setting parameters and execute TCC.
"""
parser.clusters_to_analyse = ['10B', 'FCC', 'HCP']
box = [10.02301606, 10.02301606, 10.02301606]

parser.run(
    "data.xyz", box=box,
    analyse_all_clusters=False,
    clusts=True, raw=True
)

"""
Parsing the output and print the population
"""
parser.parse()
population = parser.population
print(population)
