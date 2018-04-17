Name:           ros-kinetic-julius-ros
Version:        2.1.8
Release:        0%{?dist}
Summary:        ROS julius_ros package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       julius-voxforge
Requires:       nkf
Requires:       python-lxml
Requires:       python-rospkg
Requires:       ros-kinetic-audio-capture
Requires:       ros-kinetic-audio-common-msgs
Requires:       ros-kinetic-julius
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sound-play
Requires:       ros-kinetic-speech-recognition-msgs
Requires:       ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rostest

%description
The julius_ros package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Apr 17 2018 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.1.8-0
- Autogenerated by Bloom

* Mon Apr 09 2018 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.1.7-0
- Autogenerated by Bloom

* Thu Nov 23 2017 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.1.6-0
- Autogenerated by Bloom

* Sun Jul 16 2017 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.1.4-0
- Autogenerated by Bloom

* Wed Jul 05 2017 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.1.1-0
- Autogenerated by Bloom

* Sun Jul 02 2017 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

