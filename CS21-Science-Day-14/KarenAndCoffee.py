recipes, admisionNums, questions = list(map(int, input().split()))
recipeList = []
questionList = []
partialSum = [0]*(200002)
preSum = [0]*(200002)
partialSum2 = [0]*(200002)
preSum2 = [0]*(200002)
counter = 0

for i in range(recipes):
    recipeList.append(list(map(int, input().split())))

for i in range(questions):
    questionList.append(list(map(int, input().split())))

for i in range(recipes):
    partialSum[recipeList[i][0]] += 1
    partialSum[recipeList[i][1]+1] -= 1

preSum[0] = partialSum[0]
for i in range(1,200002):
    preSum[i] = preSum[i-1] + partialSum[i]

####################################
for i in range(200002):
    if preSum[i] >= admisionNums:
        partialSum2[i] = 1
    else:
        partialSum2[i] = 0

preSum2[0] = partialSum2[0]
for i in range(1,200002):
    preSum2[i] = preSum2[i-1] + partialSum2[i]

for question in questionList:
    print(preSum2[question[1]] - preSum2[question[0]-1])
