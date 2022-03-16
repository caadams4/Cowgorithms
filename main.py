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


sortedCowList = sorted(newList, key = lambda item: item['lowest'])

sortingLatestWeight = []
cowRecords = len(sortedCowList)

for i in range(cowRecords):
  sortingLatestWeight = []
  sortedCowListDuplicates = []
  #print(sortedCowList[i]['lowest'])
  if i < cowRecords-1:
    if sortedCowList[i]['lowest'] == sortedCowList[i+1]['lowest']: 
        # check for duplicate lowest weight in the next index
      j = i
      while sortedCowList[j]['lowest'] == sortedCowList[i]['lowest']:    
          # if duplicate found, record duplicates until non duplicate is found
        sortingLatestWeight.append(sortedCowList[j])  # copy duplicates into new list
        j = j+1
      sortedCowListDuplicates = sorted(sortingLatestWeight, key = lambda item: item['latest']) 
        # sort the  duplicate *lowest weights* by their *latest weight*
      cowLatestDuplicates = len(sortedCowListDuplicates)

      print('yeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
      
      
      for k in range(cowLatestDuplicates):
        sortMilkProd = []
        sortingMilk = []
        if k < cowLatestDuplicates-1:
          
          #print(sortedCowListDuplicates[k])
          if sortedCowListDuplicates[k]['latest'] == sortedCowListDuplicates[k+1]['latest']:
            print('hi')
            l = k
            while sortedCowListDuplicates[k]['latest'] == sortedCowListDuplicates[l]['latest']:
              print('bruh')
              sortingMilk.append(sortedCowListDuplicates[l])
              l=l+1
            sortMilkProd = sorted(sortingMilk, key = lambda item: item['milk'])
            print(k,l)
            sortedCowListDuplicates[k+1:l] = sortMilkProd
            print('dups',sortedCowListDuplicates)
            print('milksort',sortMilkProd)
        # now, check for duplicate latest weights and sort by thier milk production

      #sortedCowListDuplicates[k:l] = sortMilkProd
      #print(sortMilkProd)
      #print(sortedCowListDuplicates)
      
      sortedCowList[i:j] = sortedCowListDuplicates
      i=j-1
      
      # insert similar lowest weights back into the original sorted list, sorted by thier latest weights
    
      

# check for duplicate lowest weights
#for x in sortedCowList:
 # print(x)
  