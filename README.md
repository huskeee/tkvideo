<p align="center">
  <a href="https://github.com/MysteryBlokHed/tkvideo-moviepy">
    <img src="images/logo.png" alt="Logo" >
  </a>

  <h1 align="center">tkVideo</h1>

  <p align="center">
    Python module for playing videos (without sound) inside tkinter Label widget using Pillow and imageio
    <br />

<p align="center">
  <a href="https://github.com/MysteryBlokHed/tkvideo-moviepy/graphs/contributors">
    <img
      src="https://img.shields.io/github/contributors/MysteryBlokHed/tkvideo-moviepy.svg?style=flat-square"
      alt="Contributors"
    />
  </a>
  <a href="https://github.com/MysteryBlokHed/tkvideo-moviepy/network/members">
    <img
      src="https://img.shields.io/github/forks/MysteryBlokHed/tkvideo-moviepy.svg?style=flat-square"
      alt="Forks"
    />
  </a>
  <a href="https://github.com/MysteryBlokHed/tkvideo-moviepy/stargazers">
    <img
      src="https://img.shields.io/github/stars/MysteryBlokHed/tkvideo-moviepy.svg?style=flat-squarem/MysteryBlokHed/tkvideo-moviepy/network/members"
      alt="Stargazers"
    />
  </a>
  <a href="https://github.com/MysteryBlokHed/tkvideo-moviepy/issues">
    <img
      src="https://img.shields.io/github/issues/MysteryBlokHed/tkvideo-moviepy.svg?style=flat-square"
      alt="Issues"
    />
  </a>
  <a href="https://github.com/MysteryBlokHed/tkvideo-moviepy/blob/master/LICENSE">
    <img
      src="https://img.shields.io/github/license/MysteryBlokHed/tkvideo-moviepy.svg?style=flat-square"
      alt="MIT License"
    />
  </a>
</p>

## About The Project

tkVideo is a Python module for playing videos in GUIs created with tkinter.
It does so by binding to a `tkinter.Label` widget of the user's choice and rapidly changing its image object.

### Built With

- [tkinter (Python built-in)](https://docs.python.org/3/library/tkinter.html)
- [imageio](https://imageio.github.io)
- [Pillow](https://pypi.org/project/Pillow/)

## Installation

### Users

### From PyPI

```sh
pip install tkvideo
```

#### From cloned repo

```sh
git clone https://github.com/MysteryBlokHed/tkvideo-moivepy
cd tkvideo-moviepy
python setup.py install
```

### Developers and contributors

#### From cloned repo

```sh
git clone https://github.com/MysteryBlokHed/tkvideo-moivepy
cd tkvideo-moviepy
python setup.py develop
```

or

#### Editable mode from PyPI

```sh
pip install -e tkvideo-moviepy
```

This will create a shim between your code and the module binaries that gets updated every time you change your code.

## Usage

- Import tkinter and tkvideo-moviepy
- Create `Tk()` parent and the label you'd like to use
- Get a moviepy video
- Create `tkvideo` object with its parameters (moviepy clip, label name, whether to loop the video or not and size of the video)
- Start the player thread with `<player_name>.play()`
- Start the Tk main loop

Example code:

```py
from tkinter import *
from tkvideo import tkvideo
from moviepy.editor import VideoFileClip

root = Tk()
my_label = Label(root)
my_label.pack()

clip = VideoFileClip('path/to/video.mp4')

player = tkvideo(clip, my_label, loop = 1, size = (1280,720))
player.play()

root.mainloop()
```

## Issues & Suggestions

Have a problem that needs to be solved or a suggestion to make? See the [issues](https://github.com/MysteryBlokHed/tkvideo-moviepy/issues) page.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
