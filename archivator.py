import zipfile
import os

class Archivator:
    def archivate(self, path):
        self.path = path
        z = zipfile.ZipFile('JenkinsLauncher.zip', 'w')      
        for root, dirs, files in os.walk(self.path):
            for file in files:
                z.write(os.path.join(root,file))        
        z.close()