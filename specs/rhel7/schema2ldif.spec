Name:           schema2ldif
Version:        1.3
Release:        1%{?dist}
Summary:        Tool to convert schema into ldif format

License:        BSD
URL:            https://forge.fusiondirectory.org/projects/schema2ldif
Source0:        http://repos.fusiondirectory.org/sources/1.0/schema2ldif/schema2ldif-1.3.tar.gz
Patch0:         default-path-for-ldap-schema-manager.patch
BuildArch:      noarch

%description
schema2ldif is a tool to convert files in ldap schema format to ldif. 
It support various schema format and export clean an well format schema 
in ldif format.

%prep
%setup -q -n schema2ldif-1.3
%patch0 -p1

%build

%install
# Install the command line utility
install -d %{buildroot}%{_bindir}
install -p -m 0755 bin/schema2ldif %{buildroot}%{_bindir}/schema2ldif
install -p -m 0755 bin/ldap-schema-manager %{buildroot}%{_bindir}/ldap-schema-manager

#install the manpage
install -d %{buildroot}%{_mandir}/man1/
install -p -m 0644  man/schema2ldif.1 %{buildroot}%{_mandir}/man1/schema2ldif.1.gz
install -p -m 0644  man/ldap-schema-manager.1 %{buildroot}%{_mandir}/man1/ldap-schema-manager.1.gz

%files
%doc Changelog LICENSE
%{_bindir}/schema2ldif
%{_bindir}/ldap-schema-manager
%{_mandir}/man1/schema2ldif.1.gz
%{_mandir}/man1/ldap-schema-manager.1.gz

%changelog
* Tue Apr 25 2017 SWAELENS Jonathan <jonathan@opensides.be> - 1.3-1
- Fixes #5490 We should have a generic tool ldap-schema-manager

* Mon Oct 10 2013 Benoit Mortier <benoit.mortier@opensides.be> - 1.0-1
- Initial Release
