#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lsof
Version  : 4.98.0
Release  : 28
URL      : https://github.com/lsof-org/lsof/archive/4.98.0/lsof-4.98.0.tar.gz
Source0  : https://github.com/lsof-org/lsof/archive/4.98.0/lsof-4.98.0.tar.gz
Summary  : A utility which lists open files on a Linux/UNIX system
Group    : Development/Tools
License  : BSD-4-Clause Spencer-94
Requires: lsof-bin = %{version}-%{release}
Requires: lsof-license = %{version}-%{release}
Requires: lsof-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(libtirpc)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-fix-build.patch
Patch2: test.patch

%description
[![Circle CI](https://circleci.com/gh/lsof-org/lsof.svg?style=svg)](https://circleci.com/gh/lsof-org/lsof)
[![Cirrus CI](https://img.shields.io/cirrus/github/lsof-org/lsof)](https://cirrus-ci.com/github/lsof-org/lsof)
[![Read the Docs](https://readthedocs.org/projects/lsof/badge/?version=latest)](https://lsof.readthedocs.io/en/latest/)

%package bin
Summary: bin components for the lsof package.
Group: Binaries
Requires: lsof-license = %{version}-%{release}

%description bin
bin components for the lsof package.


%package license
Summary: license components for the lsof package.
Group: Default

%description license
license components for the lsof package.


%package man
Summary: man components for the lsof package.
Group: Default

%description man
man components for the lsof package.


%prep
%setup -q -n lsof-4.98.0
cd %{_builddir}/lsof-4.98.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674492978
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd tests
make test
make opt
popd

%install
export SOURCE_DATE_EPOCH=1674492978
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lsof
cp %{_builddir}/lsof-%{version}/COPYING %{buildroot}/usr/share/package-licenses/lsof/a426cf8ac94c5030e6687ba1d013b428469d2734 || :
%make_install
## install_append content
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/man/man8
install -p -m 0755 lsof %{buildroot}/usr/bin
install -p -m 0644 Lsof.8 %{buildroot}/usr/share/man/man8
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lsof

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lsof/a426cf8ac94c5030e6687ba1d013b428469d2734

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/Lsof.8
