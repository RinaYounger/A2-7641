# traveling salesman algorithm implementation in jython
# This also prints the index of the points of the shortest route.
# To make a plot of the route, write the points at these indexes
# to a file and plot them in your favorite tool.
import sys
import os
import time
sys.path.append("C:\Users\Rina\Documents\ML 7641\ABAGAIL-master\jython\ABAGAIL.jar")

import java.io.FileReader as FileReader
import java.io.File as File
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.util.Random as Random

import dist.DiscreteDependencyTree as DiscreteDependencyTree
import dist.DiscreteUniformDistribution as DiscreteUniformDistribution
import dist.Distribution as Distribution
import dist.DiscretePermutationDistribution as DiscretePermutationDistribution
import opt.DiscreteChangeOneNeighbor as DiscreteChangeOneNeighbor
import opt.EvaluationFunction as EvaluationFunction
import opt.GenericHillClimbingProblem as GenericHillClimbingProblem
import opt.HillClimbingProblem as HillClimbingProblem
import opt.NeighborFunction as NeighborFunction
import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.example.FourPeaksEvaluationFunction as FourPeaksEvaluationFunction
import opt.ga.CrossoverFunction as CrossoverFunction
import opt.ga.SingleCrossOver as SingleCrossOver
import opt.ga.DiscreteChangeOneMutation as DiscreteChangeOneMutation
import opt.ga.GenericGeneticAlgorithmProblem as GenericGeneticAlgorithmProblem
import opt.ga.GeneticAlgorithmProblem as GeneticAlgorithmProblem
import opt.ga.MutationFunction as MutationFunction
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm
import opt.ga.UniformCrossOver as UniformCrossOver
import opt.prob.GenericProbabilisticOptimizationProblem as GenericProbabilisticOptimizationProblem
import opt.prob.MIMIC as MIMIC
import opt.prob.ProbabilisticOptimizationProblem as ProbabilisticOptimizationProblem
import shared.FixedIterationTrainer as FixedIterationTrainer
import opt.example.TravelingSalesmanEvaluationFunction as TravelingSalesmanEvaluationFunction
import opt.example.TravelingSalesmanRouteEvaluationFunction as TravelingSalesmanRouteEvaluationFunction
import opt.SwapNeighbor as SwapNeighbor
import opt.ga.SwapMutation as SwapMutation
import opt.example.TravelingSalesmanCrossOver as TravelingSalesmanCrossOver
import opt.example.TravelingSalesmanSortEvaluationFunction as TravelingSalesmanSortEvaluationFunction
import shared.Instance as Instance
import util.ABAGAILArrays as ABAGAILArrays

from array import array
import shared.writer.CSVWriter as CSVWriter



import random as Rand
import dist.Distribution as Distribution
import util.ABAGAILArrays as ABAGAILArrays

# Random number generator */
random = Random()
random.setSeed(613)
Distribution.random.setSeed(613)
ABAGAILArrays.random.setSeed(613)
Rand.seed(613)

# set N value.  This is the number of points
N = 50


points = [[0 for x in xrange(2)] for x in xrange(N)]
for i in range(0, len(points)):
    points[i][0] = random.nextDouble()
    points[i][1] = random.nextDouble()




################################
#########TUNING TUNING
###Tuning should be run first - before running the other code in this file
# To achieve the same output as the report
####################################


