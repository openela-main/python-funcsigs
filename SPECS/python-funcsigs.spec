%global pypi_name funcsigs

# funcsigs functionality is available in Python 3's inspect module
# Nothing should use python3-funcsigs as an external library.
%global with_python3 0

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        13%{?dist}
Summary:        Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+

License:        ASL 2.0
URL:            https://github.com/testing-cabal/funcsigs?
Source0:        https://pypi.io/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6, 2.7
as well as 3.2 and up.


%package -n     python2-%{pypi_name}
Summary:        Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6, 2.7
as well as 3.2 and up.


%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-unittest2

%description -n python3-%{pypi_name}
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6, 2.7
as well as 3.2 and up.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?rhel} && 0%{?rhel} == 7
sed -i '/extras_require/,+3d' setup.py
%endif

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if 0%{?with_python3}
%py3_install
%endif

export RHEL_ALLOW_PYTHON2_FOR_BUILD=1
%py2_install


%check
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Thu Apr 25 2019 Tomas Orsava <torsava@redhat.com> - 1.0.2-13
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Fri Jul 13 2018 Lumír Balhar <lbalhar@redhat.com> - 1.0.2-12
- First version for python27 module

* Mon Jul 09 2018 Petr Viktorin <pviktori@redhat.com> - 1.0.2-11
- Disable the python3 subpackage
  Functionality of funcsigs is available in Python 3's inspect module.

* Mon Jul 02 2018 Petr Viktorin <pviktori@redhat.com> - 1.0.2-10
- Skip python2 tests to allow removing python2-unittest2 from the distribution
- Fix workaround for allowing Python 2 for build

* Mon Jun 25 2018 Petr Viktorin <pviktori@redhat.com> - 1.0.2-9
- Allow Python 2 for build
  see https://hurl.corp.redhat.com/rhel8-py2
- Switch to python3-sphinx

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 1.0.2-7
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.0.2-4
- Enable tests

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.0.2-3
- Rebuild for Python 3.6
- Disable python3 tests for now

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Jun 11 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.0.2-1
- Upstream 1.0.2 (RHBZ#1341262)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4-2
- Add license file in doc subpackage

* Wed Dec 02 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4-1
- Initial package.
