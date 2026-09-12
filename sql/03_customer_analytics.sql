WITH CustomerRFM AS (
    SELECT CustomerKey,
           DATEDIFF(DAY,MAX(OrderDate),(SELECT MAX(OrderDate) FROM dbo.FactOrder)) AS RecencyDays,
           COUNT(DISTINCT OrderId) AS Frequency,
           SUM(NetRevenue) AS MonetaryValue
    FROM dbo.FactOrder
    GROUP BY CustomerKey
), Scored AS (
    SELECT *,
           NTILE(5) OVER (ORDER BY RecencyDays DESC) AS RScore,
           NTILE(5) OVER (ORDER BY Frequency) AS FScore,
           NTILE(5) OVER (ORDER BY MonetaryValue) AS MScore
    FROM CustomerRFM
)
SELECT *, CONCAT(RScore,FScore,MScore) AS RFMCode
FROM Scored;
