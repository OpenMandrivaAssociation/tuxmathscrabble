%define oname      TuxMathScrabble
%define pythonlibs %{_libdir}/python%pyver/site-packages/asymptopia/


Summary: A math version of the popular board game for ages 4-40
Name: tuxmathscrabble
Version: 3.0.4
Release: %mkrel 2
URL: http://www.asymptopia.org/
Source0: http://prdownloads.sourceforge.net/tuxmathscrabble/%{oname}-%{version}LIN.tar.bz2
License: GPL
Group: Games/Boards
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Requires: python-pygame

%description
TuxMathScrabble is an OpenSource math version of the popular board game for 
ages 4-40. it challenges young people to construct compound equations and 
consider multiple abstract possibilities. There are 4 skill levels, the 
hardest uses numbers up to 20 and supports division as well as 
add/subtract/multiply. Upon completing a successful move little Tux's 
pop-out of the most recently moved tiles and do a little dance. Tux moves 
his own pieces as well as performing various animated antics.

%prep

%setup -q -n TuxMathScrabble-%{version}LIN

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{pythonlibs}
cp -R %name/* %{buildroot}%{pythonlibs}/

mkdir -p %{buildroot}%{_gamesbindir}
cp %oname.py %{buildroot}%{_gamesbindir}/tuxmathscrabble


install -d -m 0755 %buildroot/%_menudir
cat >%buildroot/%_menudir/%name <<EOF
?package(%{name}): command="%{_gamesbindir}/tuxmathscrabble" \
icon="" \
needs="x11" \
title="TuxMathScrabble" \
longtitle="Fun game to learn math" \
section="More Applications/Games/Boards"  \
xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=TuxMathScrabble
Comment=Fun game to learn math
Exec=%{_gamesbindir}/tuxmathscrabble
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame;
Encoding=UTF-8
EOF


find $RPM_BUILD_ROOT -name .xvpics | xargs rm -Rf 

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%update_menus

%files
%defattr(-,root,root)
%{_gamesbindir}/*
%{pythonlibs}
%{_menudir}/*
%{_datadir}/applications/mandriva-%{name}.desktop 



