import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data from SQL into a Pandas DataFrame
conn = sqlite3.connect('parts_data.db')
query = '''
SELECT p.part_name, pr.source_country, pr.price_eur 
FROM prices pr
JOIN parts p ON pr.part_id = p.id
'''
df = pd.read_sql_query(query, conn)

# 2. Pivot the data to compare DE vs UAE side-by-side
pivot_df = df.pivot_table(index='part_name', columns='source_country', values='price_eur')

# 3. Calculate the "Spread" (Profit)
pivot_df['Profit_EUR'] = pivot_df['UAE'] - pivot_df['DE']
pivot_df = pivot_df.sort_values(by='Profit_EUR', ascending=False) # Sort by highest profit

print("--- 📊 MARKET ANALYSIS REPORT ---")
print(pivot_df)

# 4. Generate the Chart
plt.figure(figsize=(10, 6))
# Plot DE and UAE prices as bars
pivot_df[['DE', 'UAE']].plot(kind='bar', color=['#1f77b4', '#ff7f0e'])
plt.title('Arbitrage Opportunity: German Auto Parts (DE vs. UAE)')
plt.ylabel('Price (EUR)')
plt.xlabel('Car Part')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the chart
plt.savefig('market_gap_chart.png')
print("\n✅ Chart saved as 'market_gap_chart.png'")