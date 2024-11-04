# conan_assimp_test

See https://github.com/conan-io/conan-center-index/issues/25765

docker run --memory=10g --cpus=10 --rm -ti debian:bullseye

apt -y update

apt install -y python3-pip cmake ninja-build git vim pkg-config

pip install --upgrade "conan"

git clone https://github.com/EstebanDugueperoux2/conan_assimp_test.git

cd conan_assimp_test

# With gcc
time conan install . --build missing -s build_type=Debug --profile:build .conan/profiles/build_profile --profile:host .conan/profiles/build_profile -c tools.system.package_manager:mode=install &> build.log

time conan build . --build missing -s build_type=Debug --profile:build .conan/profiles/build_profile --profile:host .conan/profiles/build_profile -c tools.system.package_manager:mode=install &> build.log

conan graph info . --format=html  -s build_type=Debug --profile:build .con
an/profiles/build_profile --profile:host .conan/profiles/build_profile &> graph.html

cp $HOME/.conan2/p/b/conan9c3d7421a84e0/b/build/Debug/game .
export ALICEVISION_OCIO=$PWD/config.ocio
./game

#Cannot use conanio docker images because cmake release is too old
#sudo docker run --memory=10g --cpus=10 --rm -ti  conanio/gcc12-ubuntu18.04
sudo docker run --memory=10g --cpus=10 --rm -ti debian:bullseye
apt -y update
apt install -y python3-pip cmake ninja-build git vim pkg-config
pip install --upgrade "conan"
git clone https://github.com/EstebanDugueperoux2/conan_assimp_test.git
cd conan_assimp_test/
conan install . --build missing --profile:build .conan/profiles/build_profile --profile:host .conan/profiles/build_profile -c tools.system.package_manager:mode=install &> install.log
conan build . --build missing --profile:build .conan/profiles/build_profile --profile:host .conan/profiles/build_profile -c tools.system.package_manager:mode=install &> build.log

# With clang

conan install . --build missing -s build_type=Debug --profile:build .conan/profiles/build_profile_clang --profile:host .conan/profiles/build_profile_clang

configure: error: *** Compiler does not support -std=gnu11

pulseaudio/14.2: ERROR: 
Package '11163bd72edfa8a64f1022d859d8f33bc067da22' build failed
pulseaudio/14.2: WARN: Build folder /home/esteban/.conan2/p/b/pulsebde12124f614f/b/build-debug
ERROR: pulseaudio/14.2: Error in build() method, line 131
	autotools.configure()
	ConanException: Error 1 while executing


time conan build . --build missing -s build_type=Debug --profile:build .conan/profiles/build_profile --profile:host .conan/profiles/build_profile -c tools.system.package_manager:mode=install &> build.log
