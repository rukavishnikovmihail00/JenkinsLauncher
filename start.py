import jenkins_file
from jenkins_file import JenkinsJob
import argparse

url = 'http://localhost:8080/'
username = 'admin'
password = 'admin'


server = JenkinsJob(url, username, password, 'JobReport')

#server.get_last_info()
server.get_all_info()