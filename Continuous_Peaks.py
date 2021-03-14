import sys
import os
import time
from time import clock
import random

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
import opt.example.ContinuousPeaksEvaluationFunction as ContinuousPeaksEvaluationFunction
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


N=60
T=N/10
fill = [2] * N
ranges = array('i', fill)


################################
#########TUNING TUNING
########Tuning code should not be run before the other code in this file to achieve the same reults
# as the report
####################################
#
#
# writer = CSVWriter("MIMIC_Peaks_Tuning rss.csv", ["run","param1", "param2", "1000 iter", "2000 iter", "3000 iter", "4000 iter", "5000 iter"])
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
#         ef = ContinuousPeaksEvaluationFunction(T)
#         odd = DiscreteUniformDistribution(ranges)
#         nf = DiscreteChangeOneNeighbor(ranges)
#         mf = DiscreteChangeOneMutation(ranges)
#         cf = SingleCrossOver()
#         df = DiscreteDependencyTree(.1, ranges)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
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
#         print("yay")
#
# writer.close()
#
#
#
# writer = CSVWriter("GA_Peaks_Tuning rss.csv", ["run","param1", "param2", "param3", "1000 iter", "2000 iter", "3000 iter", "4000 iter", "5000 iter", "6000 iter", "7000 iter", "8000 iter", "9000 iter", "10000 iter","6000 iter", "7000 iter", "8000 iter", "9000 iter", "10000 iter"])
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
#         ef = ContinuousPeaksEvaluationFunction(T)
#         odd = DiscreteUniformDistribution(ranges)
#         nf = DiscreteChangeOneNeighbor(ranges)
#         mf = DiscreteChangeOneMutation(ranges)
#         cf = SingleCrossOver()
#         df = DiscreteDependencyTree(.1, ranges)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#         pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#         ga = StandardGeneticAlgorithm(param1[x], param2[x], param3[x], gap)
#         fit = FixedIterationTrainer(ga, 1000)
#
#         for r in range(15):
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
# writer = CSVWriter("SA_Peaks_Tuning rss.csv", ["run","param1", "param2", "1000 iter", "2000 iter", "3000 iter", "4000 iter", "5000 iter", "6000 iter", "7000 iter", "8000 iter", "9000 iter", "10000 iter"])
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
#         ef = ContinuousPeaksEvaluationFunction(T)
#         odd = DiscreteUniformDistribution(ranges)
#         nf = DiscreteChangeOneNeighbor(ranges)
#         mf = DiscreteChangeOneMutation(ranges)
#         cf = SingleCrossOver()
#         df = DiscreteDependencyTree(.1, ranges)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#         pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
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
#
# ################################
# #########TUNING TUNING end
# ####################################

