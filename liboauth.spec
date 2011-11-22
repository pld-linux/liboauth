Summary:	OAuth library functions
Name:		liboauth
Version:	0.9.5
Release:	1
License:	MIT
Group:		Libraries
URL:		http://liboauth.sourceforge.net/
Source0:	http://liboauth.sourceforge.net/pool/%{name}-%{version}.tar.gz
# Source0-md5:	2a8e01914dc85f297ef69c1ab300d0ec
BuildRequires:	curl-devel
BuildRequires:	nss-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liboauth is a collection of POSIX-c functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and
encode parameters according to OAuth specification and offers
high-level functionality to sign requests or verify OAuth signatures
as well as perform HTTP requests.


%package devel
Summary:	Development files for liboauth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel

%description    devel
This package contains libraries and header files for developing
applications that use liboauth.


%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-nss
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING.MIT README
%attr(755,root,root) %{_libdir}/liboauth.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liboauth.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/oauth.h
%{_libdir}/liboauth.so
%{_pkgconfigdir}/oauth.pc
%{_mandir}/man3/oauth.3*
