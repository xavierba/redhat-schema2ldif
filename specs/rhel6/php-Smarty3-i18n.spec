Name:           php54-php-Smarty3-i18n
Version:        1.0     
Release:        1%{dist}
Summary:        Gettext support for Smarty3

Group:          Development/Libraries
License:        LGPLv2
URL:            https://forge.fusiondirectory.org/projects/smarty3-i18n
Source0:        http://repos.fusiondirectory.org/sources/1.0/smarty3-i18n/smarty3-i18n-1.0.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:       php54-php-Smarty3
BuildArch:      noarch
Obsoletes:      smarty-gettext

%description
Smarty gettext plug-in provides an internationalization support
for the PHP template engine Smarty version 3.

%prep
%setup -q -n smarty3-i18n-%{version}

%build

%install
# Clean buildroot before install
rm -rf %{buildroot} 

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
%doc README COPYING ChangeLog AUTHORS
%{_datadir}/php/Smarty3/plugins/block.t.php
%{_bindir}/tsmarty2c

%changelog
* Sat Jun 18 2016 SWAELENS Jonathan <jonathan@opensides.be> - 1.0-2
- Take the same name type of collections package

* Mon Oct 7 2013 Benoit Mortier <benoit.mortier@opensides.be> - 1.0-1
- Initial Release
