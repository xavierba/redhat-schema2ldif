Name:           schema2ldif
Version:        1.3
Release:        2%{?dist}
Summary:        Tool to convert schema into ldif format

License:        BSD-3-Clause
URL:            https://gitlab.fusiondirectory.org/fusiondirectory/schema2ldif
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch0:         default-path-for-ldap-schema-manager.patch
BuildRequires:  perl-generators
BuildArch:      noarch

%description
schema2ldif is a tool to convert files in ldap schema format to ldif.
It supports various schema formats and exports clean and well formatted schema
in ldif format.

%prep
%setup -q
%patch -P0 -p1

%build

%install
# Install the command line utility
install -d %{buildroot}%{_bindir}
install -p -m 0755 bin/schema2ldif %{buildroot}%{_bindir}/schema2ldif
install -p -m 0755 bin/ldap-schema-manager %{buildroot}%{_bindir}/ldap-schema-manager

# Install the manpages
install -d %{buildroot}%{_mandir}/man1/
install -p -m 0644 man/schema2ldif.1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 man/ldap-schema-manager.1 %{buildroot}%{_mandir}/man1/

%files
%doc Changelog
%license LICENSE
%{_bindir}/schema2ldif
%{_bindir}/ldap-schema-manager
%{_mandir}/man1/schema2ldif.1.*
%{_mandir}/man1/ldap-schema-manager.1.*

%changelog
* Tue Jul 18 2023 Xavier Bachelot <xavier@bachelot.org> - 1.3-2
- Cleanup specfile.

* Tue Apr 25 2017 SWAELENS Jonathan <jonathan@opensides.be> - 1.3-1
- Fixes #5490 We should have a generic tool ldap-schema-manager

* Thu Oct 10 2013 Benoit Mortier <benoit.mortier@opensides.be> - 1.0-1
- Initial Release
