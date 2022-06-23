```
                                   ██              ██               
                              ▄███▄██   ▄████▄   ███████   ▄▄█████▄ 
                             ██▀  ▀██  ██▀  ▀██    ██      ██▄▄▄▄ ▀ 
                             ██    ██  ██    ██    ██       ▀▀▀▀██▄ 
                             ▀██▄▄███  ▀██▄▄██▀    ██▄▄▄   █▄▄▄▄▄██ 
                               ▀▀▀ ▀▀    ▀▀▀▀       ▀▀▀▀    ▀▀▀▀▀▀  
```                                                    
## Features

1. apps [config](/.config)
    * ***global***
        * catppuccin colorscheme
    * ***alacritty*** (mostly default, fonts and cursor changed)
    * ***conky***
        * ~~*stolen*~~
        * \+ fortune cookie 
    * ***lvim***
        * mostly default 
        * added some LSP's, formatters and some autocommands
        * added the following plugins:
            * `catppuccin/nvim`
            * `Pocco81/AutoSave.nvim`
            * `norcalli/nvim-colorizer.lua`
            * `ethanholz/nvim-lastplace`
            * `iamcco/markdown-preview.nvim`
    * ***nwg-launchers***
        * nwgbar
            * used for powermenu
        * nwgdmenu
          * not used
        * nwggrid
          * rarely used
    * ***qtile***:
        + Apps tied to specific groups
        + Mouse bindings for every widget
        + Keybindings for ***every freakin' program***
        + Layouts that just ***make sense***
        + Sensible picom config
    * ***reflector***: the best config for my location and capabilities
    * ***rofi***:
        * run, drun, window list
    * ***zathura***:
        * clean af UI
    * ***zsh***:
        * ~~**stolen**~~ from Kali Linux and added some stuff over time:
            * .zshenv: 
              * env vars for $HOME cleaning
              * nvidia env vars (fuck nvidia) 
              * random env vars
              * aliases
              * cleanup some systemd mess
          * .zshrc:
              * setopts that ***just make sense***
              * keybindings, completions, prompt

2. [Font](/usr/share/fonts/Code%20New%20Roman%20Bold%20Nerd%20Font%20Complete%20Mono.otf)

3. 57 scripts that each do one thing only
(KISS UNIX philosophy): [bin](/.local/bin/)

4. Package list backup: [pkgs](/pkgs)

## Install

```
cp etc/zsh/* /etc/zsh
cp .config/* $HOME/.config
mkdir -p $HOME/.local/bin
cp -al .local/bin/* $HOME/.local/bin/
sudo mkdir -p /usr/share/fonts/OTF
sudo cp usr/share/fonts/Code* /usr/share/fonts/OTF/
sudo fc-cache -f -v 
```

