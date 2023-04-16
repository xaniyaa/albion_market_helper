def get_min_sell_price(response: str) -> int:
    '''Возвращает минимальную цену на предмет, независимо от качества, получая на вход json в str. \n
    Возвращает только по одному городу, который первый был в запросе ^-^'''
    prices = []
    city = response[0].get('city')
    for j in range(len(response)):
        if response[j].get('sell_price_min') != 0 and response[j].get('city') == city:
            prices.append(response[j].get('sell_price_min'))
    return min(prices)

def get_max_buy_price(response: str) -> int:
    '''Возвращает максимальную цену запроса на покупку предмета, независящую от качества, получая json в str.
    Возвращает только по одному городу, который первый был в запросе ^-^'''
    prices = []
    city = response[0].get('city')
    for j in range(len(response)):
        if response[j].get('buy_price_max') != 0 and response[j].get('city') == city:
            prices.append(response[j].get('buy_price_max'))
    return max(prices)