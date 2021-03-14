"""
Implementation of randomized hill climbing, simulated annealing, and genetic algorithm to
find optimal weights to a neural network that is classifying abalone as having either fewer
or more than 15 rings.

Based on AbaloneTest.java by Hannah Lau
"""
from __future__ import with_statement
import os
import csv
import time
import random
import sys
sys.path.append("C:\Users\Rina\Documents\ML 7641\ABAGAIL-master\jython\ABAGAIL.jar")



from func.nn.backprop import BackPropagationNetworkFactory
from func.nn import OptNetworkBuilder
from shared import SumOfSquaresError, DataSet, Instance
from opt.example import NeuralNetworkOptimizationProblem

import opt.RandomizedHillClimbing as RandomizedHillClimbing
import dist.Distribution as Distribution
import util.ABAGAILArrays as ABAGAILArrays


Distribution.random.setSeed(26)
ABAGAILArrays.random.setSeed(26)
random.seed(26)

INPUT_FILE = os.path.join("spambase.data")

INPUT_LAYER = 40
HIDDEN_LAYER = 50
OUTPUT_LAYER = 1
TRAINING_ITERATIONS = 5000


def initialize_instances():
    """Read the abalone.txt CSV data into a list of instances."""
    instances = []

    # Read in the abalone.txt CSV file
    with open(INPUT_FILE, "r") as abalone:
        reader = csv.reader(abalone)

        for row in reader:
            instance = Instance([float(value) for value in row[:-18]])
            # instance.setLabel(Instance(0 if float(row[-1]) < 15 else 1))
            instance.setLabel(Instance(int(row[-1])))

            instances.append(instance)

    return instances


def train(oa, network, oaName, instances, measure, testing):
    """Train a given network on a set of instances.

    :param OptimizationAlgorithm oa:
    :param BackPropagationNetwork network:
    :param str oaName:
    :param list[Instance] instances:
    :param AbstractErrorMeasure measure:
    """
    print "\nError results for %s\n---------------------------" % (oaName,)

    FILE_NAME = oaName + ".csv"
    OUTPUT_FILE = os.path.join(FILE_NAME)
    with open(OUTPUT_FILE, "wb") as results:
        writer = csv.writer(results, delimiter=',')

        writer.writerow(["Train Error", "Test Error", "Training Time", "Query Time",
                         "Train Percentage Correct",
                         "Test Percentage Correct",
                         "Train Correct", "Train Incorrect", "Test Correct", "Test Incorrect"])



        total_time = 0
        for iteration in xrange(TRAINING_ITERATIONS):

            train_correct = 0
            train_incorrect = 0

            test_correct = 0
            test_incorrect = 0

            start = time.time()
            oa.train()
            end = time.time()

            total_time += (end-start)

            start = time.time()
            error = 0.00
            for instance in instances:
                network.setInputValues(instance.getData())
                network.run()

                output = instance.getLabel()
                output_values = network.getOutputValues()
                example = Instance(output_values, Instance(output_values.get(0)))
                error += measure.value(output, example)

                actual = instance.getLabel().getContinuous()
                predicted = network.getOutputValues().get(0)

                if abs(predicted - actual) < 0.5:
                    train_correct += 1
                else:
                    train_incorrect += 1

            end = time.time()

            query_time = (end - start)

            test_error = 0.00
            for instance in testing:
                network.setInputValues(instance.getData())
                network.run()

                output = instance.getLabel()
                output_values = network.getOutputValues()
                example = Instance(output_values, Instance(output_values.get(0)))
                test_error += measure.value(output, example)

                actual = instance.getLabel().getContinuous()
                predicted = network.getOutputValues().get(0)

                if abs(predicted - actual) < 0.5:
                    test_correct += 1
                else:
                    test_incorrect += 1

            writer.writerow([error / len(instances), test_error/ len(testing), total_time, query_time,
                             float(train_correct) / (train_correct + train_incorrect) * 100.0,
                             float(test_correct) / (test_correct + test_incorrect) * 100.0,
                             train_correct, train_incorrect, test_correct, test_incorrect])



def main():
    """Run algorithms on the abalone dataset."""
    instances = initialize_instances()
    instances = instances[:-975]

    random.shuffle(instances)

    #from https://stackoverflow.com/questions/13423759/percent-list-slicing
    training = instances[ : int(len(instances) * .70)]
    testing = instances[ int(len(instances) * .70) : ]


    factory = BackPropagationNetworkFactory()
    measure = SumOfSquaresError()
    # data_set = DataSet(instances)
    data_set = DataSet(training)

    networks = []  # BackPropagationNetwork
    nnop = []  # NeuralNetworkOptimizationProblem
    oa = []  # OptimizationAlgorithm
    oa_names = ["RHC"]
    results = ""

    for name in oa_names:
        classification_network = factory.createClassificationNetwork([INPUT_LAYER, HIDDEN_LAYER, OUTPUT_LAYER])
        networks.append(classification_network)
        nnop.append(NeuralNetworkOptimizationProblem(data_set, classification_network, measure))

    oa.append(RandomizedHillClimbing( nnop[0]))



    for i, name in enumerate(oa_names):
        start = time.time()
        train_correct = 0
        train_incorrect = 0

        test_correct = 0
        test_incorrect = 0

        # train(oa[i], networks[i], oa_names[i], instances, measure)
        train(oa[i], networks[i], oa_names[i], training, measure, testing)
        end = time.time()
        training_time = end - start

        optimal_instance = oa[i].getOptimal()
        networks[i].setWeights(optimal_instance.getData())

        start = time.time()
        for instance in training:
            networks[i].setInputValues(instance.getData())
            networks[i].run()

            actual = instance.getLabel().getContinuous()
            predicted = networks[i].getOutputValues().get(0)

            if abs(predicted - actual) < 0.5:
                train_correct += 1
            else:
                train_incorrect += 1

        end = time.time()
        training_query_time = end - start

        start = time.time()
        for instance in testing:
            networks[i].setInputValues(instance.getData())
            networks[i].run()

            actual = instance.getLabel().getContinuous()
            predicted = networks[i].getOutputValues().get(0)

            if abs(predicted - actual) < 0.5:
                test_correct += 1
            else:
                test_incorrect += 1
        end = time.time()
        testing_time = end - start


        results += "\nTraining Results for %s: \nCorrectly classified %d instances." % (name, train_correct)
        results += "\nTraining Incorrectly classified %d instances.\nPercent correctly classified: %0.03f%%" % (
        train_incorrect, float(train_correct) / (train_correct + train_incorrect) * 100.0)
        results += "\nTraining time: %0.03f seconds" % (training_time,)
        results += "\nTraining Query time: %0.03f seconds\n" % (training_query_time,)

        results += "\n\nTesting Results for %s: \nCorrectly classified %d instances." % (name, test_correct)
        results += "\nTesting Incorrectly classified %d instances.\nPercent correctly classified: %0.03f%%" % (
            train_incorrect, float(test_correct) / (test_correct + test_incorrect) * 100.0)
        results += "\nTesting Query time: %0.03f seconds\n" % (testing_time,)

    print results


if __name__ == "__main__":
    main()

