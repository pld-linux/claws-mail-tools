%define		_name	claws-mail
Summary:	Tools for Claws-Mail (metapackage)
Summary(pl.UTF-8):	Narzędzia dla Claws-Mail (metapakiet)
Summary(hu.UTF-8):	Eszközök Claws-Mail-hez (metacsomag)
Name:		claws-mail-tools
Version:	20100109
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.claws-mail.org/tools/%{_name}-fix_date.tar.gz
# Source0-md5:	a6b14a22feee978adc3ec9efd7c2e0f0
Source1:	http://www.claws-mail.org/tools/%{_name}-freshmeat_search.tar.gz
# Source1-md5:	bb66ad379db3b2175641a14c5da4c7db
Source2:	http://www.claws-mail.org/tools/%{_name}-google_msgid.tar.gz
# Source2-md5:	d33e9c394221ff544f065410ae07e102
Source3:	http://www.claws-mail.org/tools/%{_name}-google_search.tar.gz
# Source3-md5:	6f9bf1e61f17978ddf1d95a5bcdeb16d
Source4:	http://www.claws-mail.org/tools/%{_name}-mairix.tar.gz
# Source4-md5:	7a4cbaa1215758de5e9dcc5f67505a00
Source5:	http://www.claws-mail.org/tools/%{_name}-multiwebsearch.tar.gz
# Source5-md5:	b5e495d3de1a5ef09dcace3dd5ca54cd
Source6:	http://www.claws-mail.org/tools/%{_name}-textviewer.tar.gz
# Source6-md5:	4d441088f9e7a05e0ba88aebd967892c
Source7:	http://www.claws-mail.org/tools/%{_name}-uudec.tar.gz
# Source7-md5:	58011671c1be76534e8c862c15ae61a4
Source8:	http://www.claws-mail.org/tools/%{_name}-uuooffice.tar.gz
# Source8-md5:	0b8a8e37af069d13a8cd11c072c62b78
Source9:	http://www.claws-mail.org/tools/%{_name}-clawsxml2csv.tar.gz
# Source9-md5:	80210a5a544b8bbedc977e8b17d7a16a
Source10:	http://www.claws-mail.org/tools/%{_name}-csv2addressbook.tar.gz
# Source10-md5:	b4e104180b2e0d5343ead82be5695c24
Source11:	http://www.claws-mail.org/tools/%{_name}-eud2gc.tar.gz
# Source11-md5:	a9b0f2e70c04b1af0467cfbb239b3922
Source12:	http://www.claws-mail.org/tools/%{_name}-mew2claws-mail.tar.gz
# Source12-md5:	8201881a0515b02de7c35951227cdcaf
Source13:	http://www.claws-mail.org/tools/%{_name}-tb2claws-mail.tar.gz
# Source13-md5:	08251ae61f6fcff5f4d17d43b509f8ba
Source14:	http://www.claws-mail.org/tools/%{_name}-outlook2claws-mail.tar.gz
# Source14-md5:	3c79b07762b3c28b838f91ab6d0a4f2d
Source15:	http://www.claws-mail.org/tools/%{_name}-vcard2xml.tar.gz
# Source15-md5:	64659bb6efe0d9a2537f5eb4af5aa53c
Source16:	http://www.claws-mail.org/tools/%{_name}-calypso_convert.tar.gz
# Source16-md5:	7cad5f850a30ac13506abc97894c3178
Source17:	http://www.claws-mail.org/tools/%{_name}-convert_mbox.tar.gz
# Source17-md5:	94f6e335f89f9a1cea3251ba4cb23453
Source18:	http://www.claws-mail.org/tools/%{_name}_kmail-mailbox2claws-mail.tar.gz
# Source18-md5:	04e99962dfa44baea36d0de2a046db78
Source19:	http://www.claws-mail.org/tools/%{_name}-tbird2claws.tar.gz
# Source19-md5:	4f35982285d9501733aea4a4944ee137
Source20:	http://www.claws-mail.org/tools/%{_name}-acroread2claws-mail.tar.gz
# Source20-md5:	d0c9f496d0e735782757b0458fe4065d
Source21:	http://www.claws-mail.org/tools/%{_name}-filter_conv_new.tar.gz
# Source21-md5:	107218041790e081ac4b19a08c5b40f8
Source22:	http://www.claws-mail.org/tools/%{_name}-filter_conv.tar.gz
# Source22-md5:	17d38982a59894dae6230ffcbf79ba54
Source23:	http://www.claws-mail.org/tools/%{_name}-gif2xface.tar.gz
# Source23-md5:	dda4a85a27c777f19dc626301f820234
Source24:	http://www.claws-mail.org/tools/%{_name}_kdeservicemenu-1.4.tar.gz
# Source24-md5:	dfa1da465c7f7c65a90fced19ed94c84
Source25:	http://www.claws-mail.org/tools/%{_name}-nautilus2claws-mail.tar.gz
# Source25-md5:	07b612f042ee9f404712f09997fc94fc
Source26:	http://www.claws-mail.org/tools/%{_name}-OOo2claws-mail.tar.gz
# Source26-md5:	e9ef781ab465600c90f3c9f3fe8db42f
Source27:	http://www.claws-mail.org/tools/%{_name}-popfile-link.tar.gz
# Source27-md5:	8aa324bb774e61eeb5ce741da08a8ea1
Source28:	http://www.claws-mail.org/tools/%{_name}-scrot2imageshack.tar.gz
# Source28-md5:	76ada2078235f8114c30830f1bac19ba
Source29:	http://www.claws-mail.org/tools/%{_name}-textviewer-pl.tar.gz
# Source29-md5:	40307fcb98a0f981c9621de6075f9436
Source30:	http://www.claws-mail.org/tools/%{_name}-thunderbird-filters-convertor.tar.gz
# Source30-md5:	84c26bca846bda374ac87fae45f76a63
Source31:	http://www.claws-mail.org/tools/%{_name}-update_po.tar.gz
# Source31-md5:	778f26d07ba903e41056d69ad44a6969
URL:		http://www.claws-mail.org/tools.php
Requires:	claws-mail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Tools for Claws-Mail (metapackage).

