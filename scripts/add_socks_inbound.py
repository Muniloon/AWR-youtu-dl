#!/usr/bin/env python3
import json, sys

# Default input file
input_file = "merged_outbounds.json"  # Use the fetched file first
# If an argument is given, use that instead
if len(sys.argv) > 1:
    input_file = sys.argv[1]

try:
    with open(input_file, "r") as f:
        outbounds = json.load(f)
except FileNotFoundError:
    # Fallback to old config.json if exists
    with open("config.json", "r") as f:
        outbounds = json.load(f)

# Clean unsupported fields or deprecated stuff
for ob in outbounds:
    ob.pop("tcp_fast_open", None)
    tls = ob.get("tls")
    if isinstance(tls, dict):
        tls.pop("record_fragment", None)

# Add auto urltest and selector
config = {
    "inbounds": [
        {
            "type": "socks",
            "tag": "socks-in",
            "listen": "127.0.0.1",
            "listen_port": 1080,
            "sniff": True,
            "users": []
        }
    ],
    "outbounds": outbounds + [
        {
            "type": "selector",
            "tag": "select",
            "outbounds": [ob["tag"] for ob in outbounds],
            "interrupt_exist_connections": False
        },
        {
            "type": "urltest",
            "tag": "auto",
            "outbounds": [ob["tag"] for ob in outbounds],
            "url": "https://www.gstatic.com/generate_204",
            "interval": "5m",
            "tolerance": 10
        }
    ],
    "route": {
        "rules": [
            {"action": "sniff"},
            {"protocol": "dns", "action": "hijack-dns"}
        ],
        "auto_detect_interface": True,
        "final": "auto"
    }
}

with open("config_singbox.json", "w") as f:
    json.dump(config, f, indent=2)

print("config_singbox.json created with socks inbound and auto server selection.")
