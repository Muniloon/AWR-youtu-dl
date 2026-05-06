#!/usr/bin/env python3
import json

with open("config.json", "r") as f:
    outbounds = json.load(f)

# Clean unsupported or deprecated fields for sing-box v1.11.0
for ob in outbounds:
    # Remove deprecated tcp_fast_open
    ob.pop("tcp_fast_open", None)
    # Remove unsupported record_fragment from tls
    tls = ob.get("tls")
    if isinstance(tls, dict):
        tls.pop("record_fragment", None)

# Build a complete sing-box configuration
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
        # Selector that uses urltest for automatic best server
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
        "final": "auto"  # Use the urltest group
    }
}

with open("config_singbox.json", "w") as f:
    json.dump(config, f, indent=2)

print("config_singbox.json created (record_fragment removed, socks inbound, auto server selection).")
