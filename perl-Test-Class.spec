#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Class
Summary:	Test::Class - easily create test classes in an xUnit style
Summary(pl.UTF-8):	Test::Class - łatwe tworzenie testowych klas w stylu xUnit
Name:		perl-Test-Class
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	66a96dd9acfc2256b54012a3487ccf87
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Attribute-Handlers >= 0.77
BuildRequires:	perl-Class-ISA >= 0.32
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-Test-Simple >= 0.46
BuildRequires:	perl-Test-Builder-Tester >= 0.09
BuildRequires:	perl-Test-Differences >= 0.43
BuildRequires:	perl-Test-Exception >= 0.10
%endif
Requires:	perl(IO::File) >= 1.14
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Class provides a simple way of creating classes and objects to
test your code in an xUnit style.

%description -l pl.UTF-8
Test::Class udostępnia prosty sposób tworzenia klas i obiektów,
testujących Twój kod w stylu xUnit.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
