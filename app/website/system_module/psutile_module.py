import psutil  
import platform
import socket
import time
from datetime import datetime

def take_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    freq_info = {
            "current": cpu_freq.current if cpu_freq else "Null",
            "min": cpu_freq.min if cpu_freq else "Null",
            "max": cpu_freq.max if cpu_freq else "Null"
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
        "Total_RAM:":total_mb,
        "Available_RAM:":available_mb,
        "Used_RAM:":used_mb,
        "Usage":percent_used,
    }

def take_general_info():
    hostname = socket.gethostname()
    os_info = platform.platform() 
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    uptime_seconds = time.time() - boot_time_timestamp
    uptime_formatted = str(int(uptime_seconds // 86400)) + ' days, ' + \
                       str(int((uptime_seconds % 86400) // 3600)) + ' hours, ' + \
                       str(int((uptime_seconds % 3600) // 60)) + ' minutes, ' + \
                       str(int(uptime_seconds % 60)) + ' seconds'
    num_users = len(psutil.users())
    net_addrs = psutil.net_if_addrs()
    main_ip = 'Null'  
    for interface, addrs in net_addrs.items():
        if interface == 'lo':  
            continue
        for addr in addrs:
            if addr.family == socket.AF_INET:  
                main_ip = addr.address
                break  
        if main_ip != 'N/A':
            break
    data = {
        'hostname': hostname,
        'os_info': os_info,
        'boot_time': boot_time,
        'uptime_formatted': uptime_formatted, 
        'num_users': num_users,
        'main_ip': main_ip
    }
    return data
