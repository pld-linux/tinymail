#
# TODO:
# - package and use oasyncworker
# - separate GTK+ dependencies into separate library
# - check dependencies
#
Summary:	A memory-efficient mail access library
Name:		tinymail
%define snap 2019
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
BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tinymail is a development framework (or collection of libraries) for accessing
E-mail services using devices with few resources; like mobile devices (phones
and PDAs) and embedded devices (settopboxes, digital tv, embedded E-mail
appliances and others). It supports IMAP, POP and NNTP. It can be used to send
messages over SMTP. It supports SSL and many authentication methods. It's
licensed under the LGPL. 

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
  --enable-acap   \
  --enable-uigtk       \
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
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
