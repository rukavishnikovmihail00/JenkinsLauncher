import jenkins_file
from jenkins_file import JenkinsJob
import argparse
from jinja2 import Environment, FileSystemLoader
from argparse import ArgumentParser
import webbrowser
import os
import yaml

class ParseArgs:
    def __init__(self):
        self.parser = ArgumentParser()


    def parse(self):
        self.parser.add_argument('-m', help='L is for the last build and A is for all the builds')
        self.parser.add_argument('-u', help='Username')
        self.parser.add_argument('-p', help='Password')
        args = vars(self.parser.parse_args())
        return args


class ParseYamlFile:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file


    def parse_yaml(self):
        config = yaml.load(open(self.yaml_file), Loader = yaml.Loader)
        for i in range(len(config['builds'])):
            print(config['builds'][i]['parameters']['number']) # just an example of YAML parcing
        return config['jenkins_server']


if __name__ == "__main__":
    args = ParseArgs().parse()
    yaml_config = ParseYamlFile('config.yaml')
    username = args['u']
    password = args['p']
    url = yaml_config.parse_yaml()

    server = JenkinsJob(url, username, password, 'JobReport')
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    if (args['m'] == 'L'):  
        template = env.get_template('report.html')
        status, time, dur, number = server.get_last_info()

        with open('templates/report.html', 'w') as f:
            rend = template.render(status=status, timestamp=time, duration=dur, number=number)
            f.write(rend)

        try:
            webbrowser.open('file://' + os.path.realpath('C:/Users/MARukavishnikov/Desktop/JenkinsLauncher/templates/report.html'))
        except:
            print('You need to change a path manually')
        
    if (args['m'] == 'A'):  
        template = env.get_template('report1.html')  
        builds, cur_job = server.get_all_info()

        with open('file://' + 'templates/report1.html', 'w') as f:
            rend = template.render(builds=builds, cur_job=cur_job, url=url)
            f.write(rend)
        try:
            webbrowser.open('file://' + os.path.realpath('C:/Users/MARukavishnikov/Desktop/JenkinsLauncher/templates/report1.html'))
        except:
            print('You need to change a path manually')

    
 