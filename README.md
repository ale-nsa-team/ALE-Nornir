# ALE-Nornir

This repository provides reusable Nornir/NAPALM workflows and Jinja2 templates to automate on Alcatel‑Lucent Enterprise OmniSwitch AOS:
- VLAN configuration (create, name, port membership)
- Layer‑3 inter‑switch interfaces (/31 links, SVI/L3 interfaces)
- SPB/ISIS backbone deployment and enablement

## Usage 

- Create a Python virtual environment and install requirements (Nornir, nornir‑napalm, nornir‑jinja2, nornir‑utils, napalm, napalm‑aos).
- Edit defaults.yaml (platform, credentials) and hosts.yaml (devices and data: VLANs, links).
- Adjust templates/ if needed.
- Preview changes:
```python render_push_config.py (dry‑run by default)```

- Apply changes:
Switch ```dry_run``` to False (global in InitNornir or per task) and re‑run ```python render_push_config.py```.

- Persist configs (optional):
```python save_config_on_device.py```

- Backup configs:
```python export_config.py``` (files stored under backups/)


