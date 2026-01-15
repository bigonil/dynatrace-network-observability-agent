
import socket
import time

def tcp_latency(host, port, timeout=3):
    start = time.perf_counter()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            pass
        end = time.perf_counter()
        return (end - start) * 1000.0
    except Exception:
        return float("nan")

def run(context):
    for target in context.config["targets"]:
        context.emit_metric(
            "custom.network.icmp.latency",
            icmp_latency(target),
            {"target": target}
        )
        context.emit_metric(
            "custom.network.tcp.connect_time",
            tcp_latency(target, 443),
            {"target": target}
        )