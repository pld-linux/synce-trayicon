Summary:	SynCE tray icon for GNOME 2.
Name:		synce-trayicon
Version:	0.9.0
Release:	0.2
License:	MIT
Source0: 	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	b639e3f681d01d69e6a1c703ab4fc8e8
Group:		Applications/Communications
Vendor:		The SynCE Project
URL:		http://synce.sourceforge.net/
BuildRequires:	synce-devel = %{version}
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libgtop-devel >= 1:2.0.0
Requires:	synce
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
synce-trayicon is part of the SynCE project:

  http://synce.sourceforge.net/

This application shows when a device is connected.

%prep
%setup -q 

%build
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure
%{__make}

%install
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
