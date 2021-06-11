# Picludo
From Latin: Pictura & Secludo - Image & Hide
**Work in progress:**
### dependencies
- NumPy
- Pillow
### basic functionality 
Simple functions to encrypting images. Will include two main functions: \
**split_pic** use random NumPy array subtraction to make two separate images of random RGB noise. \
**join_pics** takes two noise images and recovers the original by simple addition. \
**random_key** noise map generator

### about
- takes all Pillow supported formats with limitations to RGB and 8bit's per channel
- works best on lossless bitmaps
- images cannot be recovered from one noise half 
