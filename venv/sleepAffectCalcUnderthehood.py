class processAlg():
    def processAlgIdealDeviation(idealsleeptime,avgweeksleeptime,lastnightsleeptime):
        #derives relevant variables from three initial points of data
        if(idealsleeptime>lastnightsleeptime):
            undersleep=idealsleeptime-lastnightsleeptime
        elif(idealsleeptime<lastnightsleeptime):
            oversleep=avgweeksleeptime-lastnightsleeptime
        if(idealsleeptime>avgweeksleeptime):
            totalweeksleeptime=((idealsleeptime-avgweeksleeptime)*7)
        elif (idealsleeptime < avgweeksleeptime):
            totalweeksleeptime = ((avgweeksleeptime-idealsleeptime) * 7)
        else:print("invalid")