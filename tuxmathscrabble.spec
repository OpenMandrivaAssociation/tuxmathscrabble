%define oname      TuxMathScrabble

Name:       tuxmathscrabble
Version:    0.5.8
Release:    %mkrel 1
Summary:    A math version of the popular board game for ages 4-40
License:    GPL
Epoch:      1
Group:      Games/Boards
URL:        http://www.asymptopia.org/
Source0:    http://prdownloads.sourceforge.net/tuxmathscrabble/%oname-%version.tgz
Patch0:    TuxMathScrabble-0.5.8-fix-path.patch
Requires:   python-pygame
Requires:   wxPythonGTK
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%patch0 -p1

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/tuxmathscrabble
cp -pr Globals %{buildroot}%{_gamesdatadir}/tuxmathscrabble
cp -pr Font %{buildroot}%{_gamesdatadir}/tuxmathscrabble
install -d -m 755 %{buildroot}%{_gamesdatadir}/tuxmathscrabble/lib
cp -pr TuxMathScrabble %{buildroot}%{_gamesdatadir}/tuxmathscrabble/lib

install -d -m 755 %{buildroot}%{_gamesbindir}
install -m 755 tuxmathscrabble %{buildroot}%{_gamesbindir}/tuxmathscrabble

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

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%files
%defattr(-,root,root)
%doc INSTALL LICENSE README CHANGES
%{_gamesbindir}/tuxmathscrabble
%{_gamesdatadir}/tuxmathscrabble
%{_datadir}/applications/mandriva-%{name}.desktop 
