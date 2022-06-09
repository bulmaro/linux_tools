#!/usr/bin/python3
import os
import json
import copy

# Use sim_ua_init_config to generate v1_config.json & uptane_config.json
# for each sample_uaX

os.chdir(f"{os.path.expanduser('~')}/work/Rel/sample_ua/V2.1.0.429/") # cd ~/work/MultiECU

sim_ua = json.load(open("/data/aqconfig/sim_ua_init_config.json"))

for i in range(0, 4):
    sim_ua["config"][i]["mutexes"][0] = f"SampleUA{i+1}"
    with open(f"./build{i+1}/sample_ua/v1_config.json", 'w') as v1c:
        json.dump({"config":[sim_ua["config"][i]]}, v1c, indent=4)
    with open(f"./build{i+1}/sample_ua/uptane_config.json", 'w') as uc:
        json.dump( {"thisEcuId" : sim_ua["config"][i]["serialNumber"]}, uc, indent=4)

# Erase and recreate /data configuration files

os.chdir("/data")

os.system("rm -rf conf_sampleua*")

os.system("mkdir conf_sampleua1")
os.system("mkdir conf_sampleua2")
os.system("mkdir conf_sampleua3")
os.system("mkdir conf_sampleua4")

os.system("cp -R aqconfig/uptane conf_sampleua1")
os.system("cp -R aqconfig/uptane conf_sampleua2")
os.system("cp -R aqconfig/uptane conf_sampleua3")
os.system("cp -R aqconfig/uptane conf_sampleua4")

os.system("rm -rf sampleua*")

os.system("mkdir -p sampleua1/factory_default_uptane")
os.system("mkdir -p sampleua2/factory_default_uptane")
os.system("mkdir -p sampleua3/factory_default_uptane")
os.system("mkdir -p sampleua4/factory_default_uptane")

# Copy the factory_default_uptane dir to /data/sampleuaX dir
# Use master installed_ecus to create each individual
# installed_ecus file
#
# Also create map.json for each individual ECU config

installed_ecus = json.load(open("/data/otamatic/factory_default_uptane/installed_ecus.json"))

backend_config = json.load(open("/data/aqconfig/backend_config.json"))
map_config = backend_config["UptaneMAPFILE"]

for i in range(1, 5):
    os.system(f"cp -R /data/otamatic/factory_default_uptane/ /data/sampleua{i}")
    
    this_ecu = installed_ecus[i]
    this_ecu["verificationSupported"] = "local"
    with open(f"/data/sampleua{i}/factory_default_uptane/installed_ecus.json", 'w') as f:
        json.dump([this_ecu], f, indent=4)
 
    # Fix to "full" instead of "local"       
    installed_ecus[i]["verificationSupported"] = "full"

    with open(f"/data/sampleua{i}/map.json", "w") as m:
        json.dump(map_config, m, indent=4)

# Save "fixed" installed file (with "full")

with open(f"/data/otamatic/factory_default_uptane/installed_ecus.json", 'w') as ie:
    json.dump(installed_ecus, ie, indent=4)

# Get and set non-expiration meta-data

os.system("~/work/Rel/client/V2.1.0.429/lib/security/test/uptane/scripts/populate_metadata.py ~/work/temp/keys ~/work/vsdmqautilities/Client-Build/Bighorn/tools/stage/backend_config_bootstrap.json /data/otamatic/uptane/files/A")

for i in range(1, 5):
    os.system(f"rm -rf /data/sampleua{i}/factory_default_uptane/cached")
    os.system(f"rm -rf /data/sampleua{i}/factory_default_uptane/trust_root")
    os.system(f"cp -R ~/work/temp/keys/cached /data/sampleua{i}/factory_default_uptane")
    os.system(f"cp -R ~/work/temp/keys/trust_root /data/sampleua{i}/factory_default_uptane")

# Update MUA config
mua_config = json.load(open("/data/aqconfig/mua_config.json"))
if( len(mua_config["event_routing"]["routes"]) == 1):
    a_config = mua_config["event_routing"]["routes"][0]
    # del a_config["matches"]
    # del a_config["configuration"]["url_activate"]
    
    mua_config["event_routing"]["routes"] = []
    for i in range(1, 5):
        my_config = copy.deepcopy(a_config)
        my_config["configuration"]["host_port"] = 8090+i
        my_config["configuration"]["ua_name"] = f"SampleUA{i}"
        my_config["configuration"]["ua_is_local"] = False
        my_config["configuration"]["url_root"] = f"/SampleUA{i}/install/"
        mua_config["event_routing"]["routes"].append(my_config)
        print(my_config)

    with open(f"/data/aqconfig/mua_config.json", 'w') as mc:
        json.dump(mua_config, mc, indent=4)