%description -l pl.UTF-8
Narzędzia dla Claws-Mail (metapakiet).

%description -l hu.UTF-8
Eszközök Claws-Mail-hez (metacsomag).

%package -n claws-mail-tools-fix_date
Summary:	Fix date script for Claws Mail
Summary(pl.UTF-8):	Skrypt poprawiający datę dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-fix_date
Add or fix the Date header of a message that is missing the header or
showing a non RFC-compliant value.

%description -n claws-mail-tools-fix_date -l pl.UTF-8
Dodaje lub poprawia nagłówek z datą wiadomości tak aby był zgodny z
RFC.

%package -n claws-mail-tools-freshmeat_search
Summary:	Freshmeat search script for Claws Mail
Summary(pl.UTF-8):	Skrypt do przeszukiwania freshmeat dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-freshmeat_search
Search freshmeat for the selected text.

%description -n claws-mail-tools-freshmeat_search -l pl.UTF-8
Przeszukuje serwis freshmeat według zadanego wzorca.

%package -n claws-mail-tools-google_msgid
Summary:	Script google msgid for Claws Mail
Summary(pl.UTF-8):	Skrypt google msgid dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-google_msgid
Search google for selected message-id.

%description -n claws-mail-tools-google_msgid -l pl.UTF-8
Przeszukuje google według identyfikatora wiadomości.

%package -n claws-mail-tools-google_search
Summary:	Script google search for Claws Mail
Summary(pl.UTF-8):	Skrypt google search dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-google_search
Search google for the selected text.

%description -n claws-mail-tools-google_search -l pl.UTF-8
Przeszukuje google według zadanego tekstu.

%package -n claws-mail-tools-mairix
Summary:	Mairix script for Claws Mail
Summary(pl.UTF-8):	Skrypt Mairix dla Claws Mail
Summary(hu.UTF-8):	Mairix script Claws Mail-hez
Group:		Applications
Requires:       %{name} = %{version}-%{release}
Requires:	mairix

