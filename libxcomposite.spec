%define libname %mklibname xcomposite 1
%define develname %mklibname xcomposite -d
%define staticname %mklibname xcomposite -s -d

Name: libxcomposite
Summary: X Composite Library
Version: 0.4.3
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxfixes-devel >= 3.0.1.2
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Composite Library

#-----------------------------------------------------------

%package -n %{libname}
Summary: X Composite Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Composite  Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Requires: x11-proto-devel >= 1.0.0
Requires: libxfixes-devel >= 3.0.1.2
Provides: libxcomposite-devel = %{version}-%{release}
Provides: libxcomposite1-devel = %{version}-%{release}
Obsoletes: %{mklibname xcomposite 1 -d}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXcomposite.so
%{_libdir}/libXcomposite.la
%{_libdir}/pkgconfig/xcomposite.pc
%{_includedir}/X11/extensions/Xcomposite.h
%{_mandir}/man3/*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libxcomposite-static-devel = %{version}-%{release}
Provides: libxcomposite1-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xcomposite 1 -s -d}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXcomposite.a

#-----------------------------------------------------------

%prep
%setup -q -n libXcomposite-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0


