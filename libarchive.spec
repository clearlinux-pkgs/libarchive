#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libarchive
Version  : 3.2.0
Release  : 17
URL      : http://www.libarchive.org/downloads/libarchive-3.2.0.tar.gz
Source0  : http://www.libarchive.org/downloads/libarchive-3.2.0.tar.gz
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
BuildRequires : lzo-dev
BuildRequires : nettle-dev nettle-lib
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(zlib)
BuildRequires : xz-dev
BuildRequires : zlib-dev

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
%setup -q -n libarchive-3.2.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
