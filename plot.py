import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns; sns.set()





if __name__ == "__main__":

    ################################
    #KNAPSACK STUFF##
    #############################

    # data = np.genfromtxt("MIMIC_Knapsack_Tuning rss.csv", delimiter=",")
    #
    # # plt.figure(figsize=(9, 5))
    #
    # score = []
    # labels = []
    #
    # for x in range(1,71,10):
    #     scores = data[x:(x+10), -1]
    #
    #     new = np.mean(scores, axis=0)
    #     score.append(new)
    #     labels.append("P:" + str(str(int(data[x,1]))) + " TK: " + str(int(data[x,2])))
    #
    # score_order = [score[5], score[6], score[3], score[4], score[0], score[1], score[2]]
    # labels_order = [labels[5],labels[6],labels[3],labels[4],labels[0],labels[1], labels[2]]
    #
    #
    # plt.plot( labels_order, score_order, label = "MIMIC")
    #
    # plt.xticks(fontsize=8)
    #
    # # Adding legend patches from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # handles = []
    # patch1 = mpatches.Patch(color='royalblue', label='MIMIC')
    # patch2 = mpatches.Patch(color='lavender', label='P = Population Size')
    # patch3 = mpatches.Patch(color='lavender', label='TK = Samples To Keep')
    # handles.append(patch1)
    # handles.append(patch2)
    # handles.append(patch3)
    # plt.legend(handles=handles)
    #
    # plt.title("MIMIC Tuning")
    # plt.xlabel("Iteration")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.savefig('Knapsack MIMIC new tunes.png')
    # plt.close()
    # plt.figure()

    # data = np.genfromtxt("SA_Knapsack_Tuning rss.csv", delimiter=",")
    #
    # vals = ['1E11','1E11','1E11', '1E15', '1E15', '1E9', '1E9']
    #
    # score = []
    # labels = []
    # val = 0
    # for x in range(1,71,10):
    #     scores = data[x:(x+10), -1]
    #
    #     new = np.mean(scores, axis=0)
    #     score.append(new)
    #     labels.append("T: " + str(vals[val]) + " C: " + str(data[x,2]))
    #     val+=1
    #
    # score_order = [score[5], score[6], score[0], score[2], score[3], score[4]]
    # labels_order = [labels[5],labels[6],labels[0],labels[2],labels[3], labels[4]]
    #
    # print(score)
    # print(labels)
    # plt.plot( labels_order, score_order, label = "SA", color = "green")
    #
    # plt.xticks(fontsize=8)
    #
    # # Adding legend patches from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # handles = []
    # patch1 = mpatches.Patch(color='green', label='SA')
    # patch2 = mpatches.Patch(color='lavender', label='T = Initial Temperature')
    # patch3 = mpatches.Patch(color='lavender', label='C = Cooling Factor')
    # handles.append(patch1)
    # handles.append(patch2)
    # handles.append(patch3)
    # plt.legend(handles=handles)
    #
    # plt.title("SA Tuning")
    # plt.xlabel("Iteration")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.savefig('Knapsack SA new tunes.png')
    # plt.close()
    # plt.figure()

    # data = np.genfromtxt("GA_Knapsack_Tuning rss.csv", delimiter=",")
    # plt.figure(figsize=(11, 5))
    # score = []
    # labels = []
    # val = 0
    # for x in range(1, 61, 10):
    #     scores = data[x:(x + 10), -1]
    #
    #     new = np.mean(scores, axis=0)
    #     score.append(new)
    #     labels.append("P: " + str(data[x, 1]) + " Ma: " + str(data[x, 2]))
    #     val += 1
    #
    # score_order = [score[4], score[5], score[0], score[1], score[2], score[3]]
    # labels_order = [labels[4], labels[5], labels[0], labels[1], labels[2], labels[3]]
    #
    # plt.plot(labels_order, score_order, label="GA", color = "red")
    #
    # plt.xticks(fontsize=9)
    #
    # # Adding legend patches from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # handles= []
    # patch1 = mpatches.Patch(color='red', label='GA')
    # patch2 = mpatches.Patch(color='lavender', label='P = Population Size')
    # patch3 = mpatches.Patch(color='lavender', label='Ma = To Mate')
    # handles.append(patch1)
    # handles.append(patch2)
    # handles.append(patch3)
    # plt.legend(handles=handles)
    #
    # plt.title("GA Tuning")
    # plt.xlabel("Iteration")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.savefig('Knapsack GA new tunes.png')
    # plt.close()
    # plt.figure()

    # file = "RHC_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1,10):
    #     file = "RHC_Knapsack rss" + str(r+1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data/10)
    #
    # print(data)
    #
    # plt.plot(data[:, 0], data[:, 1], label="RHC")
    #
    # file = "SA_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "SA_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="SA")
    #
    # file = "GA_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "GA_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="GA")
    #
    # file = "MIMIC_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "MIMIC_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="MIMIC")
    #
    # plt.title("Iterations vs Fitness")
    # plt.xlabel("Iterations")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('Knapsack Fitness Score Chart rss.png')
    # plt.close()
    # plt.figure()
    #
    #

    # file = "RHC_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1,10):
    #     file = "RHC_Knapsack rss" + str(r+1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data/10)
    # plt.plot(data[:, 0], data[:, 1], label="RHC")
    #
    # file = "SA_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "SA_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="SA")
    #
    # file = "GA_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "GA_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="GA")
    #
    # file = "MIMIC_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "MIMIC_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="MIMIC")
    #
    # plt.title("Iterations vs Fitness")
    # plt.xlabel("Iterations")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('Knapsack Fitness Score Chart rss.png')
    # plt.close()
    # plt.figure()
    #

    #
    # file = "RHC_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "RHC_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="RHC")
    #
    # file = "SA_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "SA_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="SA")
    #
    # file = "GA_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "GA_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="GA")
    #
    # file = "MIMIC_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "MIMIC_Knapsack rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="MIMIC")
    #
    # plt.title("Iterations vs Time")
    # plt.xlabel("Iterations")
    # plt.ylabel("Log Time")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('Knapsack Time Elapsed Chart rss.png')
    # plt.close()
    # plt.figure()

    #
    # file = "Volume_Knapsack rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1,10):
    #     file = "Volume_Knapsack rss" + str(r+1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data/10)
    #
    # plt.plot(data[3:8, 0], data[3:8,1], label="RHC")
    # plt.plot(data[3:8, 0], data[3:8,2], label="SA")
    # plt.plot(data[3:8, 0], data[3:8,3], label="GA")
    # plt.plot(data[3:8, 0], data[3:8,4], label="MIMIC")
    #
    # plt.title("Weight Limit vs Score")
    # plt.xlabel("Weight Limit Multiplier")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('Knapsack Volume vs Score chart rss.png')
    # plt.close()
    # plt.figure()

    ################################
    #KNAPSACK STUFF end##
    #############################


    ################################
    #Traveling Sales Man PRobelm STUFF end##
    #############################


    # data = np.genfromtxt("MIMIC_TSP_Tuning rss.csv", delimiter=",")
    #
    # # plt.figure(figsize=(9, 5))
    #
    # score = []
    # labels = []
    #
    # for x in range(1,71,10):
    #     scores = data[x:(x+10), -1]
    #
    #     new = np.mean(scores, axis=0)
    #     score.append(new)
    #     labels.append("P:" + str(str(int(data[x,1]))) + " TK: " + str(int(data[x,2])))
    #
    # score_order = [score[5], score[6], score[3], score[4], score[0], score[1], score[2]]
    # labels_order = [labels[5],labels[6],labels[3],labels[4],labels[0],labels[1], labels[2]]
    #
    #
    # plt.plot( labels_order, score_order, label = "MIMIC")
    #
    # # Adding legend patches from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # handles = []
    # patch1 = mpatches.Patch(color='royalblue', label='MIMIC')
    # patch2 = mpatches.Patch(color='lavender', label='P = Population Size')
    # patch3 = mpatches.Patch(color='lavender', label='TK = Samples To Keep')
    # handles.append(patch1)
    # handles.append(patch2)
    # handles.append(patch3)
    #
    # plt.legend(handles=handles)
    #
    # plt.xticks(fontsize=8)
    #
    # plt.title("MIMIC Tuning")
    # plt.xlabel("Iteration")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.savefig('TSP MIMIC new tunes.png')
    # plt.close()
    # plt.figure()
    #
    # data = np.genfromtxt("SA_TSP_Tuning rss.csv", delimiter=",")
    #
    # vals = ['1E11','1E11','1E11', '1E15', '1E15', '1E9', '1E9']
    #
    # score = []
    # labels = []
    # val = 0
    # for x in range(1,71,10):
    #     scores = data[x:(x+10), -1]
    #
    #     new = np.mean(scores, axis=0)
    #     score.append(new)
    #     labels.append("T: " + str(vals[val]) + " C: " + str(data[x,2]))
    #     val+=1
    #
    # score_order = [score[5], score[6], score[1], score[0], score[2], score[3], score[4]]
    # labels_order = [labels[5],labels[6],labels[1],labels[0],labels[2],labels[3], labels[4]]
    #
    # print(score)
    # print(labels)
    # plt.plot( labels_order, score_order, label = "SA", color = "green")
    #
    # plt.xticks(fontsize=8)
    #
    # # Adding legend patches from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # handles = []
    # patch1 = mpatches.Patch(color='green', label='SA')
    # patch2 = mpatches.Patch(color='lavender', label='T = Temperature')
    # patch3 = mpatches.Patch(color='lavender', label='C = Cooling Factor')
    # handles.append(patch1)
    # handles.append(patch2)
    # handles.append(patch3)
    # plt.legend(handles=handles)
    #
    # plt.title("SA Tuning")
    # plt.xlabel("Iteration")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.savefig('TSP SA new tunes.png')
    # plt.close()
    # plt.figure()
    #
    #
    #
    # data = np.genfromtxt("GA_TSP_Tuning rss.csv", delimiter=",")
    # plt.figure(figsize=(11, 5))
    # score = []
    # labels = []
    # val = 0
    # for x in range(1, 61, 10):
    #     scores = data[x:(x + 10), -1]
    #
    #     new = np.mean(scores, axis=0)
    #     score.append(new)
    #     labels.append("P: " + str(data[x, 1]) + " Ma: " + str(data[x, 2]))
    #     val += 1
    #
    # score_order = [score[4], score[5], score[0], score[1], score[2], score[3]]
    # labels_order = [labels[4], labels[5], labels[0], labels[1], labels[2], labels[3]]
    #
    # plt.plot(labels_order, score_order, label="GA", color = "red")
    #
    # plt.xticks(fontsize=9)
    #
    # # Adding legend patches from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # handles = []
    # patch1 = mpatches.Patch(color='red', label='GA')
    # patch2 = mpatches.Patch(color='lavender', label='P = Population Size')
    # patch3 = mpatches.Patch(color='lavender', label='Ma = Samples To Mate')
    # handles.append(patch1)
    # handles.append(patch2)
    # handles.append(patch3)
    # plt.legend(handles=handles)
    #
    #
    # plt.title("GA Tuning")
    # plt.xlabel("Iteration")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.savefig('TSP GA new tunes.png')
    # plt.close()
    # plt.figure()
    #
    #
    #



    # file = "RHC_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1,10):
    #     file = "RHC_TSP rss" + str(r+1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data/10)
    # plt.plot(data[:, 0], data[:, 1], label="RHC")
    #
    # file = "SA_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "SA_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="SA")
    #
    # file = "GA_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "GA_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="GA")
    #
    # file = "MIMIC_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "MIMIC_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="MIMIC")
    #
    # plt.title("Iterations vs Fitness")
    # plt.xlabel("Iterations")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('TSP Fitness Score Chart rss.png')
    # plt.close()
    # plt.figure()
    #
    # file = "RHC_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "RHC_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="RHC")
    #
    # file = "SA_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "SA_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="SA")
    #
    # file = "GA_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "GA_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="GA")
    #
    # file = "MIMIC_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "MIMIC_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="MIMIC")
    #
    # plt.title("Iterations vs Time")
    # plt.xlabel("Iterations")
    # plt.ylabel("Log Time")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('TSP Time Elapsed Chart rss.png')
    # plt.close()
    # plt.figure()
    #
    #
    # file = "RHC_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1,10):
    #     file = "RHC_TSP rss" + str(r+1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data/10)
    # plt.plot(data[:, 0], data[:, 3], label="RHC")
    #
    # file = "SA_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "SA_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 3], label="SA")
    #
    # file = "GA_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "GA_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 3], label="GA")
    #
    # file = "MIMIC_TSP rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "MIMIC_TSP rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 3], label="MIMIC")
    #
    # plt.title("Iterations vs Function Evaluations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Function Evaluations")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('TSP Function Evaluations Chart rss.png')
    # plt.close()
    # plt.figure()
    #
    #
    # file = "Nodes_TSP rss bam" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1,6):
    #     file = "Nodes_TSP rss bam" + str(r+1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data/10)
    #
    #
    # # data[4, 6] = data[3,6]
    # # print(data[:,6])
    # plt.plot(data[:, 0], np.log10(data[:,5]), label="RHC")
    # plt.plot(data[:, 0], np.log10(data[:,6]), label="SA")
    # plt.plot(data[:, 0], np.log10(data[:,7]), label="GA")
    # plt.plot(data[:, 0], np.log10(data[:,8]), label="MIMIC")
    #
    # plt.title("Number of Nodes vs Time")
    # plt.xlabel("Number of Nodes")
    # plt.ylabel("Log Time")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('TSP Nodes vs time rss.png')
    # plt.close()
    # plt.figure()


