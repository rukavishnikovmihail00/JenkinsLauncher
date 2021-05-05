import jenkins_file
from jenkins_file import JenkinsJob
import argparse
from jinja2 import Environment, FileSystemLoader
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-m', help='L is for the last build and A is for all the builds')
parser.add_argument('-u', help='Username')
parser.add_argument('-p', help='Password')
args = vars(parser.parse_args())
   
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
    
if (args['m'] == 'A'):  
    template = env.get_template('report1.html')  
    builds, cur_job = server.get_all_info()

    with open('templates/report1.html', 'w') as f:
        rend = template.render(builds=builds, cur_job=cur_job, url=url)
        f.write(rend)


