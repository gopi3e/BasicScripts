import random

def tossCoin(times):
    results, _ = tossCoinV2(times)
    return results

def tossCoinV2(times, weights = None):
    coin = ['H', 'T']

    if weights == None:        
        headWeight = random.choice(range(1,99))
        weights = [headWeight, 100 - headWeight]
        
    return random.choices(coin, k = times, weights=weights), weights

