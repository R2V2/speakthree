string = "Word."
string3 = "Every word speaks."
string7 = "While every magic word known speaks three."
string15 = "A while ago every banished magic resembled word he'd known often speaks with three sisters."
string31 = "Not a long while bla ago bla every bla banished bla magic bla resembled bla word bla he'd bla known bla often bla speaks bla with bla three bla sisters bla."
string63 = "bla Not bla a bla long bla while bla bla bla ago bla bla bla every bla bla bla banished bla bla bla magic bla bla bla resembled bla bla bla word bla bla bla he'd bla bla bla known bla bla bla often bla bla bla speaks bla bla bla with bla bla bla three bla bla bla sisters bla bla bla."


def stroll(df):
    length = len(df) - 1
    middle = length//2 
    if len(df) != 3:
        pre = df[:middle]
        post = df[middle+1:]
        length = len(pre) - 1
        middleHalves = length//2 
        keter = [df[middle], [stroll(pre), stroll(post)]]
        return keter
    else:
        keter = [df[1], [df[0], df[2]]]
        return keter
    
def firstPass(string):
    words = [[word] for word in string.split(" ")]
    length = len(words) - 1
    middle = length//2
    if len(words) != 3:
        temp = []
        temp.append([words[middle]])
        temp.append([])
        for word in words[:middle]:
            temp[1].append(word)
        for word in words[middle:]:
            temp[1].append(word)
        return stroll(temp[1])
    else:
        temp = [words[1], [words[0], [words[1]], words[2]]]
        return temp


def flatten(ls):
    flatList = []
    for item in ls:
        if type(item)!=str:
            for sub in item:
                flatList.append(sub)
        else:
            flatList.append(item)
    return flatList

def prettify(ls):
    words = flatten(ls)
    sentence = " ".join(words).capitalize()
    if sentence.endswith("."):
        return sentence
    else:
        return sentence + "." 

def abra(df):
    ind = 0
    currentLayer = [[df[0]]]
    replace = df.index(df[0])
    newStruct = df[1]
    newLayer = currentLayer
    newLayer.insert(replace+1,newStruct[1])
    newLayer.insert(replace-2,newStruct[0])
    words = [x[0] for x in newLayer]
    return newLayer
        
def speakThree(struct, pos):
    ind = pos - 1
    currentLayer = struct
    replace = currentLayer.index(currentLayer[ind])
    newStruct = [currentLayer[ind]]
    before = newStruct[0][1][0]
    after = newStruct[0][1][1]
    newStruct.append([after])
    newStruct.insert(0,[before])
    words = [x[0] for x in newStruct]

    del (currentLayer[ind])
    counter = 0
    for word in words:
        if counter == 1:
            currentLayer.insert(ind+counter,[word])
        else:
            currentLayer.insert(ind+counter,word)
        counter += 1
    return currentLayer


#get this to work and you're done I think! (well, then there's the GUI :/ )
def fold(df, pos):
    ind = pos-1
    if len([x[0] for x in df]) == 1:
        ind = 1
        preWord = currentLayer[:ind]
        postWord = currentLayer[ind+1:]

        newLayer = currentLayer[ind]
        print(newLayer)
        newLayer.append([])
        newLayer[1].insert(0,preWord)
        print(newLayer)
        newLayer[1].insert(1,postWord)
        print(newLayer)
        words = [x[0] for x in newLayer]
        return newLayer
    elif ind-1 == 0:
        preWord = df[:ind-2]
        postWord = df[ind+2:]
        newLayer = [df[ind]]
        if ind == 1:
            newLayer[0].insert(1,[])
            newLayer[0][1].insert(0,df[ind-1])
            newLayer[0][1].insert(1,df[ind+1])
            for word in postWord:
                newLayer.append(word)
            return newLayer
    elif pos == len([x[0] for x in df])-1:
        preWord = df[:ind-1]
        postWord = df[ind+2:]
        ws = [df[ind]]
        ws[0].insert(1,[])
        ws[0][1].insert(0,df[ind-1])
        ws[0][1].insert(1,df[ind+1])
        newLayer = []
        for word in preWord:
            newLayer.append(word)
        newLayer.append(ws[0])
        for word in postWord:
            newLayer.append(word)
        return newLayer
    else:
        target = speakMore(speakThree(firstPass(string15)),1)
        df = speakMore(speakMore(speakThree(firstPass(string15)),1),3)
        ind = 4-1
        preWord = df[:ind-1]
        postWord = df[ind+2:]
        ws = [df[ind]]
        ws[0].insert(1,[])
        ws[0][1].insert(0,df[ind-1])
        ws[0][1].insert(1,df[ind+1])
        newLayer = []
        for word in preWord:
            newLayer.append(word)
        newLayer.append(ws[0])
        for word in postWord:
            newLayer.append(word)
        return newLayer


def moveOld(struct):
    num = int(input("Which word?"))
    direction = input("Which direction?")
    if direction == "down":
        newStruct = speakMore(struct, num)
        print(prettify([x[0] for x in newStruct]))
    if direction == "up":
        newStruct = fold(struct, num)
        print(prettify([x[0] for x in newStruct]))


def traverse(struct = firstPass(string15)):
    print(prettify(struct[0]))
    three = speakThree(struct)
    move(three)

def move(struct, pos):
    dir = len(struct[pos-1])
    if dir == 2:
        newStruct = speakThree(struct, pos)
        return newStruct
    if dir == 1:
        newStruct = fold(struct, pos)
        return newStruct
