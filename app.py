from flask import Flask
from datetime import datetime
import pytz  # Timezone library

app = Flask(__name__)

# Pakistan Timezone set karein
PAKISTAN_TZ = pytz.timezone('Asia/Karachi')

@app.route('/')
def hello():
    # Timezone-aware current time hasil karein
    now_pkt = datetime.now(PAKISTAN_TZ)
    
    # Time ko format karein (e.g., 05:30:45 PM)
    time_str = now_pkt.strftime('%I:%M:%S %p')
    # Date ko format karein (e.g., Tuesday, 04 November 2025)
    date_str = now_pkt.strftime('%A, %d %B %Y')
    
    # HTML mein time dikhayein
    html = f"""
    <html>
        <head>
            <title>Pakistan Time</title>
            <meta http-equiv="refresh" content="1">
            <style>
                body {{
                    background-color: #00401A; /* Dark green */
                    color: white;
                    font-family: 'Arial', sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                }}
                div {{
                    border: 2px solid white;
                    border-radius: 15px;
                    padding: 40px;
                    background-color: rgba(0, 0, 0, 0.2);
                }}
                h1 {{
                    font-size: 5rem; /* 5 times normal size */
                    margin: 0;
                }}
                p {{
                    font-size: 2rem;
                    margin-top: 10px;
                }}
            </style>
        </head>
        <body>
            <div>
                <p>The current time in Pakistan is:</p>
                <h1>{time_str}</h1>
                <p>{date_str}</p>
            </div>
        </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
