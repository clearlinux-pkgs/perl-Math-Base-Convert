#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Base-Convert
Version  : 0.11
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIKER/Math-Base-Convert-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIKER/Math-Base-Convert-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-base-convert-perl/libmath-base-convert-perl_0.11-2.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Math-Base-Convert-license = %{version}-%{release}
Requires: perl-Math-Base-Convert-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Math::Base::Convert - very fast base to base conversion
SYNOPSIS
As a function

%package dev
Summary: dev components for the perl-Math-Base-Convert package.
Group: Development
Provides: perl-Math-Base-Convert-devel = %{version}-%{release}
Requires: perl-Math-Base-Convert = %{version}-%{release}

%description dev
dev components for the perl-Math-Base-Convert package.


%package license
Summary: license components for the perl-Math-Base-Convert package.
Group: Default

%description license
license components for the perl-Math-Base-Convert package.


%package perl
Summary: perl components for the perl-Math-Base-Convert package.
Group: Default
Requires: perl-Math-Base-Convert = %{version}-%{release}

%description perl
perl components for the perl-Math-Base-Convert package.


%prep
%setup -q -n Math-Base-Convert-0.11
cd %{_builddir}
tar xf %{_sourcedir}/libmath-base-convert-perl_0.11-2.debian.tar.xz
cd %{_builddir}/Math-Base-Convert-0.11
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Math-Base-Convert-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Base-Convert
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Math-Base-Convert/a9cf7b07a3b87ee68fcf59d527c77660dfd112a6
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Base::Convert.3
/usr/share/man/man3/Math::Base::Convert::Bases.3
/usr/share/man/man3/Math::Base::Convert::Bitmaps.3
/usr/share/man/man3/Math::Base::Convert::CalcPP.3
/usr/share/man/man3/Math::Base::Convert::Shortcuts.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Base-Convert/a9cf7b07a3b87ee68fcf59d527c77660dfd112a6

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Math/Base/Convert.pm
/usr/lib/perl5/vendor_perl/5.30.3/Math/Base/Convert/Bases.pm
/usr/lib/perl5/vendor_perl/5.30.3/Math/Base/Convert/Bitmaps.pm
/usr/lib/perl5/vendor_perl/5.30.3/Math/Base/Convert/CalcPP.pm
/usr/lib/perl5/vendor_perl/5.30.3/Math/Base/Convert/Shortcuts.pm