<!DOCTYPE html>
<html>
<body>
	<h2>Directory Tree</h2><p>
	├── <a href="/archinstall.md">archinstall.md</a><br>
	├── <a href="/.config/">.config</a><br>
	│   ├── <a href="/.config/alacritty/">alacritty</a><br>
	│   │   └── <a href="/.config/alacritty/alacritty.yml">alacritty.yml</a><br>
	│   ├── <a href="/.config/conky/">conky</a><br>
	│   │   ├── <a href="/.config/conky/conky_budgie.conf">conky_budgie.conf</a><br>
	│   │   ├── <a href="/.config/conky/conky.conf">conky.conf</a><br>
	│   │   ├── <a href="/.config/conky/conky_qtile.conf">conky_qtile.conf</a><br>
	│   │   ├── <a href="/.config/conky/filesize.lua">filesize.lua</a><br>
	│   │   ├── <a href="/.config/conky/local.conf">local.conf</a><br>
	│   │   ├── <a href="/.config/conky/main.lua">main.lua</a><br>
	│   │   ├── <a href="/.config/conky/start_budgie.sh">start_budgie.sh</a><br>
	│   │   ├── <a href="/.config/conky/start_qtile.sh">start_qtile.sh</a><br>
	│   │   └── <a href="/.config/conky/utils.lua">utils.lua</a><br>
	│   ├── <a href="/.config/dunst/">dunst</a><br>
	│   │   └── <a href="/.config/dunst/dunstrc">dunstrc</a><br>
	│   ├── <a href="/.config/eww/">eww</a><br>
	│   │   ├── <a href="/.config/eww/eww.scss">eww.scss</a><br>
	│   │   ├── <a href="/.config/eww/eww.yuck">eww.yuck</a><br>
	│   │   ├── <a href="/.config/eww/images/">images</a><br>
	│   │   │   ├── <a href="/.config/eww/images/apps/">apps</a><br>
	│   │   │   │   ├── <a href="/.config/eww/images/apps/alacritty.svg">alacritty.svg</a><br>
	│   │   │   │   ├── <a href="/.config/eww/images/apps/firefox.svg">firefox.svg</a><br>
	│   │   │   │   ├── <a href="/.config/eww/images/apps/nautilus.svg">nautilus.svg</a><br>
	│   │   │   │   ├── <a href="/.config/eww/images/apps/software.svg">software.svg</a><br>
	│   │   │   │   ├── <a href="/.config/eww/images/apps/spotify.svg">spotify.svg</a><br>
	│   │   │   │   └── <a href="/.config/eww/images/apps/vscode.svg">vscode.svg</a><br>
	│   │   │   ├── <a href="/.config/eww/images/bg.png">bg.png</a><br>
	│   │   │   ├── <a href="/.config/eww/images/bluetooth-connected.svg">bluetooth-connected.svg</a><br>
	│   │   │   ├── <a href="/.config/eww/images/bluetooth-off.svg">bluetooth-off.svg</a><br>
	│   │   │   ├── <a href="/.config/eww/images/bluetooth-on.svg">bluetooth-on.svg</a><br>
	│   │   │   ├── <a href="/.config/eww/images/dribble.svg">dribble.svg</a><br>
	│   │   │   ├── <a href="/.config/eww/images/github.svg">github.svg</a><br>
	│   │   │   ├── <a href="/.config/eww/images/gmail.svg">gmail.svg</a><br>
	│   │   │   ├── <a href="/.config/eww/images/music.svg">music.svg</a><br>
	│   │   │   ├── <a href="/.config/eww/images/profile.png">profile.png</a><br>
	│   │   │   ├── <a href="/.config/eww/images/reddit.svg">reddit.svg</a><br>
	│   │   │   ├── <a href="/.config/eww/images/study.svg">study.svg</a><br>
	│   │   │   └── <a href="/.config/eww/images/youtube.svg">youtube.svg</a><br>
	│   │   ├── <a href="/.config/eww/launch_eww">launch_eww</a><br>
	│   │   └── <a href="/.config/eww/scripts/">scripts</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/bluetooth">bluetooth</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/brightness-slider.sh">brightness-slider.sh</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/get-title">get-title</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/getvol.sh">getvol.sh</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/karma">karma</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/launch-apps">launch-apps</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/mail">mail</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/quotes">quotes</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/scroll-title">scroll-title</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/spotify-echo-cover">spotify-echo-cover</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/spotify-get-artist">spotify-get-artist</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/spotify-get-cover">spotify-get-cover</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/system">system</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/time">time</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/eww/scripts/volume-slider.sh">volume-slider.sh</a><br>
	│   │   &nbsp;&nbsp;&nbsp; └── <a href="/.config/eww/scripts/weather-info">weather-info</a><br>
	│   ├── <a href="/.config/git/">git</a><br>
	│   │   ├── <a href="/.config/git/config">config</a><br>
	│   │   └── <a href="/.config/git/gitk">gitk</a><br>
	│   ├── <a href="/.config/glava/">glava</a><br>
	│   │   ├── <a href="/.config/glava/bars-left/">bars-left</a><br>
	│   │   │   └── <a href="/.config/glava/bars-left/1.frag">1.frag</a><br>
	│   │   ├── <a href="/.config/glava/bars-left.glsl">bars-left.glsl</a><br>
	│   │   ├── <a href="/.config/glava/bars-right/">bars-right</a><br>
	│   │   │   └── <a href="/.config/glava/bars-right/1.frag">1.frag</a><br>
	│   │   ├── <a href="/.config/glava/bars-right.glsl">bars-right.glsl</a><br>
	│   │   ├── <a href="/.config/glava/circle/">circle</a><br>
	│   │   ├── <a href="/.config/glava/circle.glsl">circle.glsl</a><br>
	│   │   ├── <a href="/.config/glava/env_awesome.glsl">env_awesome.glsl</a><br>
	│   │   ├── <a href="/.config/glava/env_default.glsl">env_default.glsl</a><br>
	│   │   ├── <a href="/.config/glava/env_i3.glsl">env_i3.glsl</a><br>
	│   │   ├── <a href="/.config/glava/env_KWin.glsl">env_KWin.glsl</a><br>
	│   │   ├── <a href="/.config/glava/env_Openbox.glsl">env_Openbox.glsl</a><br>
	│   │   ├── <a href="/.config/glava/env_Xfwm4.glsl">env_Xfwm4.glsl</a><br>
	│   │   ├── <a href="/.config/glava/graph/">graph</a><br>
	│   │   ├── <a href="/.config/glava/graph.glsl">graph.glsl</a><br>
	│   │   ├── <a href="/.config/glava/radial/">radial</a><br>
	│   │   ├── <a href="/.config/glava/radial.glsl">radial.glsl</a><br>
	│   │   ├── <a href="/.config/glava/rc.glsl">rc.glsl</a><br>
	│   │   ├── <a href="/.config/glava/smooth_parameters.glsl">smooth_parameters.glsl</a><br>
	│   │   ├── <a href="/.config/glava/util/">util</a><br>
	│   │   ├── <a href="/.config/glava/wave/">wave</a><br>
	│   │   └── <a href="/.config/glava/wave.glsl">wave.glsl</a><br>
	│   ├── <a href="/.config/hypr/">hypr</a><br>
	│   │   └── <a href="/.config/hypr/hypr.conf">hypr.conf</a><br>
	│   ├── <a href="/.config/lf/">lf</a><br>
	│   │   ├── <a href="/.config/lf/cleaner">cleaner</a><br>
	│   │   ├── <a href="/.config/lf/lfrc">lfrc</a><br>
	│   │   └── <a href="/.config/lf/scope">scope</a><br>
	│   ├── <a href="/.config/libinput-gestures-budgie.conf">libinput-gestures-budgie.conf</a><br>
	│   ├── <a href="/.config/libinput-gestures.conf">libinput-gestures.conf</a><br>
	│   ├── <a href="/.config/libinput-gestures-qtile.conf">libinput-gestures-qtile.conf</a><br>
	│   ├── <a href="/.config/lvim/">lvim</a><br>
	│   │   └── <a href="/.config/lvim/config.lua">config.lua</a><br>
	│   ├── <a href="/.config/nwg-launchers/">nwg-launchers</a><br>
	│   │   ├── <a href="/.config/nwg-launchers/nwgbar/">nwgbar</a><br>
	│   │   │   ├── <a href="/.config/nwg-launchers/nwgbar/bar.json">bar.json</a><br>
	│   │   │   └── <a href="/.config/nwg-launchers/nwgbar/style.css">style.css</a><br>
	│   │   ├── <a href="/.config/nwg-launchers/nwgdmenu/">nwgdmenu</a><br>
	│   │   │   └── <a href="/.config/nwg-launchers/nwgdmenu/style.css">style.css</a><br>
	│   │   └── <a href="/.config/nwg-launchers/nwggrid/">nwggrid</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/nwg-launchers/nwggrid/style.css">style.css</a><br>
	│   │   &nbsp;&nbsp;&nbsp; └── <a href="/.config/nwg-launchers/nwggrid/terminal">terminal</a><br>
	│   ├── <a href="/.config/picom.conf">picom.conf</a><br>
	│   ├── <a href="/.config/pythonrc">pythonrc</a><br>
	│   ├── <a href="/.config/qtile/">qtile</a><br>
	│   │   ├── <a href="/.config/qtile/config.py">config.py</a><br>
	│   │   ├── <a href="/.config/qtile/images/">images</a><br>
	│   │   │   ├── <a href="/.config/qtile/images/mod1.png">mod1.png</a><br>
	│   │   │   ├── <a href="/.config/qtile/images/mod4-control.png">mod4-control.png</a><br>
	│   │   │   ├── <a href="/.config/qtile/images/mod4-mod1.png">mod4-mod1.png</a><br>
	│   │   │   ├── <a href="/.config/qtile/images/mod4.png">mod4.png</a><br>
	│   │   │   ├── <a href="/.config/qtile/images/mod4-shift.png">mod4-shift.png</a><br>
	│   │   │   └── <a href="/.config/qtile/images/no_modifier.png">no_modifier.png</a><br>
	│   │   └── <a href="/.config/qtile/modules/">modules</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/colors.py">colors.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/groups.py">groups.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/hooks.py">hooks.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/__init__.py">__init__.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/keys.py">keys.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/layouts.py">layouts.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/matches.py">matches.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/mouse.py">mouse.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/screens.py">screens.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/settings.py">settings.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/tox.ini">tox.ini</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/widget_functions.py">widget_functions.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; └── <a href="/.config/qtile/modules/widgets.py">widgets.py</a><br>
	│   ├── <a href="/.config/rofi/">rofi</a><br>
	│   │   ├── <a href="/.config/rofi/config.rasi">config.rasi</a><br>
	│   │   ├── <a href="/.config/rofi/powermenu.rasi">powermenu.rasi</a><br>
	│   │   ├── <a href="/.config/rofi/powermenu.sh">powermenu.sh</a><br>
	│   │   └── <a href="/.config/rofi/themes/">themes</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/rofi/themes/catppuccin.rasi">catppuccin.rasi</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/rofi/themes/nord.rasi">nord.rasi</a><br>
	│   │   &nbsp;&nbsp;&nbsp; └── <a href="/.config/rofi/themes/powermenu_nord.rasi">powermenu_nord.rasi</a><br>
	│   ├── <a href="/.config/X11/">X11</a><br>
	│   │   ├── <a href="/.config/X11/xinitrc">xinitrc</a><br>
	│   │   ├── <a href="/.config/X11/xprofile">xprofile</a><br>
	│   │   └── <a href="/.config/X11/Xresources">Xresources</a><br>
	│   ├── <a href="/.config/zathura/">zathura</a><br>
	│   │   ├── <a href="/.config/zathura/catppuccin">catppuccin</a><br>
	│   │   ├── <a href="/.config/zathura/dark">dark</a><br>
	│   │   ├── <a href="/.config/zathura/nord">nord</a><br>
	│   │   └── <a href="/.config/zathura/zathurarc">zathurarc</a><br>
	│   └── <a href="/.config/zsh/">zsh</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/zsh/abbreviations">abbreviations</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/zsh/.zshenv">.zshenv</a><br>
	│   &nbsp;&nbsp;&nbsp; └── <a href="/.config/zsh/.zshrc">.zshrc</a><br>
	├── <a href="/etc/">etc</a><br>
	│   ├── <a href="/etc/sudoers">sudoers</a><br>
	│   ├── <a href="/etc/xdg/">xdg</a><br>
	│   │   └── <a href="/etc/xdg/reflector/">reflector</a><br>
	│   │   &nbsp;&nbsp;&nbsp; └── <a href="/etc/xdg/reflector/reflector.conf">reflector.conf</a><br>
	│   └── <a href="/etc/zsh/">zsh</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/etc/zsh/zprofile">zprofile</a><br>
	│   &nbsp;&nbsp;&nbsp; └── <a href="/etc/zsh/zshenv">zshenv</a><br>
	├── <a href="/.gitignore">.gitignore</a><br>
	├── <a href="/install.sh">install.sh</a><br>
	├── <a href="/LICENSE">LICENSE</a><br>
	├── <a href="/.local/">.local</a><br>
	│   └── <a href="/.local/bin/">bin</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/all_disk_usage">all_disk_usage</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/anbox-shell">anbox-shell</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/ascii-images">ascii-images</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/autohide.py">autohide.py</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/autostart">autostart</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bat_cap">bat_cap</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bat_charging_icon">bat_charging_icon</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bat_icon">bat_icon</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/battery-notification">battery-notification</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bl_ctl">bl_ctl</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bl_icon">bl_icon</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bl_off">bl_off</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bl_on">bl_on</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/brightness_ctl">brightness_ctl</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bt-bat">bt-bat</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/change_conky_alpha">change_conky_alpha</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/change_wallpaper">change_wallpaper</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/chkup">chkup</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/corona.sh">corona.sh</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/cpu_temp">cpu_temp</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/display_center">display_center</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/dot-backup">dot-backup</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/dots-dir-tree">dots-dir-tree</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/editqtile">editqtile</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/filesizes">filesizes</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/find_hardlink">find_hardlink</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/get_birthdays_from_csv">get_birthdays_from_csv</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/getdata">getdata</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/hdd_usage">hdd_usage</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/lfub">lfub</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/libinput-gestures-start">libinput-gestures-start</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/md-preview">md-preview</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/media_ctl">media_ctl</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/memory">memory</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/netspeed">netspeed</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/network_text">network_text</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/pachist">pachist</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/pkglist-backup">pkglist-backup</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/qtile_keybinds">qtile_keybinds</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/qtile_key_pdf">qtile_key_pdf</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/ram_usage">ram_usage</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/reboot-win">reboot-win</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/rmshit.py">rmshit.py</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/rofi-power-menu">rofi-power-menu</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/set_max_layout">set_max_layout</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/spotify-notification">spotify-notification</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/ssd_usage">ssd_usage</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/start-spotify">start-spotify</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/suspend-off">suspend-off</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/suspend-on">suspend-on</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/tray.py">tray.py</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/tsize">tsize</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/uptime.sh">uptime.sh</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/vol_ctl">vol_ctl</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/vol_mute">vol_mute</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/wallpaper">wallpaper</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/window_icon">window_icon</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/window_name">window_name</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/workdays">workdays</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/wttr">wttr</a><br>
	│   &nbsp;&nbsp;&nbsp; └── <a href="/.local/bin/x64ver">x64ver</a><br>
	├── <a href="/pkgs">pkgs</a><br>
	├── <a href="/README.md">README.md</a><br>
	├── <a href="/usr/">usr</a><br>
	│   └── <a href="/usr/share/">share</a><br>
	│   &nbsp;&nbsp;&nbsp; └── <a href="/usr/share/fonts/">fonts</a><br>
	│   &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; └── <a href="/usr/share/fonts/Code%20New%20Roman%20Bold%20Nerd%20Font%20Complete%20Mono.otf">Code New Roman Bold Nerd Font Complete Mono.otf</a><br>
	└── <a href="/wallpaper.png">wallpaper.png</a><br>

41 directories, 190 files

</p>
</body>
</html>
