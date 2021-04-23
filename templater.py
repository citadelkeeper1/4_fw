from jinja2 import Template
import os

SITE_PATH = 'templates'

def render(template, path=SITE_PATH, **kwargs):
    file_path = os.path.join(path, template)

    with open(file_path, encoding='utf-8') as template_file:
        rendered_template = Template(template_file.read())
    return rendered_template.render(**kwargs)

