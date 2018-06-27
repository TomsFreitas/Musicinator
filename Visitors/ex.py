from midiutil import MIDIFile
from math import ceil
import sys
import copy

bpm = 160
midi = MIDIFile(numTracks=1000, file_format=1)
midi.addTempo(0,0,bpm)
currtrack = 0
longest = 0

bass = [44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44]
piano = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
violin = [41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41]
porcoespinho = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
drums = [119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119]
guitar = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
cello = [43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43]
tamborBarulhento = 60

def addnotes(notes):
    time = notes[0] #When the sequence will start time wise
    temp = 1 #default instrument
    global currtrack #we want the global scope of this variable
    duration(notes)

    repeat_times = (int)(notes[len(notes)-1])

    for x in range(len(time)):
        initialTime = time[x] - duration(notes[1])
        for _ in range(repeat_times):
            initialTime += duration(notes[1])
            for i in range(0, len(notes[1])):
                try:
                    note = notes[1][i][0] #getting the note
                    noteDur = notes[1][i][1] #duration of the note
                    toInsert = notes[1][i][3] + initialTime
                    if note < 0:
                        continue

                except:
                    pass

                try: #trying for instrument change
                    instrument = notes[1][i][2] #checking for instrument
                    if(instrument != temp):
                        midi.addProgramChange(currtrack, 0, toInsert, instrument) #changing the current instrument
                        temp = instrument
                except:
                    instrument = temp #it keeps the old instrument
                    pass

                midi.addNote(currtrack,0,note,toInsert,noteDur,100)

                print("Added note {}, with instument {} with a duration of {} on time {}, on channel {}".format(note, instrument, noteDur, (toInsert*(85/bpm)), currtrack))
        currtrack += 1

def getInt(varstr):
    while True:
        try:
            a = int(input(varstr))
        except ValueError:
            print("Please input a valid number")
            continue
        else:
            break
    return a

def duration(toCheck):
    if len(toCheck) == 0:
        return 0
    if type(toCheck[0]) is tuple:
        size = len(toCheck)-1
        return toCheck[0][3] + toCheck[size][3] + toCheck[size][1]
    else:
        if len(toCheck[1]) == 0:
            return 0
        size = len(toCheck[1]) - 1
        return toCheck[1][0][3] + toCheck[1][size][3] + toCheck[1][size][1]

def modPitch(toMod, ModNumber):
    modded = []
    if type(toMod[0]) is tuple:
        for tup in toMod:
            newPitch = tup[0] + ModNumber
            try:
                if newPitch < 0:
                    raise ValueError
            except ValueError:
                print("Modulated note below 0, expect silence")
                pass
            newtup = (newPitch, tup[1],tup[2],tup[3])
            modded.append(newtup)
        return modded
    else:
        temp = copy.deepcopy(toMod)
        for tup in toMod[1]:
            newPitch = tup[0] + ModNumber
            try:
                if newPitch < 0:
                    raise ValueError
            except ValueError:
                print("Modulated note below 0, expect silence")
                pass
            newtup = (newPitch, tup[1],tup[2],tup[3])
            modded.append(newtup)
        temp[1] = modded
        return temp


def modTempo(toMod, ModNumber):
    modded = []
    if type(toMod[0]) is tuple:
        for tup in toMod:
            newTempo = tup[1] * ModNumber
            newtup = (tup[0], newTempo,tup[2],tup[3])
            modded.append(newtup)
        return modded
    else:
        temp = copy.deepcopy(toMod)
        for tup in toMod[1]:
            newTempo = tup[1] * ModNumber
            newtup = (tup[0], newTempo,tup[2],tup[3])
            modded.append(newtup)
        temp[1] = modded
        return temp

def extendseq(original, toextend):
    modded = []
    if len(original) == 0:
        for tup in toextend:
            newtup = (tup[0], tup[1], tup[2], 0)
            modded.append(newtup)
        return modded
    else:
        for tup in original:
            modded.append(tup)
        time = duration(original)
        for tup in toextend:
            newtup = (tup[0], tup[1], tup[2], time)
            modded.append(newtup)
        return modded

