# 利用qt+cv2+摄像头实现实时的项目抓取
import cv2


class mycamera():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        print(self.cap)

    def open(self):

        # 默认设备编号为0，如果有外接摄像头则需要可以改为别的值
        #ret, frame = self.cap.read()
        while (True):
            if self.cap.isOpened() == False:
                print('can not open camera')

                break
            # Capture frame-by-frame
            ret, frame = self.cap.read()
           # print(ret,frame)
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('opencv', frame)
            # 按q可以退出
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()
        self.cap = cv2.VideoCapture(0)
    def close(self):
        # self.cap = cv2.VideoCapture(0)
        self.cap.release()
        cv2.destroyAllWindows()
        print(self.cap)
# open()
