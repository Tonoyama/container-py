import os

"""cgroupの設定
cgroupは"Control Group"の略。
プロセスをグループ化して、そのグループ内に存在するプロセスに共通の設定を適用できる。
たとえば、ホストOSが持つCPUやメモリなどのリソースに対して、グループごとに制限をかけることができる。
"""

# プロセスIDを取得
pid = os.getpid()
# メモリ設定用のcgroupsディレクトリのパス
cgroups_mem_dir = "/sys/fs/cgroup/memory/" + str(pid)
# CPU設定用のcgroupsディレクトリのパス
cgroups_cpu_dir = "/sys/fs/cgroup/cpu/" + str(pid)

# メモリ制限の設定
def memory_limit(memory_limit):
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(cgroups_mem_dir):
        os.makedirs(cgroups_mem_dir)
    # memory.limit_in_bytesにメモリ制限を設定
    with open(cgroups_mem_dir + "/memory.limit_in_bytes", "w") as f:
        # 下限は、1 メガバイト(1MB)
        f.write(memory_limit * 1024 * 1024)
    print("Memory limit set to: " + str(memory_limit * 1024 * 1024))
    # 権限を700に設定
    os.chmod(cgroups_mem_dir, 0o700)
    print("$ chmod 700 " + cgroups_mem_dir)
    # pidをグループに追加すると、グループのメモリ制限が効く。
    # cgroup v1, v2は、/cgroup.procsに書き込む
    with open(cgroups_mem_dir + "/cgroup.procs", "w") as f:
        f.write(str(pid))

# メモリの使用量を取得
def memory_usage():
    with open(cgroups_mem_dir + "/memory.usage_in_bytes", "r") as f:
        mem_usage = f.read()
    print("Memory usage: " + mem_usage)
    return mem_usage

# CPU制限の設定
def cpu_limit(cpu_limit):
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(cgroups_cpu_dir):
        os.makedirs(cgroups_cpu_dir)
    # cpu.cfs_quota_usにCPU制限を設定
    # 注意：マルチコアの場合、全 CPU コアを対象に分配される
    with open(cgroups_cpu_dir + "/cpu.cfs_quota_us", "w") as f:
        # 下限は、1000 マイクロ秒(0.001秒)、上限は、1秒
        f.write(str(cpu_limit * 1000))
    print("CPU limit set to: " + str(cpu_limit * 1000))
    # 権限を700に設定
    os.chmod(cgroups_cpu_dir, 0o700)
    print("$ chmod 700 " + cgroups_cpu_dir)
    # pidをグループに追加すると、グループのCPU制限が効く。
    with open(cgroups_cpu_dir + "/cgroup.procs", "w") as f:
        f.write(str(pid))

# CPUの使用量を取得
def cpu_usage():
    with open(cgroups_cpu_dir + "/cpu.cfs_quota_us", "r") as f:
        cpu_usage = f.read()
    print("CPU usage: " + cpu_usage)
    return cpu_usage
