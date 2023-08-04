import random
import numpy as np

# Function to Optimize
def oneMax(chromosome):
    score = chromosome.sum(axis=1)
    return score

# Fitness Function: How Good is the chromosome to the Fitness Function
def fitness(chromosome):
    score = oneMax(chromosome)
    return score

def initialPopulation(initialSOlutions):
    solutions = np.random.uniform(low=0, high=1.0, size=(initialSOlutions,5))
    return solutions

def evaluatePopulation(solutions):
    populationsScore = fitness(solutions).reshape(-1, 1)
    populationsScore = np.append(solutions, populationsScore, axis=1)
    return populationsScore

def sortPopulation(populationsScore):
    sorted_indices = np.argsort(populationsScore[:, -1])[::-1]
    populationsScore = populationsScore[sorted_indices]
    return populationsScore

def geneticSelection(selectBest, populationsScore):
    selectedSolutions = populationsScore[:selectBest]
    return selectedSolutions

def geneticCrossOver(selectedSolutions, offspringsCount):
    selectedSolutions = selectedSolutions[:,:-1]
    offsprings = np.apply_along_axis(np.random.choice, axis=0, arr=selectedSolutions, replace=True, size=offspringsCount)
    return offsprings

def geneticMutation(offsprings):
    offsprings = offsprings + np.random.random(size=offsprings.shape)*0.01 
    return offsprings

def nextGenerations(numberOfGenerations, selectBest,  populationsScore, offspringsCount):
    for generation in range(numberOfGenerations):
        print(f'=== Gen {generation} Best Solution ===')
        print(populationsScore[0])
        selectedSolutions = geneticSelection(selectBest, populationsScore)
        offsprings = geneticCrossOver(selectedSolutions, offspringsCount)
        offsprings = geneticMutation(offsprings)
        solutions = np.append(selectedSolutions[:,:-1], offsprings, axis=0)
        populationsScore = evaluatePopulation(solutions)
        populationsScore = sortPopulation(populationsScore)

    pass

if __name__=='__main__':
    np.random.seed(42)
    initialSOlutions = 500
    selectBest = 10
    numberOfGenerations = 200
    offspringsCount = 5
    solutions = initialPopulation(initialSOlutions)
    populationsScore = evaluatePopulation(solutions)
    populationsScore = sortPopulation(populationsScore)
    nextGenerations(numberOfGenerations, selectBest,  populationsScore, offspringsCount)



