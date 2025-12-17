
import websocket, json, threading, time
from db import init_db

conn = init_db()

def on_message(ws, message):
    data = json.loads(message)
    if 'p' in data:
        conn.execute(
            "INSERT INTO ticks VALUES (?, ?, ?, ?)",
            (time.time(), data['s'], float(data['p']), float(data['q']))
        )
        conn.commit()

def start_ws(symbol="btcusdt"):
    url = f"wss://stream.binance.com:9443/ws/{symbol}@trade"
    ws = websocket.WebSocketApp(url, on_message=on_message)
    threading.Thread(target=ws.run_forever, daemon=True).start()
