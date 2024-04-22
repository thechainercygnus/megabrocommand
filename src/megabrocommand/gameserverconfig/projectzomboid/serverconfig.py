from os import path

def _clean_config_file(config_file_contents: list[str]) -> list[str]:
    cleaned_config_file = []
    for line in config_file_contents:
        stripped_line = line.strip().strip("\n")
        if stripped_line != "" and not stripped_line.startswith("#"):
            cleaned_config_file.append(stripped_line)
    return cleaned_config_file


def _parse_config_contents(cleaned_config_contents: list[str]) -> list[str]:
    parsed_config_contents = {}
    for line in cleaned_config_contents:
        key, value = line.split("=")
        parsed_config_contents[key] = value
    return parsed_config_contents


def get_parsed_config(config_file: str):
    config_friendly_name = config_file.strip(".ini").split("/")[-1]
    server_config = {
        "config_friendly_name": config_friendly_name,
        "config_contents": {}
    }
    if not config_file.endswith(".ini"):
        raise Exception
    if path.exists(config_file):
        with open(config_file, 'r') as configreader:
            config_contents = configreader.readlines()    
    else:
        raise FileNotFoundError
    clean_config = _clean_config_file(config_contents)
    parsed_config = _parse_config_contents(clean_config)
    server_config['config_contents'] = parsed_config
    return server_config