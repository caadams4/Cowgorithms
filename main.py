listCows = {}

def recordWeight(id, weight):     # number of operations = 4
  listCows[id]['latestWeight'] = weight
  cowLowestWeight = listCows[id]['lowestWeight']
  if cowLowestWeight > weight or cowLowestWeight == 0:
    listCows[id]['lowestWeight'] = weight
  return

def recordMilk(id, milk):    # number of operations = 3
  listCows[id]['totalMilkProd'] = listCows[id]['totalMilkProd'] + milk
  listCows[id]['milkings'] = listCows[id]['milkings'] + 1
  listCows[id]['averageMilkProd'] = (listCows[id]['totalMilkProd']) / listCows[id]['milkings']
  return

def buildLowestWeightsDict():
  #-------#------- 
  # Sorting based on lowest weight
  
  sortedLowestWeightList = sorted(newList, key = lambda item: item['lowest']) # 1
  for i in sortedLowestWeightList: # number of operations = c + 7
    lowest = i['lowest']
    if lowest in sortedWeightDict:
      sortedWeightDict[lowest]['cowLowestData'].append({'id':i['id'],'latest':i['latest'],'milk':i['milk']})

      
      lowestWeightDuplicates.append(lowest)
    else:
      cowDataList = [{'id':i['id'],'latest':i['latest'],'milk':i['milk']}]
      sortedWeightDict[lowest] = {
      'cowLowestData': cowDataList
    }
  
  #-------#-------
  # Sorting lowest weight duplicates by latest weight

  
  for i in lowestWeightDuplicates: 

    sortedWeightDict[i]['cowLowestData'] = sorted(sortedWeightDict[i]['cowLowestData'], key = lambda item: item['latest'])

    print(sortedWeightDict[i]['cowLowestData'])
    newNode = {}
    newNodeLatest = []
    
    for j in sortedWeightDict[i]['cowLowestData']:
      newNodeLatest.append({'id':j['id'],'milk':j['milk']})
      newNode[j['latest']] = {
        'cowLatestData': newNodeLatest
      }
    
    for latestWeight in newNode.values():
      
      latestWeight['cowLatestData'] = sorted(latestWeight['cowLatestData'], key = lambda item: item['milk'])
    
    sortedWeightDict[i] = newNode
  
  return 



with open('cowData4.txt') as file:
  contents = file.read()
  cowListRaw = contents.split('\n')
  rows = len(cowListRaw)
  
  for i in range(rows):
    incomingCow = cowListRaw[i].split(' ')    
    id = incomingCow[0]
    actionCode = incomingCow[1]
    actionNum = int(incomingCow[2])

    if id not in listCows:        # ROWS * 1
      listCows[id] = { 
          'lowestWeight': 0,
          'latestWeight': 0,
          'averageMilkProd': 0,  
          'totalMilkProd': 0,
          'milkings':0,
        }
      
    if actionCode == 'W':
      recordWeight(id, actionNum)
    elif actionCode == 'M':
      recordMilk(id, actionNum)

  newList = []
  
  for c in listCows.items():
    if c[1]['lowestWeight'] != 0 and c[1]['averageMilkProd'] != 0: 
      newList.append({'id':c[0],'lowest':c[1]['lowestWeight'],'latest':c[1]['latestWeight'],'milk':c[1]['averageMilkProd']})


sortedWeightDict = {}

lowestWeightDuplicates = []   # Tracks items with duplicate lowest weights to later sort latest weights

buildLowestWeightsDict()

#for key in sortedWeightDict.values():
  #print(key)
  
#with open('output.txt', 'w') as f:
#    f.write(output)
    
