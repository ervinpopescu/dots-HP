#! /usr/bin/env python3

import os
import shutil

shittyfiles = [
    '~/.nvidia-settings-rc',
    '~/.xsession-errors',
    '~/.xsession-errors.old',
    '~/.Xauthority',
    '~/octave-workspace',
    '~/.hplip',
    '~/.mysql'
    '~/.vim',
    '~/.gphoto',
    '~/.john',
    '~/.yarn',
    '~/.yarnrc',
    '~/.gtkrc-2.0',
    '~/.bash_history',
    '~/.ACEStream',
    '~/.dat.ngspice',
    '~/.viminfo',
    '~/.cortex',
    '~/.lesshst',
    '~/.fehbg',
    '~/.python_history',
    '~/Documents/Videos',
    '~/Documents/Pictures/',
    '~/Documents/Downloads/',
    '~/Documents/Templates/',
    '~/Documents/Music/',
    '~/.octave_hist',
    '~/SoftMaker',
    '~/.wget-hsts',
    '~/.zsh_history',
    '~/.adobe',
    '~/.macromedia',
    '~/.recently-used',
    '~/.local/share/recently-used.xbel',
    '~/Desktop',
    '~/.thumbnails',
    '~/.gconfd',
    '~/.gconf',
    '~/.local/share/gegl-*',
    '~/.FRD/log/app.log',
    '~/.FRD/links.txt',
    '~/.objectdb',
    '~/.gstreamer-0.10',
    '~/.pulse',
    '~/.esd_auth',
    '~/.config/enchant',
    '~/.spicec',
    '~/.dropbox-dist',
    '~/.parallel',
    '~/.dbus',
    '~/ca2',
    '~/ca2~',
    '~/.distlib/',
    '~/.bazaar/',
    '~/.bzr.log',
    '~/.nv/',
    '~/.viminfo',
    '~/.npm/',
    '~/.java/',
    '~/.oracle_jre_usage/',
    '~/.jssc/',
    '~/.tox/',
    '~/.pylint.d/',
    '~/.qute_test/',
    '~/.QtWebEngineProcess/',
    '~/.qutebrowser/',
    '~/.asy/',
    '~/.cmake/',
    '~/.gnome/',
    '~/unison.log',
    '~/.texlive/',
    '~/.w3m/',
    '~/.subversion/',
    '~/nvvp_workspace/',
    '~/.ansible/',
    '~/.fltk/',
    '~/.vnc/',
]

def yesno(question, default="n"):
    """ Asks the user for YES or NO, always case insensitive.
        Returns True for YES and False for NO.
    """
    prompt = "%s (y/[n]) " % question

    ans = input(prompt).strip().lower()

    if not ans:
        ans = default

    if ans == "y":
        return True
    return False

def rmshit():
    print("Found shittyfiles:")
    found = []
    for f in shittyfiles:
        absf = os.path.expanduser(f)
        if os.path.exists(absf):
            found.append(absf)
            print("    %s" % f)

    if len(found) == 0:
        print("No shitty files found :)")
        return

    if yesno("Remove all?", default="n"):
        for f in found:
            if os.path.isfile(f):
                os.remove(f)
            else:
                shutil.rmtree(f)
        print("All cleaned")
    else:
        print("No file removed")

if __name__ == '__main__':
    rmshit()
