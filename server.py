from flask import Flask, request, jsonify

from modules.logger import (
    initialize_logs,
    write_event,
    write_alert,
)

from modules.detector import analyze_event
from modules.backup_manager import backup_files

from config.settings import SERVER_HOST, SERVER_PORT

app = Flask(__name__)

# Create log files when the server starts
initialize_logs()


@app.route("/", methods=["GET"])
def home():
    return "✅ Ransomware Defense Server is Running"


@app.route("/event", methods=["POST"])
def receive_event():

    data = request.get_json()

    if not data:
        return jsonify(
            {
                "status": "error",
                "message": "No JSON received"
            }
        ), 400

    timestamp = data.get("timestamp")
    event_type = data.get("event_type")
    file_path = data.get("file_path")

    # Validate required fields
    if not timestamp or not event_type or not file_path:
        return jsonify(
            {
                "status": "error",
                "message": "Missing required fields"
            }
        ), 400

    # Automatically back up files when they are created or modified
    if event_type in ["created", "modified"]:
        success, message = backup_files()

        if success:
            print(f"[BACKUP] {message}")
        else:
            print(f"[BACKUP ERROR] {message}")

    # Log the event
    log_message = (
        f"{timestamp} | "
        f"{event_type.upper()} | "
        f"{file_path}"
    )

    write_event(log_message)

    detected, count = analyze_event()

    print(f"[EVENT] {log_message}")

    if detected:

        alert = (
            f"{timestamp} | "
            f"🚨 ALERT | "
            f"Possible ransomware detected "
            f"({count} rapid events)"
        )

        write_alert(alert)

        print(alert)

        return jsonify(
            {
                "status": "alert",
                "events": count
            }
        )

    return jsonify(
        {
            "status": "ok",
            "events": count
        }
    )


if __name__ == "__main__":

    print("=" * 50)
    print("Starting Ransomware Defense Server...")
    print("=" * 50)

    app.run(
        host=SERVER_HOST,
        port=SERVER_PORT,
        debug=False
    )