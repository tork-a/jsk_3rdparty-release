%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-bayesian-belief-networks
Version:        2.1.20
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS bayesian_belief_networks package

License:        Apache License, Version 2.0
URL:            https://github.com/eBay/bayesian-belief-networks
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-rospy
Requires:       ros-noetic-std-msgs
BuildRequires:  git
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-mk
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The bayesian_belief_networks package form https://github.com/eBay/bayesian-
belief-networks, Authored by Neville Newey, Anzar Afaq, Copyright 2013 eBay
Software Foundation

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
* Fri Aug 07 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.20-1
- Autogenerated by Bloom

