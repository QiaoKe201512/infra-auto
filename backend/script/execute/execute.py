import paramiko

from backend.common.host import Host
from backend.common.script import Script


def connect_and_execute_script(host: Host, script: Script):
    # 创建一个 sft 对象
    ssh = paramiko.SSHClient()

    # 允许连接不在 know_hosts 文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接到远程服务器
    ssh.connect(hostname=host.host, port=host.port, username=host.username, password=host.password)

    sftp_client = ssh.open_sftp()
    # 将本地脚本文件上传到远程服务器
    sftp_client.put(script.script_url, script.script_host_path)

    # 在远程服务器上执行脚本文件

    if script.script_type == "shell":
        stdin, stdout, stderr = ssh.exec_command("sh " + script.script_host_path)
    else:
        stdin, stdout, stderr = ssh.exec_command("python " + script.script_host_path)

    # 获取脚本执行的结果
    output = stdout.readlines()
    error = stderr.readlines()

    # 关闭连接
    ssh.close()

    return output, error
