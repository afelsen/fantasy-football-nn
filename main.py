from data import Data
import pandas as pd

def main():

    positions = ["QB", "RB", "WR", "TE"]
    position = positions[2]

    df=pd.read_csv('Data/' + position + 'data.csv', sep=',',header=None)
    a = df.values

    modelname = "Models/" + position + "FantasyNNModel.h5"

    data = Data(a,modelname)
    data.parseData()
    data.trainNN()

    data.testNN()

    #Draw visualization
    data.drawvisualization(position)
main()
