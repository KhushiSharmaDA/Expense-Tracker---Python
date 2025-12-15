import pandas as pd

data = {
    "Date": [
        "2025-01-01", "2025-01-02", "2025-01-03", "2025-01-05", "2025-01-06",
        "2025-01-08", "2025-01-10", "2025-01-12", "2025-01-14", "2025-01-15",
        "2025-01-18", "2025-01-20", "2025-01-22", "2025-01-24", "2025-01-26",
        "2025-01-28", "2025-01-30", "2025-01-31"
    ],
    "Category": [
        "Salary", "Groceries", "Rent", "Entertainment", "Investment",
        "Freelance Income", "Utilities", "Health", "Transport", "Bonus",
        "Food Delivery", "Shopping", "Groceries", "Rent", "Internet",
        "Freelance Income", "Health", "Interest"
    ],
    "Description": [
        "January Salary", "Supermarket shopping", "Monthly house rent", "Movie & Snacks",
        "Mutual Fund SIP", "Website project", "Electricity Bill", "Doctor visit",
        "Fuel refill", "Performance bonus", "Swiggy/Zomato", "Clothes purchase",
        "Monthly essentials", "Monthly house rent", "Wi-Fi recharge",
        "Data entry project", "Medicines", "Bank Interest"
    ],
    "Payment_Mode": [
        "Bank Transfer", "UPI", "Bank Transfer", "Cash", "Bank Transfer", "UPI",
        "UPI", "Cash", "UPI", "Bank Transfer", "UPI", "Credit Card", "UPI",
        "Bank Transfer", "UPI", "UPI", "Cash", "Bank Transfer"
    ],
    "Amount": [
        50000, 1500, 10000, 800, 2000, 7000, 1200, 600, 1500, 5000, 450, 2500,
        1300, 10000, 700, 4000, 900, 3000
    ],
    "Type": [
        "Income", "Expense", "Expense", "Expense", "Expense", "Income", "Expense",
        "Expense", "Expense", "Income", "Expense", "Expense", "Expense", "Expense",
        "Expense", "Income", "Expense", "Income"
    ]
}

df = pd.DataFrame(data)
print(df)
total_income = df[df['Type'] == 'Income']['Amount'].sum()
total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
savings = total_income - total_expense
print("Total Income:", total_income)
print("Total Expense:", total_expense)
print("Total Savings:", savings)


import matplotlib.pyplot as plt
expense_data = df[df['Type'] == 'Expense']
category_total = expense_data.groupby('Category')['Amount'].sum()
category_total.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title('Expense Distribution by Category')
plt.show()

