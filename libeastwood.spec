%define	major	1
%define	libname %mklibname eastwood %{major}
%define	libdev	%mklibname -d eastwood

%define	sdlname %mklibname SDL_eastwood %{major}

Summary:	Game data library
Name:		libeastwood
Version:	0.3
Release:	%mkrel 2
License:	GPLv3
Group:		System/Libraries
URL:		http://launchpad.net/doonlunacy
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	SDL-devel SDL_mixer-devel libsamplerate-devel python-devel
BuildRequires:	cmake python-setuptools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This library provides support for handling wsa, shp, icn, cps, pal, adl, voc,
pak++ data files used in some games (mainly targetting Dune 2).

%package -n	%{libname}
Summary:	Game data library
Group:		System/Libraries

%description -n	%{libname}
This library provides support for handling wsa, shp, icn, cps, pal, adl, voc,
pak++ data files used in some games (mainly targetting Dune 2).

%package -n	%{sdlname}
Summary:	Game data library
Group:		System/Libraries

%description -n	%{sdlname}
This library provides SDL support for libeastwood.

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
%define _cmake_verbose 1
%cmake -DLIBEASTWOOD_BUILD_PYTHON=1 -DLIBEASTWOOD_BUILD_SDL=1
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/libeastwood.so.%{major}*

%files -n %{sdlname}
%defattr(-,root,root)
%{_libdir}/libSDL_eastwood.so.%{major}*

%files -n %{libdev}
%defattr(-,root,root)
%doc doc/* TODO
%{_includedir}/eastwood
%{_libdir}/libeastwood.so
%{_libdir}/libSDL_eastwood.so
%{_libdir}/pkgconfig/libeastwood.pc
%{_datadir}/cmake/Modules/FindLibEastwood.cmake

%files -n python-eastwood
%defattr(-,root,root)
%{_bindir}/eastwood
%{python_sitearch}/eastwood.py*
%{python_sitearch}/pyeastwood*
