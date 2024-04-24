#!/bin/python3

import os
import random
import re
import sys

#
# INCLUDE all functions for PARTS 1, 2, 3, 4, 5, 6 and 7 below.
#
#

"""
Group Information:
Member 1: 620163342 
Member 2: 620157851
"""


#Part 1
def makePatient(age,sex,trestbps, chol,fbs,thalach,oldpeak):
    return ("HDPT",{"age":age,"sex":sex,"trestbps":trestbps,"chol":chol,"fbs":fbs,"thalach":thalach,"oldpeak":oldpeak})

def patientInfo(pt):
    if isPatient(pt):
        return pt[1]
    else:
        return "Error: Not a patient"

def getPatientAge(pt):
    if isPatient(pt):
        if not isEmptyPt(pt):
            return patientInfo(pt)["age"]
        else:
            return "Dictionary is Empty"
    else:
        return "Error: Not a patient"

def getPatientSex(pt):
    if isPatient(pt):
        if not isEmptyPt(pt):
            return patientInfo(pt)["sex"]
        else:
            return "Dictionary is Empty"
    else:
        return "Error: Not a patient"

def getPatientTres(pt):
    if isPatient(pt):
        if not isEmptyPt(pt):
            return patientInfo(pt)["trestbps"]
        else:
            return "Dictionary is Empty"
    else:
        return "Error: Not a patient"

def getPatientChol(pt):
    if isPatient(pt):
        if not isEmptyPt(pt):
            return patientInfo(pt)["chol"]
        else:
            return "Dictionary is Empty"
    else:
        return "Error: Not a patient"

def getPatientFbs(pt):
    if isPatient(pt) and not isEmptyPt(pt):
        return patientInfo(pt)["fbs"]
    else:
        return "Error: Not a patient"

def getPatientTlach(pt):
    if isPatient(pt):
        if not isEmptyPt(pt):
            return patientInfo(pt)["thalach"]
        else:
            return "Dictionary is Empty"
    else:
        return "Error: Not a patient"

def getPatientST(pt):
    if isPatient(pt):
        if not isEmptyPt(pt):
            return patientInfo(pt)["oldpeak"]
        else:
            return "Dictionary is Empty"
    else:
        return "Error: Not a patient"

def isPatient(pt):
    return pt[0]=="HDPT" and type(pt[1])==type({})

def isEmptyPt(pkt):
    return patientInfo(pkt) == {}


#Part 2
def isHypertensive(age,sex,trestbps):
    if 1 <= age <= 3:
        if (sex == "male" or sex == "M") or (sex == "female" or sex == "F") :#to take out
            if trestbps >= 98:
                return True
            else:
                return False
    elif age >= 4:
        if (sex == "male" or sex == "M") or (sex == "female" or sex == "F") :#to take out
            if trestbps >= 140:
                return True
            else:
                return False
    return False

def hasHighCholesterol(chol):
    return chol >= 220

def isPhysicallyInactive(thalach, sex, age):
    if (sex=="male" and age >= 35 and thalach>=220) or (sex=="M" and age >= 35 and thalach>=220)or (sex=="female" and age >= 35 and thalach>=226) or (sex=="F" and age >= 35 and thalach>=226):
        return True
    if (sex=="male" and age < 35 and thalach>=230) or (sex=="M" and age < 35 and thalach>=230) or (sex=="female" and age < 35 and thalach>=236) or (sex=="F" and age < 35 and thalach>=236):
        return True
    return False

#Part 3
def calcPScore(pt):
    score = 0.0
    if isHypertensive(getPatientAge(pt),getPatientSex(pt),getPatientTres(pt)):
        score += 4
    if hasHighCholesterol(getPatientChol(pt)):
        score += 3
    if isPhysicallyInactive(getPatientTlach(pt), getPatientSex(pt), getPatientAge(pt)):
        score += 2
    if getPatientSex(pt) == "male" or getPatientSex(pt) == "M":
        score += 1.5
    if getPatientSex(pt) == "female" or getPatientSex(pt) == "F":
        score += 1
    return score
    
def makePscore(ptLst):
    return ["PS",[]]

def getSLst(Pscore):
    return Pscore[1]

def addPatient(PSLst,pt):
    getSLst(PSLst).append((pt,calcPScore(pt)))

#might have an issue
def getCritical(Score):
    return [i[0] for i in getSLst(PSLst) if i[1] >= Score]

def getNonCrit(Score):
    return [i[0] for i in getSLst(PSLst) if i[1] <= Score]

def isScore(Score):
    return type(Score) == float

def isEmptyScore(Score):
    #print("-",getSLst(PSLst))
    
    return Score == len(ptScores(PSLst))

def ptScores(PSLst):
    #Selector
    #This function takes a Score List and returns the list of patient and scores (without the tag) i.e. PSLst[1]
    return PSLst[1]

#Part 4
    
def makePtQueue(Qtype):
    if Qtype == 1:
        return ("C-Q",[])
    elif Qtype == 2:
        return ("N-Q",[])
    elif Qtype == 3:
        return ("W-Q",[])

def contentsQ(q):
    if isPatientQ(q):
        return q[1]
    else:
        return "Error: Not a patient queue"

