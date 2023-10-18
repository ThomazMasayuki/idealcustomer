#Import librarys 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

customer = pd.read_csv("Customers.csv", sep=",")

#Verify the base
print(customer)

customer.describe()

#Verify missing values
customer.isnull().sum()

# Rename columns Annual Income and Spending Score
customer = customer.rename(columns={'Annual Income ($)': 'Annual income'})
customer = customer.rename(columns={'Spending Score (1-100)': 'Spending Score'})

#Verify changes before
print(customer)

#Checks using library matplotlib for view age 
plt.hist(x = customer['Age'])

#How much this customers have Annual Income equal 0? 
customer.loc[customer['Annual income'] == 0]

#And, Why the top Annual Income? 
customer['Annual income'].max()
plt.hist(x = customer['Annual income'])

# Verify profession about customers
customer[['Profession']].value_counts()

# Verify relationships between types of customers and gender types
customer[['Profession', 'Gender']].value_counts()

# Verify informations about customers with Profession and Spending Score
customer[['Profession', 'Spending Score']].value_counts()

# Why customers have biggest Work Experience
customer[['Profession', 'Work Experience']].value_counts()

# Verify the max Family Size
customer[['Profession', 'Family Size']].value_counts()

#Verify Gender and Age of the best customer
customer_group = customer.groupby(["Age", "Gender"]).size().reset_index(name="Count").head()
print(customer_group)

#Certified max score 
customer[['Spending Score']].max()

# Return the best Scores
customer.nlargest(5, "Spending Score")

# How much and who is 100 score?
customer.loc[(customer)["Spending Score"] == 100]

# This peoples with score 100, how much is Artist?
customer.loc[(customer)["Spending Score"] == 100] & [(customer)["Profession"] == Artist]

# Verify how many of the type Gender
Gender = customer[['Gender']].value_counts()
Gender.plot(kind='barh', color=['red', 'green'])

#Check work experience the top 
customer[['Work Experience']].max()

#Who this peoples? 
customer.nlargest(5, "Work Experience")

#Who this peoples is the top Work Experience equal 17? 
customer.loc[(customer)["Work Experience"] == 17]

#Now, percepts in this script how much Artist have 17 Work Experience, but, one Profession show in the base. Our have one people with gender Female, age 91 and Lawyer. And your Spending Score is good, 78
#So, with informations, our have some perceptions about the base
professions = customer[['Profession']].value_counts() / 2000
professions.plot(kind='barh', color=['green'], title='Professions')