#!/usr/bin/env python3
import json

with open("config.json", "r") as f:
    cfg = json.load(f)

# Remove the problematic dns section
cfg.pop("dns", None)

# Remove any existing socks inbound to avoid duplicates
cfg["inbounds"] = [
    {
        "type": "socks",
        "tag": "socks-in",
        "listen": "127.0.0.1",
        "listen_port": 1080,
        "sniff": True,
        "sniff_override_destination": False,
        "users": []
    }
] + [i for i in cfg.get("inbounds", []) if i.get("tag") != "socks-in"]

# Ensure the final route points to the selector
if "route" not in cfg:
    cfg["route"] = {}
cfg["route"]["final"] = "✅ Selector"

with open("config_singbox.json", "w") as f:
    json.dump(cfg, f, indent=2)

print("config_singbox.json created with socks inbound on port 1080")
