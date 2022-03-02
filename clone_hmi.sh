git clone --recursive git@vc1.airbiquity.com:sdm_c_modules/hmi_console_can.git
cd hmi_console_can
git checkout $1
git submodule update --init --recursive
cd ..
mv hmi_console_can $1
