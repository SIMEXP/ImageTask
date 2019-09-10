# memory_task_neuromod
![alt text][logo_neuromod]
## An fMRI experiment on memory
[logo_neuromod]: https://raw.githubusercontent.com/mtl-brainhack-school-2019/memory_task_neuromod/master/logo_neuromod.jpg "Logo on web page"
### Getting in Context
#### A Brief Introduction to Cognitive Neuroscience: {https://drive.google.com/file/d/18pzaJ2LAO5HN4JsgCkx1rnSsju32KLrN/view?usp=sharing}
#### The aim of this code is to program an fMRI experiment very similar the CIMA-Q memory task with open tools.
#### Protocol: 15 images are randomly shown to subject in one of four quadrants on screen. 1 target image is shown twice. Subject must press a key when the repeated target image is displayed and indicate in which quadrant it previously appeared.
###### The experiment actually shows 12 unique images and a target instead of 14 unique and a target to prevent needing to download any more heavy image category folder.
##### See project abstract here: {https://github.com/mtl-brainhack-school-2019/memory_task_neuromod/blob/master/projectAbstract.md "projectAbstract"}


## Prerequisites
#### N.B: You need to have a dedicated graphic card (in most cases) to display the experimental monitor created by the script.

#### Download, extract (if compressed) and install Psychopy toolbox (select the latest stable version, which is 3.1.5 at the moment).
{https://www.psychopy.org/download.html}
```python
s = pip install psychopy
```
#### From the 'Inanimate' directory on this Drive, download and extract the clothing, food and furniture folders.
{https://drive.google.com/drive/folders/1FbHI3wNBzHRyp8FSZ6wLiyWRXulq-mV9?usp=sharing}
#### Make sure these folders are in your current working directory alongside the python file
##### You can use the shutil module to easily navigate through directories (similar to how the Unix Shell commands work)
```python
s = import shutil
s = shutil.move(files,destination) #works just like the Unix Shell mv command
```
## Image stimuli preprocessing
### To make sure all images in a given category (i.e. 'clothing') are formatted appropriately, execute the 'square_resize.py' function on the previously extracted folders in your terminal or IDE.
##### Here's a link to individually download 'square_resize.py' from the GitHub repository:
{https://github.com/mtl-brainhack-school-2019/memory_task_neuromod/blob/master/square_resize.py "Link to function script"}
```python
s = square_resize('categoryNameHere')
```
#### I use the Spyder IDE to edit and run python files.
```python
s = conda install -c anaconda spyder 
s = spyder square_resize.py
```
##### In Spyder, click the run button to launch the experiment demo.

## Next objectives
- [x] Create a class (image matrix) containing all images in their respective subcategories and categories to access them all.
- [x] Initiate a stimuli selection function to ensure proper randomization without replacement across each subcategory and categories.
- [x] Create a class containing all images that will be repeated after each trial
- [] Create a noisy image stimulus (distractor) showing up at random moments to avoid habituation phenomenon in subjects brain activity.
- [] IN PROGRESS: missing noisy image - Randomize the presentation of either target, image distractor or noisy distractor across trials.
- [] IN PROGRESS: Adapt the demo code to the main experimental code
- [] Continue compiling creative commons complex images
