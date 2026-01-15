from ping3 import ping

def icmp_latency(target):
    latency = ping(target, timeout=2)
    return latency * 1000 if latency else None
