%define module  Template-Plugin-Number-Format
%define name    perl-%{module}
%define version 1.02
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Plugin/filter interface to Number::Format
License:        Artistic
group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Template/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
Buildrequires:  perl(Number::Format)
Buildrequires:  perl(Template)
buildArch:      noarch
buildRoot:      %{_tmppath}/%{name}-%{version}

%description
Template::Plugin::Number::Format makes the number-munging grooviness of
Number::Format available to your templates. It is used like a plugin, but
installs filters into the current context.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/Template
%{_mandir}/*/*


