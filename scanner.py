#!/usr/bin/env python3
"""
MiniPortScanner v0.1
Author: <your-handle>
License: MIT
"""
import argparse
import concurrent.futures
import ipaddress
import socket
import sys
from datetime import datetime


def scan_port(host: str, port: int, timeout: float = 1.0):
    """Attempt a TCP connect() to *host*:*port*. Return (port, is_open)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return port, True
        except (socket.timeout, ConnectionRefusedError):
            return port, False


def scan_host(host: str, ports):
    print(f"\nScanning {host} • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    open_ports = []

    # Thread pool = faster than a naïve loop
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as pool:
        futures = {pool.submit(scan_port, host, p): p for p in ports}
        for fut in concurrent.futures.as_completed(futures):
            port, is_open = fut.result()
            status = "OPEN" if is_open else "closed"
            print(f"  {port:<5} {status}")
            if is_open:
                open_ports.append(port)

    print(f"\n{host} → {len(open_ports)} open port(s): {open_ports or 'None'}")


def expand_ports(port_arg: str):
    """Turn '22,80,443' or '1-1024' into a sorted list of ints."""
    ports = set()
    for part in port_arg.split(","):
        if "-" in part:
            start, end = map(int, part.split("-"))
            ports.update(range(start, end + 1))
        else:
            ports.add(int(part))
    return sorted(ports)


def parse_args():
    ap = argparse.ArgumentParser(description="Simple TCP port scanner")
    ap.add_argument("target", help="IP/CIDR or hostname")
    ap.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Port list or range (e.g. 22,80,443 or 1-65535)",
    )
    return ap.parse_args()


def main():
    args = parse_args()
    ports = expand_ports(args.ports)

    # Accept single IP/host OR an entire CIDR block
    try:
        targets = [str(ip) for ip in ipaddress.ip_network(args.target, strict=False)]
    except ValueError:
        targets = [args.target]  # treat as plain hostname/IP

    for host in targets:
        scan_host(host, ports)


if __name__ == "__main__":
    if sys.platform != "linux" and sys.platform != "darwin":
        print("⚠️  Non-POSIX platform detected; some features may be limited.")
    main()
