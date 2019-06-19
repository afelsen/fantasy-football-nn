import random
import os
from keras.models import Sequential
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.optimizers import Adam
import keras
import numpy as np


class FantasyScoreNN():
    cGOODGAMESCORETHRESHOLD=400;
    cLOADBOTPATH="QBFantasyNNModel.h5";
    def __init__(self,iObservationSpaceSize,iActionSpaceSize, data, labels):
        print(iObservationSpaceSize)

        #Observations are The Input For Our Network So Their Size Is Improtant
        self.data = data
        self.labels = labels
        self.mObservationSpaceSize=iObservationSpaceSize;
        self.mActionSpaceSize=iActionSpaceSize;
        #Checks if we already have a Pre-Trained Modal Present
        if(os.path.isfile(self.cLOADBOTPATH)):
            #IF There is Use that Modal
            self.mModel = keras.models.load_model(self.cLOADBOTPATH);
            self.mDoesRequireTraining=False;
        else:
            #If Not Generate Model And Set The Training Flag
            #Simple Model With Fully Connected Layers: Input Is The Observations Output is a Value between 0 To 1
            self.mModel = Sequential();

            self.mModel.add(Conv2D(22, activation='relu',padding='same',kernel_size=(3, 3),input_shape=self.mObservationSpaceSize));
            self.mModel.add(Conv2D(10, activation='relu',padding='same',kernel_size=(5, 5)));

            self.mModel.add(Flatten())
            self.mModel.add(Dense(64, activation='relu'));
            self.mModel.add(Dense(1, activation='linear'));
            self.mModel.compile(loss='mse', optimizer=Adam());


            # self.mModel.add(Dense(32, activation='relu', input_shape=self.mObservationSpaceSize));
            # self.mModel.add(Dense(16, activation='relu'));
            # self.mModel.add(Dense(8, activation='relu'));
            # self.mModel.add(Dense(4, activation='relu'));
            # self.mModel.add(Flatten())
            # self.mModel.add(Dense(1, activation='linear' ));
            # self.mModel.compile(loss='mse', optimizer=Adam());
            self.mDoesRequireTraining=True;
    def Train(self):
        #Run With RandomBot

        vTrainingDataFeatures = []
        vTrainingDataResults = []

        # vAllActions=vEnv.guess(500,vRandomBot);
        # for i in range(len(vAllActions)):
        #     if abs(vAllActions[i]-self.labels[i]) < 100:
        #         vTrainingDataFeatures.append(self.data[i])
        #         vTrainingDataResults.append(vAllActions[i])



        #Input Had To Be A NumPy Array
        # vTrainingData=np.array(vTrainingDataFeatures);
        # vTrainingLabels=np.array(vTrainingDataResults);
        #
        # print(vTrainingData)
        # print(vTrainingLabels)


        vTrainingData = self.data
        vTrainingLabels = self.labels

        #This Is Where Model IS Trained
        self.mModel.fit(vTrainingData,vTrainingLabels,epochs=150);
        #Saving The Trained Model
        self.mModel.save(self.cLOADBOTPATH);
        self.mDoesRequireTraining=False;


    def GetAction(self,iObservations):
        #Ask Network For An Output
        iObservations = np.expand_dims(iObservations, axis=0)
        vPredictionResult=self.mModel.predict(iObservations);
        return vPredictionResult[0][0];
