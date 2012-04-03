Summary: mako for apptansu-python3.2
Name: apptansu-python3.2-mako
Version: 0.6.2
Release: 1%{?dist}
License: MIT
Vendor: Apptansu
Group: Development/Languages
Source: mako-%{version}.tgz

BuildRequires: apptansu-python3.2
BuildRequires: apptansu-python3.2-distribute
# Without AutoReq: no, the system python gets picked up as a dependency
# possibly due to it being the first one found when resolving shebangs with
# /usr/bin/env python
AutoReq: no
Requires: apptansu-python3.2

%define _prefix /usr/lib/apptansu

%description
mako for apptansu-python3.2

%prep
%setup -q -n mako-%{version}

%build

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_prefix}/bin/mako-render \
   %{buildroot}%{_prefix}/bin/mako-render-3.2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}/*

%changelog
* Sun Feb 05 2012 Apptansu <support@apptansu.com> 0.6.2-1
- Initial packaging.
