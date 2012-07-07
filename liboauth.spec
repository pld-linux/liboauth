Summary:	OAuth library functions
Summary(pl.UTF-8):	Biblioteka Funkcji OAuth
Name:		liboauth
Version:	0.9.7
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://liboauth.sourceforge.net/pool/%{name}-%{version}.tar.gz
# Source0-md5:	103ea90e3330dfcda7b6d59c4c697472
URL:		http://liboauth.sourceforge.net/
BuildRequires:	curl-devel
BuildRequires:	nss-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liboauth is a collection of POSIX-C functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and
encode parameters according to OAuth specification and offers
high-level functionality to sign requests or verify OAuth signatures
as well as perform HTTP requests.

%description
liboauth to zbiór funkcji POSIX-C implementujących standard OAuth Core
wg RFC 5849. liboauth udostępnia funkcje zabezpieczające i kodujące
parametry zgodnie ze specyfikacją OAuth. Oferuje także funkcje
wyższego poziomu do podpisywania żądań oraz kontroli podpisów OAuth, a
także wykonywania żądań HTTP

%package devel
Summary:	Development files for liboauth
Summary(pl.UTF-8):	Pliki programistyczne biblioteki liboauth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	nss-devel

%description devel
This package contains the header files for developing applications
that use liboauth.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących liboauth.

%package static
Summary:	Static liboauth library
Summary(pl.UTF-8):	Statyczna biblioteka liboauth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static liboauth library.

%description static -l pl.UTF-8
Statyczna biblioteka liboauth.

%prep
%setup -q

%build
%configure \
	--enable-nss
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liboauth.la

%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.MIT ChangeLog README
%attr(755,root,root) %{_libdir}/liboauth.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liboauth.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboauth.so
%{_includedir}/oauth.h
%{_pkgconfigdir}/oauth.pc
%{_mandir}/man3/oauth.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/liboauth.a
