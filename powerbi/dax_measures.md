# DAX measures
```DAX
Revenue = SUM(FactOrder[NetRevenue])
Orders = DISTINCTCOUNT(FactOrder[OrderId])
Customers = DISTINCTCOUNT(FactOrder[CustomerId])
Average Order Value = DIVIDE([Revenue],[Orders])
Return Rate = DIVIDE(CALCULATE([Orders],FactOrder[Returned]=1),[Orders])
Revenue MTD = TOTALMTD([Revenue],DimDate[Date])
Revenue Rolling 30D = CALCULATE([Revenue],DATESINPERIOD(DimDate[Date],MAX(DimDate[Date]),-30,DAY))
```
