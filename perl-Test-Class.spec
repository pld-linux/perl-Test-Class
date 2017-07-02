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
Version:	0.50
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4cc3aaad36b72f424ed90122701d2451
URL:		http://search.cpan.org/dist/Test-Class/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Attribute-Handlers >= 0.77
BuildRequires:	perl-Class-ISA >= 0.32
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-Test-Simple >= 0.46
BuildRequires:	perl-Test-Builder-Tester >= 1.04
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
%{perl_vendorlib}/Test/Class.pm
%{perl_vendorlib}/Test/Class
%{_mandir}/man3/Test::Class.3pm*
%{_mandir}/man3/Test::Class::*.3pm*
