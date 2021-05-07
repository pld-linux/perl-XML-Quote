#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	Quote
Summary:	XML::Quote - functions to quote/dequote strings in "XML"-way
Summary(pl.UTF-8):	XML::Quote - funkcje do cytowania łańcuchów w sposób "XML-owy"
Name:		perl-XML-Quote
Version:	1.02
Release:	14
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	98f45c2efeeea13793949e5c74689741
URL:		http://search.cpan.org/dist/XML-Quote/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions to quote/dequote strings in "XML"-way.

All functions are written in XS and are very fast; they correctly
process UTF-8, tied, overloaded variables and all the rest of Perl
"magic".

%description -l pl.UTF-8
Ten moduł udostępnia funkcje do cytowania łańcuchów w sposób
"XML-owy".

Wszystkie funkcje są napisane w XS i są bardzo szybkie. Poprawnie
przetwarzają UTF-8, zmienne związane i przeciążone, a także całą
resztę perlowej "magii".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/XML/Quote.pm
%dir %{perl_vendorarch}/auto/XML/Quote
%attr(755,root,root) %{perl_vendorarch}/auto/XML/Quote/Quote.so
%{perl_vendorarch}/auto/XML/Quote/autosplit.ix
%{_mandir}/man3/*
