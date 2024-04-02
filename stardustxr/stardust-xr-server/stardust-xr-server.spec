%global commit 807928a8d3e631ba4717e805edfefe7c5014c7a6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240306
%global snapshot_info %{commit_date}.%{shortcommit}

Name:       stardust-xr-server
Version:	  %snapshot_info
Release:		1%?dist
Summary:		Stardust XR Reference Server
License:		GPL-2
URL:			  https://stardustxr.org/
Source0:		https://github.com/stardustxr/server/archive/%{commit}/server-%{shortcommit}.tar.gz
BuildRequires: anda-srpm-macros rust-packaging gcc g++ cmake libX11-devel libGL-devel fontconfig-devel libxkbcommon-devel openxr-devel libgbm-devel libXfixes-devel clang-devel

%description
%summary.

%prep
%autosetup -n server-%{commit}
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install
rm -rf .cargo

%files
%doc README.md
%license LICENSE
%_bindir/stardust-xr-server

%changelog
%autochangelog
