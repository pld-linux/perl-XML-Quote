#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Quote
Summary:	XML::Quote - functions to quote/dequote strings in "XML"-way
Summary(pl):	XML::Quote - funkcje do cytowania ³añcuchów w sposób "XML-owy"
Name:		perl-XML-Quote
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	98f45c2efeeea13793949e5c74689741
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions to quote/dequote strings in "XML"-way.

All functions are written in XS and are very fast; they correctly
process UTF-8, tied, overloaded variables and all the rest of Perl
"magic".

%description -l pl
Ten modu³ udostêpnia funkcje do cytowania ³añcuchów w sposób
"XML-owy".

Wszystkie funkcje s± napisane w XS i s± bardzo szybkie. Poprawnie
przetwarzaj± UTF-8, zmienne zwi±zane i przeci±¿one, a tak¿e ca³±
resztê perlowej "magii".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/auto/XML/Quote/Quote.bs
%attr(755,root,root) %{perl_vendorarch}/auto/XML/Quote/Quote.so
%{perl_vendorarch}/auto/XML/Quote/autosplit.ix
%{_mandir}/man3/*
