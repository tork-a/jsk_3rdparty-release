Name:           ros-hydro-julius
Version:        2.0.3
Release:        6%{?dist}
Summary:        ROS julius package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/julius
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-rospack

%description
julius: Open-Source Large Vocabulary CSR Engine
(http://julius.sourceforge.jp/index.php)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Aug 02 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-6
- Autogenerated by Bloom

* Sat Aug 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-5
- Autogenerated by Bloom

* Sat Aug 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-4
- Autogenerated by Bloom

* Sat Aug 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-3
- Autogenerated by Bloom

* Sat Aug 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-2
- Autogenerated by Bloom

* Sat Aug 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-1
- Autogenerated by Bloom

* Sat Aug 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

