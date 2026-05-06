#!/usr/bin/env python3
import json

with open("config.json", "r") as f:
    outbounds = json.load(f)

# Remove unsupported fields that sing-box 1.11.0 doesn't recognize
for ob in outbounds:
    # tls.record_fragment removed earlier, now also remove utls if present? sing-box 1.11 does support utls.
    # But we'll keep utls as it is supported.
    # Remove deprecated tcp_fast_open (not used, but safe to delete)
    ob.pop("tcp_fast_open", None)
    # packet_encoding is fine for vless (XUDP)
    # Also remove any empty "tls" field if it has only "enabled": false? No need.

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
        # Add a selector that uses urltest for automatic best server
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

print("config_singbox.json created with socks inbound and auto server selection.")
