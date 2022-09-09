
# A simple YouTube video downloader using Python

![GUI screenshot](images/screenshot.png)

- When supplied with a link, program will find and download a progressive stream of the video.
  - "Progressive stream" refers to a stream that contains the audio and video in a single file. Due to YouTube using different techniques for high resolution videos, highest possible downloaded video quality is 720p. More in [PyTube documentation](https://pytube.io/en/latest/user/streams.html).
    - During execution program displays its current state with messages, e.g "Fetching for the video" or "Passed link is not a valid YouTube link".
- Video fetching and downloading has been implemented with [PyTube v12.1.0](https://pytube.io/en/latest/) Python library.
- Graphical user interface has been written with HTML & CSS.
  - [eel](https://github.com/ChrisKnott/Eel) library has been used to connect JavaScript with Python, a library based on JavaScript's [Electron framework](https://www.electronjs.org).
  - similarly to Electron apps, it requires a Chromium browser to properly display a window.
    - used code is stored within the `web` folder.
