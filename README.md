<p align="center">
  <a href="https://github.com/huskeee/tkvideo">
    <img src="https://raw.githubusercontent.com/huskeee/tkvideo/master/images/logo.png" alt="Logo" >
  </a>

  <h1 align="center">tkVideo</h1>

  <p align="center">
    Python module for playing videos (without sound) inside tkinter Label widget using Pillow and imageio
    <br />

</p>

<p align = center>
	<a href="https://github.com/huskeee/tkvideo/graphs/contributors">
		<img src="https://img.shields.io/github/contributors/huskeee/tkvideo.svg?style=flat-square" alt="Contributors" />
	</a>
	<a href="https://github.com/huskeee/tkvideo/network/members">
		<img src="https://img.shields.io/github/forks/huskeee/tkvideo.svg?style=flat-square" alt="Forks" />
	</a>
	<a href="https://github.com/huskeee/tkvideo/stargazers">
		<img src="https://img.shields.io/github/stars/huskeee/tkvideo.svg?style=flat-squarem/huskeee/tkvideo/network/members" alt="Stargazers" />
	</a>
	<a href="https://github.com/huskeee/tkvideo/issues">
		<img src="https://img.shields.io/github/issues/huskeee/tkvideo.svg?style=flat-square" alt="Issues" />
	</a>
	<a href="https://github.com/huskeee/tkvideo/blob/master/LICENSE">
		<img src="https://img.shields.io/github/license/huskeee/tkvideo.svg?style=flat-square" alt="MIT License" />
	</a>
</p>

<!-- ABOUT THE PROJECT -->

## About The Project

tkVideo is a Python module for playing videos in GUIs created with tkinter. It does so by binding to a `tkinter.Label` widget of the user's choice and rapidly changing its image object.

### Built With

- [tkinter (Python built-in)](https://docs.python.org/3/library/tkinter.html)
- [imageio](https://imageio.github.io)
- [Pillow](https://pypi.org/project/Pillow/)

## Installation

### End-users:

- Clone the repo and run `setup.py`

```sh
git clone https://github.com/huskeee/tkvideo.git
python ./tkvideo/setup.py
```

or

- Install the package from PyPI

```sh
pip install tkvideo
```

### Developers and contributors

- Clone the repo and install the module in developer mode

```sh
git clone https://github.com/huskeee/tkvideo.git
python ./tkvideo/setup.py develop
```

or

- Install the package from PyPI in editable mode

```sh
pip install -e tkvideo
```

This will create a shim between your code and the module binaries that gets updated every time you change your code.

<!-- USAGE EXAMPLES -->

## Usage

- Import tkinter and tkvideo
- Create `Tk()` parent and the label you'd like to use
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

## Issues / suggestions

Have a problem that needs to be solved or a suggestion to make? See the [issues](https://github.com/huskeee/tkvideo/issues) page.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contact

Xenofon Konitsas - [@huskeeeeee](https://twitter.com/huskeeeeee) - konitsasx@gmail.com

Project Link: [https://github.com/huskeee/tkvideo](https://github.com/huskeee/tkvideo)

## Special thanks to

- [@Pythonista](https://stackoverflow.com/users/5230901/pythonista) on StackOverflow for the frame loading code

##### Readme file created using [Othneil Drew's awesome template ♥](https://github.com/othneildrew/Best-README-Template)
