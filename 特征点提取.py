import cv2
import dlib
# 读取图片
img_path = "1.jpg"
img = cv2.imread(img_path)
# 转换为灰阶图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 正向人脸检测器将图像
detector = dlib.get_frontal_face_detector()
# 使用训练好的5个特征点模型
predictor_path = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)
# 使用检测器来检测图像中的人脸
faces = detector(gray, 1)

# 生成 Dlib 的图像窗口
win = dlib.image_window()
win.set_image(img)
# 打印结果
print("人脸数: ", len(faces))
for i, face in enumerate(faces):
    print("第", i+1, "个人脸的矩形框坐标：\n","left:", face.left(), "right:", face.right(), "top:", face.top(), "bottom:", face.bottom())
    # 获取人脸特征点
    shape = predictor(img, face)
    print("第", i+1, '个人脸特征点:')
    print(shape.parts())
    win.add_overlay(shape)

win.add_overlay(faces)
dlib.hit_enter_to_continue()