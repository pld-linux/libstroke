Summary:	a stroke translation library
Summary(pl):	biblioteka translacji przesuwu myszki
Name:		libstroke
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://www.etla.net/libstroke/%{name}-%{version}.tar.gz
URL:		http://www.etla.net/libstroke/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%description -l pl devel
Pliki nag³ówkowe i dokumetacja do libstroke.

%package static
Summary:	Static libstroke library
Summary(pl):	Biblioteka statyczna libstroke
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libstroke library.

%description -l pl static
Biblioteka statyczna libstroke.

%prep
%setup -q

%build
%configure2_13 \
	--with-x \
	--disable-tcl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS CREDITS README* NEWS TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
