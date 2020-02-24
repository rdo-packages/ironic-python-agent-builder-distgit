# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           openstack-ironic-python-agent-builder
Summary:        Builder of ironic-python-agent ramdisk images
Version:        1.0.0
Release:        1%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://docs.openstack.org/ironic-python-agent-builder
Source0:        https://tarballs.openstack.org/ironic-python-agent-builder/ironic-python-agent-builder-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

Requires:       diskimage-builder

%description
This package contains a script to build an ironic-python-agent builder, as well
as a diskimage-builder element for it.

%prep
%autosetup -n ironic-python-agent-builder-%{upstream_version} -S git

%build
%{pyver_build}

%install
%{pyver_install}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

%files
%license LICENSE
%doc README.rst
%doc AUTHORS
%doc ChangeLog
%{pyver_sitelib}/ironic_python_agent_builder*
%{_bindir}/ironic-python-agent-builder
%{_datadir}/ironic-python-agent-builder

%changelog
* Thu Oct 10 2019 RDO <dev@lists.rdoproject.org> 1.0.0-1
- Update to 1.0.0

