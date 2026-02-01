import sqlite3
from datetime import date

def add_price(part_number, part_name, country, price, url):
    conn = sqlite3.connect('parts_data.db')
    cursor = conn.cursor()

    # 1. Ensure the part exists in our 'parts' table
    cursor.execute('INSERT OR IGNORE INTO parts (part_number, part_name) VALUES (?, ?)', 
                   (part_number, part_name))
    
    # 2. Get the Part ID
    cursor.execute('SELECT id FROM parts WHERE part_number = ?', (part_number,))
    part_id = cursor.fetchone()[0]

    # 3. Insert the price observation
    today = date.today()
    cursor.execute('''
    INSERT INTO prices (part_id, source_country, price_eur, url, date_observed)
    VALUES (?, ?, ?, ?, ?)
    ''', (part_id, country, price, url, today))

    conn.commit()
    conn.close()
    print(f"✅ Added {part_name} | Market: {country} | Price: €{price}")

if __name__ == "__main__":
    # --- REAL DATA ENTRY ZONE ---
    # List of 5 common German car parts with prices in Germany vs Dubai (UAE)
    # Format: (part_number, part_name, price_de_eur, price_uae_eur, url_de, url_uae)
    
# MARKET DATA: Q1 2026 BENCHMARKS
    # Strategy: Mixed (Import High Value / Export High Volume)
    car_parts = [
        # 1. PORSCHE HEADLIGHT (The "Gold Mine")
        # Strategy: IMPORT (Dubai Scrap/Surplus -> Germany Used Market)
        # Note: Prices compare OEM Used condition.
        ("9586311", "Porsche Cayenne 958 Headlight (Right)", 620.00, 215.00, "https://ebay.de/itm/porsche-958", "https://betaautoparts.com/porsche"),

        # 2. MERCEDES FUEL PUMP (The "Volume Runner")
        # Strategy: IMPORT (Dubai Surplus -> Germany Retail)
        # Compact size = Low shipping cost.
        ("A2054701594", "Mercedes W205 Fuel Pump (Bosch)", 145.50, 75.00, "https://www.autodoc.de/bosch/1156484", "https://germanparts.ae/fuel-pump"),

        # 3. SACHS CLUTCH KIT (The "Export Balance")
        # Strategy: EXPORT (Germany Retail -> Dubai Workshop)
        # German parts are premium priced in UAE workshops.
        ("3000950019", "Sachs Clutch Kit (VW Golf 7)", 110.00, 185.00, "https://www.motointegrator.de/sachs", "https://partsmarket.ae/sachs-clutch"),
        
        # 4. MANN AIR FILTER (The "Container Filler")
        # Strategy: EXPORT (Add to shipment to fill space)
        ("C30005", "Mann Air Filter C 30 005", 14.50, 28.00, "https://www.autodoc.de/mann", "https://noon.com/mann-filter"),
    ]
    
    # Add all parts to the database using a loop
    for part_number, part_name, price_de, price_uae, url_de, url_uae in car_parts:
        # Add German price
        add_price(part_number, part_name, "DE", price_de, url_de)
        # Add UAE price
        add_price(part_number, part_name, "UAE", price_uae, url_uae)
        # Calculate and display arbitrage opportunity
        arbitrage_profit = price_uae - price_de
        arbitrage_margin = (arbitrage_profit / price_de) * 100
        print(f"   💰 Arbitrage Opportunity: €{arbitrage_profit:.2f} profit ({arbitrage_margin:.1f}% margin)\n")