################################
#Traveling Sales Man PRobelm STUFF end##
#############################

################################
# Continuous PRobelm STUFF ##
#############################
    #
    #
    # data = np.genfromtxt("MIMIC_Peaks_Tuning rss.csv", delimiter=",")
    #
    # # plt.figure(figsize=(9, 5))
    #
    # score = []
    # labels = []
    #
    # for x in range(1,71,10):
    #     scores = data[x:(x+10), -1]
    #
    #     new = np.mean(scores, axis=0)
    #     score.append(new)
    #     labels.append("P:" + str(str(int(data[x,1]))) + " TK: " + str(int(data[x,2])))
    #
    # score_order = [score[5], score[6], score[3], score[4], score[0], score[1], score[2]]
    # labels_order = [labels[5],labels[6],labels[3],labels[4],labels[0],labels[1], labels[2]]
    #
    #
    # plt.plot( labels_order, score_order, label = "MIMIC")
    #
    # plt.xticks(fontsize=8)
    #
    # # Adding legend patches from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # handles = []
    # patch1 = mpatches.Patch(color='royalblue', label='MIMIC')
    # patch2 = mpatches.Patch(color='lavender', label='P = Population Size')
    # patch3 = mpatches.Patch(color='lavender', label='TK = Samples To Keep')
    # handles.append(patch1)
    # handles.append(patch2)
    # handles.append(patch3)
    # plt.legend(handles=handles)
    #
    # plt.title("MIMIC Tuning")
    # plt.xlabel("Iteration")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.savefig('Peaks MIMIC new tunes.png')
    # plt.close()
    # plt.figure()
    #
    # data = np.genfromtxt("SA_Peaks_Tuning rss.csv", delimiter=",")
    #
    # vals = ['1E11','1E11','1E11', '1E15', '1E15', '1E9', '1E9']
    #
    # score = []
    # labels = []
    # val = 0
    # for x in range(1,71,10):
    #     scores = data[x:(x+10), -1]
    #
    #     new = np.mean(scores, axis=0)
    #     score.append(new)
    #     labels.append("T: " + str(vals[val]) + " C: " + str(data[x,2]))
    #     val+=1
    #
    # score_order = [score[5], score[6], score[1], score[0], score[2], score[3], score[4]]
    # labels_order = [labels[5],labels[6],labels[1],labels[0],labels[2],labels[3], labels[4]]
    #
    # print(score)
    # print(labels)
    # plt.plot( labels_order, score_order, label = "SA", color = "green")
    #
    # plt.xticks(fontsize=8)
    #
    # # Adding legend patches from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # handles = []
    # patch1 = mpatches.Patch(color='green', label='SA')
    # patch2 = mpatches.Patch(color='lavender', label='T = Temperature')
    # patch3 = mpatches.Patch(color='lavender', label='C = Cooling Factor')
    # handles.append(patch1)
    # handles.append(patch2)
    # handles.append(patch3)
    # plt.legend(handles=handles)
    #
    # plt.title("SA Tuning")
    # plt.xlabel("Iteration")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.savefig('Peaks SA new tunes.png')
    # plt.close()
    # plt.figure()
    #
    #
    # data = np.genfromtxt("GA_Peaks_Tuning rss.csv", delimiter=",")
    # plt.figure(figsize=(11, 5))
    # score = []
    # labels = []
    # val = 0
    # for x in range(1, 61, 10):
    #     scores = data[x:(x + 10), -1]
    #
    #     new = np.mean(scores, axis=0)
    #     score.append(new)
    #     labels.append("P: " + str(data[x, 1]) + " Ma: " + str(data[x, 2]))
    #     val += 1
    #
    # score_order = [score[4], score[5], score[0], score[1], score[2], score[3]]
    # labels_order = [labels[4], labels[5], labels[0], labels[1], labels[2], labels[3]]
    #
    # plt.plot(labels_order, score_order, label="GA", color = "red")
    #
    # plt.xticks(fontsize=11)
    #
    # # Adding legend patches from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # handles = []
    # patch1 = mpatches.Patch(color='red', label='GA')
    # patch2 = mpatches.Patch(color='lavender', label='P = Population Size')
    # patch3 = mpatches.Patch(color='lavender', label='Ma = To Mate')
    # handles.append(patch1)
    # handles.append(patch2)
    # handles.append(patch3)
    # plt.legend(handles=handles)
    #
    #
    # plt.title("GA Tuning")
    # plt.xlabel("Iteration")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.savefig('Peaks GA new tunes.png')
    # plt.close()
    # plt.figure()

    #
    # file = "RHC_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1,10):
    #     file = "RHC_Peaks rss" + str(r+1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data/10)
    # plt.plot(data[:, 0], data[:, 1], label="RHC")
    #
    # file = "SA_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "SA_Peaks rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="SA")
    #
    # file = "GA_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "GA_Peaks rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="GA")
    #
    # file = "MIMIC_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "MIMIC_Peaks rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], data[:, 1], label="MIMIC")
    #
    # plt.title("Iterations vs Fitness")
    # plt.xlabel("Iterations")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('Peaks Fitness Score Chart rss.png')
    # plt.close()
    # plt.figure()

    # file = "RHC_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "RHC_Peaks rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="RHC")
    #
    # file = "SA_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "SA_Peaks rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="SA")
    #
    # file = "GA_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "GA_Peaks rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="GA")
    #
    # file = "MIMIC_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1, 10):
    #     file = "MIMIC_Peaks rss" + str(r + 1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data / 10)
    # plt.plot(data[:, 0], np.log10(data[:, 2]), label="MIMIC")
    #
    # plt.title("Iterations vs Time")
    # plt.xlabel("Iterations")
    # plt.ylabel("Log Time")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('Peaks Time Elapsed Chart rss.png')
    # plt.close()
    # plt.figure()


    # file = "N_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1,10):
    #     file = "N_Peaks rss" + str(r+1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data/10)
    #
    # plt.plot(data[:, 0], np.log10(data[:,5]), label="RHC")
    # plt.plot(data[:, 0], np.log10(data[:,6]), label="SA")
    # plt.plot(data[:, 0], np.log10(data[:,7]), label="GA")
    # plt.plot(data[:, 0], np.log10(data[:,8]), label="MIMIC")
    #
    # plt.title("N vs Time")
    # plt.xlabel("N")
    # plt.ylabel("Log Time")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('Peaks N vs time rss.png')
    # plt.close()
    # plt.figure()
    #

    # file = "N_Peaks rss" + str(1) + ".csv"
    # data = np.genfromtxt(file, delimiter=",")
    # for r in range(1,10):
    #     file = "N_Peaks rss" + str(r+1) + ".csv"
    #     d = np.genfromtxt(file, delimiter=",")
    #     data += d
    # data = (data/10)
    #
    # plt.plot(data[:, 0], data[:,1], label="RHC")
    # plt.plot(data[:, 0], data[:,2], label="SA")
    # plt.plot(data[:, 0], data[:,3], label="GA")
    # plt.plot(data[:, 0], data[:,4], label="MIMIC")
    #
    # plt.title("N vs Score")
    # plt.xlabel("N")
    # plt.ylabel("Score")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('Peaks N vs Score rss.png')
    # plt.close()
    # plt.figure()
    #

