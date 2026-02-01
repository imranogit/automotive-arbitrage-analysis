# 🚗 Automotive Arbitrage Analysis (DACH vs. GCC)

## 📊 Executive Summary
This project quantifies price inefficiencies in the automotive spare parts market between **Germany (DACH)** and the **UAE (GCC)**. By tracking live pricing data, we identified a **bi-directional arbitrage model** that capitalizes on regional supply chain imbalances.

## 📉 Key Findings (Q1 2026 Analysis)
Analysis of the current basket reveals two distinct profit mechanisms:

### 1. The "Reverse Arbitrage" (Import Opportunity)
**High-Value / Low-Volume parts are significantly cheaper in the UAE due to surplus stock and lower overheads.**
* **Target:** Porsche Cayenne Bi-Xenon Headlight (OEM)
* **Germany Market Price:** ~€620 (Used/Refurbished)
* **UAE Sourcing Price:** ~€215 (Surplus/Half-Cut)
* **Gross Margin:** **~65%** (after estimated logistics & 19% Import VAT)

### 2. The "Export Premium" (Export Opportunity)
**German-manufactured consumables command a premium in the GCC.**
* **Target:** Sachs Clutch Kit (VW Golf 7)
* **Arbitrage Gap:** +68% price increase in Dubai.

![Market Gap Chart](market_gap_chart.png)

## 🛠️ Methodology
* **Data Sources:** Real-time scraping of Tier-1 suppliers (Autodoc, Motointegrator) vs. GCC hubs (Sharjah Industrial, PartsMarket.ae).
* **Tech Stack:** Python (Data Processing), SQLite (Inventory), Matplotlib (Visualization).

---
*Project maintained by [Imran Ismail]*