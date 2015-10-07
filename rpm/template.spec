Name:           ros-indigo-rosping
Version:        2.0.10
Release:        0%{?dist}
Summary:        ROS rosping package

Group:          Development/Libraries
License:        Boost Software License, Version 1.0
URL:            http://ros.org/wiki/rosping
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-rosboost-cfg
BuildRequires:  ros-indigo-rosbuild
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs

%description
rosping is the tool to send ICMP ECHO_REQUEST to network hosts where roscore is
running, and send back to you as rostopic message. For echoing ROS node, use
rosnode.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Oct 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.10-0
- Autogenerated by Bloom

* Tue Sep 29 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.9-0
- Autogenerated by Bloom

* Tue Sep 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.7-0
- Autogenerated by Bloom

* Tue Sep 08 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.6-0
- Autogenerated by Bloom

* Mon Aug 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.4-1
- Autogenerated by Bloom

* Tue Aug 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.4-0
- Autogenerated by Bloom

* Sun Aug 02 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

