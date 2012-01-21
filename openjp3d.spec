%define fver    %(echo %{version} | tr . _)
Summary:	JPEG2000 Part 10 Verification Model library
Summary(pl.UTF-8):	Biblioteka obsługująca JPEG 2000 Part 10 Verification Model library
Name:		openjp3d
Version:	1.3
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: http://code.google.com/p/openjpeg/downloads/list
Source0:	http://openjpeg.googlecode.com/files/%{name}_v%{fver}.tar.gz
# Source0-md5:	9520aeaf1877424b5c537dd7fd809926
URL:		http://www.openjpeg.org/
BuildRequires:	cmake >= 2.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenJP3D library contains a complete JPEG2000 Part 10 (ISO/IEC 15444-10
JP3D) Verification Model encoder and decoder.

%description -l pl.UTF-8
Biblioteka OpenJP3D zawiera pełną implementację kodera i dekodera
danych JPEG2000 Part 10 (ISO/IEC 15444-10 JP3D) Verification Model.

%package devel
Summary:	Header file for OpenJP3D library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki OpenJP3D
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header file needed for developing programs
using the OpenJP3D library.

%description devel -l pl.UTF-8
Ten pakiet zawiera plik nagłówkowy potrzebny do tworzenia programów
wykorzystujących bibliotekę OpenJP3D.

%package progs
Summary:	OpenJP3D codec programs
Summary(pl.UTF-8):	Programy kodujące/dekodujące format OpenJP3D
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
OpenJP3D codec programs.

%description progs -l pl.UTF-8
Programy kodujące/dekodujące format OpenJP3D.

%prep
%setup -q -n %{name}_v%{fver}

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE
%attr(755,root,root) %{_bindir}/jp3d_to_volume
%attr(755,root,root) %{_bindir}/volume_to_jp3d
%attr(755,root,root) %{_libdir}/libopenjp3d.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenjp3d.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenjp3d.so
%{_includedir}/openjp3d-1.3
%{_includedir}/openjp3d.h
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/OpenJP3D*.cmake
%{_pkgconfigdir}/libopenjp3d.pc
