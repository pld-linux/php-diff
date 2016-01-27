%define		pkgname	diff
%define		php_min_version 5.2.0
Summary:	PHP Diff Class
Name:		php-%{pkgname}
Version:	1.0.2
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/phpspec/php-diff/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	09f18f5cf843a63b359d8ca7186e8f56
URL:		https://github.com/phpspec/php-diff
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A comprehensive library for generating differences between two strings
in multiple formats (unified, side by side HTML etc).

Based on the difflib implementation in Python

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a lib/* $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{php_data_dir}/Diff.php
%{php_data_dir}/Diff
%{_examplesdir}/%{name}-%{version}
