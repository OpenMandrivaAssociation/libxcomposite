%define major 1
%define libname %mklibname xcomposite %{major}
%define devname %mklibname xcomposite -d

Summary:	X Composite Library
Name:		libxcomposite
Version:	0.4.4
Release:	11
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
X Composite Library

%package -n %{libname}
Summary:	X Composite Library
Group:		Development/X11
Provides:	%{name} = %{version}

%description -n %{libname}
X Composite  Library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxcomposite-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%setup -qn libXcomposite-%{version}
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%pre -n %{devname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libname}
%{_libdir}/libXcomposite.so.%{major}*

%files -n %{devname}
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
%{_includedir}/X11/extensions/Xcomposite.h
%{_mandir}/man3/*

