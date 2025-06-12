#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

# Create a demo financial dataset for a fictional company
years = list(range(2020, 2026))  # Past and projected years
data = {
    "Year": years,
    "Revenue": [500000, 550000, 600000, 660000, 720000, 790000],
    "Cost of Goods Sold": [200000, 220000, 240000, 260000, 280000, 300000],
    "Operating Expenses": [100000, 110000, 120000, 125000, 130000, 140000],
    "Interest Expense": [10000, 10000, 12000, 12000, 13000, 13000],
    "Taxes": [30000, 35000, 40000, 45000, 50000, 55000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate financial metrics
df["Gross Profit"] = df["Revenue"] - df["Cost of Goods Sold"]
df["Operating Income"] = df["Gross Profit"] - df["Operating Expenses"]
df["Net Income"] = df["Operating Income"] - df["Interest Expense"] - df["Taxes"]

# Save to Excel
file_path = "/mnt/data/Financial_Analysis_Template.xlsx"
#df.to_excel(file_path, index=False)


# In[5]:


#df.to_excel(file_path, index=False)
df = pd.DataFrame(data)


# In[6]:


df


# ### Here is an Excel tabular presentation
Year	Revenue	Cost of Goods Sold	Operating Expenses	Interest Expense	Taxes	Gross Profit	Operating Income	Net Income
2020	500000	200000	            100000	            10000	            30000	300000	        200000	            160000
2021	550000	220000	            110000	            10000	            35000	330000	        220000	            175000
2022	600000	240000	            120000	            12000	            40000	360000	        240000	            188000
2023	660000	260000	            125000	            12000	            45000	400000	        275000	            218000
2024	720000	280000	            130000	            13000	            50000	440000	        310000	            247000
2025	790000	300000	            140000	            13000	            55000	490000	        350000	            282000

# In[7]:


# Calculate financial metrics
df["Gross Profit"] = df["Revenue"] - df["Cost of Goods Sold"]
df["Operating Income"] = df["Gross Profit"] - df["Operating Expenses"]
df["Net Income"] = df["Operating Income"] - df["Interest Expense"] - df["Taxes"]


# In[10]:


df["Gross Profit"]


# In[11]:


df["Operating Income"]


# In[9]:


df["Net Income"]


# ### Here is a Documentation Template or Framework for the supermarket Financial Analysis

# In[ ]:


#Create a documentation template or framework that can be used to analyse my supermarket sales, 
#revenue, operational expenses, interest expenses, taxes, Gross Profit, Operational income, and Net income etc?

### Supermarket Financial Analysis Template
1. Document Title
Supermarket Financial Performance Report
Reporting Period: (e.g., January 2024 – December 2024)
Prepared by:
Date Prepared:2. Executive Summary
Brief overview of performance

Key financial highlights (Revenue, Profitability, etc.)

Major challenges and opportunities3. Sales and Revenue Analysis
Month/Quarter|	Total Sales	|Number of Transactions| Average Sale Value| Key Products/Departments
_____________|______________|______________________|___________________|_____________________________
Notes:

Comment on sales trends

Seasonal impacts or promotions

Top-selling and underperforming categories4. Cost of Goods Sold (COGS)
Period | Inventory Start | Purchases | Inventory End | COGS
_______|_________________|___________|_______________|__________
COGS = Inventory Start + Purchases - Inventory End

Notes:

Supplier changes

Shrinkage or spoilage issues5. Operating Expenses
Category | Monthly/Quarterly Cost |	Notes
_________|________________________|__________
Rent		
Salaries & Wages		
Utilities		
Marketing & Advertising		
Repairs & Maintenance		
Other	6. Other Financial Items
Category         |	Amount   |  Notes
_________________|___________|_______________
Interest Expense		        Loan Details
Taxes		                    Tax bracket, changes7. Profit & Loss Summary
Metric	      |        Amount
______________|___________________
Revenue	
(-) COGS	
= Gross Profit	
(-) Operating Exp.	
= Operating Income	
(-) Interest Exp.	
(-) Taxes	
= Net Income	8. Performance Ratios (Optional)
Ratio	           |       Formula	                  | Value
___________________|__________________________________|___________
Gross Margin	          Gross Profit / Revenue	
Operating Margin	      Operating Income / Revenue	
Net Profit Margin	      Net Income / Revenue	
Inventory Turnover	      COGS / Avg Inventory9. Visual Analysis
Line/bar charts of sales and net income over time

Pie chart of expense breakdown

Forecasting (if applicable)10. Key Insights and Recommendations
What is working well?

Areas needing attention

Action steps (e.g., reduce costs, renegotiate supplier terms, marketing improvements)