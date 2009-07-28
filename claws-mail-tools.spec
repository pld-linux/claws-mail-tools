Summary:	Tools for Claws-Mail (metapackage)
Summary(hu.UTF-8):	Eszközök Claws-Mail-hez (metacsomag)
Name:		claws-mail-tools
Version:	20090728
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.claws-mail.org/tools/claws-mail-mairix.tar.gz
# Source0-md5:	7a4cbaa1215758de5e9dcc5f67505a00
URL:		http://www.claws-mail.org/tools.php
Requires:	claws-mail-tool-mairix
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Tools for Claws-Mail (metapackage).

%description -l hu.UTF-8
Eszközök Claws-Mail-hez (metacsomag).

%package -n claws-mail-tool-mairix
Summary:	Mairix plugin for Claws Mail
Summary(hu.UTF-8):	Mairix plugin Claws Mail-hez
Group:		Applications
Requires:	claws-mail
Requires:	mairix

%description -n claws-mail-tool-mairix
A wrapper to mairix, to enable global searches in mail folders. See
README!

%description -n claws-mail-tool-mairix -l hu.UTF-8
Egy wrapper a mairix-hez, amely globális kereséseket tesz lehetővé a
könyvtárakban. Lásd a README-ben!

%prep
%setup -q -n claws-mail-mairix

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/claws-mail-tools/mairix
install README mairix.sh $RPM_BUILD_ROOT%{_datadir}/claws-mail-tools/mairix

%clean
rm -rf $RPM_BUILD_ROOT

%files -n claws-mail-tool-mairix
%defattr(644,root,root,755)
%dir %{_datadir}/claws-mail-tools
%dir %{_datadir}/claws-mail-tools/mairix
%doc %{_datadir}/claws-mail-tools/mairix/README
%attr(755,root,root) %{_datadir}/claws-mail-tools/mairix/mairix.sh
