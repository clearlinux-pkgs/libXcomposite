#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXcomposite
Version  : 0.4.4
Release  : 5
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-0.4.4.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-0.4.4.tar.bz2
Summary  : X Composite Extension Library
Group    : Development/Tools
License  : MIT
Requires: libXcomposite-lib
Requires: libXcomposite-doc
BuildRequires : pkgconfig(compositeproto)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : xmlto

%description
libXcomposite - client library for the Composite extension to the X11 protocol
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the libXcomposite package.
Group: Development
Requires: libXcomposite-lib

%description dev
dev components for the libXcomposite package.


%package doc
Summary: doc components for the libXcomposite package.
Group: Documentation

%description doc
doc components for the libXcomposite package.


%package lib
Summary: lib components for the libXcomposite package.
Group: Libraries

%description lib
lib components for the libXcomposite package.


%prep
%setup -q -n libXcomposite-0.4.4

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/Xcomposite.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
