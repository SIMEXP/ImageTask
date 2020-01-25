# memory_task_neuromod
![alt text][logo_neuromod]
### An fMRI experiment on memory

[logo_neuromod]: https://raw.githubusercontent.com/mtl-brainhack-school-2019/memory_task_neuromod/master/logo_neuromod.jpg "Logo on web page"

## Protocol

#### Images are randomly shown to subject in one of four quadrants on screen. Participants must memorize these images and their respective position. Later, are shown the same images along with novel ones and must remember if the image was seen earlier and if so, in which quadrant.

#### Project abstract: {https://github.com/mtl-brainhack-school-2019/memory_task_neuromod/blob/master/projectAbstract.md}

## Prerequisites
#### N.B: You need to have a dedicated graphic card (in most cases) to display the experimental monitor created by the script.

### Psychopy

#### Download and install Psychopy toolbox (select latest stable version).
{https://www.psychopy.org/download.html}
```python
s = pip install psychopy
```
### Download the following images in a common folder

#### Inanimate objects:
{https://drive.google.com/drive/folders/14V2LWbqvvw46JU7Hoz9A1rpeybQCltQ9?usp=sharing}

#### Non-human animals:
{https://drive.google.com/drive/folders/1VVQzqC8nGIS8GG4Jw_wklp7ZDvgXqLzT?usp=sharing}

#### Useful Spyder IDE to edit and run python files
```python
s = conda install -c anaconda spyder
s = spyder square_resize.py
```

## Next objectives

- [ ] Align instruction messages properly
- [ ] Display image to be remembered and instructions at the same time
- [ ] Set random inter-stimulus interval
- [ ] Implement fMRI & eye-tracker compatibility
- [ ] Implement participant identification & detailed event monitoring
