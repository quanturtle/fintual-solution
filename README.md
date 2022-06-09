# Portfolio Exercise

El repo consiste en la solucion al siguiente desafio:

> Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates. Assume each Stock has a "Price" method that receives a date and returns its price.
Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.

## Usage
Importar modulo
```
from portfolio import Portfolio, Stock
```

Crear stocks, especificando precio y fecha:
```
stock_1 = Stock(200, '12/05/2022')
stock_2 = Stock(230, '13/05/2022')
stock_3 = Stock(250, '14/05/2022')
```

Crear un portfolio:
```
portfolio = Portfolio()
```

Hacer compras para el portafolio, especificando fecha de compra y monto de inversion
```
portfolio.purchase_stock('12/05/2022', 1000)
portfolio.purchase_stock('14/05/2022', 500)
```

Calcular profit sobre un rango de fecha:
```
portfolio.profit('11/05/2022', '17/05/2022')
```