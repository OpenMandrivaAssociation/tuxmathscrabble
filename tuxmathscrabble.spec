Name:       tuxmathscrabble
Version:    0.7.4
Release:    2
Summary:    A math version of the popular board game for ages 4-40

License:    GPLv2+
Epoch:      1
Group:      Games/Boards
URL:        http://www.asymptopia.org/
Source0:    http://prdownloads.sourceforge.net/tuxmathscrabble/%{name}-%{version}.tar.bz2
Patch0:    tuxmathscrabble-0.7.4-fix-path.patch
BuildRequires:	imagemagick
Requires:   python-pygame
Requires:   wxPythonGTK
BuildArch:  noarch

%description
TuxMathScrabble is an OpenSource math version of the popular board game for 
ages 4-40. it challenges young people to construct compound equations and 
consider multiple abstract possibilities. There are 4 skill levels, the 
hardest uses numbers up to 20 and supports division as well as 
add/subtract/multiply. Upon completing a successful move little Tux's 
pop-out of the most recently moved tiles and do a little dance. Tux moves 
his own pieces as well as performing various animated antics.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build

%install
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{name}
cp -pr Font %{buildroot}%{_gamesdatadir}/%{name}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{name}/lib
cp -pr TuxMathScrabble %{buildroot}%{_gamesdatadir}/%{name}/lib
cp .tms_config_master  %{buildroot}%{_gamesdatadir}/%{name}

install -d -m 755 %{buildroot}%{_gamesbindir}
install -m 755 %{name}.py %{buildroot}%{_gamesbindir}/%{name}

mkdir -p %{buildroot}%{_liconsdir}
mkdir -p %{buildroot}%{_iconsdir}
mkdir -p %{buildroot}%{_miconsdir}
convert -resize 48x48 tms.ico %{buildroot}%{_liconsdir}/%{name}.png
convert -resize 32x32 tms.ico %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 16x16 tms.ico %{buildroot}%{_miconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=TuxMathScrabble
Comment=Fun game to learn math
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-admin.desktop << EOF
[Desktop Entry]
Name=TuxMathScrabble Admin
Comment=Fun game to learn math with administration mode enabled
Exec=%{_gamesbindir}/%{name} -wx
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%clean

%files
%doc INSTALL LICENSE README CHANGES
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*.desktop 
%{_iconsdir}/*



