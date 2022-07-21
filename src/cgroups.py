# Create dir for set memory limit in cgroups dir

import os

pid = os.getpid()
cgroups_mem_dir = "/sys/fs/cgroup/memory/" + str(pid)

def memory_limit(limit):
    if not os.path.exists(cgroups_mem_dir):
        os.makedirs(cgroups_mem_dir)
    with open(cgroups_mem_dir + "/memory.limit_in_bytes", "w") as f:
        f.write(str(limit))
    print("Memory limit set to: " + str(limit))
    return

#os.mkdir(cgroups_mem_dir)
# pidをファイル名にして、cgroupsディレクトリに作成する("/sys/fs/cgroup/memory/" & $pid)
# chmod 700 cgroupsディレクトリ
# cgroupsMemDir & "/memory.limit_in_bytes"にメモリ制限を設定する
# MBをバイトに変換するために(1024*1024)をかける

# "/sys/fs/cgroup/cpu/" & $pid
# chmod 700
# cgroupsCpuDir & "/cpu.cfs_quota_us"にCPU制限を設定する
# cpulimit = cpuLimit * 1000