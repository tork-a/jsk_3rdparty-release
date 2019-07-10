Name:           ros-melodic-julius
Version:        2.1.12
Release:        3%{?dist}
Summary:        ROS julius package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/julius
Source0:        %{name}-%{version}.tar.gz

Requires:       rsync
Requires:       unzip
Requires:       wget
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-mk
BuildRequires:  ros-melodic-roslib
BuildRequires:  ros-melodic-rospack
BuildRequires:  rsync
BuildRequires:  unzip
BuildRequires:  wget

%description
julius: Open-Source Large Vocabulary CSR Engine
(http://julius.sourceforge.jp/index.php)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Jul 10 2019 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.12-3
- Autogenerated by Bloom

* Mon May 27 2019 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.12-2
- Autogenerated by Bloom

* Mon May 27 2019 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.12-1
- Autogenerated by Bloom

* Thu Aug 30 2018 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.11-0
- Autogenerated by Bloom

