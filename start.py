import jenkins_file
from jenkins_file import JenkinsJob
import argparse
from jinja2 import Environment, FileSystemLoader


url = 'http://localhost:8080/'
username = 'admin'
password = 'admin'

server = JenkinsJob(url, username, password, 'JobReport')

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('report.html')
status, time, dur, number = server.get_last_info()

with open('templates/report.html', 'w') as f:
    rend = template.render(status=status, timestamp=time, duration=dur, number=number)
    f.write(rend)
    
    


#server.get_last_info()

#server.get_all_info()