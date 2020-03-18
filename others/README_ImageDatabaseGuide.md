# NeuroMod Natural Image Database
## Natural (real-life pictures) of inanimate and animate objects for scientific use
### Work under construction

## Description

#### The goal of creating this database it to provide the scientific community with an open-source, large natural image database meant for functional brain imaging. This database responds to an issue pointed out in the BOLD5000 paper (Chang et al., 2018). The human eye and its data reception and transmission system can form, transmit and analyse 10-12 images per second (Read & Meyer, 2000). This means several thousands images are perceived in a short amount of time. In computer vision, it is possible to achieve such high numbers of presented stimuli, but it has yet to be done while studying humans. In fact, the number of stimuli used in vision experiments is ten thousand times smaller with humans than with computers. This is why if we want AI to behave more like the human brain does, it is important to scale up the number of stimuli in human experiments to elaborate Deep Neural Networks (DNNs) closer to reality.

## Contents

## Inanimate Database

#### 'Inanimate' qualifies an object (organic, inonrganic, natural or human-made) that is unable to move at its own will or without the help of an animate being.
#### 5 760 inanimate images have been retained for experimentation (18 categories having 16 subcategories, each containing 20 images).

### Inanimate Database hierarchy (4 levels):

#### 1. Inanimate objects
#### 2. Category name
#### 3. Object/Subcategory name 
#### 4. Pictures (20 of each object listed in the inventory)

##### Link to inventory spreadsheet: 

https://docs.google.com/spreadsheets/d/1p411JQ-0d_Yvl9ZCXH_ecjJx-JrUJhvcL9rqoDZAWnw/edit?usp=sharing

![alt text][inventory_inanimate_example]

[inventory_inanimate_example]:https://github.com/FrancoisNadeau/ImageTask/blob/master/inventory_inanimate_example.jpg

## Non-human Animate Database

#### 'Animate' qualifies a being that is alive, sensitive and has capacity for spontaneous movement by itself.

### Non-human Animate Database hierarchy (5 levels)

#### 1. Non-human
#### 2. Category name
#### 3. Animal/Subcategory name
#### 4. Body, body parts or face (of the specified animal)
#### 5. Pictures

##### Link to non-human animals inventory spreadsheet:

https://docs.google.com/spreadsheets/d/1UjkGdKmNUstoQ2LJUbrKxZrJ5CIw-0aJw_9q-__gvbA/edit?usp=sharing


## Specifications

#### Labels from WordNet are used to start from a well established lexicon/database, but are organized in a different way. 

#### In the database, each subcategory only has 1 hypernym (corresponding to its main category name).The WordNet hierarchy, however, has more levels and any word can have a different amount of hypernyms.

##### Link to WordNet Web:

http://wordnetweb.princeton.edu/perl/webwn

## Next steps
- [x] Create user manual as markdown file (in progress)

- [ ] find category matches for THINGS & BOLD 5000 vs Image15K

- [ ] Validate synset choice for each image

- [ ] Justify category selection

- [ ] Balance animate (human & non-human) image categories

## References
#### Read, P., & Meyer, M.-P.(2000). Restauration of Motion Picture Films. Oxford, United Kingdom: Elsevier, 368p.
#### Chang, N. et al.(2019). BOLD5000, a public fMRI dataset while viewing 5000 visual images, https://doi.org/10.1038/s41597-019-0052-3


