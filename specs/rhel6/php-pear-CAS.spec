# remirepo/fedora spec file for php-pear-CAS
#
# Copyright (c) 2010-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name CAS
%global channel   __uri
#global prever    RC7


Name:           php54-pear-CAS
Version:        1.3.4
Release:        3%{?dist}
Summary:        Central Authentication Service client library in php

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://wiki.jasig.org/display/CASC/phpCAS

Source0:        http://downloads.jasig.org/cas-clients/php/%{version}%{?prever}/%{pear_name}-%{version}%{?prever}.tgz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  php54-pear
BuildRequires:  php54-composer(theseer/autoload)

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php54-pear(PEAR)
Requires:       php54-curl
Requires:       php54-dom
Requires:       php54-pcre
Requires:       php54-pdo
Requires:       php54-session
Requires:       php54-spl
# Optional: php54-imap (when use Proxied Imap)

Provides:       php54-pear(%{channel}/%{pear_name}) = %{version}
Provides:       php54-composer(jasig/phpcas) = %{version}
# this library is mostly known as phpCAS
Provides:       phpCAS = %{version}-%{release}


%description
This package is a PEAR library for using a Central Authentication Service.

Autoloader '%{pear_phpdir}/CAS/Autoload.php';


%prep
%setup -q -c

cd %{pear_name}-%{version}%{?prever}
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}%{?prever}
# Empty build section, most likely nothing required.


%install
rm -rf %{buildroot}
cd %{pear_name}-%{version}%{?prever}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

# Rewrite a classmap autoloader (upstream is broken)
%{_bindir}/phpab \
    --output %{buildroot}%{pear_phpdir}/CAS/Autoload.php  \
             %{buildroot}%{pear_phpdir}


%clean
rm -rf %{buildroot}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{channel}/%{pear_name} >/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/CAS
%{pear_phpdir}/CAS.php


%changelog
* Wed Feb 01 2017 SWAELENS Jonathan <jonathan@opensides.be> - 1.3.4-3
- make packages compatible with php 5.4

* Wed Oct 19 2016 Remi Collet <remi@fedoraproject.org> - 1.3.4-3
- fix broken autoloader

* Tue Nov 17 2015 Remi Collet <remi@fedoraproject.org> - 1.3.4-1
- update to Version 1.3.4
- add provides php-composer(jasig/phpcas)

* Mon Jul 28 2014 Remi Collet <remi@fedoraproject.org> - 1.3.4-1
- update to Version 1.3.3

* Sat Dec 29 2012 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to Version 1.3.2, security fix for
  CVE-2012-5583 Missing CN validation of CAS server certificate
- add requires for all needed php extensions

* Wed Mar 14 2012 Remi Collet <remi@fedoraproject.org> - 1.3.0-2
- License is ASL 2.0, https://github.com/Jasig/phpCAS/issues/32
- New sources,        https://github.com/Jasig/phpCAS/issues/31
- update to Version 1.3.0

* Sat Jun 11 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.2.2-1
- update to Version 1.2.2 (stable) - API 1.2.2 (stable)
- dont requires domxml-php4-to-php5 anymore
- fix URL
- link %%doc to pear_docdir

* Mon Oct 04 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.3-1
- update to 1.1.3
- fix CVE-2010-3690, CVE-2010-3691, CVE-2010-3692
- set timezone during build

* Tue Aug 03 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.2-1
- update to 1.1.2
- fix  CVE-2010-2795, CVE-2010-2796, #620753

* Thu May 20 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.1-1
- update to 1.1.1

* Thu May 20 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.0-1
- update to 1.1.0 finale

* Sun Mar 14 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.0-0.1.RC7
- initial packaging (using pear make-rpm-spec CAS-1.1.0RC7.tgz)
