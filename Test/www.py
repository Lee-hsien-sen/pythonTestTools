import subprocess

if __name__ == '__main__':

    # 使用adb命令获取CPU核心数
    adb_command_core = "adb shell grep -c processor /proc/cpuinfo"
    process_core = subprocess.Popen(adb_command_core, shell=True, stdout=subprocess.PIPE)
    output_core, _ = process_core.communicate()
    core_count = int(output_core.strip())

    # 使用adb命令获取CPU最大主频
    adb_command_freq = "adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq"
    process_freq = subprocess.Popen(adb_command_freq, shell=True, stdout=subprocess.PIPE)
    output_freq, _ = process_freq.communicate()
    cpu_frequency = int(output_freq.strip()) / 1000  # 转换为MHz单位

    # 输出CPU核心数和最大主频
    print("CPU核心数:", core_count)
    print("最大主频:", cpu_frequency, "MHz")