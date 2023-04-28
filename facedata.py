'''
    人脸图像预处理
    目标:将人脸图像先从目标图像中框出来
    然后裁剪出来
    最后设置为统一的大小
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
   #face_detector = cv2.CascadeClassifier(
    #    "C:\\Users\\Administrator\\AppData\\Local\\Programs\\"
     #   "Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt_tree.xml")
# "D:\\anconda3\\envs\\face_recognition\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
    face_detector=cv2.CascadeClassifier("D:\\anconda3\\envs\\face_recognition\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
    # 3、检测人脸（用灰度图检测，返回人脸矩形坐标(4个角)）
    faces_rect = face_detector.detectMultiScale(gray, 1.05, 3)
    #                                          灰度图  图像尺寸缩小比例  至少检测次数（若为3，表示一个目标至少检测到3次才是真正目标）
    print("人脸矩形坐标faces_rect：", faces_rect)

    # 4、遍历每个人脸，画出矩形框
    dst = image.copy()
    for x, y, w, h in faces_rect:
        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 1)  # 画出矩形框
    #注意x轴和y轴可能是反过来的
    #[[ 38  55 135 135]]
    crop = image[y:y + h,x:x + w]
    #crop = dst[x:x + w,y:y + h]

    #图像进行一次压缩
    new_image=cv2.resize(crop,(128,128))
    # 显示
    cv2.imshow("kuang1", new_image)
    cv2.imshow("kuang2", dst)
    cv2.waitKey(0)
    new_name=imagepath.replace(".jpeg",".jpg")
    #print(new_name)
    cv2.imwrite(new_name,new_image)
    return dst


#使用
Face_Detect_Pic("./photo/luorun/89.jpg")