import markdown
import os
from jinja2 import Template

with open('data/index.md') as file_index:
    index_md = file_index.read()

with open('template/index.j2') as file_index_tmpl:
    index_tmpl = file_index_tmpl.read()

index_data = markdown.markdown(index_md, extensions=['meta'])

index_html = Template(index_tmpl).render(body=index_data)

with open('docs/index.html', 'w') as file_index_html:
    file_index_html.write(index_html)
print('Index file generated')

os.system('cp -rf template/styles/* docs/styles')
print('Styles copied')


