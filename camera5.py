'''
人脸识别案例1：先尝试弄清楚级目标检测的联分类器，以及级联分类器如何使用
'''

import cv2


# 图片中人脸识别
def Face_Detect_Pic(imagepath):
    # 1、转灰度图
    image = cv2.imread(imagepath)
    print(imagepath)
    #print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #灰度图
    #cv2.imshow("gray", gray)

    # 2、训练一组人脸
    #haarcascade_frontalface_alt_tree.xml是opencv训练好的模型
    face_detector = cv2.CascadeClassifier(
        "C:\\Users\\Administrator\\AppData\\Local\\Programs\\"
        "Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt_tree.xml")

    # 3、检测人脸（用灰度图检测，返回人脸矩形坐标(4个角)）
    faces_rect = face_detector.detectMultiScale(gray, 1.05, 3)
    #                                          灰度图  图像尺寸缩小比例  至少检测次数（若为3，表示一个目标至少检测到3次才是真正目标）
    print("人脸矩形坐标faces_rect：", faces_rect)

    # 4、遍历每个人脸，画出矩形框
    dst = image.copy()
    for x, y, w, h in faces_rect:
        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 3)  # 画出矩形框

    #图像进行一次压缩
    new_image=cv2.resize(dst,(480,320))
    # 显示
    cv2.imshow("压缩后", new_image)
    return new_image

if __name__ == "__main__":
    # 读取图片
    #img = cv2.imread("./photo/duo.jpg")
    #cv2.imshow("img", img)

    Face_Detect_Pic("./photo/duo.jpg")  # 人脸识别（图片）
   # Face_Detect_Pic('C:/Users/Administrator/Pictures/miaomiao/1.jpg')  # 人脸识别（图片）

    cv2.waitKey(0)

