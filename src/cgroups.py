# Create dir for set memory limit in cgroups dir

import os

pid = os.getpid()
cgroups_mem_dir = "/sys/fs/cgroup/memory/" + str(pid)

def memory_limit(limit):
    if not os.path.exists(cgroups_mem_dir):
        os.makedirs(cgroups_mem_dir)
    with open(cgroups_mem_dir + "/memory.limit_in_bytes", "w") as f:
        mem_limit = str(limit) * 1024 * 1024
        f.write(mem_limit)
    print("Memory limit set to: " + str(mem_limit))
    os.chmod(cgroups_mem_dir, 0o700)
    print("$ chmod 700 " + cgroups_mem_dir)

def memory_usage():
    with open(cgroups_mem_dir + "/memory.usage_in_bytes", "r") as f:
        mem_usage = f.read()
    print("Memory usage: " + mem_usage)
    return mem_usage

def cpu_limit(limit):
    with open(cgroups_mem_dir + "/cpu.shares", "w") as f:
        cpu_limit = limit * 1000
        f.write(str(cpu_limit))
    print("CPU limit set to: " + str(cpu_limit))
    os.chmod(cgroups_mem_dir, 0o700)
    print("$ chmod 700 " + cgroups_mem_dir)

def cpu_usage():
    with open(cgroups_mem_dir + "/cpu.usage_in_usermode", "r") as f:
        cpu_usage = f.read()
    print("CPU usage: " + cpu_usage)
    return cpu_usage

#os.mkdir(cgroups_mem_dir)
# pidをファイル名にして、cgroupsディレクトリに作成する("/sys/fs/cgroup/memory/" & $pid)
# chmod 700 cgroupsディレクトリ
# cgroupsMemDir & "/memory.limit_in_bytes"にメモリ制限を設定する
# MBをバイトに変換するために(1024*1024)をかける

# "/sys/fs/cgroup/cpu/" & $pid
# chmod 700
# cgroupsCpuDir & "/cpu.cfs_quota_us"にCPU制限を設定する
# cpulimit = cpuLimit * 1000