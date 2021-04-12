

# Some very useful terminal commands for rendering a movie out of individual frames:

- Rename a bunch of files so that `ffmpeg` can get the correct order in the rendering:

```
rename 's/\d+/sprintf("%05d", $&)/e' *.png
```

- Generate a video from a sequence of image files:

```
ffmpeg -framerate 10 -pattern_type glob -i "smith_grid_%d.png" \
  -c:v libx264 -vb 20M out4.mp4
```

- Reverse a video:

```
ffmpeg -framerate 30 -pattern_type glob -i '*.png' -vf reverse \
  -c:v libx264 -vb 20M reversed.mp4
```



