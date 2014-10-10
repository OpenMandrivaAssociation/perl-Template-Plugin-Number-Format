%define upstream_name    Template-Plugin-Number-Format
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Plugin/filter interface to Number::Format
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Number::Format)
BuildRequires:	perl(Template)
BuildArch:	noarch

%description
Template::Plugin::Number::Format makes the number-munging grooviness of
Number::Format available to your templates. It is used like a plugin, but
installs filters into the current context.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Template
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 405534
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.02-3mdv2009.0
+ Revision: 241951
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2008.0
+ Revision: 63963
- update to new version 1.02


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2007.1
+ Revision: 138861
- Imported perl-Template-Plugin-Number-Format-1.01-1mdv2007.1 into SVN repository.

* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2007.1
- first mdv release

