
import cv2


def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    # 这是核心算法
    return cv2.Laplacian(image, cv2.CV_64F).var()


imagePath="./photo/luorun/img/2.jpg"
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
text="ClEAR"#清晰的
print(fm)
# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
if fm < 100:
    text = "BLURRY"#模糊的

# show the image
cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.imshow("Image", image)
key = cv2.waitKey(0)

# 现在我的理解是先设置一个阈值，这个阈值可以通过已知的一个图片的计算出的值来进行规定
# CV2库为一个图像处理库