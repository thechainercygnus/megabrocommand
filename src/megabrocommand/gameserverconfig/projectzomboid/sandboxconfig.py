from os import path

import luadata

def get_parsed_sandbox(config_file: str):
    config_friendly_name = config_file.strip("_SandboxVars.lua").split("/")[-1]
    sandbox_config = {
        "config_friendly_name": config_friendly_name,
        "config_contents": {}
    }
    if path.exists(config_file):
        sandbox_config['config_contents'] = luadata.read(config_file)
    else:
        raise FileNotFoundError
    return sandbox_config