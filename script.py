# 💰 Expense Tracker Dashboard (Advanced Version)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1: Load the Data
# -----------------------------
df = pd.read_csv("data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# Step 2: Basic Info
# -----------------------------
print("========== EXPENSE TRACKER DASHBOARD ==========")
print(df.head())

# -----------------------------
# Step 3: Summary Calculations
# -----------------------------
total_income = df[df['Type'] == 'Income']['Amount'].sum()
total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
savings = total_income - total_expense

print("\n💰 Total Income  :", total_income)
print("💸 Total Expense :", total_expense)
print("💵 Total Savings :", savings)

# -----------------------------
# Step 4: Add Month & Week Columns
# -----------------------------
df['Month'] = df['Date'].dt.strftime('%b')
df['Week'] = df['Date'].dt.isocalendar().week

# -----------------------------
# Step 5: Category-Wise Expenses
# -----------------------------
expense_data = df[df['Type'] == 'Expense']
category_total = expense_data.groupby('Category')['Amount'].sum().sort_values(ascending=False)

# -----------------------------
# Step 6: Monthly Summary
# -----------------------------
monthly_summary = df.groupby(['Month', 'Type'])['Amount'].sum().unstack().fillna(0)
monthly_summary['Savings'] = monthly_summary['Income'] - monthly_summary['Expense']

print("\n===== Monthly Summary =====")
print(monthly_summary)

# -----------------------------
# Step 7: Visualization Section
# -----------------------------
sns.set_style("whitegrid")

# 1️⃣ Bar Chart – Expenses by Category
plt.figure(figsize=(10,6))
sns.barplot(x=category_total.index, y=category_total.values, palette="OrRd_r")
plt.title("Expenses by Category", fontsize=14, fontweight='bold')
plt.xlabel("Category")
plt.ylabel("Total Expense")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2️⃣ Pie Chart – Expense Distribution
plt.figure(figsize=(6,6))
plt.pie(category_total, labels=category_total.index, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("Expense Distribution by Category")
plt.show()

# 3️⃣ Line Chart – Monthly Income vs Expense
plt.figure(figsize=(10,6))
plt.plot(monthly_summary.index, monthly_summary['Income'], marker='o', label='Income', color='green')
plt.plot(monthly_summary.index, monthly_summary['Expense'], marker='o', label='Expense', color='red')
plt.plot(monthly_summary.index, monthly_summary['Savings'], marker='o', label='Savings', color='blue')
plt.title("Monthly Income vs Expense Trend", fontsize=14, fontweight='bold')
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.tight_layout()
plt.show()

# 4️⃣ Weekly Trend (Optional)
weekly_summary = df.groupby(['Week', 'Type'])['Amount'].sum().unstack().fillna(0)
plt.figure(figsize=(10,6))
sns.lineplot(data=weekly_summary[['Income', 'Expense']], markers=True)
plt.title("Weekly Income vs Expense", fontsize=14)
plt.xlabel("Week Number")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

# 5️⃣ Expense by Payment Mode
payment_total = expense_data.groupby('Payment_Mode')['Amount'].sum()
plt.figure(figsize=(8,6))
sns.barplot(x=payment_total.index, y=payment_total.values, palette="cool")
plt.title("Expenses by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Amount")
plt.show()

# 6️⃣ Category vs Payment Mode Heatmap
pivot_data = expense_data.pivot_table(values='Amount', index='Category', columns='Payment_Mode', aggfunc='sum', fill_value=0)
plt.figure(figsize=(8,6))
sns.heatmap(pivot_data, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Expense Heatmap (Category vs Payment Mode)")
plt.show()

# -----------------------------
# Step 8: Monthly Report Export
# -----------------------------
monthly_summary.to_csv("monthly_summary_report.csv")
print("\n✅ Monthly summary report saved as 'monthly_summary_report.csv'")

# -----------------------------
# Step 9: Extra Insights
# -----------------------------
print("\n===== Extra Insights =====")
top_category = category_total.idxmax()
print(f"🏆 Highest Spending Category: {top_category} ({category_total.max()} ₹)")

lowest_category = category_total.idxmin()
print(f"💡 Lowest Spending Category: {lowest_category} ({category_total.min()} ₹)")

most_used_payment = payment_total.idxmax()
print(f"💳 Most Used Payment Mode: {most_used_payment}")

avg_daily_expense = expense_data.groupby('Date')['Amount'].sum().mean()
print(f"📅 Average Daily Expense: {avg_daily_expense:.2f} ₹")
