#!/usr/bin/env python3
import json

with open("config.json", "r") as f:
    cfg = json.load(f)

# Remove sections that are not used in our workflow or may cause issues
cfg.pop("dns", None)
cfg.pop("ntp", None)
cfg.pop("experimental", None)

# Clean outbounds: remove unsupported TLS fields
for ob in cfg.get("outbounds", []):
    tls = ob.get("tls")
    if isinstance(tls, dict):
        tls.pop("record_fragment", None)   # not supported in sing-box 1.11

# Add socks inbound
cfg["inbounds"] = [
    {
        "type": "socks",
        "tag": "socks-in",
        "listen": "127.0.0.1",
        "listen_port": 1080,
        "sniff": True,
        "users": []
    }
] + [i for i in cfg.get("inbounds", []) if i.get("tag") != "socks-in"]

# Ensure final route points to selector
if "route" not in cfg:
    cfg["route"] = {}
cfg["route"]["final"] = "✅ Selector"

with open("config_singbox.json", "w") as f:
    json.dump(cfg, f, indent=2)

print("config_singbox.json created with socks inbound on port 1080")
