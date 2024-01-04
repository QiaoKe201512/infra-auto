import paramiko

from backend.common.host import Host
from backend.common.script import Script
from backend.script.execute.execute import connect_and_execute_script

if __name__ == "__main__":
    # 远程服务器的 hostname、port、username 和 password
    hostname = "212.129.252.187"
    port = 22
    username = "root"
    password = "vd0N4ERzV51qwFB8uZXo"

    host = Host(hostname, port, username, password)
    script = Script(script_type="shell", script_url=r"F:\code\python\infra-auto\backend\script\test.sh", script_host_path="/tmp/test.sh", script_id=1, name="test", description="test")

    res, err = connect_and_execute_script(host, script)

    print(res)
    print(err)
