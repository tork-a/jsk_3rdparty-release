Name:           ros-indigo-sklearn
Version:        2.0.10
Release:        0%{?dist}
Summary:        ROS sklearn package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python-scikit-learn
Requires:       ros-indigo-ml-classifiers
Requires:       ros-indigo-rospy
BuildRequires:  python-scikit-learn
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ml-classifiers
BuildRequires:  ros-indigo-rospy

%description
ROS wrapper for the sklearn library

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

