Summary:	SynCE tray icon for GNOME 2
Summary(pl.UTF-8):   SynCE jako ikona tacki dla środowiska GNOME 2
Name:		synce-trayicon
Version:	0.9.0
Release:	3
License:	MIT+LGPL
Vendor:		The SynCE Project
Group:		Applications/Communications
Source0: 	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	b639e3f681d01d69e6a1c703ab4fc8e8
URL:		http://www.synce.org/
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libgtop-devel >= 1:2.0.0
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-librapi2-devel >= 0.9.1
Requires:	synce-librapi2 >= 0.9.1
Requires:	synce-dccm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
synce-trayicon is part of the SynCE project:
<http://www.synce.org/>.

This application shows when a device is connected.

%description -l pl.UTF-8
synce-trayicon to część projektu SynCE:
<http://www.synce.org/>.

Ta aplikacja pokazuje, kiedy urządzenie jest podłączone.

%prep
%setup -q 

%build
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog src/LICENSE*
%attr(755,root,root) %{_bindir}/*
# dir shared with synce-gnomevfs
%dir %{_pixmapsdir}/synce
%{_pixmapsdir}/synce/*.png
# dir shared with synce-rra, synce-gnomevfs, synce-software-manager
%dir %{_datadir}/synce
%{_datadir}/synce/*.glade
