Name:           ros-kinetic-bayesian-belief-networks
Version:        2.1.0
Release:        0%{?dist}
Summary:        ROS bayesian_belief_networks package

Group:          Development/Libraries
License:        Apache License, Version 2.0
URL:            https://github.com/eBay/bayesian-belief-networks
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-std-msgs
BuildRequires:  git
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-mk
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-std-msgs

%description
The bayesian_belief_networks package form https://github.com/eBay/bayesian-
belief-networks, Authored by Neville Newey, Anzar Afaq, Copyright 2013 eBay
Software Foundation

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
* Sun Jul 02 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Tue May 09 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.20-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.19-0
- Autogenerated by Bloom

* Sun Oct 30 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.18-1
- Autogenerated by Bloom

* Sat Oct 29 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.18-0
- Autogenerated by Bloom

