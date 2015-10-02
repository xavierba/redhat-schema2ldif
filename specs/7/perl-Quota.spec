Name:           perl-Quota
Version:        1.7.2
Release:        1%{?dist}
Summary:        Perl interface to file system quotas
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Quota/
Source0:        http://www.cpan.org/authors/id/T/TO/TOMZO/Quota-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Quota module provides access to file system quotas. The quotactl
system call or ioctl is used to query or set quotas on the local host, or
queries are submitted via RPC to a remote host. Mount tables can be parsed
with getmntent and paths can be translated to device files (or whatever
the actual quotactl implementations needs as argument) of the according
file system.

%prep
%setup -q -n Quota-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Quota*
%{_mandir}/man3/*

%changelog
* Thu Oct 01 2015 SWAELENS Jonathan <jonathan@opensides.be> 1.7.2-1
- Specfile autogenerated by cpanspec 1.78.
