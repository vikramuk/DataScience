import random
def coin_trial():
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
            heads +=1
    return heads

def simulate(n):
   trials = []
   for i in range(n):
       trials.append(coin_trial())
   return(sum(trials)/n)
'''
#https://www.kdnuggets.com/2018/08/basic-statistics-python-probability.html
if __name__=="__main__":
    simulate(10)
'''
