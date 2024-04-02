%global commit fef8c317928a1d1798d8cee9af94d219a7c09e8c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240306
%global snapshot_info %{commit_date}.%{shortcommit}

Name:       flatland
Version:	  %snapshot_info
Release:		1%?dist
Summary:		Flat panel UI client for Stardust XR like SimulaVR or xrdesktop
License:		MIT
URL:			  https://stardustxr.org/
Source0:		https://github.com/stardustxr/flatland/archive/%{commit}/flatland-%{shortcommit}.tar.gz
BuildRequires: anda-srpm-macros rust-packaging

%description
%summary.

%prep
%autosetup -n flatland-%{commit}
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install
rm -rf .cargo

%files
%doc README.md
%license LICENSE
%_bindir/flatland

%changelog
%autochangelog
