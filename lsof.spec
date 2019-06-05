Name:           lsof
Version:        4.91
Release:        14
License:        BSD-4-Clause
Summary:        A utility which lists open files on a Linux/UNIX system
URL:            http://people.freebsd.org/~abe/
Group:          Development/Tools
Source0:        https://src.fedoraproject.org/repo/pkgs/rpms/lsof/lsof_4.91-rh.tar.xz/sha512/c73037ef2b69ebb49ba4badc19508adafe0eff8216a4d7007aa084d8ba246cba4f5fd1d729a5e53fa2d55cb7f27dbaf340c72575b297e5ac331a1d547e986e70/lsof_4.91-rh.tar.xz

Patch1: test.patch

%description
Lsof stands for LiSt Open Files, and it does just that: it lists
information about files that are open by the processes running on a
UNIX system.

%prep
%setup -q -n lsof_%{version}-rh
chmod u+w tests/*
%patch1 -p1


%build
./Configure -n linux
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/man/man8
install -p -m 0755 lsof %{buildroot}/usr/bin
install -p -m 0644 lsof.8 %{buildroot}/usr/share/man/man8

%check
pushd tests
make test
make opt

popd


%files
%doc 00* README.lsof_*
/usr/bin/lsof
/usr/share/man/man*/*
