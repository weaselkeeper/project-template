Name:           someproject
Version:        %(git describe)
Release:        0
Summary:        A few python scripts that do something
License:        GPLv2
URL:            https://github.com/weaselkeeper/%{name}
Group:          System Environment/Base
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       python
Requires:       rpm-python
Requires:       python-argparse
Requires:       python-simplejson

%description
A few utilities to ???
repos.

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{name}
#%{__mkdir_p} %{buildroot}%{_datadir}/%{name}/plugins
%{__mkdir_p} %{buildroot}%{_localstatedir}/log/%{name}
#cp -r ./plugins/*.py %{buildroot}%{_datadir}/%{name}/plugins/
cp -r ./*.py %{buildroot}%{_bindir}/
cp -r ./*.conf %{buildroot}%{_sysconfdir}/%{name}

%files
%{_bindir}/*.py
%{_sysconfdir}/%{name}/*
#%{_datadir}/%{name}/*

%pre

%post

%clean
rm -rf %{buildroot}

%changelog

* Mon Aug 26 2013 Jim Richardson <weaselkeeper@gmail.com> - 0.1
- Initial commit of base project
