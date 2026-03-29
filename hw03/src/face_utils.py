import face_recognition
import numpy as np
import os

class FaceRecognition:
    """人脸检测与识别类"""
    def __init__(self, known_faces_dir="known_faces"):
        self.known_face_encodings = []
        self.known_face_names = []
        self.known_faces_dir = known_faces_dir
        self.load_known_faces()

    def load_known_faces(self):
        """加载已知人脸库中的图片并编码"""
        if not os.path.exists(self.known_faces_dir):
            os.makedirs(self.known_faces_dir)
            print(f"已创建目录 {self.known_faces_dir}，请将已知人脸图片放入该目录，并以人名命名（如 张三.jpg）")
            return

        for filename in os.listdir(self.known_faces_dir):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                name = os.path.splitext(filename)[0]
                image_path = os.path.join(self.known_faces_dir, filename)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)

                if len(encodings) > 0:
                    self.known_face_encodings.append(encodings[0])
                    self.known_face_names.append(name)
                else:
                    print(f"警告：{filename} 中未检测到人脸")

        print(f"已加载 {len(self.known_face_names)} 个人脸")

    def detect_faces(self, image):
        """检测图片中所有人脸，返回位置列表和编码列表"""
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        return face_locations, face_encodings

    def recognize_faces(self, face_encodings):
        """根据已知人脸库识别，返回识别结果列表"""
        names = []
        for face_encoding in face_encodings:
            if not self.known_face_encodings:
                names.append("未知")
                continue

            distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(distances)
            if distances[best_match_index] < 0.6:
                names.append(self.known_face_names[best_match_index])
            else:
                names.append("未知")
        return names
