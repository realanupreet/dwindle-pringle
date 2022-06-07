prices = [7, 1, 5, 3, 6, 4]
def bestprofit(prices):
    lowesttillnow = 100000
    bestprofit = 0
    for price in prices:
        print(price)
        if lowesttillnow > price:
            lowesttillnow = price
        elif bestprofit<price-lowesttillnow:
            bestprofit = price-lowesttillnow

    return bestprofit
    
