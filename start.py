import jenkinsapi
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.build import Build

url = 'http://localhost:8080/'
username = 'admin'
password = 'admin'
server = Jenkins(url, username, password, useCrumb=True)

job = server.get_job('JobReport')
print(job.get_last_build().get_status())
