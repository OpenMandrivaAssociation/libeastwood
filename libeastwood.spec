%define	major	1
%define	libname %mklibname eastwood %{major}
%define	libdev	%mklibname -d eastwood

Summary:	Game data library
Name:		libeastwood
Version:	0.3.1
Release:	2
License:	GPLv3+
Group:		System/Libraries
URL:		https://launchpad.net/doonlunacy
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	SDL-devel SDL_mixer-devel libsamplerate-devel python-devel
BuildRequires:	cmake python-setuptools

%description
This library provides support for handling wsa, shp, icn, cps, pal, adl, voc,
pak++ data files used in some games (mainly targetting Dune 2).

%package -n	%{libname}
Summary:	Game data library
Group:		System/Libraries

%description -n	%{libname}
This library provides support for handling wsa, shp, icn, cps, pal, adl, voc,
pak++ data files used in some games (mainly targetting Dune 2).

%package -n	%{libdev}
Summary:	Development files and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n	%{libdev}
This package contains the headers needed to build applications with %{name}.

%package -n	python-eastwood
Summary:	Python bindings for %{name}
Group:		Development/Python

%description -n	python-eastwood
This package contains python bindings for %{name} and eastwood, a command line
utility using the bindings.

%prep
%setup -q

%build
%cmake -DLIBEASTWOOD_BUILD_PYTHON=1 -DLIBEASTWOOD_BUILD_SDL=1
%make

%install
cd build
%makeinstall_std

%files -n %{libname}
%doc README
%{_libdir}/libeastwood.so.%{major}*

%files -n %{libdev}
%doc doc/* TODO
%{_includedir}/eastwood
%{_libdir}/libeastwood.so
%{_libdir}/pkgconfig/libeastwood.pc
%{_datadir}/cmake/Modules/FindLibEastwood.cmake

%files -n python-eastwood
%{_bindir}/eastwood
%{python_sitearch}/eastwood.py*
%{python_sitearch}/pyeastwood*
