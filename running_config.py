from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get


nr = InitNornir(config_file="config.yaml")

result = nr.run(task=napalm_get, getters=["get_config"])

print_result(result)
# run_config = result["switch2"][0].result["get_config"]["running"]

# print(run_config)