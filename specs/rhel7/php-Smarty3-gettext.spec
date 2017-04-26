Name:           php-Smarty3-gettext
Version:        1.1.0
Release:        2%{dist}
Summary:        Gettext support for Smarty3

Group:          Development/Libraries
License:        LGPLv2
URL:            https://github.com/smarty-gettext/smarty-gettext
Source0:        https://github.com/smarty-gettext/smarty-gettext/archive/1.1.0.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:       php-Smarty3
BuildArch:      noarch
Obsoletes:      smarty-gettext

%description
Smarty gettext plug-in provides an internationalization support
for the PHP template engine Smarty version 3.

%prep
%setup -n smarty-gettext-1.1.0

%build

%install
# Install the Smarty Plugin
install -d -m 0755 %{buildroot}%{_datadir}/php/Smarty3/plugins
install -p -m 0644 block.t.php %{buildroot}%{_datadir}/php/Smarty3/plugins

# Install the command line utility
install -d %{buildroot}%{_bindir}
install -p -m 0755 tsmarty2c.php %{buildroot}%{_bindir}/tsmarty2c

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog
%{_datadir}/php/Smarty3/plugins/block.t.php
%{_bindir}/tsmarty2c

%changelog
* Tue Apr 25 2017 SWAELENS Jonathan <jonathan@opensides.be> - 1.1.0-1
- Use smarty-gettext github as official source

* Mon Jul 11 2016 SWAELENS Jonathan <jonathan@opensides.be> - 1.0-3
- Remove bumping php version beceause php-Smarty3 don't have the version number of PHP

* Sat Jun 18 2016 SWAELENS Jonathan <jonathan@opensides.be> - 1.0-2
- Bump php version

* Mon Oct 7 2013 Benoit Mortier <benoit.mortier@opensides.be> - 1.0-1
- Initial Release

