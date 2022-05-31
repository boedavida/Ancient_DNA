"""
This code was inspired by the report on a fossil named "Oase1" in the reference 
Fu, Q., et. al. The Genetic History of Ice Age Europe. Nature, May 2016. Oase1 
is a modern human fossil mandible (jaw bone) found in Peştera cu Oase, Romania 
that is dated at 37,000–42,000 years old, which is at a time in which modern humans 
and Neanderthals overlapped in Europe near the times of both the first appearance 
of modern humans in Europe and the end of the time range of Neanderthals. Oase1 was 
a modern human but had a high percentage of Neanderthal DNA, about 10% of the genome. 
It is fascinating that a human fossil was found that had such recent Neanderthal 
ancestry. This code--either the Python file or the Jupyter notebook--estimates the 
number of generations that Oase1 was from a direct Neanderthal ancestor. By changing 
the values of the variables, this code can be used similarly for other ancient human 
fossils with Neanderthal ancestry. 
"""

# Data input. Data source is Fu, Q., et. al. The Genetic History of Ice Age Europe. Nature, May 2016.
fossil_name = "Oase1"  # 37,000–42,000-year-old modern human fossil from Peştera cu Oase, Romania
fossil_percNeander = 0.099
fossil_percNeander_err = 0.015
modHumPop_avePercNeander = 0.05

# Begin computation
# First generation: Offspring of mating between a Neanderthal and modern human
numGen = 1
percNeanderthal = 1 / 2 + modHumPop_avePercNeander / 2
print(f"Proportion of Neanderthal ancestry in offspring of mating between a modern human and a Neanderthal = {percNeanderthal*100:.2f}%")

# Subsequent generations with mating between descendant of previous generation and a modern human
# Compute the lower bound
while percNeanderthal > (fossil_percNeander + fossil_percNeander_err):
    numGen += 1
    percNeanderthal = percNeanderthal / 2 + modHumPop_avePercNeander / 2
    print(f'Proportion of Neanderthal ancestry in the next generation = {percNeanderthal*100:.2f}%')
lowerBound = numGen

# Compute the upper bound
while percNeanderthal > (fossil_percNeander - fossil_percNeander_err):
    numGen += 1
    percNeanderthal = percNeanderthal / 2 + modHumPop_avePercNeander / 2
    print(f'Proportion of Neanderthal ancestry in the next generation = {percNeanderthal*100:.2f}%')
upperBound = numGen

# Output final result
if lowerBound == 1 and upperBound == 1:
    print(f"\n{fossil_name}'s Neanderthal ancestor was {numGen} generation earlier")
elif lowerBound != 1 and upperBound != 1 and lowerBound == upperBound:
    print(f"\n{fossil_name}'s Neanderthal ancestor was {numGen} generations earlier")
else:
    print(f"\n{fossil_name}'s Neanderthal ancestor was from {lowerBound} to {upperBound} generations earlier\n")

