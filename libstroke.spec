Summary:	a stroke translation library
Summary(pl):	biblioteka translacji przesuwu myszki
Name:		libstroke
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://www.etla.net/libstroke/%{name}-%{version}.tar.gz
Patch0:		%{name}-am15.patch
URL:		http://www.etla.net/libstroke/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
LibStroke is a stroke translation library. Strokes are motions of the
mouse that can be interpreted by a program as a command. Strokes are
used extensively in CAD programs. I fell in love with them when I was
using the Mentor Graphics CAD tools and the CAD tools internally
developed by Intel.

%description -l pl
LibStroke to biblioteka t³umacz±ca ruchy myszk±. Ruchy mog± byæ
przechwycone przez program i zinterpretowane jako komenda. Tego typu
komendy s± bardzo czêsto stosowane w programach typu CAD.

%package devel
Summary:	Header files and develpment documentation for libstroke
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libstroke
Group:		X11/Development/Libraries

Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for libstroke.

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libstroke.

%package static
Summary:	Static libstroke library
Summary(pl):	Biblioteka statyczna libstroke
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libstroke library.

%description static -l pl
Biblioteka statyczna libstroke.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS README* NEWS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
