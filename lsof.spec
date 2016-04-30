Name:           lsof
Version:        4.88
Release:        9
License:        BSD-4-Clause
Summary:        A utility which lists open files on a Linux/UNIX system
URL:            http://people.freebsd.org/~abe/
Group:          Development/Tools
Source0:        https://download.clearlinux.org/sources/1.0/lsof_4.88-rh.tar.xz

Patch1: test.patch

%description
Lsof stands for LiSt Open Files, and it does just that: it lists
information about files that are open by the processes running on a
UNIX system.

%prep
%setup -q -n %{name}_%{version}-rh
chmod u+w tests/*
%patch1 -p1


%build
./Configure -n linux
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8
install -p -m 0755 lsof %{buildroot}%{_sbindir}
install -p -m 0644 lsof.8 %{buildroot}%{_mandir}/man8

%check
pushd tests
make test
make opt

popd


%files
%doc 00* README.lsof_*
%{_sbindir}/%{name}
%{_mandir}/man*/*
