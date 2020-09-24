#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cups-pk-helper
Version  : 0.2.6
Release  : 7
URL      : https://www.freedesktop.org/software/cups-pk-helper/releases/cups-pk-helper-0.2.6.tar.xz
Source0  : https://www.freedesktop.org/software/cups-pk-helper/releases/cups-pk-helper-0.2.6.tar.xz
Summary  : A helper that makes system-config-printer use PolicyKit
Group    : Development/Tools
License  : GPL-2.0
Requires: cups-pk-helper-data = %{version}-%{release}
Requires: cups-pk-helper-libexec = %{version}-%{release}
Requires: cups-pk-helper-license = %{version}-%{release}
Requires: cups-pk-helper-locales = %{version}-%{release}
BuildRequires : cups-dev
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(polkit-gobject-1)

%description
cups-pk-helper
==============
http://www.freedesktop.org/wiki/Software/cups-pk-helper

%package data
Summary: data components for the cups-pk-helper package.
Group: Data

%description data
data components for the cups-pk-helper package.


%package libexec
Summary: libexec components for the cups-pk-helper package.
Group: Default
Requires: cups-pk-helper-license = %{version}-%{release}

%description libexec
libexec components for the cups-pk-helper package.


%package license
Summary: license components for the cups-pk-helper package.
Group: Default

%description license
license components for the cups-pk-helper package.


%package locales
Summary: locales components for the cups-pk-helper package.
Group: Default

%description locales
locales components for the cups-pk-helper package.


%prep
%setup -q -n cups-pk-helper-0.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557082884
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557082884
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cups-pk-helper
cp COPYING %{buildroot}/usr/share/package-licenses/cups-pk-helper/COPYING
%make_install
%find_lang cups-pk-helper

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.opensuse.CupsPkHelper.Mechanism.service
/usr/share/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf
/usr/share/polkit-1/actions/org.opensuse.cupspkhelper.mechanism.policy

%files libexec
%defattr(-,root,root,-)
/usr/libexec/cups-pk-helper-mechanism

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cups-pk-helper/COPYING

%files locales -f cups-pk-helper.lang
%defattr(-,root,root,-)

