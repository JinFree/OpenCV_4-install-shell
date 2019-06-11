#!/bin/bash
sudo apt purge libopencv* python-opencv -y
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
sudo apt install -y apt-utils cmake gcc unzip gedit vim pkg-config build-essential cmake libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev libv4l-dev v4l-utils libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libqt4-dev mesa-utils libgl1-mesa-dri libqt4-opengl-dev libatlas-base-dev gfortran libeigen3-dev python2.7-dev python3-dev python-pip python3-pip
pip install numpy && pip3 install numpy
cd && mkdir OPENCV_INSTALL && cd OPENCV_INSTALL && wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.0.zip && unzip opencv.zip && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.0.zip && unzip opencv_contrib.zip
cd && cd OPENCV_INSTALL/opencv-4.1.0/ && mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D WITH_TBB=ON \
-D WITH_IPP=ON \
-D WITH_1394=OFF \
-D BUILD_WITH_DEBUG_INFO=OFF \
-D BUILD_DOCS=OFF \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_EXAMPLES=ON \
-D BUILD_TESTS=ON \
-D BUILD_PERF_TESTS=ON \
-D WITH_QT=ON \
-D WITH_GTK=OFF \
-D WITH_OPENGL=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.1.0/modules \
-D WITH_V4L=ON  \
-D WITH_FFMPEG=ON \
-D WITH_XINE=ON \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D OPENCV_GENERATE_PKGCONFIG=ON ../
make -j $(nproc)
sudo make install
sudo ldconfig
echo "export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH" >> ~/.bashrc
#!/bin/sh
source ~/.bashrc
