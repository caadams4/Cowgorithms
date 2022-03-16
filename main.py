

def recordWeight(id, weight):     # Records latest weight and compares to the lowest recorded cow weight to the cow-ID-specific record
  listCows[id]['latestWeight'] = weight  # about four operations
  cowLowestWeight = listCows[id]['lowestWeight']
  if cowLowestWeight > weight or cowLowestWeight == 0:
    listCows[id]['lowestWeight'] = weight
  return

def recordMilk(id, milk):    # Records milk production and calculates the average to the cow-ID-specific record
  listCows[id]['totalMilkProd'] = listCows[id]['totalMilkProd'] + milk  # about three operations
  listCows[id]['milkings'] = listCows[id]['milkings'] + 1
  listCows[id]['averageMilkProd'] = round((listCows[id]['totalMilkProd']) / listCows[id]['milkings'])
  return


#---------ProgramStart---------#

  # -- Reading file input -- #

listCows = {}
with open('cowData4.txt') as file:    # Reading a file input
  contents = file.read()
  cowListRaw = contents.split('\n')
  rows = len(cowListRaw)
  
  for i in range(rows):               # Iterating through each row as an individual record. Runtime increased to O(r)
    incomingCow = cowListRaw[i].split(' ')    
    id = incomingCow[0]               # parsing data from record 
    actionCode = incomingCow[1]  
    actionNum = int(incomingCow[2])

    if id not in listCows:        # Creating a new record if cowID (key) not in dictionary
      listCows[id] = { 
          'lowestWeight': 0,
          'latestWeight': 0,
          'averageMilkProd': 0,  
          'totalMilkProd': 0,
          'milkings':0,
        }
      
    if actionCode == 'W':          # Calling calling recordWeight or recordMilk based on action code
      recordWeight(id, actionNum)
    elif actionCode == 'M':
      recordMilk(id, actionNum)

  # -- Transferring Dict data to list -- #
  
newListFromDict = []
for c in listCows.items():    # Transferring each cow from dict to list to sort based on lowest weight. Runtime now O(c + r)
  if c[1]['lowestWeight'] != 0 and c[1]['averageMilkProd'] != 0: 
    newListFromDict.append({'id':c[0],'lowest':c[1]['lowestWeight'],'latest':c[1]['latestWeight'],'milk':c[1]['averageMilkProd']})

  # -- Sorting based on lowestWeight -- #

sortedCowList = sorted(newListFromDict, key = lambda item: item['lowest'])  # using Python sorted build in method. Sorting based on lowest weight.
                                                                            # sorted() runtime is O(nlogn). Our runtime is now O( 2c * logc + r)

  # -- Finding lowestWeight Duplicates to sort latestWeight -- #

cowRecords = len(sortedCowList)
i=0
while i < cowRecords:              #creating a while loop that will iterate through each cow and compare. Runtime now O(3c logc + r)
  sortingLatestWeight = []         #duplicates. Any 'lowestWeight' duplicates will be sorted by their 'latestWeight'
  sortedCowListDuplicates = []     #and any 'latestWeight' duplicates will be sorted by 'AvgMilkProduction'
  if i < cowRecords-1:
    if sortedCowList[i]['lowest'] == sortedCowList[i+1]['lowest']: # check for duplicate 'lowestWeight' in the next index
      j = i
      while sortedCowList[j]['lowest'] == sortedCowList[i]['lowest']:  #duplicate found. record duplicates until non duplicate found  
        sortingLatestWeight.append(sortedCowList[j])  # copy duplicates into new list
        j = j+1
      sortedCowListDuplicates = sorted(sortingLatestWeight, key = lambda item: item['latest']) # sort the duplicate 'lowestWeight's by their 'latestWeight'
                                                                                               # Runtime now O(4c logc + r)

  # -- Sorting latestWeight duplicates from the set of lowestWeight duplicates -- #

      cowLatestDuplicates = len(sortedCowListDuplicates)
      k = 0
      while k < len(sortedCowListDuplicates)-1:
        sortMilkProd = []
        sortingMilk = []
        if k < cowLatestDuplicates-1:
          
          if sortedCowListDuplicates[k]['latest'] == sortedCowListDuplicates[k+1]['latest']:
            l = k
            while sortedCowListDuplicates[k]['latest'] == sortedCowListDuplicates[l]['latest']:
              sortingMilk.append(sortedCowListDuplicates[l])
              if l == len(sortedCowListDuplicates)-1:
                break
              else: 
                l=l+1
            sortMilkProd = sorted(sortingMilk, key = lambda item: item['milk'])
            if len(sortedCowListDuplicates) == len(sortMilkProd):
              sortedCowListDuplicates = sortMilkProd
            else:
              sortedCowListDuplicates[k:l] = sortMilkProd
            k=l+1
        k=k+1
        
        # now, check for duplicate latest weights and sort by thier milk production

      
      sortedCowList[i:j] = sortedCowListDuplicates
      i=j+1
  i=i+1
      # insert similar lowest weights back into the original sorted list, sorted by thier latest weights

# check for duplicate lowest weights
for sortedCowRecord in sortedCowList:
  print(sortedCowRecord['id'],sortedCowRecord['lowest'],sortedCowRecord['latest'],sortedCowRecord['milk'])
  