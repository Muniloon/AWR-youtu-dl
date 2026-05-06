#!/usr/bin/env python3
import base64, json, re, requests

# List of public V2Ray subscription URLs (plain text or base64)
URLS = [
    "https://raw.githubusercontent.com/free18/v2ray/main/v.txt",
    "https://raw.githubusercontent.com/Danialsamadi/v2go/main/AllConfigsSub.txt",
    # Add more if needed
]

def decode_link(link: str):
    """Convert vmess:// vless:// trojan:// link to sing-box outbound object."""
    if link.startswith("vmess://"):
        b64 = link[8:].strip()
        # Fix padding
        missing = len(b64) % 4
        if missing:
            b64 += "=" * (4 - missing)
        try:
            data = json.loads(base64.b64decode(b64).decode())
        except:
            return None
        ob = {
            "tag": "",
            "type": "vmess",
            "server": data["add"],
            "server_port": int(data["port"]),
            "uuid": data["id"],
            "security": data.get("scy", "auto"),
            "alterId": int(data.get("aid", 0)),
            "transport": {},
        }
        net = data.get("net", "tcp")
        ob["transport"]["type"] = net
        if net == "ws":
            ob["transport"]["path"] = data.get("path", "/")
            ob["transport"]["headers"] = {"Host": data.get("host", "")}
        tls = data.get("tls", "")
        if tls == "tls":
            ob["tls"] = {"enabled": True, "server_name": data.get("sni", "")}
        return ob

    elif link.startswith("vless://"):
        # vless://uuid@server:port?params#tag
        # Simplified parsing (full params parsing omitted for brevity, but we'll do basic)
        # This is a bit more complex. For now, we skip VLESS in this basic example, but you can extend.
        return None
    elif link.startswith("trojan://"):
        # trojan://password@server:port?params#tag
        return None
    return None

def fetch_and_merge():
    all_outbounds = []
    for url in URLS:
        try:
            resp = requests.get(url, timeout=30)
            content = resp.text
        except:
            continue

        # Try base64 decode if it looks like base64 (e.g., starts with vmess:// or contains only base64 chars)
        lines = content.splitlines()
        decoded_lines = []
        for line in lines:
            line = line.strip()
            if line.startswith(("vmess://", "vless://", "trojan://")):
                decoded_lines.append(line)
            else:
                # Maybe base64 encoded subscription
                try:
                    decoded = base64.b64decode(line).decode()
                    sublines = decoded.splitlines()
                    decoded_lines.extend(sublines)
                except:
                    pass  # ignore non-decodable lines

        for link in decoded_lines:
            ob = decode_link(link)
            if ob:
                all_outbounds.append(ob)

    # Simple deduplication by server+port+uuid
    seen = set()
    unique = []
    for ob in all_outbounds:
        key = (ob.get("server"), ob.get("server_port"), ob.get("uuid"))
        if key not in seen:
            seen.add(key)
            ob["tag"] = f"{len(unique)+1}"
            unique.append(ob)

    with open("merged_outbounds.json", "w") as f:
        json.dump(unique, f, indent=2)
    print(f"Merged {len(unique)} outbounds into merged_outbounds.json")

if __name__ == "__main__":
    fetch_and_merge()
