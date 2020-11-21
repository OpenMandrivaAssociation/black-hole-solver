%define basen black-hole-solver
%define libname_orig lib%{basen}
%define major 1
%define libname %mklibname %{basen} %{major}
%define develname %mklibname -d %{basen}

Name: %{basen}
Version: 1.10.1
Release: 1
# The entire source code is MIT except xxHash-0.6.5/ which is BSD
License: MIT and BSD
Source0: https://fc-solve.shlomifish.org/downloads/fc-solve/%{basen}-%{version}.tar.xz
URL: https://www.shlomifish.org/open-source/projects/black-hole-solitaire-solver/
Requires: %{libname}%{?_isa} = %version-%release
Summary: The Black Hole Solitaire Solver Executable
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: glibc-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Env::Path)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Inline)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(autodie)
BuildRequires: perl(base)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl-devel
BuildRequires: python3
BuildRequires: rinutils-devel
BuildRequires: valgrind
BuildRequires: xxhash-devel

%description
This is a solver, written in C, to solve the Solitaire variants “Golf”,
“Black Hole” and “All in a Row”. It provides a portable C library, and
a command line application that after being fed with a layout will emit the
cards to move.

%files
%license COPYING
%doc NEWS.asciidoc README.md
%{_bindir}/black-hole-solve
%{_mandir}/man6/black-hole-solve.6*

#--------------------------------------------------------------------

%package -n %{libname}
Summary: The Black Hole Solver dynamic libraries

%description -n %{libname}
Contains the Black Hole Solver libraries that are used by some programs.

This package is mandatory for the Black Hole Solver executable too.

%files -n %{libname}
%{_libdir}/libblack_hole_solver.so.%{major}{,.*}

#--------------------------------------------------------------------

%package -n %{develname}
Summary: The Black Hole Solitaire development tools
Requires: %{libname}%{?_isa} = %version-%release
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
Development tools for the Black Hole Solitaire Solver.

%files -n %{develname}
%_includedir/black-hole-solver/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libblack_hole_solver.so

#--------------------------------------------------------------------

%prep
%autosetup -p1
# The game limit flags are recommended by the PySolFC README.
%cmake -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir} -DBUILD_STATIC_LIBRARY= -DDISABLE_APPLYING_RPATH=TRUE -DUSE_SYSTEM_XHASH=TRUE -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
