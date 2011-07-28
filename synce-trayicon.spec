Summary:	SynCE tray icon for GNOME 2
Summary(pl.UTF-8):	SynCE jako ikona tacki dla środowiska GNOME 2
Name:		synce-trayicon
Version:	0.15.1
Release:	2
License:	MIT+LGPL
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	b6ab20a0a4814817b486585b6b63130e
Patch0:		%{name}-libnotify.patch
Patch1:		%{name}-backends.patch
URL:		http://www.synce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libgtop-devel >= 1:2.0.0
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libtool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.559
BuildRequires:	synce-librapi2-devel >= 0.15
BuildRequires:	synce-orange-libs-devel >= 0.4-3
BuildRequires:	synce-rra-devel >= 0.14
%requires_ge_to synce-librapi2 synce-librapi2-devel
%requires_ge_to	synce-rra synce-rra-devel
Requires:	synce-connector
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
synce-trayicon is part of the SynCE project: <http://www.synce.org/>.

This application shows when a device is connected.

%description -l pl.UTF-8
synce-trayicon to część projektu SynCE: <http://www.synce.org/>.

Ta aplikacja pokazuje, kiedy urządzenie jest podłączone.

%prep
%setup -q
%patch0 -p1
%patch1 -p2

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-vdccm-support \
	--enable-odccm-support \
	--disable-hal-support \
	--enable-udev-support

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*.la

install -d $RPM_BUILD_ROOT/etc/xdg/autostart
mv $RPM_BUILD_ROOT{%{_datadir}/gnome/autostart,/etc/xdg/autostart}/%{name}-autostart.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}.schemas
%scrollkeeper_update_post
%update_desktop_database_post

%postun
%scrollkeeper_update_postun

%preun
%gconf_schema_uninstall %{name}.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/synce
%{_datadir}/synce/*.glade
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so
%{_iconsdir}/hicolor/*/apps/synce-*.png
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
/etc/xdg/autostart/%{name}-autostart.desktop
