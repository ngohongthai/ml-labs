# The ratio of boys to girls for babies born in Russia is 1.09:1. 
# If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Input Format
# 1.09 1

# data = list(map(float, input().split()))
# boyP = data[1]
# girlP = data[0]

boyP = 1/(1+1.09)
girlP = 1-boyP

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
def combination(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

totalProb = 0
for numBoy in range(3):
    numGirl = 6 - numBoy
    prob = combination(6,numBoy)*(boyP**numBoy)*(girlP**numGirl)
    print('boys: {}, girls: {}, prob: {}'.format(numBoy, numGirl, prob))
    totalProb += prob
print(1-round(totalProb, 3))