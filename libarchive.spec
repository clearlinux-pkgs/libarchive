#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF040F7196BA99AF4 (mm@FreeBSD.org)
#
Name     : libarchive
Version  : 3.4.0
Release  : 54
URL      : https://github.com/libarchive/libarchive/releases/download/v3.4.0/libarchive-3.4.0.tar.gz
Source0  : https://github.com/libarchive/libarchive/releases/download/v3.4.0/libarchive-3.4.0.tar.gz
Source1 : https://github.com/libarchive/libarchive/releases/download/v3.4.0/libarchive-3.4.0.tar.gz.asc
Summary  : A library for handling streaming archive formats
Group    : Development/Tools
License  : BSD-2-Clause
Requires: libarchive-bin = %{version}-%{release}
Requires: libarchive-lib = %{version}-%{release}
Requires: libarchive-license = %{version}-%{release}
Requires: libarchive-man = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : e2fsprogs-dev
BuildRequires : lz4-dev
BuildRequires : lzo-dev
BuildRequires : openssl-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev
BuildRequires : zstd-dev
Patch1: 0001-test-disable-one-zstd-assertion.patch

%description
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package bin
Summary: bin components for the libarchive package.
Group: Binaries
Requires: libarchive-license = %{version}-%{release}

%description bin
bin components for the libarchive package.


%package dev
Summary: dev components for the libarchive package.
Group: Development
Requires: libarchive-lib = %{version}-%{release}
Requires: libarchive-bin = %{version}-%{release}
Provides: libarchive-devel = %{version}-%{release}
Requires: libarchive = %{version}-%{release}

%description dev
dev components for the libarchive package.


%package lib
Summary: lib components for the libarchive package.
Group: Libraries
Requires: libarchive-license = %{version}-%{release}

%description lib
lib components for the libarchive package.


%package license
Summary: license components for the libarchive package.
Group: Default

%description license
license components for the libarchive package.


%package man
Summary: man components for the libarchive package.
Group: Default

%description man
man components for the libarchive package.


%prep
%setup -q -n libarchive-3.4.0
%patch1 -p1
pushd ..
cp -a libarchive-3.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568064552
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --without-libxml2 \
--without-expat \
--without-lz4 \
--without-nettle
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --without-libxml2 \
--without-expat \
--without-lz4 \
--without-nettle
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../buildavx2;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1568064552
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libarchive
cp COPYING %{buildroot}/usr/share/package-licenses/libarchive/COPYING
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bsdcat
/usr/bin/bsdcpio
/usr/bin/bsdtar
/usr/bin/haswell/bsdcat
/usr/bin/haswell/bsdcpio
/usr/bin/haswell/bsdtar

%files dev
%defattr(-,root,root,-)
/usr/include/archive.h
/usr/include/archive_entry.h
/usr/lib64/haswell/libarchive.so
/usr/lib64/libarchive.so
/usr/lib64/pkgconfig/libarchive.pc
/usr/share/man/man3/archive_entry.3
/usr/share/man/man3/archive_entry_acl.3
/usr/share/man/man3/archive_entry_linkify.3
/usr/share/man/man3/archive_entry_misc.3
/usr/share/man/man3/archive_entry_paths.3
/usr/share/man/man3/archive_entry_perms.3
/usr/share/man/man3/archive_entry_stat.3
/usr/share/man/man3/archive_entry_time.3
/usr/share/man/man3/archive_read.3
/usr/share/man/man3/archive_read_add_passphrase.3
/usr/share/man/man3/archive_read_data.3
/usr/share/man/man3/archive_read_disk.3
/usr/share/man/man3/archive_read_extract.3
/usr/share/man/man3/archive_read_filter.3
/usr/share/man/man3/archive_read_format.3
/usr/share/man/man3/archive_read_free.3
/usr/share/man/man3/archive_read_header.3
/usr/share/man/man3/archive_read_new.3
/usr/share/man/man3/archive_read_open.3
/usr/share/man/man3/archive_read_set_options.3
/usr/share/man/man3/archive_util.3
/usr/share/man/man3/archive_write.3
/usr/share/man/man3/archive_write_blocksize.3
/usr/share/man/man3/archive_write_data.3
/usr/share/man/man3/archive_write_disk.3
/usr/share/man/man3/archive_write_filter.3
/usr/share/man/man3/archive_write_finish_entry.3
/usr/share/man/man3/archive_write_format.3
/usr/share/man/man3/archive_write_free.3
/usr/share/man/man3/archive_write_header.3
/usr/share/man/man3/archive_write_new.3
/usr/share/man/man3/archive_write_open.3
/usr/share/man/man3/archive_write_set_options.3
/usr/share/man/man3/archive_write_set_passphrase.3
/usr/share/man/man3/libarchive.3
/usr/share/man/man3/libarchive_changes.3
/usr/share/man/man3/libarchive_internals.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libarchive.so.13
/usr/lib64/haswell/libarchive.so.13.4.0
/usr/lib64/libarchive.so.13
/usr/lib64/libarchive.so.13.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libarchive/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bsdcat.1
/usr/share/man/man1/bsdcpio.1
/usr/share/man/man1/bsdtar.1
/usr/share/man/man5/cpio.5
/usr/share/man/man5/libarchive-formats.5
/usr/share/man/man5/mtree.5
/usr/share/man/man5/tar.5
