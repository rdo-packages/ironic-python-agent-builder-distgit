# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		openstack-ironic-python-agent-builder
Summary:	Builder of ironic-python-agent ramdisk images
Version:    XXX
Release:    XXX
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://docs.openstack.org/ironic-python-agent-builder
Source0:        https://tarballs.openstack.org/ironic-python-agent-builder/ironic-python-agent-builder-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python%{pyver}-devel
BuildRequires:	python%{pyver}-setuptools
BuildRequires:	python%{pyver}-pbr

Requires:	diskimage-builder

%description
This package contains a script to build an ironic-python-agent builder, as well
as a diskimage-builder element for it.

%prep
%setup -q -n ironic-python-agent-builder-%{upstream_version}

%build
%{pyver_build}

%install
%{pyver_install}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

%files
%doc LICENSE
%doc README.rst
%doc AUTHORS
%doc ChangeLog
%{pyver_sitelib}/ironic_python_agent_builder*
%{_bindir}/ironic-python-agent-builder
%{_datadir}/ironic-python-agent-builder

%changelog
