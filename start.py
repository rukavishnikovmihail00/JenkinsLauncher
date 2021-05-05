import jenkins_file
from jenkins_file import JenkinsJob
import argparse
from jinja2 import Environment, FileSystemLoader
from argparse import ArgumentParser
from archivator import Archivator
import webbrowser
import os

class ParseArgs:
    def __init__(self):
        self.parser = ArgumentParser()


    def parse(self):
        self.parser.add_argument('-m', help='L is for the last build and A is for all the builds')
        self.parser.add_argument('-u', help='Username')
        self.parser.add_argument('-p', help='Password')
        self.parser.add_argument('-z', default=0, help='Option "1" to create a .zip')
        args = vars(self.parser.parse_args())
        return args


if __name__ == "__main__":
    args = ParseArgs().parse()
    print(args)
    username = args['u']
    password = args['p']
    url = 'http://localhost:8080/'

    server = JenkinsJob(url, username, password, 'JobReport')
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    if (args['m'] == 'L'):  
        template = env.get_template('report.html')
        status, time, dur, number = server.get_last_info()

        with open('templates/report.html', 'w') as f:
            rend = template.render(status=status, timestamp=time, duration=dur, number=number)
            f.write(rend)

        webbrowser.open('file://' + os.path.realpath('C:/Users/MARukavishnikov/Desktop/JenkinsLauncher/templates/report.html'))
        
        
    if (args['m'] == 'A'):  
        template = env.get_template('report1.html')  
        builds, cur_job = server.get_all_info()

        with open('file://' + 'templates/report1.html', 'w') as f:
            rend = template.render(builds=builds, cur_job=cur_job, url=url)
            f.write(rend)

        webbrowser.open('file://' + os.path.realpath('C:/Users/MARukavishnikov/Desktop/JenkinsLauncher/templates/report1.html'))

    if (args['z'] == '1'):
        Archivator().archivate()
 