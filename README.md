# MARKET-BASKET-ANALYSIS

Project on products that can be recommended on some purchased product.Market Basket Analysis will help you to design different store Layouts.

![0_svFzvtdonTOmAcPO](https://user-images.githubusercontent.com/100334542/178120888-53430ac9-f7ae-4b6c-ba5d-752d86d820ad.gif)

## Introduction

Nowadays Machine Learning is helping the Retail Industry in many different ways. You can imagine that from forecasting the performance of sales to identify the buyers, there are many applications of machine learning(ML) in the retail industry. “Market Basket Analysis” is one of the best applications of machine learning in the retail industry. By analyzing the past buying behavior of customers, we can find out which are the products that are bought frequently together by the customers.

![image](https://user-images.githubusercontent.com/100334542/179158401-09118e6d-639c-4ace-a4fc-d843e1d5f8fe.png)

## What is Market Basket Analysis?

When we go to any supermarket or shop online we try to purchase all the item we need together instead of buying each item seperately. Thus we can define Market Basket as a basket which is used to group together items of a person’s interest which he/she will buy in one transaction. Each trip to the market is a single transaction, and in case of e-commerce all items bought in a single login is a transaction

This process identifies customer buying habits by finding associations between the different items that customers place in their “shopping baskets” . The discovery of this kind of association will be helpful for  retailers or marketers to develop marketing strategies by gaining insight into which items are frequently bought together by customers.

For example, if customers are buying milk, how probably are they to also buy bread (and which kind of bread) on the same trip to the supermarket? This information may lead to increase sales by helping retailers to do selective marketing and plan their ledge space.

![image](https://user-images.githubusercontent.com/100334542/179158674-b56b6ce7-302e-4e9d-a78b-149bdf7528f0.png)

## Objective of Market Basket

1. **Cross Selling**: It is a stratergy where the seller encourages the customer to spend more money by recommending related products that complement what is being bought already by the consumer. This stratergy would encourage the customer to spend more than he/she had actually thought he/she would.

2. **Product Placement**: When you go to supermarket you may see that the milk items are kept together. Moreover you may see that as you move forward you find the bread making items such as flour, butter, eggs etc kept just after the milk products. This placement of the items on the supermarket shelf follows planogram. A planogram is defined as a “diagram or model that indicates the placement of retail products on shelves in order to maximize sales”.

## What is Association Rule for Market basket Analysis?

Association Rules are widely used to analyze retail basket or transaction data, and are intended to identify strong rules discovered in transaction data using measures of interestingness, based on the concept of strong rules.

An example of Assosciation Rules 👇👇👇👇👇👇👇👇👇👇👇👇

      Assume there are 100 customers
      
      10 of them bought milk, 8 bought butter and 6 bought both of them.
      
      bought milk => bought butter
      
      support = P(Milk & Butter) = 6/100 = 0.06
      
      confidence = support/P(Butter) = 0.06/0.08 = 0.75
      
      lift = confidence/P(Milk) = 0.75/0.10 = 7.5
      
![image](https://user-images.githubusercontent.com/100334542/179159698-8dce4650-6b10-497f-b1e3-d9e999a94ba7.png)

## Apriori Algorithm

Apriori Algorithm is a widely-used and well-known Association Rule algorithm and is a popular algorithm used in market basket analysis.It helps to find frequent itemsets in transactions and identifies association rules between these items. The limitation of the Apriori Algorithm is frequent itemset generation. It needs to scan the database many times which leads to increased time and reduce performance as it is a computationally costly step because of a huge database. It uses the concept of Confidence, Support.

      Lift (A => B) = 1 means that there is no correlation within the itemset.
      Lift (A => B) > 1 means that there is a positive correlation within the itemset, i.e., products in the itemset, A, and B, are more likely to be bought together.
      Lift (A => B) < 1 means that there is a negative correlation within the itemset, i.e., products in itemset, A, and B, are unlikely to be bought together.

## Advantages of Market Basket Analysis

There are many advantages to implementing Market Basket Analysis in marketing. Market basket Analysis(MBA) can be applied to data of customers from the point of sale (PoS) systems.

It helps retailers with:

1.Increases customer engagement

2.Boosting sales and increasing RoI

3.Improving customer experience

4.Optimize marketing strategies and campaigns

5.Help to understand customers better

6.Identifies customer behavior and pattern

### How does Market Basket Analysis look from the Customer’s perspective?🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐

Let us take an example from Amazon, the world’s largest eCommerce platform. From a customer’s perspective, Market Basket Analysis is like shopping at a supermarket. Generally, it observes all items bought by customers together in a single purchase. Then it shows the most related products together that customers will tend to buy in one purchase.

![image](https://user-images.githubusercontent.com/100334542/179163342-009b4dd6-13e3-4176-a8ee-f668465e5c38.png)

### The Dataset

In this implementation, we have to use the Store Data dataset that is publicly available on Kaggle. This dataset contains a total of 7501 transaction records where every record consists of the list of items sold in just one transaction.

https://github.com/Debasishsaha123/MARKET-BASKET-ANALYSIS/blob/main/Market_Basket_Optimisation%20(1).csv


       all_items = data.melt()["value"].dropna().sort_values()
       print(f"There were {all_items.nunique()} different products:\n", all_items.unique())
       
The dataset contanins 120 different products.
  
  Among them mineral water is the most purchased products
  
![image](https://user-images.githubusercontent.com/100334542/179189498-d69aefc8-e7ed-48c3-811b-02faf19e60c1.png)

  Assuming that only one unit of each item was bought in each transaction, asparagus is sold the least.

![image](https://user-images.githubusercontent.com/100334542/179190081-25ccd1e9-c4a3-491d-b380-9bd5704ac986.png)

# Transaction

![Screenshot (36)](https://user-images.githubusercontent.com/100334542/179921824-99d93bd0-5239-40f8-b0c0-4679beef7f2c.png)


## Customer's choices

### 1.First Choice

![newplot](https://user-images.githubusercontent.com/100334542/179190763-da8cc7b8-99fd-4d68-9033-c32e9d252745.png)

### 2.Second choice

![newplot (1)](https://user-images.githubusercontent.com/100334542/179190850-51f72971-07d5-4118-b95c-acc076856339.png)

### 3.Third choice

![newplot (2)](https://user-images.githubusercontent.com/100334542/179190941-d0662deb-f3ae-4c5b-85d4-c6e516c77f9b.png)

#### **Now we apply apriori function and pass minimum support here we are passing 10%. means 10 times in total number of transaction that item was present.**

![Screenshot (38)](https://user-images.githubusercontent.com/100334542/179923411-2cda1cd2-8ddd-430e-ac98-ddbbea2c8062.png)

#### **We have association rules which need to put on itemset here we are setting based on lift and has minimum lift as 1.2.**

![Screenshot (41)](https://user-images.githubusercontent.com/100334542/179926718-9141fa30-0a38-4e6f-be9f-a9f5244422a4.png)

According the above table we can easily say that the dependency between (herb & pepper) and (ground beef) is high since lift value is approximately 2.5x of threshold value and conviction is higher than 1.

#### **Now see the confidence matrix without mineral water as**

![Screenshot (43)](https://user-images.githubusercontent.com/100334542/179939091-f3206433-4c5e-4f1b-a8e0-d583ec9ece2e.png)

### **According the redifined table there is a significant relationship between ground beef and spaghetti ,red wine,olive oli**

![Screenshot (45)](https://user-images.githubusercontent.com/100334542/179940206-48d1a50e-319e-4f8c-8722-925228db5e5c.png)

**From the above table it is easily seen the antecedents from the itemset corresponding the consequents where 'spaghetti' present.**

