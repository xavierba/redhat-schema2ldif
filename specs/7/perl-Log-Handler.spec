Name:           perl-Log-Handler
Version:        0.87
Release:        1%{?dist}
Summary:        Log messages to several outputs
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Log-Handler/
Source0:        http://www.cpan.org/authors/id/B/BL/BLOONIX/Log-Handler-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(Config::Properties)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Email::Date)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(YAML)
Requires:       perl(Carp)
Requires:       perl(Config::General)
Requires:       perl(Config::Properties)
Requires:       perl(Data::Dumper)
Requires:       perl(DBI)
Requires:       perl(Email::Date)
Requires:       perl(File::Spec)
Requires:       perl(Params::Validate)
Requires:       perl(Test::More)
Requires:       perl(Time::HiRes)
Requires:       perl(YAML)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Log::Handler is a object oriented handler for logging, tracing and
debugging. It is very easy to use and provides a simple interface for
multiple output objects with lots of configuration parameters. You can
easily filter the amount of logged information on a per-output base, define
priorities, create patterns to format the messages and reload the complete
logging machine.

%prep
%setup -q -n Log-Handler-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE META.json perl-Log-Handler.spec README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Sep 30 2015 SWAELENS Jonathan <jonathan@opensides.be> 0.87-1
- Specfile autogenerated by cpanspec 1.78.
