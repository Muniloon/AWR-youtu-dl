#!/bin/bash
warp-cli --accept-tos register >/dev/null 2>&1 || true
warp-cli --accept-tos set-mode proxy >/dev/null 2>&1
warp-cli --accept-tos connect >/dev/null 2>&1
# wait for connection
for i in $(seq 1 20); do
  if warp-cli --accept-tos status | grep -q "Connected"; then
    echo "WARP connected. SOCKS5 proxy on 127.0.0.1:40000"
    break
  fi
  sleep 1
done
