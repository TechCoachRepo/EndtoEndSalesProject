-- Dimension Table: DimDate
CREATE TABLE DimDate (
    DateID INT PRIMARY KEY,
    Date DATE,
    DayOfWeek VARCHAR(10),
    Month VARCHAR(10),
    Quarter INT,
    Year INT,
    IsWeekend BOOLEAN
);

-- Dimension Table: DimCustomer
CREATE TABLE DimCustomer (
    CustomerID INT PRIMARY KEY autoincrement start 1 increment 1,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    DateOfBirth DATE,
    Email VARCHAR(100),
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    Country VARCHAR(50),
    LoyaltyProgramID INT
);

-- Dimension Table: DimProduct
CREATE TABLE DimProduct (
    ProductID INT PRIMARY KEY autoincrement start 1 increment 1,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Brand VARCHAR(50),
    UnitPrice DECIMAL(10, 2)
);

-- Dimension Table: DimStore
CREATE TABLE DimStore (
    StoreID INT PRIMARY KEY autoincrement start 1 increment 1,
    StoreName VARCHAR(100),
    StoreType VARCHAR(50),
	StoreOpeningDate DATE,
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    Country VARCHAR(50),
    ManagerName VARCHAR(100)
);

-- Dimension Table: DimLoyaltyProgram
CREATE TABLE DimLoyaltyProgram (
    LoyaltyProgramID INT PRIMARY KEY,
    ProgramName VARCHAR(100),
    ProgramTier VARCHAR(50),
    PointsAccrued INT
);

-- Fact Table: FactOrders
CREATE TABLE FactOrders (
    OrderID INT PRIMARY KEY autoincrement start 1 increment 1,
    DateID INT,
    CustomerID INT,
    ProductID INT,
    StoreID INT,
    QuantityOrdered INT,
    OrderAmount DECIMAL(10, 2),
    DiscountAmount DECIMAL(10, 2),
    ShippingCost DECIMAL(10, 2),
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (DateID) REFERENCES DimDate(DateID),
    FOREIGN KEY (CustomerID) REFERENCES DimCustomer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID),
    FOREIGN KEY (StoreID) REFERENCES DimStore(StoreID)
);