%define		_state		stable
%define		orgname		granatier
%define		qtver		4.8.0

Summary:	bomber
Name:		kde4-granatier
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	ff07a4b61fb74d8bf94b1884d4e455b6
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-granatier
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Granatier.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang granatier	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f granatier.lang
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/granatier
%{_datadir}/apps/granatier
%{_desktopdir}/kde4/granatier.desktop
%{_datadir}/config.kcfg/granatier.kcfg
%{_iconsdir}/hicolor/*x*/apps/granatier.png
%{_iconsdir}/hicolor/scalable/apps/granatier.svgz
