import json
from typing import final, Final
import requests


BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
API_KEY: Final[str] = '6195b18e50946bf9dafa434c5795a7a4'

def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('rates.json', 'r') as file:
            return json.load(file)
    payload: dict = {'access_key': API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    with open('rates.json', 'w') as file:
        json.dump(data, file)

    return data


def get_currency(currency: str, rates: dict) -> float:
    currency: str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)

    else:
        raise ValueError(f'"{currency}" is not a valid currency.')





def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    conversion: float = round((vs_rate /  base_rate) * amount, 2)

    print(f'{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})')



def main() -> None:
    data: dict = get_rates(mock=True)
    rates: dict = data.get('rates')
    
    try:
        amount: float = float(input('Please enter amount to be converted: '))
        from_curr: str = input("Please enter the from currency type (eg: USD, INR, EUR, JPY...): ")
        to_curr: str = input("Please enter the to currency type (eg: USD, INR, EUR, JPY...): ")

        convert_currency(amount, base=from_curr, vs=to_curr,rates=rates)

    except Exception as e:
        print(e)



if __name__ == '__main__':
    main()