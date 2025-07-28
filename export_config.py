from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_utils.plugins.functions import print_result
import paramiko

nr = InitNornir(config_file='config.yaml')

def export_config_and_scp(task):
    task.run(
        task=napalm_cli,
        commands=["configuration backup"]
    )
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=task.host.hostname,
        username=task.host.username,
        password=task.host.password
    )
    sftp = ssh.open_sftp()
    sftp.get('/flash/config-backup-recovery/configuration_backup.tar', f'./backups/{task.host.hostname}_backup.tar')
    sftp.close()
    ssh.close()

host = nr
# host = nr.filter(hostname="192.168.12.247") ## Filter by IP
# host = nr.filter(name="switch1") ## Filter by inventory name


save = host.run(task=export_config_and_scp)
print_result(save)
