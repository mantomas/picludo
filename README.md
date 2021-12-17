# Picludo
From Latin: Pictura & Secludo - Image & Hide \
**Work in progress**
### dependencies
- NumPy
- Pillow
### basic functionality 
One class **Picludo** with methods to encrypting and decrypting images. It includes two main methods and one helper function to generate random noise: \
**split_pic()** use random NumPy array subtraction to make two separate images of random RGB noise. \
**join_pics()** takes two noise images and recovers the original by simple addition. \
**random_key()** noise map generator \

### about
- takes all Pillow supported formats with limitations to RGB and 8bit's per channel
- works best on lossless bitmaps
- images cannot be recovered from one noise half 

### split_pic()
`split_pic("original.bmp")`

![split_pic.bmp](/img/split_pic.bmp)

### join_pics()
`join_pics("out_B.bmp", "out_A.bmp", "recovered_original.jpg")`

![join_pics.bmp](/img/join_pics.bmp)

### Sample usage
```python
from picludo import Picludo

# can be used by creating instance of Picludo class
factory = Picludo()
factory.split_pic("original.bmp")

# or directly
Picludo.split_pic("original.bmp")
# two new image files 'out_A.bmp' and 'out_B.bmp' are created


# joins (restores original) first two files into 'recovered.bmp' image
factory.join_pics("out_A.bmp", "out_B.bmp", "recovered.bmp")
# or also directly
Picludo.join_pics("out_A.bmp", "out_B.bmp", "recovered.bmp")
```

### to do
- handling exceptions 
- OS module use to check file paths
- split multiple images with one *random_key*
- use smaller or bigger key (pattern)
- use your own key or image 
