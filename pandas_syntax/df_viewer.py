import os
import webbrowser
from datetime import datetime

import pandas as pd


def view_df(df: pd.DataFrame, filename: str = "df_preview"):
    """Save DataFrame to an HTML file and open it in the browser."""
    # Ensure filename is unique per session
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_filename = f"{filename}_{timestamp}.html"

    # Save DataFrame as HTML
    df.to_html(full_filename)

    # Open in browser using absolute path
    abs_path = os.path.abspath(full_filename)
    url = f"file://{abs_path}"
    success = webbrowser.open(url)

    if not success:
        print(f"❌ Could not open browser. Manually open: {url}")
    else:
        print(f"✅ Opened in browser: {url}")
        # Clean up
        # os.remove(full_filename)