%description -n claws-mail-tools-mairix
A wrapper to mairix, to enable global searches in mail folders. See
README!

%description -n claws-mail-tools-mairix -l pl.UTF-8
Nakładka na mairix umożliwiająca globalne wyszukiwanie w folderach
pocztowych. Zobacz README!

%description -n claws-mail-tools-mairix -l hu.UTF-8
Egy wrapper a mairix-hez, amely globális kereséseket tesz lehetővé a
könyvtárakban. Lásd a README-ben!

%package -n claws-mail-tools-multiwebsearch
Summary:	Script multiwebsearch for Claws Mail
Summary(pl.UTF-8):	Skrypt multiwebsearch dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-multiwebsearch
Search any searchable website for the selected text.

%description -n claws-mail-tools-multiwebsearch -l pl.UTF-8
Przeszukuje, według zadanego tekstu, dowolny serwis www, który się do
tego nadaje.

%package -n claws-mail-tools-textviewer
Summary:	Script textviewer for Claws Mail
Summary(pl.UTF-8):	Skrypt textviewer dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-textviewer
Attempt to view an attachment as plain text.

%description -n claws-mail-tools-textviewer -l pl.UTF-8
Próbuje wyświetlić załącznik jako zwykły tekst.

%package -n claws-mail-tools-uudec
Summary:	Script uudec for Claws Mail
Summary(pl.UTF-8):	Skrypt uudec dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-uudec
Decode and display uuencoded images.

%description -n claws-mail-tools-uudec -l pl.UTF-8
Dekoduje i wyświetla obrazki zakodowane przy pomocy uuencode.

%package -n claws-mail-tools-uuooffice
Summary:	Script uuooffice for Claws Mail
Summary(pl.UTF-8):	Skrypt uuooffice dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-uuooffice
Decode and open uuencoded documents with OpenOffice.

%description -n claws-mail-tools-uuooffice -l pl.UTF-8
Dekoduje i otwiera dokumenty OpenOffice zakodowane przy pomocy
uuencode.

%package -n claws-mail-tools-clawsxml2csv
Summary:	Script clawsxml2csv for Claws Mail
Summary(pl.UTF-8):	Skrypt clawsxml2csv dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-clawsxml2csv
Export a Claws Mail address book to csv.

%description -n claws-mail-tools-clawsxml2csv -l pl.UTF-8
Eksportuje książkę adresową claws mail do formatu csv.

%package -n claws-mail-tools-csv2addressbook
Summary:	Script csv2addressbook for Claws Mail
Summary(pl.UTF-8):	Skrypt csv2addressbook dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-csv2addressbook
Import a Thunderbird, Becky, Kmail or GMail address book.

%description -n claws-mail-tools-csv2addressbook -l pl.UTF-8
Importuje książki adresowe z: Thunderbirda, Becky, Kmaila lub GMaila.

%package -n claws-mail-tools-eud2gc
Summary:	Script eud2gc for Claws Mail
Summary(pl.UTF-8):	Skrypt eud2gc dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-eud2gc
Convert a Eudora address book to a Gnomecard.

%description -n claws-mail-tools-eud2gc -l pl.UTF-8
Konwertuje książkę adresową Eudory do formatu Gnomecard.

%package -n claws-mail-tools-mew2claws-mail
Summary:	Script mew2claws-mail for Claws Mail
Summary(pl.UTF-8):	Skrypt mew2claws-mail dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-mew2claws-mail
Import a Mew address book.

%description -n claws-mail-tools-mew2claws-mail -l pl.UTF-8
Importuje książkę adresową programu Mew.

%package -n claws-mail-tools-tb2claws-mail
Summary:	Script tb2claws-mail for Claws Mail
Summary(pl.UTF-8):	Skrypt tb2claws-mail dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-tb2claws-mail
Import The Bat! address books.

%description -n claws-mail-tools-tb2claws-mail -l pl.UTF-8
Importuje książkę adresową z programu The Bat!

