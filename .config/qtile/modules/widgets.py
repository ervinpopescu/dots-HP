import subprocess

from libqtile import bar, qtile
from libqtile.lazy import lazy
from qtile_extras import widget

from .settings import colors, decor
from .widget_functions import no_text, location, reload, weather_popup

def top_widgets():
    return [
        widget.Image(
            filename="/usr/share/pixmaps/archlinux-logo.svg",
            margin=4,
            padding=5,
            mouse_callbacks={
                "Button1": lazy.spawn("rofi -show drun -terminal alacritty -show-icons")
            },
            **decor
        ),
        widget.Spacer(length=3),
        widget.Image(
            filename="/usr/share/icons/Papirus/64x64/apps/python.svg",
            margin=4,
            padding=5,
            mouse_callbacks={
                "Button1": lazy.spawn("alacritty -e /home/ervin/.local/bin/editqtile")
            },
            **decor
        ),
        widget.Spacer(length=3),
        widget.GroupBox(
            font="Font Awesome 6 Free Solid",
            fontsize=13,
            padding=5,
            # highlight_method="block",
            inactive=colors[3],
            active=colors[7],
            this_current_screen_border=colors[10],
            padding_y=4,
            padding_x=3,
            rounded="true",
            disable_drag=True,
            hide_unused=True,
            **decor
        ),
        widget.Spacer(length=3),
        widget.CurrentLayoutIcon(scale=0.79, padding=3, **decor),
        widget.Spacer(length=3),
        widget.TaskList(
            parse_text=no_text,
            highlight_method="block",
            icon_size=18,
            border=colors[0],
            rounded=True,
            padding_x=0,
            padding_y=3,
            margin_x=2,
            margin_y=2,
            txt_floating="🗗 ",
            txt_maximized="🗖 ",
            txt_minimized="🗕 ",
            # mouse_callbacks={
            #     "Button3": lambda: qtile.current_window.kill()
            #     }
        ),
        widget.Spacer(),
        widget.Systray(),
        widget.Spacer(),
        widget.KeyboardLayout(
            font="Font Awesome 6 Free Solid",
            # font="CodeNewRoman Nerd Font Mono Bold",
            fontsize=14,
            padding=5,
            configured_keyboards=["us", "ro std"],
            display_map={"us": "US", "ro std": "RO"},
            foreground=colors[5],
            fmt=" {}",
            **decor
        ),
        widget.Spacer(length=3),
        widget.MyCheckUpdates(
            font="Font Awesome 6 Free Solid",
            # font="CodeNewRoman Nerd Font Mono",
            fontsize=14,
            padding=5,
            update_interval=60,
            foreground=colors[6],
            func=lambda: subprocess.check_output(
                "/home/ervin/.local/bin/chkup").decode(
                "utf-8"
            ),
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("up")
            },
            fmt=" {}",
            **decor
        ),
        widget.Spacer(length=3),
        widget.MyWeather(
            appkey="ce4579dd88a8d4877a8c23f2a10d61cc",
            foreground=colors[6],
            padding=5,
            font="CodeNewRoman Nerd Font Mono Bold",
            fontsize=18,
            format="{main_feels_like:.0f}°{units_temperature} {icon}",
            location=location(),
            mouse_callbacks={"Button1": weather_popup()},
            **decor
        ),
        widget.Spacer(length=3),
        widget.MyBattery(
            update_interval=1,
            padding=5,
            font="CodeNewRoman Nerd Font Mono Bold",
            fontsize=18,
            foreground=colors[6],
            func=lambda: subprocess.check_output(
                "/home/ervin/.local/bin/bat_icon"
            ).decode("utf-8"),
            **decor
        ),
        widget.Spacer(length=3),
        widget.MyData(
            update_interval=3600,
            padding=5,
            font="CodeNewRoman Nerd Font Mono Bold",
            fontsize=18,
            foreground=colors[6],
            func=lambda: subprocess.check_output(
                "/home/ervin/.local/bin/uptime.sh"
            ).decode("utf-8"),
            mouse_callbacks={"Button1": lazy.spawn("alacritty -e htop")},
            **decor
        ),
        widget.Spacer(length=3),
        widget.MouseOverClock(
            format="%H:%M",
            long_format="%d.%m.%y",
            font="CodeNewRoman Nerd Font Mono Bold",
            padding=5,
            fontsize=18,
            foreground=colors[10],
            mouse_callbacks={"Button1": lazy.spawn("gsimplecal")},
            **decor
        ),
        widget.Spacer(length=3),
        widget.TextBox(
            text="",
            font="Font Awesome 6 Free Solid",
            mouse_callbacks={"Button1": lambda: reload()},
            foreground=colors[13],
            padding=5,
            **decor
        ),
        widget.Spacer(length=3),
        widget.TextBox(
            text="",
            padding=5,
            fontsize=13,
            font="Font Awesome 6 Free Solid",
            mouse_callbacks={"Button1": lazy.spawn("nwgbar")},
            foreground=colors[11],
            **decor
        ),
    ]

