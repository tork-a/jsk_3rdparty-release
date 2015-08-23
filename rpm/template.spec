Name:           ros-indigo-collada-urdf-jsk-patch
Version:        2.0.5
Release:        0%{?dist}
Summary:        ROS collada_urdf_jsk_patch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_urdf_jsk_patch
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       gts
Requires:       python-catkin_tools
Requires:       ros-indigo-angles
Requires:       ros-indigo-assimp-devel
Requires:       ros-indigo-class-loader
Requires:       ros-indigo-collada-parser
Requires:       ros-indigo-collada-urdf
Requires:       ros-indigo-geometric-shapes
Requires:       ros-indigo-kdl-parser
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-resource-retriever
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
Requires:       ros-indigo-urdf
BuildRequires:  collada-dom-devel
BuildRequires:  git
BuildRequires:  gts
BuildRequires:  python-catkin_tools
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-assimp-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-class-loader
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-collada-parser
BuildRequires:  ros-indigo-collada-urdf
BuildRequires:  ros-indigo-geometric-shapes
BuildRequires:  ros-indigo-kdl-parser
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-resource-retriever
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-tf

%description
unaccepted patch for collada_urdf

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
* Mon Aug 24 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.4-1
- Autogenerated by Bloom

* Tue Aug 18 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.4-0
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

