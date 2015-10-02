Name:           perl-HTTP-Daemon-SSL
Version:        1.04
Release:        1%{?dist}
Summary:        Simple http server class with SSL support
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Daemon-SSL/
Source0:        http://www.cpan.org/authors/id/A/AU/AUFFLICK/HTTP-Daemon-SSL-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Daemon) >= 1
BuildRequires:  perl(IO::Socket::SSL) >= 0.93
Requires:       perl(HTTP::Daemon) >= 1
Requires:       perl(IO::Socket::SSL) >= 0.93
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Instances of the HTTP::Daemon::SSL class are HTTP/1.1 servers that listen
on a socket for incoming requests. The HTTP::Daemon::SSL is a sub-class of
IO::Socket::SSL, so you can perform socket operations directly on it too.

%prep
%setup -q -n HTTP-Daemon-SSL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
#make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc BUGS Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Sep 30 2015 SWAELENS Jonathan <jonathan@opensides.be> 1.04-1
- Specfile autogenerated by cpanspec 1.78.
