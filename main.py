import pandas as pd
import numpy as np

from nn import FantasyScoreNN
from scipy.stats import rankdata

from vis.visualization import visualize_saliency
import keras
import matplotlib.pyplot as plt


class Data():
    def __init__(self,dfvalues,modelname):
        self.a = dfvalues
        self.modelname = modelname
        self.model = keras.models.load_model(modelname)

    def parseData(self):
        a = self.a

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
        labelsall = []

        data = []
        labels = []

        data18 = []

        prev = names[0]
        j = 0
        for i in range(len(a)):

            if names[i] != prev:
                singlenames.append(names[i-1])


                #Every combination of data
                for x in range(j,i-2):
                    result = np.zeros((22,22))
                    chunk = a[j:x,:]
                    result[:chunk.shape[0],:chunk.shape[1]] = chunk
                    dataall.append(result)

                    labelsall.append(labelsT[x])


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


        dataall = np.asarray(dataall)
        labelsall = np.asarray(labelsall)

        data = np.asarray(data)
        labels = np.asarray(labels)
        data18 = np.asarray(data18)

        data[np.isnan(data)] = 0
        labels[np.isnan(labels)] = 0
        dataall[np.isnan(dataall)] = 0
        labelsall[np.isnan(labelsall)] = 0
        data18[np.isnan(data18)] = 0


        print(dataall[4])
        print(labelsall[4])


        singlenames = [s[:s.index("\\")] for s in singlenames]

        #Create a new data list with only recent players
        datanew = []
        labelsnew = []
        singlenamesnew = []
        datanew18 = []

        dataold = []
        labelsold = []

        for i in range(len(data)):
            if len(np.trim_zeros(data[i,:,1]))>0 and np.trim_zeros(data[i,:,1])[-1] == 2017:
                datanew.append(data[i,:,:])
                labelsnew.append(labels[i])
                singlenamesnew.append(singlenames[i])
                datanew18.append(data18[i,:,:])

            else:
                dataold.append(data[i,:,:])
                labelsold.append(labels[i])

        self.datanew = np.asarray(datanew)
        self.labelsnew = np.asarray(labelsnew)
        self.datanew18 = np.asarray(datanew18)

        dataold = np.asarray(dataold)
        labelsold = np.asarray(labelsold)


        ######End of organizing data#######

        self.traindata = data[:,:,:]
        self.testdata = self.datanew[:,:,:]

        self.trainlabels = labels[:]
        self.testlabels = self.labelsnew[:]


        self.testdata18 = self.datanew18[:,:,:]

        self.traindata = dataall[:,:,:]
        self.trainlabels = labelsall[:]

        print("data: ", data.shape)
        print("dataall: ", dataall.shape)

        self.singlenamesnew = singlenamesnew

    def trainNN(self):
        #####Neural Network#####
        self.traindata = self.traindata[..., np.newaxis]
        self.trainlabels = self.trainlabels
        self.testdata = self.testdata[...,np.newaxis]
        self.testlabels = self.testlabels

        self.testdata18 = self.testdata18[...,np.newaxis]
        self.singlenamesnew = self.singlenamesnew

        vBot=FantasyScoreNN((22,22,1),2,self.traindata,self.trainlabels, self.modelname);

        #If the Bot Requires Training Call Train Function To Train
        if(vBot.mDoesRequireTraining):
            print("Training The Bot");
            vBot.Train();
            print("Training Complete");

    def testNN(self):

        vBot=FantasyScoreNN((22,22,1),2,self.traindata,self.trainlabels,self.modelname);

        #Test The Bot - For 2018 Fantasy Points
        print("Testing The Bot");
        accum = 0
        runs = 0

        namesT = []
        guessesT = []
        actualT = []

        for i in range(len(self.testdata)):
            print(self.singlenamesnew[i])
            namesT.append(self.singlenamesnew[i])

            action=vBot.GetAction(self.testdata[i])
            print("Guess:",action)
            guessesT.append(action)

            print("Actual:",self.testlabels[i])
            actualT.append(self.testlabels[i])

            diff = abs(action-self.testlabels[i])
            print("Difference:",diff)
            print()
            runs += 1
            accum += diff

        print(accum/runs)
        print("Testing Complete");

        self.pointsG = guessesT
        self.guessesT = len(guessesT) - rankdata(guessesT, method = 'min') + 1

        self.pointsA = actualT
        self.actualT = len(actualT) - rankdata(actualT, method = 'min') + 1
        allInfo = [namesT,self.guessesT,self.actualT]
        allInfo = np.asarray(allInfo,dtype=np.dtype(object)).T
        print(allInfo.shape)
        allInfo = allInfo[allInfo[:,2].argsort()]

        df = pd.DataFrame(allInfo)

        print(df)


        averagediff = np.mean(np.abs(self.guessesT - self.actualT))
        mediandiff = np.median(np.abs(self.guessesT - self.actualT))
        print("Average Ranking Difference:",averagediff)
        print("Median Ranking Difference:",mediandiff)



        #Predicting 2019
        print("Predicting 2019");
        guessesT18 = []
        namesT = []

        for i in range(len(self.testdata)):

            print(self.singlenamesnew[i])
            namesT.append(self.singlenamesnew[i])

            action=vBot.GetAction(self.testdata18[i])
            print("Guess:",action)
            guessesT18.append(action)

            print()

        print("Testing Complete");

        self.pointsG18 = guessesT18
        self.guessesT18 = len(guessesT18) - rankdata(guessesT18, method = 'min') + 1

        allInfo = [namesT,self.guessesT18]
        allInfo = np.asarray(allInfo,dtype=np.dtype(object)).T

        allInfo = allInfo[allInfo[:,1].argsort()]

        df = pd.DataFrame(allInfo)
        print(df)


    def drawvisualization(self):
        ####Saliency Map and Graphic#####
        columns = 4


        rows = len(self.datanew)//columns
        if len(self.datanew)%columns != 0:
            rows += 1

        fig = plt.figure()

        for i in range(columns*(rows-1) + len(self.datanew)%columns):

            #Image
            example = self.datanew18[i]
            grads = visualize_saliency(self.model, -1, filter_indices = 0, seed_input=example[...,np.newaxis])


            #Names label
            subplot = fig.add_subplot(rows, columns, self.guessesT18[i])
            subplot.set_ylabel(self.singlenamesnew[i],fontsize = 5, rotation = 35, labelpad=20)


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

            for j in range(len(self.datanew[i,:,1])):
                if self.datanew18[i,j,1] != 0:
                    labels[j] = int(self.datanew18[i,j,1])
                else:
                    labels[j] = ""

            subplot.set_yticklabels(labels, fontsize = 1, rotation = 0)
            subplot.tick_params(axis='y', pad=1)

            #Remove Border
            subplot.spines['top'].set_visible(False)
            subplot.spines['right'].set_visible(False)
            subplot.spines['bottom'].set_visible(False)
            subplot.spines['left'].set_visible(False)

            fig.set_constrained_layout_pads(w_pad=2./72., h_pad=2./72.,
            hspace=0.2, wspace=0.2)


            #Right text
            subplot.text(2,.9, "2018 Prediction- Rk: " + str(self.guessesT[i]), size=2, ha="center",
             transform=subplot.transAxes)
            subplot.text(2,.78, "(Pts: " + str(round(self.pointsG[i],1)) + ")", size=2, ha="center",
             transform=subplot.transAxes)

            subplot.text(2,.6, "Actual Ranking-  Rk: " + str(self.actualT[i]), size=2, ha="center",
              transform=subplot.transAxes)
            subplot.text(2,.48, "(Pts: " + str(round(self.pointsA[i],1)) + ")", size=2, ha="center",
               transform=subplot.transAxes)


            subplot.text(2,.17, "2019 Prediction- Rk: " + str(self.guessesT18[i]), size=2, ha="center",
              transform=subplot.transAxes, fontweight='bold')
            subplot.text(2,.05, "(Pts: " + str(round(self.pointsG18[i],1)) + ")", size=2, ha="center",
                transform=subplot.transAxes, fontweight='bold')


            plt.imshow(example)
            plt.imshow(grads, alpha=.6)

        subplot = fig.add_subplot(rows, columns, i+2)

        plt.xticks([])
        plt.yticks([])

        plt.axis('off')

        plt.suptitle("QB Fantasy Football Predictions")

        plt.savefig('Visualizations/QB-visualization.png', dpi=750)


def main():


    df=pd.read_csv('Data/QBdata.csv', sep=',',header=None)
    a = df.values

    modelname = "Models/QBFantasyNNModel.h5"

    data = Data(a,modelname)
    data.parseData()

    data.trainNN()

    data.testNN()

    #Draw visualization
    data.drawvisualization()
main()
