from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_configure

nr = InitNornir(config_file='config.yaml', dry_run=False) ### Change the dry-run setting here ### 

def render_config_and_push(task):

    rendered_config = task.run(task=template_file, template='templates/vlans.j2', path='./', **task.host)
    config_str = rendered_config.result
    configure_devices = task.run(task=napalm_configure, dry_run=True, configuration=config_str)

result = nr.run(task=render_config_and_push)
print_result(result)



