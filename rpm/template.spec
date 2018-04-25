Name:           ros-kinetic-rospatlite
Version:        2.1.10
Release:        0%{?dist}
Summary:        ROS rospatlite package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rospatlite
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-std-msgs

%description
rospatlite

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
* Wed Apr 25 2018 Takuya Nakaoka <nakaokat@gmail.com> - 2.1.10-0
- Autogenerated by Bloom

* Tue Apr 24 2018 Takuya Nakaoka <nakaokat@gmail.com> - 2.1.9-0
- Autogenerated by Bloom

* Tue Apr 17 2018 Takuya Nakaoka <nakaokat@gmail.com> - 2.1.8-0
- Autogenerated by Bloom

* Mon Apr 09 2018 Takuya Nakaoka <nakaokat@gmail.com> - 2.1.7-0
- Autogenerated by Bloom

* Thu Nov 23 2017 Takuya Nakaoka <nakaokat@gmail.com> - 2.1.6-0
- Autogenerated by Bloom

* Sun Jul 16 2017 Takuya Nakaoka <nakaokat@gmail.com> - 2.1.4-0
- Autogenerated by Bloom

* Wed Jul 05 2017 Takuya Nakaoka <nakaokat@gmail.com> - 2.1.1-0
- Autogenerated by Bloom

* Sun Jul 02 2017 Takuya Nakaoka <nakaokat@gmail.com> - 2.1.0-0
- Autogenerated by Bloom

* Tue May 09 2017 Takuya Nakaoka <nakaokat@gmail.com> - 2.0.20-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Takuya Nakaoka <nakaokat@gmail.com> - 2.0.19-0
- Autogenerated by Bloom

* Sun Oct 30 2016 Takuya Nakaoka <nakaokat@gmail.com> - 2.0.18-1
- Autogenerated by Bloom

* Sat Oct 29 2016 Takuya Nakaoka <nakaokat@gmail.com> - 2.0.18-0
- Autogenerated by Bloom

