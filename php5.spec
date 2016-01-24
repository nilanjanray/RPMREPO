Name:           php
Version:        5.5.30
Release:        1%{?dist}
Summary:        PHP is a widely-used general-purpose scripting language.

Group:          Development/Languages
License:        PHP License v3.01
URL:            http://www.php.net
Source0:        http://www.php.net/distributions/php-%{version}.tar.gz
Patch0:         php55.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Obsoletes:      php

%description
PHP is a widely-used general-purpose scripting language that is especially
suited for Web development and can be embedded into HTML.

%prep
%setup -q -n %{name}-%{version}

#%patch0 -p0
%patch0 -p1

%build
EXTENSION_DIR=%{_datadir}/php/modules; export EXTENSION_DIR
%configure --with-layout=GNU --with-libdir=lib64 --with-enchant \
--enable-fpm --with-gd --enable-intl --enable-mbstring --enable-pcntl \
--enable-soap --enable-sockets --enable-sqlite-utf8 --enable-zip --with-zlib \
--with-curl --with-jpeg-dir --with-png-dir --with-zlib-dir --with-gettext \
--with-mcrypt --with-mysql=mysqlnd --with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd \
--with-pdo-sqlite --with-tidy --with-pear=%{_datadir}/php/pear --disable-debug \
--prefix=%{_datadir}/php --with-apxs2=%{_bindir}/apxs \


make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_initrddir}
install -Dp -m0755 sapi/fpm/init.d.php-fpm.in %{buildroot}%{_initrddir}/php-fpm
%{__make} install INSTALL_ROOT="%{buildroot}"

%clean
rm -rf %{buildroot}

#%post
#%/sbin/chkconfig --add php-fpm
#%/sbin/chkconfig --level 2345 php-fpm on

#%preun
#if [ "$1" = 0 ] ; then
 #   /sbin/service php-fpm stop > /dev/null 2>&1
  #  /sbin/chkconfig --del php-fpm
#fi
#exit 0

#%postun
#if [ "$1" -ge 1 ]; then
 #   /sbin/service php-fpm condrestart > /dev/null 2>&1
#fi
#exit 0

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_sbindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/man1/php*
%{_sysconfdir}/*
%{_datadir}/*
%{_initrddir}/*
%exclude /.channels
%exclude /.depdb
%exclude /.depdblock
%exclude /.filemap
%exclude /.lock
