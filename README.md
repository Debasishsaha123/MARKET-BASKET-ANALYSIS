# MARKET-BASKET-ANALYSIS

Project on products that can be recommended on some purchased product.Market Basket Analysis will help you to design different store Layouts.

![0_svFzvtdonTOmAcPO](https://user-images.githubusercontent.com/100334542/178120888-53430ac9-f7ae-4b6c-ba5d-752d86d820ad.gif)

## Introduction

Nowadays Machine Learning is helping the Retail Industry in many different ways. You can imagine that from forecasting the performance of sales to identify the buyers, there are many applications of machine learning(ML) in the retail industry. “Market Basket Analysis” is one of the best applications of machine learning in the retail industry. By analyzing the past buying behavior of customers, we can find out which are the products that are bought frequently together by the customers.

![image](https://user-images.githubusercontent.com/100334542/179158401-09118e6d-639c-4ace-a4fc-d843e1d5f8fe.png)

## What is Market Basket Analysis?

 A popular example of frequent itemset mining is Market Basket Analysis. This process identifies customer buying habits by finding associations between the different items that customers place in their “shopping baskets” as you can see in the following fig. The discovery of this kind of association will be helpful for  retailers or marketers to develop marketing strategies by gaining insight into which items
are frequently bought together by customers.

For example, if customers are buying milk, how probably are they to also buy bread (and which kind of bread) on the same trip to the supermarket? This information may lead to increase sales by helping retailers to do selective marketing and plan their ledge space.

![image](https://user-images.githubusercontent.com/100334542/179158674-b56b6ce7-302e-4e9d-a78b-149bdf7528f0.png)

Suppose just think of the universe as the set of items available at the store, then each item has a Boolean variable that represents the presence or absence of that item. Now each basket can then be represented by a Boolean vector of values that are assigned to these variables. The Boolean vectors can be analyzed of buying patterns that reflect items that are frequently associated or bought together. Such patterns will be represented in the form of association rules.

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