%package -n claws-mail-tools-outlook2claws-mail
Summary:	Script outlook2claws-mail for Claws Mail
Summary(pl.UTF-8):	Skrypt outlook2claws-mail dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-outlook2claws-mail
Import an Outlook generated contact list.

%description -n claws-mail-tools-outlook2claws-mail -l pl.UTF-8
Importuje listę kontaktów wygenerowaną z programu Outlook.

%package -n claws-mail-tools-vcard2xml
Summary:	Script vcard2xml for Claws Mail
Summary(pl.UTF-8):	Skrypt vcard2xml dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-vcard2xml
Convert an Evolution vCard into a Claws Mail address book.

%description -n claws-mail-tools-vcard2xml -l pl.UTF-8
Konweruje wizytówki z Evolution na kontakty w książce adresowej
claws-mail.

%package -n claws-mail-tools-calypso_convert
Summary:	Script calypso_convert for Claws Mail
Summary(pl.UTF-8):	Skrypt calypso_convert dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-calypso_convert
Import mbox files with attachments from Calypso.

%description -n claws-mail-tools-calypso_convert -l pl.UTF-8
Importuje pliki w formacie mbox wraz z załącznikami z programu
Calypso.

%package -n claws-mail-tools-convert_mbox
Summary:	Script convert_mbox for Claws Mail
Summary(pl.UTF-8):	Skrypt convert_mbox dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-convert_mbox
Convert an mbox format mailbox into the MH format used by Claws Mail.

%description -n claws-mail-tools-convert_mbox -l pl.UTF-8
Konwertuje skrzynkę pocztową z formatu mbox do formatu MH używanego
przez Claws Mail.

%package -n claws-mail-tools-kmail-mailbox2claws-mail
Summary:	Script kmail-mailbox2claws-mail for Claws Mail
Summary(pl.UTF-8):	Skrypt kmail-mailbox2claws-mail dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-kmail-mailbox2claws-mail
Convert a Kmail mailbox into a Claws Mail mailbox.

%description -n claws-mail-tools-kmail-mailbox2claws-mail -l pl.UTF-8
Konwertuje skrzynkę pocztową programu Kmail do formatu Claws Mail.

%package -n claws-mail-tools-tbird2claws
Summary:	Script tbird2claws for Claws Mail
Summary(pl.UTF-8):	Skrypt tbird2claws dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-tbird2claws
Integrate a Mozilla Thunderbird mailbox into Claws Mail.

%description -n claws-mail-tools-tbird2claws -l pl.UTF-8
Integruje skrzynkę pocztową Thunderbirda z Claws Mail.

%package -n claws-mail-tools-acroread2claws-mail
Summary:	Script acroread2claws-mail for Claws Mail
Summary(pl.UTF-8):	Skrypt acroread2claws-mail dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-acroread2claws-mail
Send PDFs from Adobe Reader 7 to Claws Mail.

%description -n claws-mail-tools-acroread2claws-mail -l pl.UTF-8
Wysyła pliki PDF z programu Adobe Reader 7 do Claws Mail.

%package -n claws-mail-tools-filter_conv_new
Summary:	Script filter_conv_new for Claws Mail
Summary(pl.UTF-8):	Skrypt filter_conv_new dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-filter_conv_new
Convert Sylpheed (>= 0.9.99) filter rules into Claws' filtering rules.

%description -n claws-mail-tools-filter_conv_new -l pl.UTF-8
Konwertuje filtry wygenerowane w Sylpheed (>= 0.9.99) do formatu Claws
Mail.

%package -n claws-mail-tools-filter_conv
Summary:	Script filter_conv for Claws Mail
Summary(pl.UTF-8):	Skrypt filter_conv dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-filter_conv
Convert Sylpheed (< 0.9.99) filter rules into Claws' filtering
rules.

%description -n claws-mail-tools-filter_conv -l pl.UTF-8
Konwertuje filtry wygenerowane w Sylpheed (< 0.9.99) do formatu Claws
Mail.

%package -n claws-mail-tools-gif2xface
Summary:	Script gif2xface for Claws Mail
Summary(pl.UTF-8):	Skrypt gif2xface dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-gif2xface
Convert a 48x48 GIF file to an X-Face header.

