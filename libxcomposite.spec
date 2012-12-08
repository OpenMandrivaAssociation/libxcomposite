%define major 1
%define libname %mklibname xcomposite %{major}
%define develname %mklibname xcomposite -d

Name: libxcomposite
Summary: X Composite Library
Version: 0.4.3
Release: 5
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxfixes-devel >= 3.0.1.2
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Composite Library

%package -n %{libname}
Summary: X Composite Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Composite  Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libxcomposite-devel = %{version}-%{release}
Obsoletes: %{_lib}xcomposite1-devel < 0.4.3
Obsoletes: %{_lib}xcomposite-static-devel < 0.4.3
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXcomposite-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libname}
%{_libdir}/libXcomposite.so.%{major}*

%files -n %{develname}
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
%{_includedir}/X11/extensions/Xcomposite.h
%{_mandir}/man3/*



%changelog
* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.4.3-4
+ Revision: 745656
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-3
+ Revision: 662421
- mass rebuild

* Fri Feb 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.4.3-2
+ Revision: 638558
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Thu Oct 28 2010 Thierry Vignaud <tv@mandriva.org> 0.4.3-1mdv2011.0
+ Revision: 589770
- new release

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 0.4.2-1mdv2011.0
+ Revision: 556454
- new release

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 0.4.1-1mdv2010.1
+ Revision: 463608
- new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.0-4mdv2010.0
+ Revision: 425882
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-3mdv2009.0
+ Revision: 223066
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.4.0-2mdv2008.1
+ Revision: 151700
- Update BuildRequires and rebuild.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 04 2007 Colin Guthrie <cguthrie@mandriva.org> 0.4.0-1mdv2008.0
+ Revision: 48013
- Update to libXcomposite 0.4.0

* Thu May 03 2007 Colin Guthrie <cguthrie@mandriva.org> 0.3.2-1mdv2008.0
+ Revision: 20928
- New Release 0.3.2 (Adds protocol man pages to -devel package)

* Wed May 02 2007 Colin Guthrie <cguthrie@mandriva.org> 0.3.1-1mdv2008.0
+ Revision: 20515
- New Release 0.3.1 (fixes an incorrect call to UnlockDisplay)


* Fri Mar 16 2007 Colin Guthrie <cguthrie@mandriva.org> 0.3-3mdv2007.1
+ Revision: 144826
- Rebuild to allow automated pkgconfig Provides: to be added.

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

