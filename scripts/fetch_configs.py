#!/usr/bin/env python3
import base64, json, re, requests

URLS = [
    "https://raw.githubusercontent.com/free18/v2ray/main/v.txt",
    "https://raw.githubusercontent.com/Danialsamadi/v2go/main/AllConfigsSub.txt",
]

def decode_vmess(link: str):
    b64 = link[8:].strip()
    missing = len(b64) % 4
    if missing:
        b64 += "=" * (4 - missing)
    try:
        data = json.loads(base64.b64decode(b64).decode())
    except:
        return None
    ob = {
        "type": "vmess",
        "server": data["add"],
        "server_port": int(data["port"]),
        "uuid": data["id"],
        "security": data.get("scy", "auto"),
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

def fetch_and_merge():
    all_obs = []
    for url in URLS:
        try:
            r = requests.get(url, timeout=30)
            content = r.text
        except:
            continue
        lines = content.splitlines()
        decoded = []
        for line in lines:
            line = line.strip()
            if line.startswith("vmess://"):
                decoded.append(line)
            else:
                try:
                    sub = base64.b64decode(line).decode()
                    decoded.extend(sub.splitlines())
                except:
                    pass
        for link in decoded:
            ob = decode_vmess(link)
            if ob:
                all_obs.append(ob)

    # Deduplicate
    seen = set()
    unique = []
    for ob in all_obs:
        key = (ob["server"], ob["server_port"], ob["uuid"])
        if key not in seen:
            seen.add(key)
            ob["tag"] = f"{len(unique)+1}"
            unique.append(ob)

    with open("merged_outbounds.json", "w") as f:
        json.dump(unique, f, indent=2)
    print(f"Merged {len(unique)} outbounds into merged_outbounds.json")

if __name__ == "__main__":
    fetch_and_merge()
