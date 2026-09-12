SELECT OrderId,COUNT(*) AS RecordCount
FROM dbo.FactOrder
GROUP BY OrderId
HAVING COUNT(*)>1;

SELECT * FROM dbo.FactOrder
WHERE Quantity<=0 OR UnitPrice<0 OR DiscountPct NOT BETWEEN 0 AND 1 OR Rating NOT BETWEEN 1 AND 5;
