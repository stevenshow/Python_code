# def fizzBuzz(n):
#     for i in range(1, n):
#         if(i % 3 == 0 and i % 5 == 0):
#             print("FizzBuzz")
#         if(i % 3 == 0 and i % 5 != 0):
#             print("Fizz")
#         if(i % 5 == 0 and i % 3 != 0):
#             print("Buzz")
#         else:
#             print(i)

# fizzBuzz(15)

# def minTime(batchSize, processingTime, numTasks):
#     alltasks = [0] * len(batchSize)
#     time = 0
#     for i in range(len(batchSize)):
#         while(numTasks[i] > 0 ):
#             time += processingTime[i]
#             numTasks[i] -= batchSize[i]
#         alltasks[i] = time
#         time = 0
#     return max(alltasks)

# batchSize = [3,2,5,7]
# processingTime = [5,4,10,12]
# numTasks = [10,6,10,5]

#print(minTime(batchSize, processingTime, numTasks))
