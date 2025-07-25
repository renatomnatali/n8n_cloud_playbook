import glob
import yaml
import pytest

PLAYBOOK_PATTERN = "n8n_cloud_playbook_v*.yaml"

@pytest.mark.parametrize("path", glob.glob(PLAYBOOK_PATTERN))
def test_yaml_is_valid(path):
    with open(path, 'r', encoding='utf-8') as f:
        yaml.safe_load(f)
