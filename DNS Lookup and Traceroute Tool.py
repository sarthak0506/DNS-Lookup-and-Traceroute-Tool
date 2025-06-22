import socket
from scapy.all import IP, ICMP, sr1
import time

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[DNS] {domain} resolves to {ip}")
        return ip
    except socket.gaierror:
        print("[DNS] Failed to resolve domain.")
        return None

def perform_traceroute(target_ip, max_hops=30):
    print("\n[Traceroute]")
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=target_ip, ttl=ttl) / ICMP()
        start_time = time.time()
        reply = sr1(pkt, verbose=0, timeout=2)
        rtt = (time.time() - start_time) * 1000  # ms

        if reply is None:
            print(f"{ttl}: Request timed out")
        else:
            print(f"{ttl}: {reply.src} ({rtt:.2f} ms)")
            if reply.src == target_ip:
                print("Traceroute complete.")
                break

def check_latency(target_ip, count=4):
    print("\n[Latency Check]")
    times = []

    for i in range(count):
        pkt = IP(dst=target_ip) / ICMP()
        start_time = time.time()
        reply = sr1(pkt, verbose=0, timeout=2)
        rtt = (time.time() - start_time) * 1000  # ms

        if reply:
            print(f"Ping {i+1}: {reply.src} - {rtt:.2f} ms")
            times.append(rtt)
        else:
            print(f"Ping {i+1}: Request timed out")

    if times:
        avg = sum(times) / len(times)
        print(f"\nAverage Latency: {avg:.2f} ms")


def main():
    domain = input("Enter a domain name (e.g., google.com): ").strip()
    ip = dns_lookup(domain)

    if ip:
        check_latency(ip)
        perform_traceroute(ip)

if __name__ == "__main__":
    main()
