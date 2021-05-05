import zipfile
import os

class Archivator:
    def archivate(self):
        z = zipfile.ZipFile('JenkinsLauncher.zip', 'w')      
        for root, dirs, files in os.walk(''):
            for file in files:
                z.write(os.path.join(root,file))        
        z.close()