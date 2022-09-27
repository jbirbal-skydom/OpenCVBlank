#conda create --name virtualenv python=3.9
#conda activate virtualenv
#pip install opencv-contrib-python


# # activate environment
# conda activate virtualenv

# # start python prompt
# python

# # import cv2 and print version
import cv2
print(cv2.__version__)

# # If OpenCV is installed correctly, the above command should output OpenCV version.



# open image
image = cv2.imread ("OpenCVBlank/Lessons/M2/Settings/datasets/caltech101/101_ObjectCategories/car_side/image_0035.jpg")
cv2.imshow("Image", image)
cv2.waitKey(0)


# # Exit and deactivate environment
# exit()
# conda deactivate

