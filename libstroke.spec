Summary:	A stroke translation library
Summary(pl.UTF-8):	Biblioteka translacji przesuwu myszki
Name:		libstroke
Version:	0.5.1
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://www.etla.net/libstroke/%{name}-%{version}.tar.gz
# Source0-md5:	51b9a4e309ac15cfcab96191eed03cb2
Patch0:		%{name}-am15.patch
Patch1:		%{name}-am18.patch
Patch2:		%{name}-link.patch
URL:		http://www.etla.net/libstroke/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibStroke is a stroke translation library. Strokes are motions of the
mouse that can be interpreted by a program as a command. Strokes are
used extensively in CAD programs. I fell in love with them when I was
using the Mentor Graphics CAD tools and the CAD tools internally
developed by Intel.

%description -l pl.UTF-8
LibStroke to biblioteka tłumacząca ruchy myszką. Ruchy mogą być
przechwycone przez program i zinterpretowane jako komenda. Tego typu
komendy są bardzo często stosowane w programach typu CAD.

%package devel
Summary:	Header files for libstroke library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libstroke
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libstroke library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libstroke.

%package static
Summary:	Static libstroke library
Summary(pl.UTF-8):	Biblioteka statyczna libstroke
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libstroke library.

%description static -l pl.UTF-8
Biblioteka statyczna libstroke.

%package -n libgstroke
Summary:	libgstroke - GNOME stroke implementation
Summary(pl.UTF-8):	libgstroke - implementacja stroke dla GNOME
Group:		X11/Libraries
Requires:	gtk+ >= 1.2.7
Conflicts:	libstroke < 0.5.1-2

%description -n libgstroke
libgstroke - GNOME stroke implementation.

%description -n libgstroke -l pl.UTF-8
libgstroke - implementacja stroke dla GNOME.

%package -n libgstroke-devel
Summary:	Header files for libgstroke library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgstroke
Group:		X11/Development/Libraries
Requires:	libgstroke = %{version}-%{release}
Requires:	gtk+-devel >= 1.2.7

%description -n libgstroke-devel
Header files for libgstroke library.

%description -n libgstroke-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgstroke.

%package -n libgstroke-static
Summary:	Static libgstroke library
Summary(pl.UTF-8):	Statyczna biblioteka libgstroke
Group:		X11/Development/Libraries
Requires:	libgstroke-devel = %{version}-%{release}

%description -n libgstroke-static
Static libgstroke library.

%description -n libgstroke-static -l pl.UTF-8
Statyczna biblioteka libgstroke.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-x \
	--disable-tcl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT CREDITS README NEWS TODO doc/standard_strokes*
%attr(755,root,root) %{_libdir}/libstroke.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstroke.so
%{_libdir}/libstroke.la
%{_includedir}/stroke.h
%{_aclocaldir}/libstroke.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libstroke.a

%files -n libgstroke
%defattr(644,root,root,755)
%doc README.libgstroke
%attr(755,root,root) %{_libdir}/libgstroke.so.*.*

%files -n libgstroke-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstroke.so
%{_libdir}/libgstroke.la
%{_includedir}/gstroke.h
%{_aclocaldir}/libgstroke.m4

%files -n libgstroke-static
%defattr(644,root,root,755)
%{_libdir}/libgstroke.a
