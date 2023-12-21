#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
Name     : lsof
Version  : 4.99.3
Release  : 30
URL      : https://github.com/lsof-org/lsof/archive/4.99.3/lsof-4.99.3.tar.gz
Source0  : https://github.com/lsof-org/lsof/archive/4.99.3/lsof-4.99.3.tar.gz
Summary  : A utility which lists open files on a Linux/UNIX system
Group    : Development/Tools
License  : BSD-4-Clause 
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
[![builds.sr.ht status](https://builds.sr.ht/~jiegec/lsof.svg)](https://builds.sr.ht/~jiegec/lsof?)
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
%setup -q -n lsof-4.99.3
cd %{_builddir}/lsof-4.99.3
%patch -P 1 -p1
%patch -P 2 -p1
pushd ..
cp -a lsof-4.99.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703119327
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
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
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703119327
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lsof
cp %{_builddir}/lsof-%{version}/COPYING %{buildroot}/usr/share/package-licenses/lsof/a426cf8ac94c5030e6687ba1d013b428469d2734 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## install_append content
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/man/man8
install -p -m 0755 lsof %{buildroot}/usr/bin
install -p -m 0644 Lsof.8 %{buildroot}/usr/share/man/man8
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
