Name:           ros-kinetic-opt-camera
Version:        2.0.19
Release:        0%{?dist}
Summary:        ROS opt_camera package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/opt_camera
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-camera-calibration-parsers
Requires:       ros-kinetic-compressed-image-transport
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-proc
Requires:       ros-kinetic-rospack
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-camera-calibration-parsers
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-compressed-image-transport
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-proc
BuildRequires:  ros-kinetic-roslang
BuildRequires:  ros-kinetic-rospack
BuildRequires:  ros-kinetic-sensor-msgs

%description
opt_camera

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
* Wed Feb 22 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.19-0
- Autogenerated by Bloom

* Sun Oct 30 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.18-1
- Autogenerated by Bloom

* Sat Oct 29 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.18-0
- Autogenerated by Bloom

