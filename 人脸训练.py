import os
import numpy as np
import cv2


# 脸部检测函数
def face_detect_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(
        "D:\\anconda3\\envs\\face_recognition\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(gray, 1.2, 6)
    # 如果未检测到面部，则返回原始图像
    if (len(faces) == 0):
        return None, None
    # 目前假设只有一张脸，xy为左上角坐标，wh为矩形的宽高
    (x, y, w, h) = faces[0]
    print("face",len(faces))
    #这里我认为是维度问题导致的图像无法处理所以我将生成的图片做一次保存
    #按坐标裁剪图片
    crop = gray[int(x):int(x-w), int(y):int(y-h)]
    cv2.imwrite("./photo/1.jpg",crop)
    print(faces)
    # 返回图像的脸部部分
    return gray[y:y + w, x:x + h], faces[0]

'''
def ReFileName(dirPath):
    """
    :param dirPath: 文件夹路径
    :return:
    """
    # 对目录下的文件进行遍历
    faces = []
    for file in os.listdir(dirPath):
        # 判断是否是文件
        if os.path.isfile(os.path.join(dirPath, file)) == True:
            c = os.path.basename(file)
            name = dirPath + '/' + c
            #print(name)
            img = cv2.imread(name)
            #print(img)
            # 检测脸部
            face, rect = face_detect_demo(img)
            # 我们忽略未检测到的脸部
            if face is not None:
                # 将脸添加到脸部列表并添加相应的标签
                faces.append(face)
            else:
                print("存在未检测出的人脸", name)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces
'''
def ReFileName(dirPath):
    faces = []
    for file in os.listdir(dirPath):
        # 判断是否是文件
        if os.path.isfile(os.path.join(dirPath, file)) == True:
            c = os.path.basename(file)
            name = dirPath + '/' + c
            # print(name)
            img = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
            cv2.imshow("",img)
            cv2.waitKey(0)
            faces.append(img)
    return faces

# 杨幂照读取
dirPathyangmi = "./photo/yangmi"  # 文件路径
yangmi = ReFileName(dirPathyangmi)  # 调用函数

labelyangmi = np.array([0 for i in range(len(yangmi))])  # 标签处理
# 刘亦菲照读取
dirPathliuyifei = "./photo/liuyifei/img"  # 文件路径
liuyifei = ReFileName(dirPathliuyifei)  # 调用函数
#print("len", len(liuyifei))
labelliuyifei = np.array([1 for i in range(len(liuyifei))])  # 标签处理
#y1 = np.array(yangmi)

dirPathwl = "./photo/wl"  # 文件路径
wulei = ReFileName(dirPathwl)  # 调用函数
labelwl = np.array([2 for i in range(len(wulei))])  # 标签处理

dirPathyyqx = "./photo/yyqx"  # 文件路径
yyqx = ReFileName(dirPathyyqx)  # 调用函数
labelyyqx = np.array([3 for i in range(len(yyqx))])  # 标签处理

dirPathlr = "./photo/luorun"  # 文件路径
lr = ReFileName(dirPathlr)  # 调用函数
labellr = np.array([4 for i in range(len(lr))])  # 标签处理
x = np.concatenate((yangmi,liuyifei,wulei,yyqx,lr), axis=0)
y = np.concatenate((labelyangmi, labelliuyifei,labelwl,labelyyqx,labellr), axis=0)
print()
index = [i for i in range(len(y))]  # test_data为测试数据
np.random.seed(1)
np.random.shuffle(index)  # 打乱索引
train_data = x[index]
train_label = y[index]

# 分类器
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(train_data, train_label)
# 保存训练数据
recognizer.write('train.yml')
