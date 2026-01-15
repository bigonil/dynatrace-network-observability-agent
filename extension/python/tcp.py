import socket, time

def tcp_latency(target, port):
    start = time.time()
    try:
        s = socket.create_connection((target, port), timeout=2)
        s.close()
        return (time.time() - start) * 1000
    except:
        return None