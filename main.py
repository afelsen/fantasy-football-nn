import pandas as pd
import numpy as np

from nn import FantasyScoreNN
from scipy.stats import rankdata

from vis.visualization import visualize_saliency
import keras
import matplotlib.pyplot as plt


def main():
    # np.set_printoptions(threshold=np.inf)

    df=pd.read_csv('QBdata.csv', sep=',',header=None)
    # df = df[pd.notnull(df[0])]
    a = df.values


    #Delete unnecessary headers
    a = np.delete(a, list(range(0, a.shape[0], 102)), axis=0)
    a = np.delete(a, list(range(0, a.shape[0], 101)), axis=0)


    #conserve the first two rows
    b = a[:2,:]

    #Change year to integer
    a[:,2] = a[:,2].astype(int)
    # a = a[a[:,2].argsort()]

    #Sort by name, then year
    a  = a[np.lexsort((a[:, 2],a[:, 1]))]


    #delete unnesessary stats

    names = a[:,1]
    print(names)
    a = np.delete(a, 1, 1)
    a = np.delete(a,3,1)
    a = np.delete(a,3,1)
    a = np.delete(a,3,1)



    #add the first two rows back
    # a = np.vstack((b,a))



    #Separate labels (fantasy points)
    temp = np.hsplit(a,[5,8,50])
    a = np.hstack((temp[0],temp[1],temp[2]))
    a = a.astype(float)
    print(a)

    labelsT = temp[1][:,0]
    labelsT = labelsT.astype(float)

    print(b)


    #Group data by individual
    singlenames = []

    dataall = []

    data = []
    labels = []

    data18 = []

    prev = names[0]
    j = 0
    print(prev)
    for i in range(len(a)):

        if names[i] != prev:
            print(names[i])
            singlenames.append(names[i-1])



            #Every combination of data
            # result = np.zeros((22,22))
            # chunk = a[j:i-1,:]
            # result[:chunk.shape[0],:chunk.shape[1]] = chunk
            # data.append(result)


            #Data until 2017
            result = np.zeros((22,22))
            chunk = a[j:i-1,:]
            result[:chunk.shape[0],:chunk.shape[1]] = chunk
            data.append(result)

            labels.append(labelsT[i-1])

            #Data until 2018
            result = np.zeros((22,22))
            chunk = a[j:i,:]
            result[:chunk.shape[0],:chunk.shape[1]] = chunk
            data18.append(result)

            j = i
            prev = names[i]

    labels.append(labelsT[-1])

    data = np.asarray(data)
    labels = np.asarray(labels)
    data18 = np.asarray(data18)
    print(data.shape)
    print(data[4,:,:])
    print(labels.shape)
    print(labels[4])

    data[np.isnan(data)] = 0
    labels[np.isnan(labels)] = 0
    data18[np.isnan(data18)] = 0



    singlenames = [s[:s.index("\\")] for s in singlenames]

    #Create a new data list with only recent players
    datanew = []
    labelsnew = []
    singlenamesnew = []
    datanew18 = []

    for i in range(len(data)):
        if len(np.trim_zeros(data[i,:,1]))>0 and np.trim_zeros(data[i,:,1])[-1] == 2017:
            datanew.append(data[i,:,:])
            labelsnew.append(labels[i])
            singlenamesnew.append(singlenames[i])
            datanew18.append(data18[i,:,:])

    datanew = np.asarray(datanew)
    labelsnew = np.asarray(labelsnew)
    datanew18 = np.asarray(datanew18)

    print(datanew.shape)
    print(labelsnew.shape)


    ######End of organizing data#######

    traindata = data[:400,:,:]
    testdata = datanew[:,:,:]

    trainlabels = labels[:400]
    testlabels = labelsnew[:]


    testdata18 = datanew18[:,:,:]



    #####Neural Network#####
    traindata = traindata[..., np.newaxis]
    testdata = testdata[...,np.newaxis]
    testdata18 = testdata18[...,np.newaxis]
    print(traindata.shape)

    vBot=FantasyScoreNN((22,22,1),2,traindata,trainlabels);
    #If the Bot Requires Training Call Train Function To Train
    if(vBot.mDoesRequireTraining):
        print("Training The Bot");
        vBot.Train();
        print("Training Complete");


    #Test The Bot - For 2018 Fantasy Points
    print("Testing The Bot");
    accum = 0
    runs = 0

    namesT = []
    guessesT = []
    actualT = []

    for i in range(len(testdata)):
        print(singlenamesnew[i])
        namesT.append(singlenamesnew[i])

        action=vBot.GetAction(testdata[i])
        print("Guess:",action)
        guessesT.append(action)

        print("Actual:",testlabels[i])
        actualT.append(testlabels[i])

        diff = abs(action-testlabels[i])
        print("Difference:",diff)
        print()
        runs += 1
        accum += diff

    print(accum/runs)
    print("Testing Complete");


    guessesT = len(guessesT) - rankdata(guessesT, method = 'min')
    actualT = len(actualT) - rankdata(actualT, method = 'min')
    allInfo = [namesT,guessesT,actualT]
    allInfo = np.asarray(allInfo,dtype=np.dtype(object)).T
    print(allInfo.shape)
    allInfo = allInfo[allInfo[:,2].argsort()]

    df = pd.DataFrame(allInfo)

    print(df)


    averagediff = np.mean(np.abs(guessesT - actualT))
    mediandiff = np.median(np.abs(guessesT - actualT))
    print("Average Ranking Difference:",averagediff)
    print("Median Ranking Difference:",mediandiff)



    #Predicting 2019
    print("Predicting 2019");
    guessesT18 = []
    namesT = []

    for i in range(len(testdata)):

        print(singlenamesnew[i])
        namesT.append(singlenamesnew[i])

        action=vBot.GetAction(testdata18[i])
        print("Guess:",action)
        guessesT18.append(action)

        print()

    print("Testing Complete");

    guessesT18 = len(guessesT18) - rankdata(guessesT18, method = 'min')

    allInfo = [namesT,guessesT18]
    allInfo = np.asarray(allInfo,dtype=np.dtype(object)).T

    allInfo = allInfo[allInfo[:,1].argsort()]

    df = pd.DataFrame(allInfo)
    print(df)



    ####Saliency Map and Graphic#####

    model = keras.models.load_model("FantasyNNModel.h5");


    columns = 4
    rows = len(datanew)//columns+1


    fig = plt.figure()

    for i in range(1, columns*(rows-1) + 3):

        #Image
        example = datanew18[i-1]
        grads = visualize_saliency(model, -1, filter_indices = 0, seed_input=example[...,np.newaxis])


        #Names label
        subplot = fig.add_subplot(rows, columns, i)
        subplot.set_ylabel(singlenamesnew[i-1],fontsize = 5, rotation = 35, labelpad=20)


        plt.xticks(np.arange(0, 22, 1.0))
        plt.yticks(np.arange(0, 22, 1.0))

        #Label each column

        title = "Rk,Year,Age,Games Played,Games Started,FantPt,PPR,FantPt/G,PPR/G,Cmp,P-Att,P-Yds,P-TD,Int,Ru-Att,Ru-Yds,Ru-TD,Rec,Rec-Yds,Rec-TD,Fmb"
        title = title.split(",")

        labels = [item.get_text() for item in subplot.get_xticklabels()]
        for j in range(len(title)):
            labels[j] = title[j]

        subplot.set_xticklabels(labels, fontsize = 1, rotation = 90)
        subplot.xaxis.tick_top()
        subplot.tick_params(axis=u'both', which=u'both',length=0)
        subplot.tick_params(axis='x', pad=-15, colors = "white")


        #Label each row

        labels = [item.get_text() for item in subplot.get_xticklabels()]

        for j in range(len(datanew[i-1,:,1])):
            if datanew18[i-1,j,1] != 0:
                labels[j] = int(datanew18[i-1,j,1])
            else:
                labels[j] = ""

        subplot.set_yticklabels(labels, fontsize = 1, rotation = 0)
        subplot.tick_params(axis='y', pad=1)

        #Remove Border
        subplot.spines['top'].set_visible(False)
        subplot.spines['right'].set_visible(False)
        subplot.spines['bottom'].set_visible(False)
        subplot.spines['left'].set_visible(False)


        #Right text
        subplot.text(2,.8, "2018 Prediction:" + str(guessesT[i-1]), size=3, ha="center",
         transform=subplot.transAxes)
        subplot.text(2,.6, "Actual Ranking:" + str(actualT[i-1]), size=3, ha="center",
          transform=subplot.transAxes)


        subplot.text(2,.2, "2019 Prediction:" + str(guessesT18[i-1]), size=3, ha="center",
          transform=subplot.transAxes)




        plt.imshow(example)
        plt.imshow(grads, alpha=.6)

    subplot = fig.add_subplot(rows, columns, i+1)

    plt.xticks([])
    plt.yticks([])

    plt.axis('off')

    plt.suptitle("Visualization of Neural Network's Fantasy Football Predictions")

    plt.savefig('Current-players-visualization.png', dpi=1000)
main()
