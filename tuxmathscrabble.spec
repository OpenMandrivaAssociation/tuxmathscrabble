%define oname      TuxMathScrabble

Name:       tuxmathscrabble
Version:    0.5.8
Release:    %mkrel 2
Summary:    A math version of the popular board game for ages 4-40
License:    GPLv2+
Epoch:      1
Group:      Games/Boards
URL:        http://www.asymptopia.org/
Source0:    http://prdownloads.sourceforge.net/tuxmathscrabble/%oname-%version.tgz
Patch0:    TuxMathScrabble-0.5.8-fix-path.patch
BuildRequires:	imagemagick
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

mkdir -p %{buildroot}%{_liconsdir}
mkdir -p %{buildroot}%{_iconsdir}
mkdir -p %{buildroot}%{_miconsdir}
convert -resize 48x48 tms.ico %{buildroot}%{_liconsdir}/%{name}.png
convert -resize 32x32 tms.ico %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 16x16 tms.ico %{buildroot}%{_miconsdir}/%{name}.png

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
%{_iconsdir}/*



%changelog
* Sat May 16 2009 Samuel Verschelde <stormi@mandriva.org> 1:0.5.8-2mdv2010.0
+ Revision: 376469
- increase release

* Sat May 16 2009 Samuel Verschelde <stormi@mandriva.org> 1:0.5.8-1mdv2010.0
+ Revision: 376452
- fix license
- add icons

* Mon Apr 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.5.8-1mdv2009.1
+ Revision: 366790
- new version
- don't forget to install configuration and fonts
- make it noarch

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:0.5.0-4.3mdv2009.0
+ Revision: 269441
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 11 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:0.5.0-0.3mdv2009.0
+ Revision: 205581
- Should not be noarch ed
- Remove all .svn files and folder

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:0.5.0-0.2mdv2008.1
+ Revision: 132015
- New version 0.5.0 Rc2
  Fix patch in Environment.py ( patch from PCLinuxOS )

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 14 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:0.5.0-0.1mdv2008.1
+ Revision: 119664
- New pre version of 0.5.0

* Fri Dec 14 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:0.4.5-1mdv2008.1
+ Revision: 119591
- New version 0.4.5

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Dec 01 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.0.4-2mdv2007.0
+ Revision: 89589
- Fix File List
- New version 3.0.4
- import tuxmathscrabble-2.7-1mdk

* Mon Jan 17 2005 Michael Scherer <misc@mandrake.org> 2.7-1mdk
- misc cleanup
- from jean-sebastien HUBERT <jshubert@free.fr>
  - first release for Linux-Mandrake