#
# writer = CSVWriter("GA_TSP_Tuning rss.csv", ["run","param1", "param2", "param3", "1000 iter", "2000 iter", "3000 iter", "4000 iter", "5000 iter", "6000 iter", "7000 iter", "8000 iter", "9000 iter", "10000 iter"])
# writer.open()
#
#
# param1 = [100,100,200,200,50,50]
# param2 = [50,80,100,150,25,40]
# param3 = [10,10,10,10,2,2]
#
# for x in range (len(param1)):
#
#     for y in range(10):
#         writer.write(str(y+1))
#         writer.write(str(param1[x]))
#         writer.write(str(param2[x]))
#         writer.write(str(param3[x]))
#         ef = TravelingSalesmanRouteEvaluationFunction(points)
#         odd = DiscretePermutationDistribution(N)
#         nf = SwapNeighbor()
#         mf = SwapMutation()
#         cf = TravelingSalesmanCrossOver(ef)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#
#         ga = StandardGeneticAlgorithm(param1[x], param2[x], param3[x], gap)
#         fit = FixedIterationTrainer(ga, 1000)
#
#         for r in range(10):
#             fit.train()
#             val = ef.value(ga.getOptimal())
#             writer.write(str(val))
#
#         writer.nextRecord()
#     print("yay")
#
# writer.close()
#
#
#
# writer = CSVWriter("SA_TSP_Tuning rss.csv", ["run","param1", "param2", "1000 iter", "2000 iter", "3000 iter", "4000 iter", "5000 iter", "6000 iter", "7000 iter", "8000 iter", "9000 iter", "10000 iter"])
# writer.open()
#
#
# param1 = [1E11,1E11,1E11, 1E15, 1E15, 1E9, 1E9]
# param2 = [.5,.3,.95,.5,.95,.5,.95]
#
#
# for x in range (len(param1)):
#
#     for y in range(10):
#         writer.write(str(y+1))
#         writer.write(str(param1[x]))
#         writer.write(str(param2[x]))
#         ef = TravelingSalesmanRouteEvaluationFunction(points)
#         odd = DiscretePermutationDistribution(N)
#         nf = SwapNeighbor()
#         mf = SwapMutation()
#         cf = TravelingSalesmanCrossOver(ef)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#
#         sa = SimulatedAnnealing(param1[x],param2[x], hcp)
#         fit = FixedIterationTrainer(sa, 1000)
#
#         for r in range(10):
#             fit.train()
#             val = ef.value(sa.getOptimal())
#             writer.write(str(val))
#
#         writer.nextRecord()
#     print("yay")
#
# writer.close()
#
#
# writer = CSVWriter("MIMIC_TSP_Tuning rss.csv", ["run","param1", "param2", "1000 iter", "2000 iter", "3000 iter", "4000 iter", "5000 iter"])
# writer.open()
#
#
# param1 = [200,200,200,100,100,50,50]
# param2 = [50,100,150,50,90,25,40]
#
#
# for x in range (len(param1)):
#
#     for y in range(10):
#         writer.write(str(y+1))
#         writer.write(str(param1[x]))
#         writer.write(str(param2[x]))
#
#         ef = TravelingSalesmanRouteEvaluationFunction(points)
#         odd = DiscretePermutationDistribution(N)
#         nf = SwapNeighbor()
#         mf = SwapMutation()
#         cf = TravelingSalesmanCrossOver(ef)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#
#         # for mimic we use a sort encoding
#         ef = TravelingSalesmanSortEvaluationFunction(points)
#         fill = [N] * N
#         ranges = array('i', fill)
#         odd = DiscreteUniformDistribution(ranges)
#         df = DiscreteDependencyTree(.1, ranges)
#         pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#         mimic = MIMIC(param1[x], param2[x], pop)
#         fit = FixedIterationTrainer(mimic, 1000)
#
#         for r in range(5):
#             fit.train()
#             val = ef.value(mimic.getOptimal())
#             writer.write(str(val))
#
#         writer.nextRecord()
#     print("yay")
#
# writer.close()





################################
#########TUNING TUNING end
####################################




#########################
#####Run from this point on to see the results of the tuned algos
#####################

