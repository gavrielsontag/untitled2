import sleepAffectCalcUnderthehood
def main():
 #where the data will be entered
 iSleepAm=int(input("ideal sleep amount \n"))
 aSleepAm = int(input("avg sleep amount \n"))
 lSleepAm = int(input("amount slept previous night\n"))
 #method call
 sleepAffectCalcUnderthehood.processAlg.processAlgIdealDeviation(iSleepAm,aSleepAm,lSleepAm)
 

if __name__ == '__main__':
    main()
    