################################
# Continuous PRobelm STUFF end##
#############################
##############################
################################
#######NNNNNNNNNNNNNNNNNNNNN
###########################
#####################


    # data = np.genfromtxt("SAE9C3.csv", delimiter=",")
    # plt.plot(range(0, len(data)), data[:, 1], label="T=1E9 C=.3")
    #
    # data = np.genfromtxt("SAE9C5.csv", delimiter=",")
    # plt.plot(range(0, len(data)), data[:, 1], label="T=1E9 C=.5")
    #
    # data = np.genfromtxt("SAE9C95.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="T=1E9 C=.95")
    #
    # data = np.genfromtxt("SAE11C3.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="T=1E11 C=.3")
    #
    # data = np.genfromtxt("SAE11C5.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="T=1E11 C=.5")
    #
    # data = np.genfromtxt("SAE11C95.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:,1], label = "T=1E11 C=.95")
    #
    # data = np.genfromtxt("SAE15C3.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="T=1E15 C=.3")
    #
    # data = np.genfromtxt("SAE15C5.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="T=1E15 C=.5")
    #
    # data = np.genfromtxt("SAE15C95.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="T=1E15 C=.95")
    #
    #
    # plt.title("Testing Error vs Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("MSE ")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('NN SA Testing Error.png')
    # plt.close()
    # plt.figure()


    # data = np.genfromtxt("SAE9C3.csv", delimiter=",")
    # plt.plot(range(0, len(data)), data[:, 2], label="T=1E9 C=.3")
    #
    # data = np.genfromtxt("SAE9C5.csv", delimiter=",")
    # plt.plot(range(0, len(data)), data[:, 2], label="T=1E9 C=.5")
    #
    # data = np.genfromtxt("SAE9C95.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="T=1E9 C=.95")
    #
    # data = np.genfromtxt("SAE11C3.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="T=1E11 C=.3")
    #
    # data = np.genfromtxt("SAE11C5.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="T=1E11 C=.5")
    #
    # data = np.genfromtxt("SAE11C95.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:,2], label = "T=1E11 C=.95")
    #
    # data = np.genfromtxt("SAE15C3.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="T=1E15 C=.3")
    #
    # data = np.genfromtxt("SAE15C5.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="T=1E15 C=.5")
    #
    # data = np.genfromtxt("SAE15C95.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="T=1E15 C=.95")

    #
    # plt.title("Training Time vs Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Trianing Time ")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('NN SA Training Time.png')
    # plt.close()
    # plt.figure()


    # data = np.genfromtxt("GAEP50K25M2.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="P=50 M=25")
    #
    # data = np.genfromtxt("GAEP50K40M2.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="P=50 M=40")
    #
    # data = np.genfromtxt("GAEP100K50M10.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:,1], label = "P=100 M=50")
    #
    # data = np.genfromtxt("GAEP100K80M10.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="P=100 M=80")
    #
    # data = np.genfromtxt("GAEP200K100M10.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="P=200 M=100")
    #
    # data = np.genfromtxt("GAEP200K150M10.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="P=200 M=150")
    #
    #
    #
    # plt.title("Testing Error vs Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Testing MSE")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('NN GA Testing Error.png')
    # plt.close()
    # plt.figure()


    # data = np.genfromtxt("GAEP50K25M2.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="P=50 M=25")
    #
    # data = np.genfromtxt("GAEP50K40M2.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="P=50 M=40")
    #
    # data = np.genfromtxt("GAEP100K50M10.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:,2], label = "P=100 M=50")
    #
    # data = np.genfromtxt("GAEP100K80M10.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="P=100 M=80")
    #
    # data = np.genfromtxt("GAEP200K100M10.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="P=200 M=100")
    #
    # data = np.genfromtxt("GAEP200K150M10.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="P=200 M=150")
    #
    #
    #
    # plt.title("Training Time vs Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Training Time")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('NN GA Training Time.png')
    # plt.close()
    # plt.figure()




    #
    # data = np.genfromtxt("ReluBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:,5], label = "Relu")
    #
    # data = np.genfromtxt("SigmoidBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 5], label="Logistic Sigmoid")
    #
    # data = np.genfromtxt("LinearBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 5], label="Linear Activation")
    #
    # data = np.genfromtxt("HyperbolicBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 5], label="Hyperbolic Tangent Sigmoid")
    #
    #
    # plt.title("Test Percent Correct vs Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Test Percent Correct")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('NN Backprop Test Percent Correct.png')
    # plt.close()
    # plt.figure()
    #
    # data = np.genfromtxt("ReluBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:,1], label = "Relu")
    #
    # data = np.genfromtxt("SigmoidBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="Logistic Sigmoid")
    #
    # data = np.genfromtxt("LinearBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="Linear Activation")
    #
    # data = np.genfromtxt("HyperbolicBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 1], label="Hyperbolic Tangent Sigmoid")
    #
    #
    # plt.title("Test Error vs Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Test Error")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('NN Backprop Test Error.png')
    # plt.close()
    # plt.figure()
    #
    #
    # data = np.genfromtxt("ReluBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:,2], label = "Relu")
    #
    # data = np.genfromtxt("SigmoidBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="Logistic Sigmoid")
    #
    # data = np.genfromtxt("LinearBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="Linear Activation")
    #
    # data = np.genfromtxt("HyperbolicBackpop.csv", delimiter=",")
    # plt.plot(range(0,len(data)), data[:, 2], label="Hyperbolic Tangent Sigmoid")
    #
    #
    # plt.title("Train Time vs Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Train Time ")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('NN Backprop Train Time.png')
    # plt.close()
    # plt.figure()
    #
    #
    # data = np.genfromtxt("GA-Bam act.csv", delimiter=",")
    # data = data[0:500,:]
    # plt.plot(range(0,len(data)), data[:, 1], label="GA")
    #
    # data = np.genfromtxt("RHC-Bam act.csv", delimiter=",")
    # data = data[0:4500, :]
    # plt.plot(range(0,len(data)), data[:, 1], label="RHC")
    #
    # data = np.genfromtxt("SigmoidBackpop.csv", delimiter=",")
    # data = data[0:70, :]
    # plt.plot(range(0,len(data)), data[:, 1], label="Backpropagation")
    #
    # data = np.genfromtxt("SA-Bam act.csv", delimiter=",")
    # data = data[0:4844, :]
    # plt.plot(range(0,len(data)), data[:, 1], label="SA")
    #
    #
    # plt.title("Test MSE vs Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Test Error")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('NN ALL Test Error bam sig.png')
    # plt.close()
    # plt.figure()
    #
    #
    # labels = ["GA", "RHC", "SA", "Backpropagation"]
    # train_times = []
    #
    # data = np.genfromtxt("GA-Bam act.csv", delimiter=",")
    # data = data[0:400, :]
    # train_times.append(data[-1, 2])
    #
    #
    # data = np.genfromtxt("RHC-Bam act.csv", delimiter=",")
    # data = data[0:4500, :]
    # train_times.append(data[-1, 2])
    #
    # data = np.genfromtxt("SA-Bam act.csv", delimiter=",")
    # data = data[0:4844, :]
    # train_times.append(data[-1, 2])
    #
    # data = np.genfromtxt("SigmoidBackpop.csv", delimiter=",")
    # data = data[0:30, :]
    # train_times.append(data[-1, 2])
    #
    #
    # plt.figure(figsize=(9, 5))
    # plt.bar(labels, train_times)
    # plt.title("Training Times")
    # plt.xlabel("Classifiers")
    # plt.ylabel("Training Time - Seconds")
    # plt.savefig('NN All Train Time bam sig.png')
    # plt.close()
    # plt.figure()
    #
    #

    # data = np.genfromtxt("GA-Bam act.csv", delimiter=",")
    # data = data[0:600,:]
    # plt.plot(range(0,len(data)), data[:, 5], label="GA")
    #
    # data = np.genfromtxt("RHC-Bam act.csv", delimiter=",")
    # data = data[0:4500, :]
    # plt.plot(range(0,len(data)), data[:, 5], label="RHC")
    #
    # data = np.genfromtxt("SigmoidBackpop.csv", delimiter=",")
    # data = data[0:100, :]
    # plt.plot(range(0,len(data)), data[:, 5], label="Backpropagation")
    #
    # data = np.genfromtxt("SA-Bam act.csv", delimiter=",")
    # data = data[0:4844, :]
    # plt.plot(range(0,len(data)), data[:, 5], label="SA")
    #
    #
    # plt.title("Test Accuracy vs Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Test Accuracy")
    # plt.tight_layout()
    # plt.legend()
    # plt.savefig('NN ALL Test Accuracy sig.png')
    # plt.close()
    # plt.figure()
