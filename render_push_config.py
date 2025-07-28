from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_configure

nr = InitNornir(config_file='config.yaml', dry_run=True) ### Change the dry-run setting here ### 

def render_config_and_push(task):
    
   #### VLAN and Gateways Config ####

    vlan_interfaces = task.run(
        task=template_file,
        template='templates/vlans.j2',
        path='./',
        **task.host
    )
    vlan_config = vlan_interfaces.result
    task.run(
        task=napalm_configure,
        configuration=vlan_config
    )

result = nr.run(task=render_config_and_push)
print_result(result)