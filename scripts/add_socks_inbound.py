#!/usr/bin/env python3
import json, sys

input_file = "merged_outbounds.json"
if len(sys.argv) > 1:
    input_file = sys.argv[1]

try:
    with open(input_file, "r") as f:
        outbounds = json.load(f)
except FileNotFoundError:
    with open("config.json", "r") as f:
        outbounds = json.load(f)

# Clean unsupported or deprecated fields for sing-box v1.11.0
for ob in outbounds:
    ob.pop("tcp_fast_open", None)
    ob.pop("alterId", None)                       # <-- جدید
    tls = ob.get("tls")
    if isinstance(tls, dict):
        tls.pop("record_fragment", None)

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