%description -n claws-mail-tools-gif2xface -l pl.UTF-8
Konwertuje obrazek GIF o wymiarach 48x48 do nagłówka X-Face.

%package -n claws-mail-tools-kdeservicemenu
Summary:	Script kdeservicemenu for Claws Mail
Summary(pl.UTF-8):	Skrypt kdeservicemenu dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-kdeservicemenu
Send files from Konqueror to Claws Mail.

%description -n claws-mail-tools-kdeservicemenu -l pl.UTF-8
Wyślij plik z Konquerora prosto do Claws Mail.

%package -n claws-mail-tools-nautilus2claws-mail
Summary:	Script nautilus2claws-mail for Claws Mail
Summary(pl.UTF-8):	Skrypt nautilus2claws-mail dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-nautilus2claws-mail
Send files from Nautilus to Claws Mail.

%description -n claws-mail-tools-nautilus2claws-mail -l pl.UTF-8
Wyślij plik z Nautilusa prosto do Claws Mail.

%package -n claws-mail-tools-OOo2claws-mail
Summary:	Script OOo2claws-mail for Claws Mail
Summary(pl.UTF-8):	Skrypt OOo2claws-mail dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-OOo2claws-mail
Send documents from OpenOffice to Claws Mail.

%description -n claws-mail-tools-OOo2claws-mail -l pl.UTF-8
Wysyła dokumenty z OpenOffice do Claws Mail.

%package -n claws-mail-tools-popfile-link
Summary:	Script popfile-link for Claws Mail
Summary(pl.UTF-8):	Skrypt popfile-link dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-popfile-link
Open messages in POPFile control center to edit their status.

%description -n claws-mail-tools-popfile-link -l pl.UTF-8
Edytuj status wiadomości w centrum sterowania POPFile.

%package -n claws-mail-tools-scrot2imageshack
Summary:	Script scrot2imageshack for Claws Mail
Summary(pl.UTF-8):	Skrypt scrot2imageshack dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}
Requires:	scrot

%description -n claws-mail-tools-scrot2imageshack
Uses scrot to take a screenshot and then sends it to
image@imageshack.us via Claws Mail.

%description -n claws-mail-tools-scrot2imageshack -l pl.UTF-8
Automatycznie, używając scrota, wysyła zrzuty ekranowe via Claws Mail
na adres image@imageshack.us.

%package -n claws-mail-tools-textviewer-pl
Summary:	Script textviewer-pl for Claws Mail
Summary(pl.UTF-8):	Skrypt textviewer-pl dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-textviewer-pl
Display various attachments as text.

%description -n claws-mail-tools-textviewer-pl -l pl.UTF-8
Wyświetla różne załączniki jako tekst.

%package -n claws-mail-tools-thunderbird-filters-convertor
Summary:	Script thunderbird-filters-convertor for Claws Mail
Summary(pl.UTF-8):	Skrypt thunderbird-filters-convertor dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-thunderbird-filters-convertor
Convert Thunderbird filter rules into Claws' filtering rules.

%description -n claws-mail-tools-thunderbird-filters-convertor -l pl.UTF-8
Konwertuje filtry z formatu Thunderbird do formatu Claws Mail.

%package -n claws-mail-tools-update_po
Summary:	Script update_po for Claws Mail
Summary(pl.UTF-8):	Skrypt update_po dla Claws Mail
Group:		Applications
Requires:       %{name} = %{version}-%{release}

%description -n claws-mail-tools-update_po
Update the .po files named on the command line.

%description -n claws-mail-tools-update_po -l pl.UTF-8
Aktualizuj pliki .po, którym nazwy nadano z linii poleceń.

