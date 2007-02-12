# TODO:	- check what causes msg. like:
#	echo "<base href=\"$PREFIX/share/dox/html/stl\"/>" >> stl.toc ; \
#	cat stl.toc.in >> stl.toc
#	/bin/sh: source: not found"
#	- maybe release separate subpackages with documentation
#	- check what going on with htdig, "configure" (/opt/www/htdig), etc
Summary:	dox - graphical documentation browser for Unix/X11
Summary(pl.UTF-8):	dox - przeglądarka dokumentacji dla Uniksa/X11
Name:		dox
Version:	1.1
Release:	0.1
Epoch:		0
License:	GPL
Group:		Documentation
Source0:	http://download.berlios.de/dox/%{name}-%{version}.tar.gz
# Source0-md5:	368afc1cc1cf1b56789dbb8754f38c50
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-destpaths.patch
URL:		http://dox.berlios.de/
BuildRequires:	qmake >= 3.0.0
BuildRequires:	qt-devel >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dox is a graphical documentation browser for Unix/X11.

Features:
 - manpage browser.
 - info browser.
 - access to books in HTML format via their respective table of contents.
   glibc and STL are included in the release, others can be downloaded.
 - integration of Debian's docbase.
 - access to books in HTML format via their respective keyword index.
 - search in manpage titles and contents (cf. apropos and whatis).
 - interface to the pydoc and perldoc utilities.
 - fulltext search in HTML documentation Extensibility: Tables of content
   and keyword indices can be added by installing simple XML files to be
   extracted from the documentation. 
 - remote controllable from the shell.
 - a utility for converting tags files generated by Doxygen to keyword
   indices.

%description -l pl.UTF-8
Dox to graficzna przeglądarka dokumentacji dla Uniksa/X11.

Możliwości:
 - przeglądanie stron man
 - przeglądanie info
 - dostęp do książek w formacie HTML poprzez ich spis treści;
   w tej wersji załączone są glibc i STL, inne można ściągnąć
 - integracja z debianowym docbase
 - dostęp do książek w formacie HTML poprzez indeks słów kluczowych
 - wyszukiwanie po tytułach i zawartości stron man (podobnie jak
   apropos i whatis)
 - interfejs do narzędzi pydoc i perldoc
 - wyszukiwanie pełnotekstowe w dokumentacji HTML, rozszerzalne po
   dodaniu indeksów spisu treści i słów kluczowych poprzez
   zainstalowanie plików XML wyciągniętych z dokumentacji
 - zdalne sterowanie z powłoki
 - narzędzie to konwersji plików znaczników wygenerowanych przez
   Doxygen do indeksów słów kluczowych.

%prep
%setup -q
%patch0 -p1

%build
./configure \
	-prefix "%{_prefix}"
%{__make} \
	QTDIR="%{_prefix}" \
	PREFIX="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man[15]/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