def appendseq(original, toappend):
    offsetTime = duration(original)
    for tup in toappend:
        newTime = tup[3] + offsetTime
        newtup = (tup[0],tup[1],tup[2],newTime)
        original.append(newtup)
    return original

def setinstrument(seq,nome):
    if len(seq)==0:
        return seq
    newseq = []
    for tup in seq:
        new = (tup[0],tup[1],nome[tup[0]],tup[3])
        newseq.append(new)
    return newseq

def prepplay(perf):
    global longest #we want the global scope of this variable
    perf_duration = max(perf[0])+duration(perf[1]) * perf[2]
    if perf_duration > longest:
        longest = perf_duration
    return perf

def preploop(perf):
    global longest #we want the global scope of this variable
    repeats = longest/duration(perf[1])
    perf[2] = ceil(repeats)
    return perf

def offsetstart(perf, offset):
    originaltime = perf[0][0]
    perf[0] = offset
    for i in range(0,len(perf[0])):
        perf[0][i] += originaltime
    return perf


############################ LINE = 2
_0 = []
_1 = [(62,1.0,-1,-1)]
_0 = extendseq(_0, _1)
_2 = [(62,1.0,-1,-1)]
_0 = extendseq(_0, _2)
_3 = [(62,1.0,-1,-1)]
_0 = extendseq(_0, _3)
_4 = [(64,0.5,-1,-1)]
_0 = extendseq(_0, _4)
_5 = [(65,0.5,-1,-1)]
_0 = extendseq(_0, _5)
_6 = [(65,1.0,-1,-1)]
_0 = extendseq(_0, _6)
_7 = [(64,0.5,-1,-1)]
_0 = extendseq(_0, _7)
_8 = [(65,0.5,-1,-1)]
_0 = extendseq(_0, _8)
_9 = [(67,0.5,-1,-1)]
_0 = extendseq(_0, _9)
_10 = [(69,2.0,-1,-1)]
_0 = extendseq(_0, _10)
_11 = [(62,0.33,-1,-1)]
_0 = extendseq(_0, _11)
_12 = [(62,0.33,-1,-1)]
_0 = extendseq(_0, _12)
_13 = [(62,0.33,-1,-1)]
_0 = extendseq(_0, _13)
_14 = [(69,0.33,-1,-1)]
_0 = extendseq(_0, _14)
_15 = [(69,0.33,-1,-1)]
_0 = extendseq(_0, _15)
_16 = [(69,0.33,-1,-1)]
_0 = extendseq(_0, _16)
_17 = [(65,0.33,-1,-1)]
_0 = extendseq(_0, _17)
_18 = [(65,0.33,-1,-1)]
_0 = extendseq(_0, _18)
_19 = [(65,0.33,-1,-1)]
_0 = extendseq(_0, _19)
_20 = [(62,0.33,-1,-1)]
_0 = extendseq(_0, _20)
_21 = [(62,0.33,-1,-1)]
_0 = extendseq(_0, _21)
_22 = [(62,0.33,-1,-1)]
_0 = extendseq(_0, _22)
_23 = [(69,1.0,-1,-1)]
_0 = extendseq(_0, _23)
_24 = [(67,1.0,-1,-1)]
_0 = extendseq(_0, _24)
_25 = [(65,1.0,-1,-1)]
_0 = extendseq(_0, _25)
_26 = [(64,1.0,-1,-1)]
_0 = extendseq(_0, _26)
_27 = [(62,1.0,-1,-1)]
_0 = extendseq(_0, _27)
row_your_boat = _0
############################ LINE = 9
_28 = setinstrument(row_your_boat, violin)
_28 = [[-1], _28, -1]
p_boat = _28
############################ LINE = 11
_29 = []
_30 = [(69,1.0,-1,-1)]
_29 = extendseq(_29, _30)
_31 = [(67,1.0,-1,-1)]
_29 = extendseq(_29, _31)
_32 = [(71,1.0,-1,-1)]
_29 = extendseq(_29, _32)
_33 = [(71,1.0,-1,-1)]
_29 = extendseq(_29, _33)
s = _29
############################ LINE = 12
_34 = []
_35 = [(67,1.0,-1,-1)]
_34 = extendseq(_34, _35)
_36 = [(67,1.0,-1,-1)]
_34 = extendseq(_34, _36)
_37 = [(60,0.5,-1,-1)]
_34 = extendseq(_34, _37)
_38 = [(60,0.5,-1,-1)]
_34 = extendseq(_34, _38)
_34 = appendseq(_34, s)
_34 = appendseq(_34, s)
_39 = [(71,1.0,-1,-1)]
_34 = extendseq(_34, _39)
_40 = [(69,1.0,-1,-1)]
_34 = extendseq(_34, _40)
_41 = [(67,1.0,-1,-1)]
_34 = extendseq(_34, _41)
_42 = [(60,0.5,-1,-1)]
_34 = extendseq(_34, _42)
pombinhas_inicio = _34
############################ LINE = 13
_43 = []
_43 = appendseq(_43, pombinhas_inicio)
_43 = appendseq(_43, pombinhas_inicio)
pombinhas_inicio2x = _43
############################ LINE = 14
_44 = []
_45 = [(64,1.0,-1,-1)]
_44 = extendseq(_44, _45)
_46 = [(64,1.0,-1,-1)]
_44 = extendseq(_44, _46)
_47 = [(67,1.0,-1,-1)]
_44 = extendseq(_44, _47)
_48 = [(64,1.0,-1,-1)]
_44 = extendseq(_44, _48)
_49 = [(67,1.0,-1,-1)]
_44 = extendseq(_44, _49)
_50 = [(64,1.0,-1,-1)]
_44 = extendseq(_44, _50)
_51 = [(62,1.0,-1,-1)]
_44 = extendseq(_44, _51)
_52 = [(62,1.0,-1,-1)]
_44 = extendseq(_44, _52)
_53 = [(65,1.0,-1,-1)]
_44 = extendseq(_44, _53)
_54 = [(65,1.0,-1,-1)]
_44 = extendseq(_44, _54)
_55 = [(64,1.0,-1,-1)]
_44 = extendseq(_44, _55)
_56 = [(64,1.0,-1,-1)]
_44 = extendseq(_44, _56)
_57 = [(62,1.0,-1,-1)]
_44 = extendseq(_44, _57)
_58 = [(62,1.0,-1,-1)]
_44 = extendseq(_44, _58)
_59 = [(60,2.0,-1,-1)]
_44 = extendseq(_44, _59)
pombinhas_refrao = _44
############################ LINE = 15
_60 = []
_60 = appendseq(_60, pombinhas_refrao)
_60 = appendseq(_60, pombinhas_refrao)
pombinhas_refrao2x = _60
############################ LINE = 17
_61 = [pombinhas_inicio,pombinhas_inicio,pombinhas_refrao,pombinhas_refrao,pombinhas_inicio,pombinhas_inicio,pombinhas_refrao,pombinhas_refrao]
sequences = _61
############################ LINE = 19
_62 = [piano,guitar,bass,drums]
band = _62
############################ LINE = 20
_63 = 0
num = _63
############################ LINE = 21
for s in sequences:
	############################ LINE = 23
	_65 = 1
	_64 = num+_65
	num = _64
	############################ LINE = 24
	_68 = 3
	_67 = num>_68
	_66 = _67
	if _66:
		############################ LINE = 25
		_69 = 0
		num = _69
############################ LINE = 29
_70 = 0
_71 = p_boat
_71[0] = [0]
_71[2] = 1
_71 = prepplay(_71)
addnotes(_71)
############################ LINE = 30
_72 = setinstrument(pombinhas_inicio, piano)
_72 = [[-1], _72, -1]
_73 = 0
_74 = _72
_74[0] = [0]
_74[2] = 1
_74 = prepplay(_74)
_76 = duration(p_boat)
_77 = 5
_75 = _76+_77
_79 = setinstrument(pombinhas_inicio, piano)
_79 = [[-1], _79, -1]
_80 = 0
_81 = _79
_81[0] = [0]
_81[2] = 1
_81 = prepplay(_81)
_78 = _79
_78 = offsetstart(_78, [_75])
_78 = prepplay(_78)
addnotes(_78)

with open("out.mid", 'wb') as file:
    midi.writeFile(file) #Writting the file
    print("MIDI File Written")