%prep
%setup -qc -n %{name} %(seq -f '-a %g' 0 31 | xargs)

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{fix_date,freshmeat_search,google_msgid,google_search,mairix,multiwebsearch,textviewer,uudec,uuooffice,clawsxml2csv,csv2addressbook,eud2gc,mew2claws-mail,tb2claws-mail,outlook2claws-mail,vcard2xml,calypso_convert,convert_mbox,kmail-mailbox2claws-mail,tbird2claws,acroread2claws-mail,filter_conv_new,filter_conv,gif2xface,kdeservicemenu,nautilus2claws-mail,OOo2claws-mail,popfile-link,scrot2imageshack,textviewer-pl,thunderbird-filters-convertor,update_po}
install %{_name}-fix_date/{README,fix_date.sh} $RPM_BUILD_ROOT%{_datadir}/%{name}/fix_date
install %{_name}-freshmeat_search/{README,freshmeat_search.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/freshmeat_search
install %{_name}-google_msgid/{README,google_msgid.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/google_msgid
install %{_name}-google_search/{README,google_search.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/google_search
install %{_name}-mairix/{README,mairix.sh} $RPM_BUILD_ROOT%{_datadir}/%{name}/mairix
install %{_name}-multiwebsearch/{README,multiwebsearch.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/multiwebsearch
install %{_name}-textviewer/{README,textviewer.sh} $RPM_BUILD_ROOT%{_datadir}/%{name}/textviewer
install %{_name}-uudec/{README,uudec} $RPM_BUILD_ROOT%{_datadir}/%{name}/uudec
install %{_name}-uuooffice/{README,uuooffice} $RPM_BUILD_ROOT%{_datadir}/%{name}/uuooffice
install %{_name}-clawsxml2csv/{README,clawsxml2csv.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/clawsxml2csv
install %{_name}-csv2addressbook/{README,csv2addressbook.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/csv2addressbook
install %{_name}-eud2gc/{README,eud2gc.py} $RPM_BUILD_ROOT%{_datadir}/%{name}/eud2gc
install %{_name}-mew2claws-mail/{README,mew2claws-mail.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/mew2claws-mail
install %{_name}-tb2claws-mail/{README,tb2claws-mail} $RPM_BUILD_ROOT%{_datadir}/%{name}/tb2claws-mail
install %{_name}-outlook2claws-mail/{README,outlook2claws-mail.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/outlook2claws-mail
install %{_name}-vcard2xml/{README,vcard2xml.py} $RPM_BUILD_ROOT%{_datadir}/%{name}/vcard2xml
install %{_name}-calypso_convert/{README,calypso_convert.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/calypso_convert
install %{_name}-convert_mbox/{README,convert_mbox.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/convert_mbox
install %{_name}_kmail-mailbox2claws-mail/{README,kmail-mailbox2claws-mail.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/kmail-mailbox2claws-mail
install %{_name}-tbird2claws/{README,tbird2claws.py} $RPM_BUILD_ROOT%{_datadir}/%{name}/tbird2claws
install %{_name}-acroread2claws-mail/{README,acroread2claws-mail.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/acroread2claws-mail
install %{_name}-filter_conv_new/{README,filter_conv_new.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/filter_conv_new
install %{_name}-filter_conv/{README,filter_conv.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/filter_conv
install %{_name}-gif2xface/{README,gif2xface.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/gif2xface
install %{_name}_kdeservicemenu-1.4/{AUTHORS,ChangeLog,README,claws-mail-kdeservicemenu.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/kdeservicemenu
install %{_name}-nautilus2claws-mail/{README,nautilus2claws-mail.sh} $RPM_BUILD_ROOT%{_datadir}/%{name}/nautilus2claws-mail
install %{_name}-OOo2claws-mail/{README,OOo2claws-mail.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/OOo2claws-mail
install %{_name}-popfile-link/{README,popfile-link.sh} $RPM_BUILD_ROOT%{_datadir}/%{name}/popfile-link
install %{_name}-scrot2imageshack/{README,scrot2imageshack.sh} $RPM_BUILD_ROOT%{_datadir}/%{name}/scrot2imageshack
install %{_name}-textviewer-pl/{README,textviewer.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/textviewer-pl
install %{_name}-thunderbird-filters-convertor/{README,thunderbird-filters-convertor.pl} $RPM_BUILD_ROOT%{_datadir}/%{name}/thunderbird-filters-convertor
install %{_name}-update_po/{README,update-po} $RPM_BUILD_ROOT%{_datadir}/%{name}/update_po

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}

%files -n claws-mail-tools-fix_date
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/fix_date
%doc %{_datadir}/%{name}/fix_date/README
%attr(755,root,root) %{_datadir}/%{name}/fix_date/fix_date.sh

%files -n claws-mail-tools-freshmeat_search
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/freshmeat_search
%doc %{_datadir}/%{name}/freshmeat_search/README
%attr(755,root,root) %{_datadir}/%{name}/freshmeat_search/freshmeat_search.pl

%files -n claws-mail-tools-google_msgid
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/google_msgid
%doc %{_datadir}/%{name}/google_msgid/README
%attr(755,root,root) %{_datadir}/%{name}/google_msgid/google_msgid.pl

%files -n claws-mail-tools-google_search
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/google_search
%doc %{_datadir}/%{name}/google_search/README
%attr(755,root,root) %{_datadir}/%{name}/google_search/google_search.pl

%files -n claws-mail-tools-mairix
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/mairix
%doc %{_datadir}/%{name}/mairix/README
%attr(755,root,root) %{_datadir}/%{name}/mairix/mairix.sh

%files -n claws-mail-tools-multiwebsearch
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/multiwebsearch
%doc %{_datadir}/%{name}/multiwebsearch/README
%attr(755,root,root) %{_datadir}/%{name}/multiwebsearch/multiwebsearch.pl

%files -n claws-mail-tools-textviewer
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/textviewer
%doc %{_datadir}/%{name}/textviewer/README
%attr(755,root,root) %{_datadir}/%{name}/textviewer/textviewer.sh

%files -n claws-mail-tools-uudec
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/uudec
%doc %{_datadir}/%{name}/uudec/README
%attr(755,root,root) %{_datadir}/%{name}/uudec/uudec

%files -n claws-mail-tools-uuooffice
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/uuooffice
%doc %{_datadir}/%{name}/uuooffice/README
%attr(755,root,root) %{_datadir}/%{name}/uuooffice/uuooffice

%files -n claws-mail-tools-clawsxml2csv
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/clawsxml2csv
%doc %{_datadir}/%{name}/clawsxml2csv/README
%attr(755,root,root) %{_datadir}/%{name}/clawsxml2csv/clawsxml2csv.pl

%files -n claws-mail-tools-csv2addressbook
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/csv2addressbook
%doc %{_datadir}/%{name}/csv2addressbook/README
%attr(755,root,root) %{_datadir}/%{name}/csv2addressbook/csv2addressbook.pl

%files -n claws-mail-tools-eud2gc
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/eud2gc
%doc %{_datadir}/%{name}/eud2gc/README
%attr(755,root,root) %{_datadir}/%{name}/eud2gc/eud2gc.py

%files -n claws-mail-tools-mew2claws-mail
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/mew2claws-mail
%doc %{_datadir}/%{name}/mew2claws-mail/README
%attr(755,root,root) %{_datadir}/%{name}/mew2claws-mail/mew2claws-mail.pl

%files -n claws-mail-tools-tb2claws-mail
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/tb2claws-mail
%doc %{_datadir}/%{name}/tb2claws-mail/README
%attr(755,root,root) %{_datadir}/%{name}/tb2claws-mail/tb2claws-mail

%files -n claws-mail-tools-outlook2claws-mail
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/outlook2claws-mail
%doc %{_datadir}/%{name}/outlook2claws-mail/README
%attr(755,root,root) %{_datadir}/%{name}/outlook2claws-mail/outlook2claws-mail.pl

%files -n claws-mail-tools-vcard2xml
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/vcard2xml
%doc %{_datadir}/%{name}/vcard2xml/README
%attr(755,root,root) %{_datadir}/%{name}/vcard2xml/vcard2xml.py

%files -n claws-mail-tools-calypso_convert
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/calypso_convert
%doc %{_datadir}/%{name}/calypso_convert/README
%attr(755,root,root) %{_datadir}/%{name}/calypso_convert/calypso_convert.pl

%files -n claws-mail-tools-convert_mbox
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/convert_mbox
%doc %{_datadir}/%{name}/convert_mbox/README
%attr(755,root,root) %{_datadir}/%{name}/convert_mbox/convert_mbox.pl

%files -n claws-mail-tools-kmail-mailbox2claws-mail
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/kmail-mailbox2claws-mail
%doc %{_datadir}/%{name}/kmail-mailbox2claws-mail/README
%attr(755,root,root) %{_datadir}/%{name}/kmail-mailbox2claws-mail/kmail-mailbox2claws-mail.pl

%files -n claws-mail-tools-tbird2claws
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/tbird2claws
%doc %{_datadir}/%{name}/tbird2claws/README
%attr(755,root,root) %{_datadir}/%{name}/tbird2claws/tbird2claws.py

%files -n claws-mail-tools-acroread2claws-mail
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/acroread2claws-mail
%doc %{_datadir}/%{name}/acroread2claws-mail/README
%attr(755,root,root) %{_datadir}/%{name}/acroread2claws-mail/acroread2claws-mail.pl

%files -n claws-mail-tools-filter_conv_new
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/filter_conv_new
%doc %{_datadir}/%{name}/filter_conv_new/README
%attr(755,root,root) %{_datadir}/%{name}/filter_conv_new/filter_conv_new.pl

%files -n claws-mail-tools-filter_conv
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/filter_conv
%doc %{_datadir}/%{name}/filter_conv/README
%attr(755,root,root) %{_datadir}/%{name}/filter_conv/filter_conv.pl

%files -n claws-mail-tools-gif2xface
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/gif2xface
%doc %{_datadir}/%{name}/gif2xface/README
%attr(755,root,root) %{_datadir}/%{name}/gif2xface/gif2xface.pl

%files -n claws-mail-tools-kdeservicemenu
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/kdeservicemenu
%doc %{_datadir}/%{name}/kdeservicemenu/AUTHORS
%doc %{_datadir}/%{name}/kdeservicemenu/ChangeLog 
%doc %{_datadir}/%{name}/kdeservicemenu/README
%attr(755,root,root) %{_datadir}/%{name}/kdeservicemenu/claws-mail-kdeservicemenu.pl

%files -n claws-mail-tools-nautilus2claws-mail
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/nautilus2claws-mail
%doc %{_datadir}/%{name}/nautilus2claws-mail/README
%attr(755,root,root) %{_datadir}/%{name}/nautilus2claws-mail/nautilus2claws-mail.sh

%files -n claws-mail-tools-OOo2claws-mail
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/OOo2claws-mail
%doc %{_datadir}/%{name}/OOo2claws-mail/README
%attr(755,root,root) %{_datadir}/%{name}/OOo2claws-mail/OOo2claws-mail.pl

%files -n claws-mail-tools-popfile-link
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/popfile-link
%doc %{_datadir}/%{name}/popfile-link/README
%attr(755,root,root) %{_datadir}/%{name}/popfile-link/popfile-link.sh

%files -n claws-mail-tools-scrot2imageshack
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/scrot2imageshack
%doc %{_datadir}/%{name}/scrot2imageshack/README
%attr(755,root,root) %{_datadir}/%{name}/scrot2imageshack/scrot2imageshack.sh

%files -n claws-mail-tools-textviewer-pl
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/textviewer-pl
%doc %{_datadir}/%{name}/textviewer-pl/README
%attr(755,root,root) %{_datadir}/%{name}/textviewer-pl/textviewer.pl

%files -n claws-mail-tools-thunderbird-filters-convertor
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/thunderbird-filters-convertor
%doc %{_datadir}/%{name}/thunderbird-filters-convertor/README
%attr(755,root,root) %{_datadir}/%{name}/thunderbird-filters-convertor/thunderbird-filters-convertor.pl

%files -n claws-mail-tools-update_po
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/update_po
%doc %{_datadir}/%{name}/update_po/README
%attr(755,root,root) %{_datadir}/%{name}/update_po/update-po
