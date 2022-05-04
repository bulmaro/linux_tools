import sys
import fileinput
from pathlib import Path

if (len(sys.argv) != 2):
    print('Please input target file')
    quit()
flag=0
CR='CLIENT_RANDOM '
if Path(sys.argv[1]).exists():
    for line in fileinput.input():
        if ('dumping \'master secret\'' in line):
            m_s=''
            c_r=''
            flag =1
        else:
            if ((flag == 1) or (flag == 2) or (flag == 3)):
                m_s = m_s + line.split('  ')[1].replace(' ','')
                flag= flag + 1
            else:
                if ((flag == 4) or (flag == 5) or (flag == 6)):
                    flag = flag + 1
                else:
                    if (flag == 7):
                        c_r = c_r + line.split('  ')[1].replace(' ','')
                        flag = flag + 1
                    else:
                        if ((flag == 8)):
                            c_r = c_r + line.split('  ')[1].replace(' ','')
                            print(CR + c_r + ' ' + m_s)
                            flag = 0
else:
    print('Target file does not exist.')