def left_widgets():
    return [
        widget.Image(
            filename="/usr/share/pixmaps/archlinux-logo.svg",
            margin=4,
            padding=5,
            mouse_callbacks={
                "Button1": lazy.spawn("rofi -show drun -terminal alacritty -show-icons")
            },
            **decor
        ),
        widget.Spacer(length=3),
        widget.Image(
            filename="/usr/share/icons/Papirus/64x64/apps/python.svg",
            margin=4,
            padding=5,
            mouse_callbacks={
                "Button1": lazy.spawn("alacritty -e /home/ervin/.local/bin/editqtile")
            },
            **decor
        ),
        widget.Spacer(length=bar.STRETCH),
        widget.KeyboardLayout(
            font="Font Awesome 6 Free Solid",
            fontsize=13,
            padding=5,
            configured_keyboards=["us", "ro std"],
            display_map={"us": "us", "ro std": "ro"},
            foreground=colors[6],
            fmt=" {}",
            **decor
        ),
        widget.Spacer(length=3),
        widget.MyCheckUpdates(
            font="Font Awesome 6 Free Solid",
            fontsize=13,
            padding=5,
            update_interval=60,
            foreground=colors[6],
            func=lambda: subprocess.check_output("/home/ervin/.local/bin/chkup").decode(
                "utf-8"
            ),
            mouse_callbacks={"Button1": lazy.spawn("alacritty -e yay")},
            fmt=" {}",
            **decor
        ),
        widget.Spacer(length=3),
        widget.MyBattery(
            update_interval=1,
            padding=5,
            fontsize=13,
            foreground=colors[6],
            func=lambda: subprocess.check_output(
                "/home/ervin/.local/bin/bat_icon"
            ).decode("utf-8"),
            **decor
        ),
        widget.Spacer(length=3),
        widget.MyWeather(
            appkey="ce4579dd88a8d4877a8c23f2a10d61cc",
            foreground=colors[6],
            fontsize=13,
            padding=5,
            format="{temp:.0f}°{units_temperature} {icon}",
            location=location(),
            mouse_callbacks={"Button1": lambda: weather_popup()},
            **decor
        ),
        widget.Spacer(length=3),
        widget.GenPollText(
            update_interval=3600,
            padding=5,
            fontsize=13,
            foreground=colors[10],
            func=lambda: subprocess.check_output(
                "/home/ervin/.local/bin/uptime.sh"
            ).decode("utf-8"),
            **decor
        ),
        widget.Spacer(length=3),
        widget.MouseOverClock(
            format="%H:%M",
            padding=5,
            fontsize=13,
            foreground=colors[10],
            mouse_callbacks={"Button1": lazy.spawn("gsimplecal")},
            **decor
        ),
        widget.Spacer(length=3),
        widget.TextBox(
            text="",
            font="Font Awesome 6 Free Solid",
            mouse_callbacks={"Button1": lambda: reload()},
            foreground=colors[13],
            padding=5,
            fontsize=13,
            **decor
        ),
        widget.Spacer(length=3),
        widget.TextBox(
            text="",
            font="Font Awesome 6 Free Solid",
            padding=5,
            fontsize=13,
            foreground=colors[11],
            mouse_callbacks={"Button1": lazy.spawn("nwgbar")},
            **decor
        ),
    ]
