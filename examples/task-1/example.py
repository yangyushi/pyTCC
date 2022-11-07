import sys
sys.path.insert(0, "../../src")
import tcc


"""
Specifying the tcc output folder for analysis
"""
parser = tcc.Parser("tcc-output")


"""
Parsing the output and print the population
"""
parser.parse()
population = parser.population
print(population)

