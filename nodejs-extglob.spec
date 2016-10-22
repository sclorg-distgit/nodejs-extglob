%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name extglob

Summary:       Convert extended globs to regex-compatible strings
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.3.1
Release:       4%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/extglob
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Convert extended globs to regex-compatible strings. 
Add (almost) the expressive power of regular expressions to glob patterns.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%doc LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.1-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.1-3
- Rebuilt with updated metapackage

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 0.3.1-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 0.3.1-1
- Initial package