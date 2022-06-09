from datetime import datetime
from typing import List

def parse_date(str_date):
    return datetime.strptime(str_date, '%d/%m/%Y')

class Stock:
    # track all instances of Stocks that have been created
    instances = []

    def __init__(self, price, add_date):
        self.price = price
        self.add_date = parse_date(add_date)

        # add instance to class variable for tracking
        self.__class__.instances.append(self)


    @classmethod
    def price(cls, search_date):
        #if there is an instance that matches in date, return price, else None
        for stock in cls.instances:
            if stock.add_date == parse_date(search_date):
                return stock.price
        
        print('No price found for date: {}'.format(search_date))
        return 


    @classmethod
    def _get_latest_price(cls):
        dates_and_prices = [(stock.add_date, stock.price) for stock in cls.instances]
        sorted_dates_and_prices = sorted(dates_and_prices, key=lambda x: x[0])
        
        return sorted_dates_and_prices[-1]


    @classmethod
    def get_stock(cls, search_date):
        for stock in cls.instances:
            if stock.add_date == parse_date(search_date):
                return stock


class Portfolio:

    def __init__(self):
        self.assets = []
        self.total_investment = 0
        self.total_shares = 0


    def display_holdings(self):
        print('Current investment: {}'.format(self.total_investment))
        print('Current number of shares: {}'.format(self.total_shares))


    def purchase_stock(self, purchase_date, investment):
        price = Stock.price(purchase_date)
        
        # if price is None, then the stock with the specified date doesn't exist
        if price is None:
            print('No price information exists for date {}'.format(purchase_date))
            return

        # price is a number, we can proceed
        else:
            if 0 < investment and 0 < price:
                shares_bought = investment / price
                self.total_shares += shares_bought 
                self.total_investment += investment

                # add current purchase to assets
                self.assets.append({
                    'stock': Stock.get_stock(purchase_date),
                    'investment': investment,
                    'shares': shares_bought
                })

            print('Stock purchase successful, {} shares @ {}'.format(shares_bought, price))
            return


    def profit(self, start_date, end_date):
        
        # check date range is valid
        if parse_date(end_date) <= parse_date(start_date):
            print('Invalid date range')
            return

        else:
            latest_date, latest_price = Stock._get_latest_price()
            
            # if the profit date range is outside of the current stock date range
            # the latest_price is the price of the last day on record
            if parse_date(end_date) < latest_date:
                latest_price = Stock.price(end_date)
                
            accumulated_shares = 0
            accumulated_investment = 0

            # check inside assets all purchases that fall within the date range provided
            for transaction in self.assets:
                if parse_date(start_date) <= transaction['stock'].add_date and transaction['stock'].add_date <= parse_date(end_date):
                    accumulated_investment += transaction['investment']
                    accumulated_shares += transaction['shares']

            # compute statistics
            current_portfolio_value = accumulated_shares * latest_price
            profit = current_portfolio_value - accumulated_investment
            
            roi = (profit / accumulated_investment) * 100
            
            print('Total amount invested: {}'.format(self.total_investment))
            print('Number of shares currently held: {0:.2f}'.format(self.total_shares))
            print('Portfolio profit: {}'.format(profit))
            print('Portfolio return: {0:.2f}%'.format(roi))

            return