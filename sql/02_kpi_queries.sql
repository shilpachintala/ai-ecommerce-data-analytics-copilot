-- Executive KPIs
SELECT COUNT(DISTINCT OrderId) AS Orders,
       COUNT(DISTINCT CustomerKey) AS Customers,
       SUM(NetRevenue) AS Revenue,
       AVG(NetRevenue) AS RevenuePerOrder,
       AVG(CAST(Returned AS FLOAT)) AS ReturnRate
FROM dbo.FactOrder;

-- Monthly trend with window functions
WITH Monthly AS (
    SELECT DATEFROMPARTS(YEAR(OrderDate),MONTH(OrderDate),1) AS MonthStart,
           SUM(NetRevenue) AS Revenue,
           COUNT(DISTINCT OrderId) AS Orders
    FROM dbo.FactOrder
    GROUP BY DATEFROMPARTS(YEAR(OrderDate),MONTH(OrderDate),1)
)
SELECT *,
       LAG(Revenue) OVER (ORDER BY MonthStart) AS PreviousMonthRevenue,
       Revenue-LAG(Revenue) OVER (ORDER BY MonthStart) AS RevenueVariance,
       AVG(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS Rolling3MonthRevenue
FROM Monthly;
