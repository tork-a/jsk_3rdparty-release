Name:           ros-hydro-collada-urdf-jsk-patch
Version:        2.0.7
Release:        0%{?dist}
Summary:        ROS collada_urdf_jsk_patch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_urdf_jsk_patch
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       gts
Requires:       python-catkin_tools
Requires:       ros-hydro-angles
Requires:       ros-hydro-assimp-devel
Requires:       ros-hydro-class-loader
Requires:       ros-hydro-collada-parser
Requires:       ros-hydro-collada-urdf
Requires:       ros-hydro-geometric-shapes
Requires:       ros-hydro-kdl-parser
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-resource-retriever
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-tf
Requires:       ros-hydro-urdf
BuildRequires:  collada-dom-devel
BuildRequires:  git
BuildRequires:  gts
BuildRequires:  python-catkin_tools
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-assimp-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-class-loader
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-collada-parser
BuildRequires:  ros-hydro-collada-urdf
BuildRequires:  ros-hydro-geometric-shapes
BuildRequires:  ros-hydro-kdl-parser
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-resource-retriever
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-tf

%description
unaccepted patch for collada_urdf

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
* Tue Sep 15 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.7-0
- Autogenerated by Bloom

* Tue Sep 08 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.6-0
- Autogenerated by Bloom

* Mon Aug 24 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.4-1
- Autogenerated by Bloom

* Tue Aug 18 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.4-0
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-14
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-13
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-12
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-11
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-10
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-9
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-8
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-7
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-6
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-5
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-4
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-3
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-2
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-1
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

