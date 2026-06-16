#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    # Lấy thông tin dung lượng
    du = shutil.disk_usage(disk)
    # Tính phần trăm còn trống
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    # Tính trung bình CPU usage trong 1 giây
    usage = psutil.cpu_percent(1)
    return usage < 75

# Khối lệnh chính chạy script
if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")