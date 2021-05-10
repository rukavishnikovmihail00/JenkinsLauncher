import yaml


def parse_yaml(yaml_file):
    config = yaml.load(open(yaml_file), Loader = yaml.Loader)
    for i in range(len(config['builds'])):
        print(config['builds'][i]['parameters']['number'])

    return config['jenkins_server']
parse_yaml('config.yaml')

