#
# TODO:
# - package and use oasyncworker
# - separate GTK+ dependencies into separate library
# - check dependencies
#
%define snap 2019
Summary:	A memory-efficient mail access library
Name:		tinymail
Version:	0.0.%{snap}
Release:	1
License:	GPL
Group:		Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	abdc0d8b0e563aeb7c85cc7600bde44a
URL:		http://www.tinymail.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc-common
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	python-devel
BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tinymail is a development framework (or collection of libraries) for
accessing E-mail services using devices with few resources; like
mobile devices (phones and PDAs) and embedded devices (settopboxes,
digital tv, embedded E-mail appliances and others). It supports IMAP,
POP and NNTP. It can be used to send messages over SMTP. It supports
SSL and many authentication methods. It's licensed under the LGPL.

%package devel
Summary:	Header files for tinymail library
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotektinymail
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tinymail library.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotektinymail.

%package static
Summary:	Static tinymail library
Summary(pl.UTF-8):	Statyczna biblioteka tinymail
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tinymail library.

%description static -l pl.UTF-8
Statyczna biblioteka tinymail.

%package python
Summary:	Python tinymail library bindings
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq  python-modules

%description python
Python tinymail library bindings.

%prep
%setup -q -n %{name}

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
cd ../../
%configure \
  --enable-demoui \
  --enable-gnome  \
  --enable-uigtk	   \
  --enable-python-bindings \
  --enable-gtk-doc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/tny-demoui
%dir %{_libdir}/camel-lite-1.2
%dir %{_libdir}/camel-lite-1.2/camel-providers
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelimap.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamellocal.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelnntp.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelpop3.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelsendmail.so
%attr(755,root,root) %{_libdir}/camel-lite-1.2/camel-providers/libcamelsmtp.so
%attr(755,root,root) %{_libdir}/libcamel-lite-1.2.so.0.0.0
%attr(755,root,root) %{_libdir}/libcamel-lite-provider-1.2.so.8.1.0
%attr(755,root,root) %{_libdir}/libtinymail-1.0.so.0.0.0
%attr(755,root,root) %{_libdir}/libtinymail-camel-1.0.so.0.0.0
%attr(755,root,root) %{_libdir}/libtinymail-gnome-desktop-1.0.so.0.0.0
%attr(755,root,root) %{_libdir}/libtinymail-gnomevfs-1.0.so.0.0.0
%attr(755,root,root) %{_libdir}/libtinymailui-1.0.so.0.0.0
%attr(755,root,root) %{_libdir}/libtinymailui-gtk-1.0.so.0.0.0
%attr(755,root,root) %{_libdir}/libtinymailui-mozembed-1.0.so.0.0.0

%files python
%{py_sitescriptdir}/tinymail-1.0/tinymail/*.py[co]
%{py_sitescriptdir}/tinymail-1.0/tinymail/*.so
%{py_sitescriptdir}/tinymail.pth

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/camel-lite
%dir %{_includedir}/camel-lite/camel/
%{_includedir}/camel-lite/camel/*.h
%dir %{_includedir}/libedataserver-lite/
%dir %{_includedir}/libedataserver-lite/libedataserver/
%{_includedir}/libedataserver-lite/libedataserver/*.h
%dir %{_includedir}/libtinymail-1.0/
%{_includedir}/libtinymail-1.0/*.h
%dir %{_includedir}/libtinymail-camel-1.0/
%{_includedir}/libtinymail-camel-1.0/*.h
%dir %{_includedir}/libtinymail-gnome-desktop-1.0/
%{_includedir}/libtinymail-gnome-desktop-1.0/*.h
%dir %{_includedir}/libtinymail-gnomevfs-1.0/
%{_includedir}/libtinymail-gnomevfs-1.0/*.h
%dir %{_includedir}/libtinymailui-1.0/
%{_includedir}/libtinymailui-1.0/*.h
%dir %{_includedir}/libtinymailui-gtk-1.0/
%{_includedir}/libtinymailui-gtk-1.0/*.h
%dir %{_includedir}/libtinymailui-mozembed-1.0/
%{_includedir}/libtinymailui-mozembed-1.0/*.h

%if 0
%{_libdir}/camel-lite-1.2/camel-providers/libcamelimap.la
%{_libdir}/camel-lite-1.2/camel-providers/libcamellocal.la
%{_libdir}/camel-lite-1.2/camel-providers/libcamelnntp.la
%{_libdir}/camel-lite-1.2/camel-providers/libcamelpop3.la
%{_libdir}/camel-lite-1.2/camel-providers/libcamelsendmail.la
%{_libdir}/camel-lite-1.2/camel-providers/libcamelsmtp.la
%{_libdir}/camel-lite-1.2/camel-providers/libcamelimap.a
%{_libdir}/camel-lite-1.2/camel-providers/libcamelimap.urls
%{_libdir}/camel-lite-1.2/camel-providers/libcamellocal.a
%{_libdir}/camel-lite-1.2/camel-providers/libcamellocal.urls
%{_libdir}/camel-lite-1.2/camel-providers/libcamelnntp.a
%{_libdir}/camel-lite-1.2/camel-providers/libcamelnntp.urls
%{_libdir}/camel-lite-1.2/camel-providers/libcamelpop3.a
%{_libdir}/camel-lite-1.2/camel-providers/libcamelpop3.urls
%{_libdir}/camel-lite-1.2/camel-providers/libcamelsendmail.a
%{_libdir}/camel-lite-1.2/camel-providers/libcamelsendmail.urls
%{_libdir}/camel-lite-1.2/camel-providers/libcamelsmtp.a
%{_libdir}/camel-lite-1.2/camel-providers/libcamelsmtp.urls
%endif

%{_libdir}/libcamel-lite-1.2.la
%{_libdir}/libcamel-lite-provider-1.2.la
%{_libdir}/libtinymail-1.0.la
%{_libdir}/libtinymail-camel-1.0.la
%{_libdir}/libtinymail-gnome-desktop-1.0.la
%{_libdir}/libtinymail-gnomevfs-1.0.la
%{_libdir}/libtinymailui-1.0.la
%{_libdir}/libtinymailui-gtk-1.0.la
%{_libdir}/libtinymailui-mozembed-1.0.la
%{_pkgconfigdir}/camel-lite-1.2.pc
%{_pkgconfigdir}/camel-lite-provider-1.2.pc
%{_pkgconfigdir}/libtinymail-1.0.pc
%{_pkgconfigdir}/libtinymail-camel-1.0.pc
%{_pkgconfigdir}/libtinymail-gnome-desktop-1.0.pc
%{_pkgconfigdir}/libtinymail-gnomevfs-1.0.pc
%{_pkgconfigdir}/libtinymailui-1.0.pc
%{_pkgconfigdir}/libtinymailui-gtk-1.0.pc
%{_pkgconfigdir}/libtinymailui-mozembed-1.0.pc

%files static
%{_libdir}/libcamel-lite-1.2.a
%{_libdir}/libcamel-lite-provider-1.2.a
%{_libdir}/libtinymail-1.0.a
%{_libdir}/libtinymail-camel-1.0.a
%{_libdir}/libtinymail-gnome-desktop-1.0.a
%{_libdir}/libtinymail-gnomevfs-1.0.a
%{_libdir}/libtinymailui-1.0.a
%{_libdir}/libtinymailui-gtk-1.0.a
%{_libdir}/libtinymailui-mozembed-1.0.a
