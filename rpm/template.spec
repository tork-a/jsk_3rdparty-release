Name:           ros-jade-voice-text
Version:        2.0.2
Release:        0%{?dist}
Summary:        ROS voice_text package

Group:          Development/Libraries
License:        HOYA License
URL:            http://ros.org/wiki/voice_text
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-jade-catkin

%description
voice_text (www.voicetext.jp)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Jun 29 2015 k-okada <t@t.com> - 2.0.2-0
- Autogenerated by Bloom

* Mon Jun 22 2015 k-okada <t@t.com> - 2.0.1-1
- Autogenerated by Bloom

* Sun Jun 21 2015 k-okada <t@t.com> - 2.0.1-0
- Autogenerated by Bloom

