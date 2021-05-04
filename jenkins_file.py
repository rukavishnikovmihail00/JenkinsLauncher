import jenkinsapi
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.build import Build, JenkinsAPIException, JobLauncherApplicationException
from requests import RequestException


class JenkinsJob:
    def __init__(self, url, username, password, jobname):
        self.url = url
        self.jobname = jobname
        try:
            self.server = Jenkins(self.url, username, password, useCrumb=True)
            print(f"\nSuccessfully connected to {url}\n")
        except (RequestException, JenkinsAPIException) as e:
            raise JobLauncherApplicationException(
                f"\nJenkins couldn`t get the URL access at {url}. Error: {e.message}\n"
            ) from e 
        
    
    def get_last_info(self):
        
        self.job = self.server.get_job(self.jobname)
        print(job.get_last_build().get_status())
        print(job.get_last_build().get_timestamp())
        print(job.get_last_build().get_duration())
        print(job.get_last_build().get_number())
        print(job.get_last_build().get_console())
        
    def get_all_info(self):
        cur_job = self.server.get_job(self.jobname)
        builds = cur_job.get_build_dict()
        
        for build in builds: 
            print(cur_job.get_build(build))
            print(cur_job.get_build(build).get_duration())
            print(cur_job.get_build(build).get_status())
            print(cur_job.get_build(build).get_timestamp())
            print(cur_job.get_build(build).get_console())
        
    
