%define upstream_name 	 XML-DT
%define upstream_version 0.53

%define req_xml_libxml_version %perl_convert_version 1.54

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A perl XML down translate module
License: 	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(XML::LibXML) >= %{req_xml_libxml_version}
BuildRequires:	perl(XML::DTDParser)
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
Requires: 	perl-XML-LibXML >= %{req_xml_libxml_version}

%description
The XML::DT module is a perl module that does XML down translation.
Based on XML::LibXML, it is designed to perform simple and
compact translation/processing of XML documents.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
