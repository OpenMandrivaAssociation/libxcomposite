%define libxcomposite %mklibname xcomposite 1
Name: libxcomposite
Summary: X Composite Library
Version: 0.4.0
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libx11-devel		>= 1.1.3
BuildRequires: libxfixes-devel		>= 4.0.3
BuildRequires: libxdmcp-devel		>= 1.0.2
BuildRequires: libxau-devel		>= 1.0.3
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: libxext-devel		>= 1.0.3

%description
X Composite Library

#-----------------------------------------------------------

%package -n %{libxcomposite}
Summary: X Composite Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxcomposite}
X Composite  Library

#-----------------------------------------------------------

%package -n %{libxcomposite}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: x11-proto-devel >= 1.0.0
Requires: libxfixes-devel >= 3.0.1.2
Provides: libxcomposite-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Requires: %{libxcomposite} = %{version}

%description -n %{libxcomposite}-devel
Development files for %{name}

%pre -n %{libxcomposite}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxcomposite}-devel
%defattr(-,root,root)
%{_libdir}/libXcomposite.so
%{_libdir}/libXcomposite.la
%{_libdir}/pkgconfig/xcomposite.pc
%{_includedir}/X11/extensions/Xcomposite.h
%{_mandir}/man3/*

#-----------------------------------------------------------

%package -n %{libxcomposite}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxcomposite}-devel = %{version}
Provides: libxcomposite-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxcomposite}-static-devel
Static development files for %{name}

%files -n %{libxcomposite}-static-devel
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxcomposite}
%defattr(-,root,root)
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0


