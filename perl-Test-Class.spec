#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Class
Summary:	Test::Class - easily create test classes in an xUnit style
Summary(pl):	Test::Class - ³atwe tworzenie testowych klas w stylu xUnit
Name:		perl-Test-Class
Version:	0.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5ed6082110c5600d1807654ff8120775
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Attribute-Handlers >= 0.77
BuildRequires:	perl-Class-ISA >= 0.32
BuildRequires:	perl-Test-Simple >= 0.46
BuildRequires:	perl-Test-Builder-Tester >= 0.09
BuildRequires:	perl-Test-Differences >= 0.43
BuildRequires:	perl-Test-Exception >= 0.10
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Class provides a simple way of creating classes and objects to
test your code in an xUnit style.

%description -l pl
Test::Class udostêpnia prosty sposób tworzenia klas i obiektów,
testuj±cych Twój kod w stylu xUnit.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv t/pod.t{,.blah}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
