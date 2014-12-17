import os
import re
path = os.path.abspath(os.curdir)
os.chdir(path)
data_files = [f for _, _, files in os.walk(path) for f in files if os.path.splitext(f)[1] == '.txt']
#data_files.remove('emstudio_to_track.dat')
for f in data_files:
    k = re.search('\d+',f)
    k = k.group(0)
    suffix = '%s%s' % ('0'*(3-len(k)), k)
    fobj = open(f, 'r')
    for eachline in fobj:
        line = eachline
    length = line.split()[2]
    fobj.close()
    with open('emstudio_to_track.dat', 'r') as fobj:
        file_content = fobj.readlines()
        file_content[2] = '%s\n' % f
        file_content[8] = '%sd0\n' % length[:7]
    with open('emstudio_to_track.dat', 'w') as fobj:
        fobj.writelines(file_content)
    os.system('EMStudio_To_TRACK.exe')
    os.rename('eh_EMS.#12', 'eh_RFQ.#%s' % suffix)
         
