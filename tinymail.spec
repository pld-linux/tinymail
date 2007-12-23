#
# TODO:
# - rename -python to python-*
# - package and use oasyncworker
# - separate GTK+ dependencies into separate library
# - check dependencies
#
%bcond_with	maemo	 # build maemo platform
#
Summary:	A memory-efficient mail access library
Summary(pl.UTF-8):	Wydajna pamięciowo biblioteka dostępu do poczty
Name:		tinymail
Version:	0.0.6
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.tinymail.org/files/releases/pre-releases/v%{version}/lib%{name}-%{version}.tar.bz2
# Source0-md5:	68498359a3c2e808c263b90312165ec1
URL:		http://www.tinymail.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc-common
BuildRequires:	intltool
%{?with_maemo:BuildRequires:	libconic-devel}
BuildRequires:	libtool
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%{!?with_maemo:BuildRequires:	xulrunner-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tinymail is a development framework (or collection of libraries) for
accessing E-mail services using devices with few resources; like
mobile devices (phones and PDAs) and embedded devices (settopboxes,
digital TV, embedded E-mail appliances and others). It supports IMAP,
POP and NNTP. It can be used to send messages over SMTP. It supports
SSL and many authentication methods. It's licensed under the LGPL.

%description -l pl.UTF-8
Tinymail to szkielet programistyczny (zestaw bibliotek) do dostępu do
usług poczty elektrocznej przy użyciu urządzeń z ograniczonymi
zasobami, takich jak urządzenia przenośne (telefony i PDA) i
urządzenia wbudowane (typu set-top box, telewizory cyfrowe, urządzenia
wbudowane do poczty elektronicznej i inne). Obsługuje protokoły IMAP,
POP i NNTP. Może być używana do wysyłania wiadomości po SMTP.
Obsługuje SSL i wiele metod uwierzytelniania. Jest na licencji LGPL.

%package devel
Summary:	Header files for tinymail library
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek tinymail
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tinymail library.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek tinymail.

%package static
Summary:	Static tinymail library
Summary(pl.UTF-8):	Statyczna biblioteka tinymail
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tinymail library.

%description static -l pl.UTF-8
Statyczna biblioteka tinymail.

%package -n python-tinymail
Summary:	Python tinymail library bindings
Summary(pl.UTF-8):	Wiązania Pythona dla biblioteki tinymail
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tinymail-python
%pyrequires_eq  python-modules

%description -n python-tinymail
Python tinymail library bindings.

%description -n python-tinymail -l pl.UTF-8
Wiązania Pythona dla biblioteki tinymail

%prep
%setup -q -n lib%{name}-%{version}

%build
%{__glib_gettextize}
%{__libtoolize}
%{__gtkdocize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd libtinymail-camel/camel-lite
%{__libtoolize}
%{__aclocal} -I ../../m4
%{__automake}
%{__autoconf}
%configure
cd ../..
%configure \
	--enable-demoui \
	%{?with_maemo:--with-platform=maemo} \
	%{!?with_maemo:--enable-gnome}  \
	--with-html-component=mozembed \
	--enable-uigtk	   \
	--enable-python-bindings \
	--enable-gtk-doc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/camel-lite-1.2/camel-providers/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/tny-demoui
%attr(755,root,root) %{_libdir}/libcamel-lite-1.2.so.*.*.*
%attr(755,root,root) %{_libdir}/libcamel-lite-provider-1.2.so.*.*.*
%attr(755,root,root) %{_libdir}/libtinymail-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libtinymail-camel-1.0.so.*.*.*
%if %{without maemo}
%attr(755,root,root) %{_libdir}/libtinymail-gnome-desktop-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libtinymail-gnomevfs-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libtinymailui-mozembed-1.0.so.*.*.*
%else
%attr(755,root,root) %{_libdir}/libtinymailui-maemo-1.0.so.*.*.*
%endif
%attr(755,root,root) %{_libdir}/libtinymailui-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libtinymailui-gtk-1.0.so.*.*.*
%dir %{_libdir}/camel-lite-1.2
%dir %{_libdir}/camel-lite-1.2/camel-providers
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelimap.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelimap.urls
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamellocal.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamellocal.urls
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelnntp.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelnntp.urls
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelpop3.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelpop3.urls
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelsendmail.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelsendmail.urls
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelsmtp.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelsmtp.urls

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcamel-lite-1.2.so
%attr(755,root,root) %{_libdir}/libcamel-lite-provider-1.2.so
%attr(755,root,root) %{_libdir}/libtinymail-1.0.so
%attr(755,root,root) %{_libdir}/libtinymail-camel-1.0.so
%attr(755,root,root) %{_libdir}/libtinymailui-1.0.so
%attr(755,root,root) %{_libdir}/libtinymailui-gtk-1.0.so
%if %{without maemo}
%attr(755,root,root) %{_libdir}/libtinymailui-mozembed-1.0.so
%attr(755,root,root) %{_libdir}/libtinymail-gnome-desktop-1.0.so
%attr(755,root,root) %{_libdir}/libtinymail-gnomevfs-1.0.so
%else
%attr(755,root,root) %{_libdir}/libtinymail-maemo-1.0.so
%endif
%{_libdir}/libcamel-lite-1.2.la
%{_libdir}/libcamel-lite-provider-1.2.la
%{_libdir}/libtinymail-1.0.la
%{_libdir}/libtinymail-camel-1.0.la
%if %{without maemo}
%{_libdir}/libtinymail-gnome-desktop-1.0.la
%{_libdir}/libtinymail-gnomevfs-1.0.la
%{_libdir}/libtinymailui-mozembed-1.0.la
%else
%{_libdir}/libtinymailui-maemo-1.0.la
%endif
%{_libdir}/libtinymailui-1.0.la
%{_libdir}/libtinymailui-gtk-1.0.la
%dir %{_includedir}/camel-lite
%dir %{_includedir}/camel-lite/camel
%{_includedir}/camel-lite/camel/*.h
%dir %{_includedir}/libedataserver-lite
%dir %{_includedir}/libedataserver-lite/libedataserver
%{_includedir}/libedataserver-lite/libedataserver/*.h
%dir %{_includedir}/libtinymail-1.0
%{_includedir}/libtinymail-1.0/*.h
%dir %{_includedir}/libtinymail-camel-1.0
%{_includedir}/libtinymail-camel-1.0/*.h
%dir %{_includedir}/libtinymail-gnome-desktop-1.0
%{_includedir}/libtinymail-gnome-desktop-1.0/*.h
%dir %{_includedir}/libtinymail-gnomevfs-1.0
%{_includedir}/libtinymail-gnomevfs-1.0/*.h
%dir %{_includedir}/libtinymailui-1.0
%{_includedir}/libtinymailui-1.0/*.h
%dir %{_includedir}/libtinymailui-gtk-1.0
%{_includedir}/libtinymailui-gtk-1.0/*.h
%dir %{_includedir}/libtinymailui-mozembed-1.0
%{_includedir}/libtinymailui-mozembed-1.0/*.h
%{_pkgconfigdir}/camel-lite-1.2.pc
%{_pkgconfigdir}/camel-lite-provider-1.2.pc
%{_pkgconfigdir}/libtinymail-1.0.pc
%{_pkgconfigdir}/libtinymail-camel-1.0.pc
%{_pkgconfigdir}/libtinymailui-1.0.pc
%{_pkgconfigdir}/libtinymailui-gtk-1.0.pc
%if %{without maemo}
%{_pkgconfigdir}/libtinymailui-mozembed-1.0.pc
%{_pkgconfigdir}/libtinymail-gnome-desktop-1.0.pc
%{_pkgconfigdir}/libtinymail-gnomevfs-1.0.pc
%else
%{_pkgconfigdir}/libtinymail-maemo-1.0.pc
%endif

%files static
%defattr(644,root,root,755)
%{_libdir}/libcamel-lite-1.2.a
%{_libdir}/libcamel-lite-provider-1.2.a
%{_libdir}/libtinymail-1.0.a
%{_libdir}/libtinymail-camel-1.0.a
%if %{without maemo}
%{_libdir}/libtinymail-gnome-desktop-1.0.a
%{_libdir}/libtinymail-gnomevfs-1.0.a
%{_libdir}/libtinymailui-mozembed-1.0.a
%else
%{_libdir}/libtinymailui-maemo-1.0.a
%endif
%{_libdir}/libtinymailui-1.0.a
%{_libdir}/libtinymailui-gtk-1.0.a

%files -n python-tinymail
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/tinymail-1.0
%{py_sitescriptdir}/tinymail-1.0/tinymail/*.py[co]
%attr(755,root,root) %{py_sitescriptdir}/tinymail-1.0/tinymail/*.so
%{py_sitescriptdir}/tinymail.pth
