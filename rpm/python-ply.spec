%define modname ply

%bcond_with tests

Name:           python-%{modname}
Summary:        Python Lex-Yacc
Version:        3.11
Release:        0
License:        BSD
URL:            https://github.com/sailfishos/python-ply
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
PLY is a straightforward lex/yacc implementation. Here is a list of its
essential features:
* It is implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger
  grammars.
* PLY provides most of the standard lex/yacc features including support
  for empty productions, precedence rules, error recovery, and support
  for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc
  functionality. In other words, it's not a large parsing framework or a
  component of some larger system.

%package -n python3-%{modname}
Summary:        Python Lex-Yacc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname}
PLY is a straightforward lex/yacc implementation. Here is a list of its
essential features:
* It is implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger
  grammars.
* PLY provides most of the standard lex/yacc features including support
  for empty productions, precedence rules, error recovery, and support
  for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc
  functionality. In other words, it's not a large parsing framework or a
  component of some larger system.

Python 3 version.

%prep
%autosetup -n %{name}-%{version}/upstream
find example/ -type f -executable -exec chmod -x {} ';'
find example/ -type f -name '*.py' -exec sed -i \
  -e '1{\@^#!/usr/bin/env python@d}' -e '1{\@^#!/usr/local/bin/python@d}' \
  {} ';'
rm -rf *.egg-info
# extract license block from beginning of README.md
grep -B1000 "POSSIBILITY OF SUCH DAMAGE" README.md > LICENSE

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
pushd test
  ./cleanup.sh
  %{__python3} testlex.py
  %{__python3} testyacc.py
popd
%endif

%files -n python3-%{modname}
%doc CHANGES README.md
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-*.egg-info/
