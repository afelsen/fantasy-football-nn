
def main():

    file = open("Data/ESPNRankings.txt")

    QB = open("Data/QBdataESPN.txt",'w')
    RB = open("Data/RBdataESPN.txt",'w')
    WR = open("Data/WRdataESPN.txt",'w')
    TE = open("Data/TEdataESPN.txt",'w')


    QBrank = {}
    RBrank = {}
    WRrank = {}
    TErank = {}


    for line in file:

        for i in range(len(line)):
            if line[i:i+3] == "(QB":
                digits = line[i+3:].index(")")

                j = i + digits + 5
                name = ""
                while line[j] != ',':
                    name += line[j]
                    j+=1

                QBrank[int(line[i+3:i+3+digits])] = name


            elif line[i:i+3] == "(RB":
                digits = line[i+3:].index(")")

                j = i + digits + 5
                name = ""
                while line[j] != ',':
                    name += line[j]
                    j+=1

                RBrank[int(line[i+3:i+3+digits])] = name

            elif line[i:i+3] == "(WR":
                digits = line[i+3:].index(")")

                j = i + digits + 5
                name = ""
                while line[j] != ',':
                    name += line[j]
                    j+=1

                WRrank[int(line[i+3:i+3+digits])] = name

            elif line[i:i+3] == "(TE":
                digits = line[i+3:].index(")")

                j = i + digits + 5
                name = ""
                while line[j] != ',':
                    name += line[j]
                    j+=1

                TErank[int(line[i+3:i+3+digits])] = name

    for i in range(1,len(QBrank)+1):
        QB.write(QBrank[i] + '\n')

    for i in range(1,len(RBrank)+1):
        RB.write(RBrank[i] + '\n')

    for i in range(1,len(WRrank)+1):
        WR.write(WRrank[i] + '\n')

    for i in range(1,len(TErank)+1):
        TE.write(TErank[i] + '\n')

    QB.close()
    RB.close()
    WR.close()
    TE.close()


main()


#Data from: https://g.espncdn.com/s/ffldraftkit/18/NFLDK2018_CS_PPR300.pdf
