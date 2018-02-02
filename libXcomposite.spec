#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXcomposite
Version  : 0.4.4
Release  : 11
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-0.4.4.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-0.4.4.tar.bz2
Summary  : X Composite Extension Library
Group    : Development/Tools
License  : MIT
Requires: libXcomposite-lib
Requires: libXcomposite-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32compositeproto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(compositeproto)
BuildRequires : pkgconfig(x11)
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
Provides: libXcomposite-devel

%description dev
dev components for the libXcomposite package.


%package dev32
Summary: dev32 components for the libXcomposite package.
Group: Default
Requires: libXcomposite-lib32
Requires: libXcomposite-dev

%description dev32
dev32 components for the libXcomposite package.


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


%package lib32
Summary: lib32 components for the libXcomposite package.
Group: Default

%description lib32
lib32 components for the libXcomposite package.


%prep
%setup -q -n libXcomposite-0.4.4
pushd ..
cp -a libXcomposite-0.4.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500993948
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1500993948
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/Xcomposite.h
/usr/lib64/libXcomposite.so
/usr/lib64/pkgconfig/xcomposite.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXcomposite.so
/usr/lib32/pkgconfig/32xcomposite.pc
/usr/lib32/pkgconfig/xcomposite.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXcomposite.so.1
/usr/lib64/libXcomposite.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXcomposite.so.1
/usr/lib32/libXcomposite.so.1.0.0
