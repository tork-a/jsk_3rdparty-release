%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-julius-ros
Version:        2.1.21
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS julius_ros package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       julius-voxforge
Requires:       nkf
Requires:       python3-lxml
Requires:       python3-rospkg
Requires:       ros-noetic-audio-capture
Requires:       ros-noetic-audio-common-msgs
Requires:       ros-noetic-julius
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sound-play
Requires:       ros-noetic-speech-recognition-msgs
Requires:       ros-noetic-std-srvs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-rostest
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The julius_ros package

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Aug 26 2020 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.1.21-1
- Autogenerated by Bloom

* Fri Aug 07 2020 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.1.20-1
- Autogenerated by Bloom

