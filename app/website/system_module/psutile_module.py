import psutil

def take_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    freq_info = {
            "current": cpu_freq.current if cpu_freq else "N/A",
            "min": cpu_freq.min if cpu_freq else "N/A",
            "max": cpu_freq.max if cpu_freq else "N/A"
        }
    return {
            "cpu_percent_per_core": cpu_percent,
            "cpu_count": cpu_count,
            "cpu_frequency_mhz": freq_info
        }

def take_disk_partision():
    disk_partitions_info = psutil.disk_partitions()
    return disk_partitions_info

def check_network_interfaces():
    network_data = psutil.net_io_counters(pernic=True)
    return network_data

def take_ram():
    mem = psutil.virtual_memory()
    total_mb = mem.total / (1024 ** 2)
    available_mb = mem.available / (1024 ** 2)
    used_mb = mem.used / (1024 ** 2)
    percent_used = mem.percent
    return {
        "Total RAM:":total_mb,
        "Available RAM:":available_mb,
        "Used RAM:":used_mb,
        "Usage":percent_used,
    }
