from crypto_data import get_coins, Coin


def alert(symbol: str, bottom_price: float, top_price: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top_price or coin.current_price < bottom_price:
                print(coin, "!!!Triggered!!!")
            else:
                print(coin)

def main():
    coins: list[Coin] = get_coins()

    alert('btc', bottom_price=20_000, top_price=24_000, coins_list=coins)
    alert('eth', bottom_price=1800, top_price=1900, coins_list=coins)
    alert('xrp', bottom_price=0.47, top_price=0.48, coins_list=coins)

if __name__ == '__main__':
    main()