import re
import os


ROOT = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(ROOT, 'frameTop.html'), 'r', encoding='utf-8') as f:
    frameTop = f.read()
#print(frameTop[:100])
with open(os.path.join(ROOT, 'frameBot.html'), 'r', encoding='utf-8') as f:
    frameBot = f.read()
#print(frameBot)

fails = []
failed_search = []

for path, dirs, files in os.walk(ROOT):
#    print(path, dirs, files)
    for filename in files:
        if '.html' in filename and 'frame' not in filename and '2011' not in path and 'archive' not in path:
            fullpath = os.path.join(path, filename)
            print(fullpath)
            with open(fullpath, 'r', encoding='utf-8') as f:
                content = f.read()
                print(len(content))
                if "No Results Found" in content:
                    failed_search.append(fullpath)
                    continue
                content, n = re.subn(r'\A.*<!-- CONTENT -->', '', content, re.MULTILINE, re.DOTALL)
                if n != 1:
                    print(n)
                    print("cannot find content begin")
                    fails.append(fullpath)
                    continue
 #                   raise ValueError
                content, n = re.subn(r'<!-- / CONTENT -->.*\Z', '', content, re.MULTILINE, re.DOTALL)
                if n != 1:
                    print(n)
                    print("cannot find content end")
                    fails.append(fullpath)
                    continue
#                    raise ValueError
            with open(fullpath, 'w', encoding='utf-8') as f:
                f.write(frameTop + content + frameBot)
print(failed_search)
print('\nfails:')
for fail in fails:
    print(fail)