#
# #######################
# ##### Run after running tuning code
# ###################
# for r in range (10):
#
#     writer = CSVWriter("RHC_Peaks rss" + str(r+1) + ".csv", ["Iteration", "Score", "Time", "Evaluations"])
#     writer.open()
#
#     ef = ContinuousPeaksEvaluationFunction(T)
#     odd = DiscreteUniformDistribution(ranges)
#     nf = DiscreteChangeOneNeighbor(ranges)
#     mf = DiscreteChangeOneMutation(ranges)
#     cf = SingleCrossOver()
#     df = DiscreteDependencyTree(.1, ranges)
#     hcp = GenericHillClimbingProblem(ef, odd, nf)
#     gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#     pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#     rhc = RandomizedHillClimbing(hcp)
#     fit = FixedIterationTrainer(rhc, 100)
#
#     total_time = 0
#     c = 1
#     for x in range (100, 10000, 100):
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
#     writer = CSVWriter("SA_Peaks rss" + str(r+1) + ".csv", ["Iteration", "Score", "Time", "Evaluations"])
#     writer.open()
#
#     ef = ContinuousPeaksEvaluationFunction(T)
#     odd = DiscreteUniformDistribution(ranges)
#     nf = DiscreteChangeOneNeighbor(ranges)
#     mf = DiscreteChangeOneMutation(ranges)
#     cf = SingleCrossOver()
#     df = DiscreteDependencyTree(.1, ranges)
#     hcp = GenericHillClimbingProblem(ef, odd, nf)
#     gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#     pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#     sa = SimulatedAnnealing(1E9, .95, hcp)
#     fit = FixedIterationTrainer(sa, 100)
#     total_time = 0
#     c = 1
#     for x in range (100, 10000, 100):
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
#     writer = CSVWriter("GA_Peaks rss" + str(r+1) + ".csv", ["Iteration", "Score", "Time", "Evaluations"])
#     writer.open()
#
#     ef = ContinuousPeaksEvaluationFunction(T)
#     odd = DiscreteUniformDistribution(ranges)
#     nf = DiscreteChangeOneNeighbor(ranges)
#     mf = DiscreteChangeOneMutation(ranges)
#     cf = SingleCrossOver()
#     df = DiscreteDependencyTree(.1, ranges)
#     hcp = GenericHillClimbingProblem(ef, odd, nf)
#     gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#     pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#
#     ga = StandardGeneticAlgorithm(100, 80, 10, gap)
#     fit = FixedIterationTrainer(ga, 100)
#     total_time = 0
#     c = 1
#     for x in range (100, 10000, 100):
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
#     writer = CSVWriter("MIMIC_Peaks rss" + str(r+1) + ".csv", ["Iteration", "Score", "Time", "Evaluations"])
#     writer.open()
#
#     ef = ContinuousPeaksEvaluationFunction(T)
#     odd = DiscreteUniformDistribution(ranges)
#     nf = DiscreteChangeOneNeighbor(ranges)
#     mf = DiscreteChangeOneMutation(ranges)
#     cf = SingleCrossOver()
#     df = DiscreteDependencyTree(.1, ranges)
#     hcp = GenericHillClimbingProblem(ef, odd, nf)
#     gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#     pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#     mimic = MIMIC(200, 50, pop)
#     fit = FixedIterationTrainer(mimic, 100)
#     total_time = 0
#     c = 1
#     for x in range (100, 10000, 100):
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
#
#
#
# ######################################
# #####################################
# #######################################
#
#
#
#
#
# params = range(5,100, 5)
#
# for x in range (10):
#
#     file = "N_Peaks rss" + str(x+1) + ".csv"
#     writer = CSVWriter(file, ["N", "RHCScore", "SAScore", "GAScore", "MIMICScore", "RHCTime","SATime","GATime", "MIMICTime" ])
#     writer.open()
#
#
#     for r in params:
#         print(r)
#         writer.write(str(r))
#
#         N = r
#         T = N / 10
#         fill = [2] * N
#         ranges = array('i', fill)
#
#         ef = ContinuousPeaksEvaluationFunction(T)
#         odd = DiscreteUniformDistribution(ranges)
#         nf = DiscreteChangeOneNeighbor(ranges)
#         mf = DiscreteChangeOneMutation(ranges)
#         cf = SingleCrossOver()
#         df = DiscreteDependencyTree(.1, ranges)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#         pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#         rhc = RandomizedHillClimbing(hcp)
#         fit = FixedIterationTrainer(rhc, 5000)
#         start_time = time.time()
#         fit.train()
#         end_time = time.time()
#         rhc_time = end_time - start_time
#         writer.write(str(ef.value(rhc.getOptimal())))
#
#         ef = ContinuousPeaksEvaluationFunction(T)
#         odd = DiscreteUniformDistribution(ranges)
#         nf = DiscreteChangeOneNeighbor(ranges)
#         mf = DiscreteChangeOneMutation(ranges)
#         cf = SingleCrossOver()
#         df = DiscreteDependencyTree(.1, ranges)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#         pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#         sa = SimulatedAnnealing(1E9, .95, hcp)
#         fit = FixedIterationTrainer(sa,5000)
#         start_time = time.time()
#         fit.train()
#         end_time = time.time()
#         sa_time = end_time - start_time
#         writer.write(str(ef.value(sa.getOptimal())))
#
#         ef = ContinuousPeaksEvaluationFunction(T)
#         odd = DiscreteUniformDistribution(ranges)
#         nf = DiscreteChangeOneNeighbor(ranges)
#         mf = DiscreteChangeOneMutation(ranges)
#         cf = SingleCrossOver()
#         df = DiscreteDependencyTree(.1, ranges)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#         pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#         ga = StandardGeneticAlgorithm(100, 80, 10, gap)
#         fit = FixedIterationTrainer(ga, 5000)
#         start_time = time.time()
#         fit.train()
#         end_time = time.time()
#         ga_time = end_time - start_time
#         writer.write(str(ef.value(ga.getOptimal())))
#
#         ef = ContinuousPeaksEvaluationFunction(T)
#         odd = DiscreteUniformDistribution(ranges)
#         nf = DiscreteChangeOneNeighbor(ranges)
#         mf = DiscreteChangeOneMutation(ranges)
#         cf = SingleCrossOver()
#         df = DiscreteDependencyTree(.1, ranges)
#         hcp = GenericHillClimbingProblem(ef, odd, nf)
#         gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
#         pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
#
#         mimic = MIMIC(200, 50, pop)
#         fit = FixedIterationTrainer(mimic, 5000)
#         start_time = time.time()
#         fit.train()
#         end_time = time.time()
#         mimic_time = end_time - start_time
#         writer.write(str(ef.value(mimic.getOptimal())))
#
#         writer.write(str(rhc_time))
#         writer.write(str(sa_time))
#         writer.write(str(ga_time))
#         writer.write(str(mimic_time))
#
#         writer.nextRecord()
#
#     writer.close()