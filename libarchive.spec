#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libarchive
Version  : 3.3.2
Release  : 30
URL      : http://www.libarchive.org/downloads/libarchive-3.3.2.tar.gz
Source0  : http://www.libarchive.org/downloads/libarchive-3.3.2.tar.gz
Summary  : Library to create and read several different archive formats
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libarchive-bin
Requires: libarchive-lib
Requires: libarchive-doc
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : e2fsprogs-dev
BuildRequires : expat-dev
BuildRequires : libxml2-dev
BuildRequires : lz4-dev
BuildRequires : lzo-dev
BuildRequires : nettle-dev nettle-lib
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(zlib)
BuildRequires : xz-dev
BuildRequires : zlib-dev
Patch1: cve-2017-5601.patch
Patch2: cve-2017-14166.patch

%description
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular TAR
variants and several CPIO formats. It can also write SHAR archives.

%package bin
Summary: bin components for the libarchive package.
Group: Binaries

%description bin
bin components for the libarchive package.


%package dev
Summary: dev components for the libarchive package.
Group: Development
Requires: libarchive-lib
Requires: libarchive-bin
Provides: libarchive-devel

%description dev
dev components for the libarchive package.


%package doc
Summary: doc components for the libarchive package.
Group: Documentation

%description doc
doc components for the libarchive package.


%package lib
Summary: lib components for the libarchive package.
Group: Libraries

%description lib
lib components for the libarchive package.


%prep
%setup -q -n libarchive-3.3.2
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505693664
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1505693664
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bsdcat
/usr/bin/bsdcpio
/usr/bin/bsdtar

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libarchive.so
/usr/lib64/pkgconfig/libarchive.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libarchive.so.13
/usr/lib64/libarchive.so.13.3.2
