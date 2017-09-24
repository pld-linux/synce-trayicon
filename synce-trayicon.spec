#
# Conditional build:
%bcond_without	appindicator	# application indicators support
%bcond_without	vdccm		# vdccm support
#
Summary:	SynCE tray icon for GNOME
Summary(pl.UTF-8):	SynCE jako ikona tacki dla środowiska GNOME
Name:		synce-trayicon
Version:	0.17
Release:	2
License:	MIT
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	0ebb11add5cf858f6334a97e3647e1e3
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool
%{?with_appindicator:BuildRequires:	libappindicator-gtk3-devel >= 0.0.7}
BuildRequires:	libgnome-keyring-devel
%{?with_vdccm:BuildRequires:	libgtop-devel >= 1:2.0.0}
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	synce-core-lib-devel >= 0.17
BuildRequires:	synce-orange-libs-devel >= 0.4-3
BuildRequires:	synce-rra-devel >= 0.17
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.26
Requires:	hicolor-icon-theme
%{?with_appindicator:Requires:	libappindicator-gtk3 >= 0.0.7}
Requires:	libxml2 >= 1:2.6.0
Requires:	synce-core >= 0.17
Requires:	synce-orange-libs >= 0.4-3
Requires:	synce-rra >= 0.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
synce-trayicon is part of the SynCE project: <http://www.synce.org/>.

This application shows when a device is connected.

%description -l pl.UTF-8
synce-trayicon to część projektu SynCE: <http://www.synce.org/>.

Ta aplikacja pokazuje, kiedy urządzenie jest podłączone.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_appindicator:--disable-appindicator} \
	--disable-hal-support \
	--enable-odccm-support \
	--disable-schemas-install \
	--enable-udev-support \
	%{?with_vdccm:--enable-vdccm-support}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*.la

install -d $RPM_BUILD_ROOT/etc/xdg/autostart
%{__mv} $RPM_BUILD_ROOT{%{_datadir}/gnome/autostart,/etc/xdg/autostart}/%{name}-autostart.desktop
rmdir $RPM_BUILD_ROOT%{_datadir}/gnome/autostart
rmdir $RPM_BUILD_ROOT%{_datadir}/gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/synce-trayicon
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so
# dir shared among some synce-* apps
%dir %{_datadir}/synce
%{_datadir}/synce/synce_trayicon_properties.glade
%{_datadir}/glib-2.0/schemas/org.synce.SynceTrayicon.gschema.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/synce-color.png
%{_iconsdir}/hicolor/*/apps/synce-gray.png
%{_mandir}/man1/%{name}.1*
/etc/xdg/autostart/%{name}-autostart.desktop
