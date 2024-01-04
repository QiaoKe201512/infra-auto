import paramiko

from backend.common.host import Host
from backend.common.script import Script

if __name__ == "__main__":
    # 远程服务器的 hostname、port、username 和 password
    hostname = "212.129.252.187"
    port = 22
    username = "root"
    password = "vd0N4ERzV51qwFB8uZXo"

    host = Host(hostname, port, username, password)
    script = Script()
