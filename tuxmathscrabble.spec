%define oname      TuxMathScrabble
%define pythonlibs %{_libdir}/python%pyver/site-packages/asymptopia/


Summary: A math version of the popular board game for ages 4-40
Name: tuxmathscrabble
Version: 0.5.0
Release: %mkrel 0.2
URL: http://www.asymptopia.org/
Source0: http://prdownloads.sourceforge.net/tuxmathscrabble/%oname-%version-rc2.tgz
Patch0:    TuxMathScrabble-0.5.0-rc2-fixpath.patch
License: GPL
Epoch:  1
Group: Games/Boards
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

%setup -q -n TuxMathScrabble
%patch0 -p0

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{pythonlibs}
cp -R %oname/* %{buildroot}%{pythonlibs}

mkdir -p %{buildroot}%{_gamesbindir}
cp %oname.py %{buildroot}%{_gamesbindir}/tuxmathscrabble


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=TuxMathScrabble
Comment=Fun game to learn math
Exec=%{_gamesbindir}/tuxmathscrabble
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;BoardGame;
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
%{_datadir}/applications/mandriva-%{name}.desktop 



