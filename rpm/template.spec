Name:           ros-indigo-lpg-planner
Version:        2.1.6
Release:        0%{?dist}
Summary:        ROS lpg_planner package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/downward
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin

%description
lpg_planner: LPGL Planner (http://zeus.ing.unibs.it/lpg/)

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Thu Nov 23 2017 Hitoshi Kamada <h-kamada@jsk.imi.i.u-tokyo.ac.jp> - 2.1.6-0
- Autogenerated by Bloom

* Sun Jul 16 2017 Hitoshi Kamada <h-kamada@jsk.imi.i.u-tokyo.ac.jp> - 2.1.4-0
- Autogenerated by Bloom

* Fri Jul 07 2017 Hitoshi Kamada <h-kamada@jsk.imi.i.u-tokyo.ac.jp> - 2.1.3-0
- Autogenerated by Bloom

* Thu Jul 06 2017 Hitoshi Kamada <h-kamada@jsk.imi.i.u-tokyo.ac.jp> - 2.1.2-0
- Autogenerated by Bloom

* Wed Jul 05 2017 Hitoshi Kamada <h-kamada@jsk.imi.i.u-tokyo.ac.jp> - 2.1.1-0
- Autogenerated by Bloom

* Sun Jul 02 2017 Hitoshi Kamada <h-kamada@jsk.imi.i.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Tue May 09 2017 Hitoshi Kamada <h-kamada@jsk.imi.i.u-tokyo.ac.jp> - 2.0.20-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Hitoshi Kamada <h-kamada@jsk.imi.i.u-tokyo.ac.jp> - 2.0.19-0
- Autogenerated by Bloom

* Sat Oct 22 2016 Hitoshi Kamada <h-kamada@jsk.imi.i.u-tokyo.ac.jp> - 2.0.17-0
- Autogenerated by Bloom