def frontPtQ(q):
    if isPatientQ(q):
        if isEmptPtQ(q):
            return "Queue is empty"
        else:
            return contentsQ(q)[0]
    else:
        return "Error: Not a patient queue"

def addToPtQ(pt,q):
    if isPatientQ(q):
        return contentsQ(q).append(pt)
    else:
        return "Error: Not a patient queue"

def removeFromPtQ(q):
    if isPatientQ(q):
        if isEmptPtQ(q):
            return "Queue is empty"
        else:
            return contentsQ(q).pop(0)
    else:
        return "Error: Not a patient queue"

def isPatientQ(q):
    return q[0] in ["C-Q","N-Q","W-Q"] and type(q) == type(())

def isEmptPtQ(q):
    return q[1] == []

#Part 5

def makePatientStack():
    return ("HDS", [])

def contentsStack(stk):
    if isPtStack(stk):
        return stk[1]
    else:
        return "Error: Not a stack"

def topPtStack(stk):
    if isPtStack(stk):
        if isEmptyPtStack(stk):
            return "Stack is empty"
        else:
            return contentsStack(stk)[0]
    else:
        return "Error: Not a patient queue"

def pushPtStack(pkt, stk):
    if isPtStack(stk):
        contentsStack(stk).insert(0, pkt)
    else:
        return "Error: Not a patient queue"

def popPtStack(stk):
    if isPtStack(stk):
        if isEmptyPtStack(stk):
            return "Stack is empty"
        else:
            contentsStack(stk).pop(0)
    else:
        return "Error: Not a patient queue"

def isPtStack(stk):
    return type(stk) == type(()) and stk[0] == 'HDS' 

def isEmptyPtStack(stk):
    return contentsStack(stk) == []

#Part 6

def sortPatients(patientList, patientStack, patientQueue):
    if patientQueue[0] == "C-Q":
        critPTq = getCritical(7.0001)
        critPTstk = getCritical(7.0001)
        #print("crit pt: ",critPT)
        critPTq.sort(key = lambda x : calcPScore(x), reverse = True)
        critPTstk.sort(key = lambda x : calcPScore(x))
        #print("crit pt sorted: ",critPT)

        #for i in range(len(critPTq)):
            #removeFromPtQ(patientQueue)
            
        for i in critPTq:
            addToPtQ(i,patientQueue)
        
        #print("patient q: ",patientQueue)
        #for i in range(len(critPTstk)):
            #popPtStack(patientStack)
        
        for i in critPTstk:
            pushPtStack(i,patientStack)
        #print("patient stk: ",patientStack)
        
    elif patientQueue[0] == "N-Q":
        noncritPTq = getNonCrit(4.9999)
        noncritPTq.sort(key = lambda x : calcPScore(x), reverse = True)
        #for i in range(len(noncritPTq)):
            #removeFromPtQ(patientQueue) 
        for i in noncritPTq:
            addToPtQ(i,patientQueue)
    elif patientQueue[0] == "W-Q":
        getWatchList = list(filter(lambda x : 5.0<= calcPScore(x) <= 7.0, patientList))
        getWatchList.sort(key = lambda x : calcPScore(x), reverse = True)
        #for i in range(len(getWatchList)):
            #removeFromPtQ(patientQueue)
        for i in getWatchList:
            addToPtQ(i,patientQueue)

#Part 7   

def analyzePatients(patient_lst):
    patients = []
    scoreLst = makePscore(patient_lst)

    #print(scoreLst)
    for i in patient_lst:
        age = i[0]
        sex = i[1]
        trestbps = i[2]
        chol = i[3]
        fbs = i[4]
        thalach = i[5]
        oldpeak = i[6]
        patients.append(makePatient(age , sex, trestbps, chol, fbs, thalach, oldpeak))
    #print(patients)
        
    for j in patients:
        #print("-",j)
        addPatient(scoreLst,j)
    #print(scoreLst)
        
    critStack = makePatientStack()
    critQueue = makePtQueue(1)
    noncritQueue = makePtQueue(2)
    watchQueue = makePtQueue(3)   
    sortPatients(patients, critStack, critQueue)
    sortPatients(patients, critStack, noncritQueue)
    sortPatients(patients, critStack, watchQueue) 
    
    return critQueue[1]+  watchQueue[1] + noncritQueue[1]

#Part 8
if __name__ == '__main__':
    number_of_patients = int(input())

    ip_lst = []
    for i in range(number_of_patients):
        ip_info = input().strip().split()
        ip_tup = (int(ip_info[0]), ip_info[1], int(ip_info[2]), \
                               int(ip_info[3]), int(ip_info[4]), int(ip_info[5]), float(ip_info[6]))
        ip_lst += [ip_tup]
        
    print(ip_lst)

    p_lst = []
    for ip_info in ip_lst:
        p_lst += [makePatient(int(ip_info[0]), ip_info[1], int(ip_info[2]), \
                           int(ip_info[3]), int(ip_info[4]), int(ip_info[5]), float(ip_info[6]))]
    PSLst = makePscore(p_lst)
    for p in p_lst:
        addPatient(PSLst,p)

    fQueue = analyzePatients(ip_lst)
    print(fQueue)
    print(calcPScore(fQueue[-1]))
    print(calcPScore(fQueue[0]))
