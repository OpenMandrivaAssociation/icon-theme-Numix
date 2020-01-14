Name: icon-theme-numix
Summary: The Numix icon theme
Version: 2020.01.13
Release: 1
Source0: https://github.com/numixproject/numix-icon-theme-circle/archive/master/Numix-circle-%{version}.tar.gz
Source1: https://github.com/numixproject/numix-icon-theme/archive/master/Numix-%{version}.tar.gz
Group: Graphical Desktop/KDE
License: GPLv3
BuildArch: noarch

%description
The Numix icon theme

%prep
%autosetup -p1 -n numix-icon-theme-circle-master -a 1

%build
# Nothing to do...

%install
mkdir -p %{buildroot}%{_datadir}/icons
cp -a Numix* numix-icon-theme-master/Numix* %{buildroot}%{_datadir}/icons/

%files
%license LICENSE
%{_datadir}/icons/Numix
%{_datadir}/icons/Numix-Light
%{_datadir}/icons/Numix-Circle
%{_datadir}/icons/Numix-Circle-Light
