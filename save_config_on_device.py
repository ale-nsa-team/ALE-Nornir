from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='nornir/config.yaml')

def save_config_with_cli(task):
    task.run(
        task=napalm_cli,
        commands=["write memory"]
    )
    
save = nr.run(task=save_config_with_cli)
print_result(save)