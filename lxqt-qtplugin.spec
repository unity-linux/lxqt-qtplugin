%define rel 1

Name: lxqt-qtplugin
Version: 0.11.1
Release: %mkrel %rel
Source0: https://github.com/lxde/lxqt-qtplugin/releases/download/%{version}/%{name}-%{version}.tar.xz
Summary: Qt plugin for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(dbusmenu-qt5)

%description
Config panel for the LXQt desktop.

%prep
%setup -q %{name}-%{version}

%build
%cmake_qt5 -DPULL_TRANSLATIONS=NO
%make

%install
%make_install -C build

%files
%_qt5_plugindir/platformthemes/*
