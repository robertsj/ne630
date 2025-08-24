
import os
import glob
pages = [page.replace(".md", "") for page in glob.glob("../pages/*.md")]

tmpl = 'python convert_to_canvas.py ../pages/{}.md {}.html'
for les in pages:
        name = les
        print(tmpl.format(name, name))
        os.system(tmpl.format(name, name)) 



os.system('python convert_to_canvas.py ../README.md syllabus.html')
os.system('rm tmp.html')

print('done!')