#
# for r in range (10):
#
#     writer = CSVWriter("RHC_TSP rss" + str(r+1) + ".csv", ["Iteration", "Score", "Time", "Evaluations"])
#     writer.open()
#
#     ef = TravelingSalesmanRouteEvaluationFunction(points)
#     odd = DiscretePermutationDistribution(N)
#     nf = SwapNeighbor()
#     mf = SwapMutation()
#     cf = TravelingSalesmanCrossOver(ef)
#     hcp = GenericHillClimbingProblem(ef, odd, nf)
#     gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#
#     rhc = RandomizedHillClimbing(hcp)
#     fit = FixedIterationTrainer(rhc, 100)
#
#     total_time = 0
#     c = 1
#     for x in range (100, 5000, 100):
#
#         writer.write(str(x))
#         start_time = time.time()
#         fit.train()
#         end_time = time.time()
#
#         total_time += (end_time-start_time)
#
#         val = ef.value(rhc.getOptimal())
#         writer.write(str(val))
#
#         writer.write(str(total_time))
#
#         writer.write(str(ef.getFunctionEvaluations()-c))
#         c+=1
#
#         writer.nextRecord()
#
#     writer.close()
#
# print("RHC")
#
#
# for r in range (10):
#
#     writer = CSVWriter("SA_TSP rss" + str(r+1) + ".csv", ["Iteration", "Score", "Time", "Evaluations"])
#     writer.open()
#
#     ef = TravelingSalesmanRouteEvaluationFunction(points)
#     odd = DiscretePermutationDistribution(N)
#     nf = SwapNeighbor()
#     mf = SwapMutation()
#     cf = TravelingSalesmanCrossOver(ef)
#     hcp = GenericHillClimbingProblem(ef, odd, nf)
#     gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#
#     sa = SimulatedAnnealing(1E11, .3, hcp)
#     fit = FixedIterationTrainer(sa, 100)
#     total_time = 0
#     c = 1
#     for x in range (100, 5000, 100):
#
#
#         writer.write(str(x))
#         start_time = time.time()
#         fit.train()
#         end_time = time.time()
#
#         total_time += (end_time-start_time)
#
#         val = ef.value(sa.getOptimal())
#         writer.write(str(val))
#
#         writer.write(str(total_time))
#
#         writer.write(str(ef.getFunctionEvaluations() - c))
#         c += 1
#
#         writer.nextRecord()
#
#     writer.close()
#
#
# print("SA")
# for r in range (10):
#
#     writer = CSVWriter("GA_TSP rss" + str(r+1) + ".csv", ["Iteration", "Score", "Time", "Evaluations"])
#     writer.open()
#
#     ef = TravelingSalesmanRouteEvaluationFunction(points)
#     odd = DiscretePermutationDistribution(N)
#     nf = SwapNeighbor()
#     mf = SwapMutation()
#     cf = TravelingSalesmanCrossOver(ef)
#     hcp = GenericHillClimbingProblem(ef, odd, nf)
#     gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#
#
#     ga = StandardGeneticAlgorithm(200, 100, 10, gap)
#     fit = FixedIterationTrainer(ga, 100)
#     total_time = 0
#     c = 1
#     for x in range (100, 5000, 100):
#
#
#         writer.write(str(x))
#         start_time = time.time()
#         fit.train()
#         end_time = time.time()
#
#         total_time += (end_time-start_time)
#
#         val = ef.value(ga.getOptimal())
#         writer.write(str(val))
#
#         writer.write(str(total_time))
#
#         writer.write(str(ef.getFunctionEvaluations() - c))
#         c += 1
#
#         writer.nextRecord()
#
#     writer.close()
#
#
# print("GA")
# for r in range (10):
#
#     writer = CSVWriter("MIMIC_TSP rss" + str(r+1) + ".csv", ["Iteration", "Score", "Time", "Evaluations"])
#     writer.open()
#
#     ef = TravelingSalesmanRouteEvaluationFunction(points)
#     odd = DiscretePermutationDistribution(N)
#     nf = SwapNeighbor()
#     mf = SwapMutation()
#     cf = TravelingSalesmanCrossOver(ef)
#     hcp = GenericHillClimbingProblem(ef, odd, nf)
#     gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#
#     # for mimic we use a sort encoding
#     ef = TravelingSalesmanSortEvaluationFunction(points)
#     fill = [N] * N
#     ranges = array('i', fill)
#     odd = DiscreteUniformDistribution(ranges)
#     df = DiscreteDependencyTree(.1, ranges)
#     pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#
#     mimic = MIMIC(200, 100, pop)
#     fit = FixedIterationTrainer(mimic, 100)
#     total_time = 0
#     c = 1
#     for x in range (100, 5000, 100):
#
#
#         writer.write(str(x))
#         start_time = time.time()
#         fit.train()
#         end_time = time.time()
#
#         total_time += (end_time-start_time)
#
#         val = ef.value(mimic.getOptimal())
#         writer.write(str(val))
#
#         writer.write(str(total_time))
#
#         writer.write(str(ef.getFunctionEvaluations() - c))
#         c += 1
#
#         writer.nextRecord()
#
#     writer.close()
#
#
# print("MIMIC")



