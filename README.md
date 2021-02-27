# Labeling Clusters Using TSNE and Flask

These steps convert a mp4 video into points that can be displayed on a website.

## Step 1
```python3 vid2imgs.py``` converts a mp4 file (game.mp4) to a set of jpg images and stores them in the imgs folder.

### Step 2
```python3 visualize.py``` takes the images from the imgs folder and flattens each (h, w, 3) image data into a h * w * 3 vector. This vector is fed into PCA into a much more manageable 50 dimensional vector before being fed into TSNE into a 2D vector. 
<br> The resultant data as well as the paths of the original image files are stored into ```data/filenames.txt``` and ```data/tsne.npy``` respectively. 
<br> <br> 
Note: ```visualize.py``` only uses a random subset of 600 images to keep computation low (this can be changed). 

### Step 3
Move the flask folder into the root of the web server and move the data folder and imgs folder into the flask folder. <br>
Execute ```flask run --host=0.0.0.0``` to create the server