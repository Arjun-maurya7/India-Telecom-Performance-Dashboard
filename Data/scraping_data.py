import requests
import pandas as pd
from io import StringIO
from dotenv import load_dotenv
import os

load_dotenv()
# ---------- API DETAILS ----------
api_key = os.getenv("API_KEY") # Add your api key for data.gov.in
base_url = "https://api.data.gov.in/resource/98e76922-ab13-474e-9bce-78942583cd0e"

limit = 5000   # Maximum rows per request (API usually allows 10,000 max)
offset = 0

all_dataframes = []

print("📥 Downloading all data...")

while True:
    url = f"{base_url}?api-key={api_key}&format=csv&limit={limit}&offset={offset}"
    print(f"➡️ Fetching rows from offset {offset}")

    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Error:", response.status_code, response.text)
        break

    csv_text = response.text.strip()

    # If API returns empty result, stop
    if len(csv_text.splitlines()) <= 1:
        print("✔️ No more rows found. Download complete.")
        break

    # Convert response to DataFrame
    df_chunk = pd.read_csv(StringIO(csv_text))

    # Add to list
    all_dataframes.append(df_chunk)

    # Move to next batch
    offset += limit

# ---------- MERGE ALL CHUNKS ----------
if all_dataframes:
    final_df = pd.concat(all_dataframes, ignore_index=True)

    output_file = "full_api_data.csv"
    final_df.to_csv(output_file, index=False)

    print(f"✅ ALL DATA SAVED SUCCESSFULLY TO: {output_file}")
    print(f"📌 Total rows downloaded: {len(final_df)}")

else:
    print("⚠️ No data downloaded.")
 