#######################################
######################################
########################################




params = range(10,150,10)

for x in range (10):
    file = "Nodes_TSP rss" + str(x + 1) + ".csv"
    writer = CSVWriter(file, ["Num Nodes", "RHCScore", "SAScore", "GAScore", "MIMICScore", "RHCTime","SATime","GATime", "MIMICTime" ])
    writer.open()

    for r in params:

        writer.write(str(r))

        # set N value.  This is the number of points
        N = r
        random = Random()

        points = [[0 for x in xrange(2)] for x in xrange(N)]
        for i in range(0, len(points)):
            points[i][0] = random.nextDouble()
            points[i][1] = random.nextDouble()



        ef = TravelingSalesmanRouteEvaluationFunction(points)
        odd = DiscretePermutationDistribution(N)
        nf = SwapNeighbor()
        mf = SwapMutation()
        cf = TravelingSalesmanCrossOver(ef)
        hcp = GenericHillClimbingProblem(ef, odd, nf)
        gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)

        rhc = RandomizedHillClimbing(hcp)
        fit = FixedIterationTrainer(rhc, 1000)
        start_time = time.time()
        fit.train()
        end_time = time.time()
        rhc_time = end_time - start_time
        writer.write(str(ef.value(rhc.getOptimal())))


        ef = TravelingSalesmanRouteEvaluationFunction(points)
        odd = DiscretePermutationDistribution(N)
        nf = SwapNeighbor()
        mf = SwapMutation()
        cf = TravelingSalesmanCrossOver(ef)
        hcp = GenericHillClimbingProblem(ef, odd, nf)
        gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)

        sa = SimulatedAnnealing(1E11, .5, hcp)
        fit = FixedIterationTrainer(sa, 1000)
        start_time = time.time()
        fit.train()
        end_time = time.time()
        sa_time = end_time - start_time
        writer.write(str(ef.value(sa.getOptimal())))



        ef = TravelingSalesmanRouteEvaluationFunction(points)
        odd = DiscretePermutationDistribution(N)
        nf = SwapNeighbor()
        mf = SwapMutation()
        cf = TravelingSalesmanCrossOver(ef)
        hcp = GenericHillClimbingProblem(ef, odd, nf)
        gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)

        ga = StandardGeneticAlgorithm(200, 100, 10, gap)
        fit = FixedIterationTrainer(ga, 100)
        start_time = time.time()
        fit.train()
        end_time = time.time()
        ga_time = end_time - start_time
        writer.write(str(ef.value(ga.getOptimal())))


        ef = TravelingSalesmanRouteEvaluationFunction(points)
        odd = DiscretePermutationDistribution(N)
        nf = SwapNeighbor()
        mf = SwapMutation()
        cf = TravelingSalesmanCrossOver(ef)
        hcp = GenericHillClimbingProblem(ef, odd, nf)
        gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)

        # for mimic we use a sort encoding
        ef = TravelingSalesmanSortEvaluationFunction(points);
        fill = [N] * N
        ranges = array('i', fill)
        odd = DiscreteUniformDistribution(ranges);
        df = DiscreteDependencyTree(.1, ranges);
        pop = GenericProbabilisticOptimizationProblem(ef, odd, df);

        mimic = MIMIC(200, 100, pop)
        fit = FixedIterationTrainer(mimic, 100)
        start_time = time.time()
        fit.train()
        end_time = time.time()
        mimic_time = end_time - start_time
        writer.write(str(ef.value(mimic.getOptimal())))

        writer.write(str(rhc_time))
        writer.write(str(sa_time))
        writer.write(str(ga_time))
        writer.write(str(mimic_time))

        writer.nextRecord()

    writer.close()


