Name:           ros-indigo-mini-maxwell
Version:        2.1.11
Release:        0%{?dist}
Summary:        ROS mini_maxwell package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-roslib

%description
mini_maxwell

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
* Wed Aug 29 2018 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.11-0
- Autogenerated by Bloom

* Wed Apr 25 2018 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.10-0
- Autogenerated by Bloom

* Tue Apr 24 2018 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.9-0
- Autogenerated by Bloom

* Tue Apr 17 2018 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.8-0
- Autogenerated by Bloom

* Thu Nov 23 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.6-0
- Autogenerated by Bloom

* Sun Jul 16 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.4-0
- Autogenerated by Bloom

* Fri Jul 07 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.3-0
- Autogenerated by Bloom

* Thu Jul 06 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.2-0
- Autogenerated by Bloom

* Wed Jul 05 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.1-0
- Autogenerated by Bloom

* Sun Jul 02 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Tue May 09 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.20-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.19-0
- Autogenerated by Bloom

* Sat Oct 22 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.17-0
- Autogenerated by Bloom

* Mon Oct 17 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.16-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.14-0
- Autogenerated by Bloom

* Tue Dec 15 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.13-0
- Autogenerated by Bloom

* Thu Nov 26 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.12-1
- Autogenerated by Bloom

* Wed Nov 18 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.11-1
- Autogenerated by Bloom

* Tue Oct 13 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.11-0
- Autogenerated by Bloom

* Wed Oct 07 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.10-0
- Autogenerated by Bloom

* Tue Sep 29 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.9-0
- Autogenerated by Bloom

* Tue Sep 15 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.7-0
- Autogenerated by Bloom

* Tue Sep 08 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.6-0
- Autogenerated by Bloom

* Mon Aug 24 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.4-1
- Autogenerated by Bloom

* Tue Aug 18 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.4-0
- Autogenerated by Bloom

* Sun Aug 02 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

