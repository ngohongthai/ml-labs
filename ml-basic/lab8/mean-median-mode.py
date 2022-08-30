N = int(input())
X = list(map(int, input().split()))

'''Mean of X with rounding to 1 decimal places'''
def mean(X):
    return round(sum(X)/len(X), 1)

'''Median of X '''
def median(X):
    X.sort()
    if len(X) % 2 == 0:
        return (X[len(X)//2] + X[len(X)//2 - 1])/2
    else:
        return X[len(X)//2]
    
'''List to Dictionary with count of each element'''
def list_to_dict(X):
    d = {}
    for x in X:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d

def mode(X):
    count_dict = list_to_dict(X)
    # get largest count
    largest_count = max(count_dict.values())
    modes = [k for k, v in count_dict.items() if v == largest_count]
    modes.sort()
    return modes[0]
    

print(mean(X))
print(median(X))
print(mode(X))