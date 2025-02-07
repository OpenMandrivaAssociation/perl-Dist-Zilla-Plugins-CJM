%define upstream_name    Dist-Zilla-Plugins-CJM
%define upstream_version 3.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Allow a dist to have a custom Build.PL
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CPAN::Meta::Converter)
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Module::Build::ModuleInfo)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(autodie)
BuildArch:	noarch

%description
Plugins implementing ModuleInfo may call their own 'get_module_info' method
to construct a the Module::Build::ModuleInfo manpage object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc README Changes META.yml LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*


