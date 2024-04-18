# Official Data Release of Sci-PosterLayout: A New Benchmark and Approach Towards Scientific Poster Layout Generation

## Introduction

{Add introduction here}

## Download

Clone this repository and obtain the `./data` folder


## Structure

Following are the files in the `./data` folder and their explanation of usage.

`poster_panel_position.npy`: A 1232 x 10 x 5 numpy bin file contains layouts of the posters. 1232: Total number of the posters, 10: Maximum of the panels in one poster. 5: Category, x, y, w, h of each panel.

`poster_id_list.txt`: Poster ID list in the order of `poster_panel_position.npy`.

`train_poster_id.txt` Poster IDs of the training set.

`test_poster_id` Poster IDs of the testing set.

`val_poster_id.txt` Poster IDs of the validation set.

`poster_meta` Meta data of the posters. Contains the text length, text ratio, figure count, figure ratio of each panel formed in JSON and named after the poster ID.

## Useful Scripts

### Convert to C-X1-Y1-W-H format

The poster layout in `poster_panel_position.npy` is in the format of C-XC-YC-W-H, if you want to convert to C-X1-Y1-W-H, run the `src\convert_to_x1y1wh.py`.

Usage: `python convert_to_x1y1wh.py \<npy_to_convert.npy> \<result.npy>`

Example: `python convert_to_x1y1wh.py poster_panel_position.npy poster_panel_position_x1y1wh.npy`

### Visualize the layouts

See [src\visualization.ipynb](src\visualization.ipynb)

![Visualization](asset\visualization.png)