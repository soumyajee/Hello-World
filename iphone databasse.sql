create database iphone;
use iphone;
create table Products
( Id INT(10),
 Productname varchar(20),
 ProductLowestprice Int(10),
 Lastupdated varchar(10)
 );
 create table variations
 ( ID INT(10),
  ProductID INT(10),
  Stock INT(10),
  Variation Varchar(20),
  Lastupdated varchar(10)
  );
  INSERT INTO Products VALUES(2,"IPhone",15000,"January");
  INSERT INTO Products VALUES(5,"IPhone",12000,"February");
  INSERT INTO Products VALUES(6,"Oneplus",11000,"April");
  INSERT INTO Products VALUES(8,"Oneplus",10000,"May");
  INSERT INTO variations VALUES(4,5,50,"Blue-64 GB","June");
  INSERT INTO variations VALUES(6,7,10,"Red-256 GB","July");
  INSERT INTO variations VALUES(9,12,100,"Nord","Augast");
  INSERT INTO variations VALUES(10,11,35,"9 Pro","September");
  select*from Products;
  select*from variations;
  
  
  
 