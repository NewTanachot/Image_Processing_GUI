import numpy as np
import cv2

def sepia(src_image):

    gray = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
    normalized_gray = np.array(gray, np.float32)/255
    
    #solid color
    sepia = np.ones(src_image.shape)
    sepia[:,:,0] *= 153 #B
    sepia[:,:,1] *= 204 #G
    sepia[:,:,2] *= 255 #R

    #hadamard
    sepia[:,:,0] *= normalized_gray #B
    sepia[:,:,1] *= normalized_gray #G
    sepia[:,:,2] *= normalized_gray #R

    sepia_img = np.array(sepia, dtype=np.uint8)
   
    return sepia_img
  
image = cv2.imread('E:\Git-hab\Image_Processing_GUI\ohm1.jpg')

# Apply sepia effect to the image
sepia_image = sepia(image)

# Show the original image
cv2.imshow('Original', image)

# Show the sepia image
cv2.imshow('Sepia', sepia_image)

cv2.waitKey(0)
cv2.destroyAllWindows()