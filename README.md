# Simple-store
This is a simple utensils store me and my buddy did in 12th grade. It uses python as a user interface and mysql as database.
WORKING 
Utensil Shop Management System

This is a basic Python + MySQL project designed to manage a small utensil shop. It supports both owner and customer functionalities like adding items, billing, stock tracking, and more.
programs Used:

   Python

   MySQL

   MySQL Connector for Python

Features
Owner Functions:

   1.Add single or multiple utensils

   2.Modify utensil details

   3.Delete utensils

   4.Display current inventory

   5.Search for utensils by name

Customer Functions:

   1.View available utensils

   2.Purchase utensils (stock updates automatically)

   3.Generate a bill for the purchase

so to run this create the database shop with 2 tables
1. item : which has 4 columns.
   ino     -     int(11)       -   item number
   iname   -     varchar(30)   -   item name
   rate    -     int(11)       -   rate of item
   qty     -     int(11)       -    quantity of item
   Image of the item table :![image](https://github.com/user-attachments/assets/4bded1c8-b583-4f2f-97dc-4aec30bf0ed7)
   
2. bill - which has 6 columns.
   cname    -    varchar(30)    -    name of customer
   DOP      -    Date           -    date of purchase    
   Iname    -    Varchar(40)    -    Item name 
   Rate     -    int(11)        -    rate of item
   QTY      -    int(11)        -    quantity of item took by customer
   AMT      -    int(11)        -    amount with respect to quantity
   Image of bill table :![image](https://github.com/user-attachments/assets/a7c10897-fdfc-44b9-8f14-1286faa95299)

   summary :
   This is a simple utensil shop using python and mysql. The code written is very basic and almost all amateur coder can understand the code. THANK YOU
   
