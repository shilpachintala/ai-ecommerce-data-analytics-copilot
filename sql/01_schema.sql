CREATE TABLE dbo.DimCustomer (
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerId VARCHAR(20) NOT NULL UNIQUE,
    Segment VARCHAR(50), City VARCHAR(100), SignupDate DATE
);
CREATE TABLE dbo.DimProduct (
    ProductKey INT IDENTITY(1,1) PRIMARY KEY,
    ProductId VARCHAR(20) NOT NULL UNIQUE,
    ProductName VARCHAR(200), Category VARCHAR(100), ListPrice DECIMAL(12,2)
);
CREATE TABLE dbo.FactOrder (
    OrderId VARCHAR(20) PRIMARY KEY,
    OrderDate DATE NOT NULL,
    CustomerKey INT NOT NULL,
    ProductKey INT NOT NULL,
    Quantity INT, UnitPrice DECIMAL(12,2), DiscountPct DECIMAL(6,4),
    Channel VARCHAR(30), ABGroup VARCHAR(20), Returned BIT,
    NetRevenue DECIMAL(14,2), ShippingDays INT, Rating INT
);
CREATE INDEX IX_FactOrder_OrderDate_Customer
ON dbo.FactOrder(OrderDate, CustomerKey)
INCLUDE (NetRevenue, Returned, Quantity);
