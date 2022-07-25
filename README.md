
# A simple YouTube video downloader using Python.

- When supplied with a link, program will find and download a progressive stream of the video.
	- "Progressive stream" refers to a stream that contains the audio and video in a single file. Due to YouTube using different techniques for high resolution videos, highest possible downloaded video quality is 720p. More about this at [PyTube documentation](https://pytube.io/en/latest/user/streams.html)
- Video fetching and downloading has been implemented with [PyTube v12.1.0](https://pytube.io/en/latest/) Python library.
- Graphical user interface has been written with HTML & CSS, and is connected to the Python script using JavaScript and HTML forms. 
	- In order to connect JavaScript with Python, an [eel](https://github.com/ChrisKnott/Eel) library has been used. This Python library is based on [JavaScript's Electron framework](https://www.electronjs.org), used to build desktop applications using JavaScript, HTML, and CSS.
	- `web` folder contains everything used to create the GUI.