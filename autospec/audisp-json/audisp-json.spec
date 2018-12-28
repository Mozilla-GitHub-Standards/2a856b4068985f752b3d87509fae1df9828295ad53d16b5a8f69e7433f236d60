#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : audisp-json
Version  : 2.1.1
Release  : 1
URL      : https://github.com/gdestuynder/audisp-json/archive/2.1.1.tar.gz
Source0  : https://github.com/gdestuynder/audisp-json/archive/2.1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0+
Requires: audisp-json-bin
Requires: audisp-json-config
Requires: audit
Requires: curl
Requires: nghttp2
Requires: nghttp2-lib
Requires: openssl
Requires: zlib
BuildRequires : audit-dev
BuildRequires : curl
BuildRequires : curl-dev
BuildRequires : nghttp2
BuildRequires : nghttp2-dev
BuildRequires : nghttp2-lib
BuildRequires : openssl-dev
BuildRequires : zlib-dev

%description
# Audisp-json
This program is a plugin for Linux Audit user space programs available at <http://people.redhat.com/sgrubb/audit/>.
It uses the audisp multiplexer.

%package bin
Summary: bin components for the audisp-json package.
Group: Binaries
Requires: audisp-json-config

%description bin
bin components for the audisp-json package.


%package config
Summary: config components for the audisp-json package.
Group: Default

%description config
config components for the audisp-json package.


%prep
%setup -q -n audisp-json-2.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531384750
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1531384750
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/audisp-json

%files config
%defattr(-,root,root,-)
%config /usr/etc/audisp/audisp-json.conf
%config /usr/etc/audisp/plugins.d/au-json.conf