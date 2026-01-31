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
    
    car_parts = [
        ("0986494166", "Bosch Brake Pad Set (W203)", 40.00, 27.50, "https://www.autodoc.de/bosch/1167796", "https://hndautomotiveparts.com/"),
        ("1457433050", "Mahle Air Filter", 12.50, 32.00, "https://ebay.de/itm/mahle-air-filter", "https://amazon.ae/dp/mahle-filter-ae"),
        ("1127300002", "Bosch Spark Plug Set", 28.75, 65.90, "https://ebay.de/itm/bosch-spark-plugs", "https://amazon.ae/dp/bosch-plugs-ae"),
        ("1601687", "Sachs Clutch Kit", 89.99, 165.00, "https://ebay.de/itm/sachs-clutch-kit", "https://amazon.ae/dp/sachs-clutch-ae"),
        ("0K2A816400", "Hyundai Engine Oil Filter", 8.50, 22.75, "https://ebay.de/itm/engine-oil-filter", "https://amazon.ae/dp/oil-filter-ae"),
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