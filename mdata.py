#!/usr/bin/env python3

import sys,os,re

data_archive = "~/work/data-archive/"

if len(sys.argv) == 1 or sys.argv[1] == "-h":
    print("Use: mdata [list|archive|restore|objects]")
else:
    curdir = "."
    if os.getcwd() != "/data":
        curdir = os.getcwd()
        print(f"--> {sys.argv[0].split('/')[-1]} expects to work from /data... moving there temporarily.")
        os.chdir("/data")
    
    if sys.argv[1] == "list":
        os.system(f"ls {data_archive}")
    elif sys.argv[1] == "archive":
        packages_loc = "/data/otamatic/package_store/packages"
        dirty = False
        if os.path.exists(packages_loc):
            if len(os.listdir(packages_loc)) > 0:
                dirty = True
    
        data_store = "/data/data_store/data"
        if os.path.isfile(data_store):
            if len(os.listdir(data_store)) > 0:
                dirty = True
                
        if dirty:
            print("\nWARNING: The scenario is dirty.\n\nDo you need to run reset_sdk.sh?\n")
            exit(0)
        
        with open('activity.log') as f:
            log = f.read()

        sec_ecus = re.search('Generating scenario for: (.+?) secondary', log).group(1)
        campaigns = re.search('Update campaigns: (.+?)\n', log).group(1)
        package_size = re.search('Packages size: (.+?) KB', log).group(1)
        download_approval = re.search('Download Approval: (.+?)\n', log).group(1)
        install_approval = re.search('Install Approval: (.+?)\n', log).group(1)
        type = "Active" if download_approval == "True" or install_approval == "True" else "Passive"
        backend = re.search('Using backend  : PBH-(.+?)\n', log).group(1)

        filename = f"1+{sec_ecus}ECUs-{campaigns}camp-{package_size}KB-{type}-{backend}.tgz"
        os.system(f"tar -czvf {filename} activity.log aqconfig/ otamatic/ > /dev/null")
        print(f"Archived current scenario in '{filename}'")
        os.system(f"cp {filename} {data_archive}")
        print(f"  also placed a copy in {data_archive}")
        os.system(f"nautilus {data_archive}")
    elif sys.argv[1] == "restore":
        print("\nPlease change to /data, then do 'tar -xvzf ~/work/data-archive/*.tgz'\n")
    elif sys.argv[1] == "objects":
        os.system("grep == activity.log")
    else:
        print("Unknown option. Use -h for help.")
        
    os.chdir(curdir)
    
