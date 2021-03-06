#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Class
Summary:	Test::Class - easily create test classes in an xUnit style
Summary(pl.UTF-8):	Test::Class - łatwe tworzenie testowych klas w stylu xUnit
Name:		perl-Test-Class
Version:	0.52
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc70accee2dec2baa95d6df6f231dfa9
URL:		https://metacpan.org/release/Test-Class
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Attribute-Handlers >= 0.77
BuildRequires:	perl-Class-ISA >= 0.32
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-MRO-Compat >= 0.11
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Storable >= 2.04
BuildRequires:	perl-Test-Simple >= 0.78
BuildRequires:	perl-Test-Builder-Tester >= 1.04
BuildRequires:	perl-Test-Exception >= 0.25
BuildRequires:	perl-Try-Tiny
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
%{perl_vendorlib}/Test/Class.pm
%{perl_vendorlib}/Test/Class
%{_mandir}/man3/Test::Class.3pm*
%{_mandir}/man3/Test::Class::*.3pm*
