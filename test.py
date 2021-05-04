from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('report.html')
msg = template.render(title="Report")
with open('templates/report.html', 'w') as f:
            f.write(msg)