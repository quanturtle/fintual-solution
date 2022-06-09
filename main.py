from datetime import datetime
from portfolio import Portfolio, Stock

def main():

    # create toy data
    stock_1 = Stock(200, '12/05/2022')
    stock_2 = Stock(230, '13/05/2022')
    stock_3 = Stock(250, '14/05/2022')
    stock_4 = Stock(238, '15/05/2022')
    stock_5 = Stock(247, '16/05/2022')
    stock_6 = Stock(262, '17/05/2022')
    stock_7 = Stock(244, '18/05/2022')
    stock_8 = Stock(270, '19/05/2022')
    stock_9 = Stock(258, '20/05/2022')
    stock_10 = Stock(224, '21/05/2022')
    stock_11 = Stock(264, '22/05/2022')
    stock_12 = Stock(204, '23/05/2022')
    stock_13 = Stock(294, '24/05/2022')
    
    # create a portfolio
    portfolio = Portfolio()

    # purchase stocks
    portfolio.purchase_stock('12/05/2022', 1000)
    portfolio.purchase_stock('14/05/2022', 500)

    # compute profit over a period of time
    portfolio.profit('11/05/2022', '17/05/2022')


main()