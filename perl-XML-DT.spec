%define module 	XML-DT
%define version 0.52
%define release %mkrel 1

%define req_xml_libxml_version 1.54

Summary:	A perl XML down translate module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Url:		http://search.cpan.org/dist/%{module}
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
Requires: 	perl-XML-LibXML >= %{req_xml_libxml_version}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(XML::LibXML) >= %{req_xml_libxml_version}
BuildRequires:	perl(XML::DTDParser)
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
The XML::DT module is a perl module that does XML down translation.
Based on XML::LibXML, it is designed to perform simple and
compact translation/processing of XML documents.

%prep
%setup -q -n %{module}-%{version}

%build
chmod 755 examples/*.pl
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
XML::LibXML
EOF
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
%doc README Changes examples
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/XML


