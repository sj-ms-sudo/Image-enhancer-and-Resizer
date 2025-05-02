import cv2 as cv
print("Press 1 for enhancing \n Press 2 for Reducing size") #choose to enhance or reduce
n = int(input())
if n==1:
    img = cv.imread('images/cat_low.jpg') #input file
    enhanced = cv.resize(img,(2048,1024),interpolation = cv.INTER_CUBIC) #to enhace
    cv.imshow("enhanced",enhanced)
    cv.waitKey(0)
elif n==2:
    img = cv.imread('images/cat_large.jpg')
    reduced = cv.resize(img,(500,500),interpolation = cv.INTER_AREA)
    cv.imshow("reduced",reduced)
    cv.waitKey(0)
cv.destroyAllWindows()
