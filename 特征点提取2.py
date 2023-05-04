import cv2
import dlib
# 读取图片
#img_path = "1.jpg"
img_path="./photo/luorun/img/2.jpg"
img = cv2.imread(img_path)
# 转换为灰阶图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 正向人脸检测器
detector = dlib.get_frontal_face_detector()
# 使用训练完成的68个特征点模型
predictor_path = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)
# 使用检测器来检测图像中的人脸
faces = detector(gray, 1)
for i, face in enumerate(faces):
    # 获取人脸特征点
    shape = predictor(img, face)
    # 遍历所有点
    for pt in shape.parts():
        # 绘制特征点
        pt_pos = (pt.x, pt.y)
        cv2.circle(img, pt_pos, 1, (255,0, 0), 2)
cv2.imshow('opencv_face_laowang',img)  # 显示图片
cv2.waitKey(0) # 等待用户关闭图片窗口
cv2.destroyAllWindows()# 关闭窗口
