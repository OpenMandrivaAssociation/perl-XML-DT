%define upstream_name 	 XML-DT
%define upstream_version 0.63

%define req_xml_libxml_version %perl_convert_version 1.54

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.63
Release:	3

Summary:	A perl XML down translate module
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/XML/XML-DT-0.63.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(XML::LibXML) >= %{req_xml_libxml_version}
BuildRequires:	perl(XML::DTDParser)
BuildArch:	noarch
Requires: 	perl(XML::LibXML) >= %{req_xml_libxml_version}

%description
The XML::DT module is a perl module that does XML down translation.
Based on XML::LibXML, it is designed to perform simple and
compact translation/processing of XML documents.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
chmod 755 examples/*.pl
perl Makefile.PL INSTALLDIRS=vendor <<EOF
XML::LibXML
EOF
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes examples
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/XML

%changelog
* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.560.0-1mdv2011.0
+ Revision: 638973
- update to new version 0.56

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.540.0-1mdv2011.0
+ Revision: 602395
- update to new version 0.54

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.530.0-1mdv2010.0
+ Revision: 408232
- rebuild using %%perl_convert_version

* Mon Jan 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.53-1mdv2009.1
+ Revision: 331172
- update to new version 0.53
- update to new version 0.53

* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.52-1mdv2009.1
+ Revision: 296762
- update to new version 0.52

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.51-4mdv2009.0
+ Revision: 258830
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.51-3mdv2009.0
+ Revision: 246722
- rebuild

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.51-1mdv2008.1
+ Revision: 174664
- update to new version 0.51

* Fri Feb 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-1mdv2008.1
+ Revision: 173893
- update to new version 0.50

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.47-1mdv2008.1
+ Revision: 136365
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Dec 11 2006 Olivier Thauvin <nanardon@mandriva.org> 0.47-1mdv2007.0
+ Revision: 94577
- 0.47
- Import perl-XML-DT

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.45-1mdv2007.0
- New release 0.45
- fix directory ownership
- spec cleanup

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.42-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL
	- URL
- use mkrel

* Tue Sep 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.42-1mdk
- 0.42

* Tue Jul 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.41-1mdk
- 0.41

* Tue Apr 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.40-1mdk
- 0.40

* Wed Mar 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.39-1mdk
- 0.39

* Tue Jan 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.38-1mdk
- 0.38

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.37-1mdk
- 0.37
- Adjust BuildRequires

* Tue Nov 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.35-1mdk
- 0.35

* Tue Nov 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.34-1mdk
- 0.34

* Tue Aug 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.31-1mdk
- 0.31
- Update description

* Thu Apr 22 2004 Michael Scherer <misc@mandrake.org> 0.30-1mdk
- 0.30
- Remove hardcoded Requires
- add url, rpmbuildupdate
- [DIRM]


