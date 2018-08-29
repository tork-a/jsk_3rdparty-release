Name:           ros-melodic-collada-urdf-jsk-patch
Version:        2.1.11
Release:        0%{?dist}
Summary:        ROS collada_urdf_jsk_patch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_urdf_jsk_patch
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       gts
Requires:       python-catkin_tools
Requires:       ros-melodic-angles
Requires:       ros-melodic-assimp-devel
Requires:       ros-melodic-class-loader
Requires:       ros-melodic-collada-parser
Requires:       ros-melodic-collada-urdf
Requires:       ros-melodic-geometric-shapes
Requires:       ros-melodic-kdl-parser
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-resource-retriever
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-tf
Requires:       ros-melodic-urdf
BuildRequires:  collada-dom-devel
BuildRequires:  git
BuildRequires:  gts
BuildRequires:  python-catkin_tools
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-assimp-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-class-loader
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-collada-parser
BuildRequires:  ros-melodic-collada-urdf
BuildRequires:  ros-melodic-geometric-shapes
BuildRequires:  ros-melodic-kdl-parser
BuildRequires:  ros-melodic-mk
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-resource-retriever
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-tf

%description
unaccepted patch for collada_urdf

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
* Thu Aug 30 2018 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.1.11-0
- Autogenerated by Bloom

