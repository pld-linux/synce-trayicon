Summary:	SynCE tray icon for GNOME 2
Summary(pl):	SynCE jako ikona tacki dla ¶rodowiska GNOME 2
Name:		synce-trayicon
Version:	0.9.0
Release:	0.2
License:	MIT
Vendor:		The SynCE Project
Group:		Applications/Communications
Source0: 	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	b639e3f681d01d69e6a1c703ab4fc8e8
URL:		http://synce.sourceforge.net/
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libgtop-devel >= 1:2.0.0
BuildRequires:	synce-devel = %{version}
Requires:	synce
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
synce-trayicon is part of the SynCE project:
http://synce.sourceforge.net/

This application shows when a device is connected.

%description -l pl
synce-trayicon to czê¶æ projektu SynCE:
http://synce.sourceforge.net/ .

Ta aplikacja pokazuje, kiedy urz±dzenie jest pod³±czone.

%prep
%setup -q 

%build
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
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/synce/*
%{_datadir}/synce/*.glade
