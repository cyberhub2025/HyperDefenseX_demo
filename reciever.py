from flask import Flask, request

app = Flask(__name__)

@app.route('/receive-logs', methods=['POST'])
def receive_logs():
    logs = request.data.decode("utf-8")
    with open("remote_flask.log", "a") as f:
        f.write(logs)
    print(f"✅ Received {len(logs.splitlines())} new log lines.")
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # accessible from internet
