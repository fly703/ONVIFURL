import cv2
from onvif import ONVIFCamera

# 定义摄像头的 IP 地址、用户名和密码
ip = '192.168.1.171'
port = 80  # 默认 ONVIF 端口
username = 'admin'
password = ''

# 初始化 ONVIFCamera
camera = ONVIFCamera(ip, port, username, password)

# 测试连接
try:
    print("Successfully connected to camera.")
except Exception as e:
    print(f"Failed to connect to camera: {e}")

# 获取设备信息
device_service = camera.create_devicemgmt_service()
device_info = device_service.GetDeviceInformation()

# 打印设备信息
print(f"Model: {device_info.Model}")
print(f"Manufacturer: {device_info.Manufacturer}")

# 获取媒体服务
media_service = camera.create_media_service()

# 获取监视配置
profiles = media_service.GetProfiles()

# 获取流的 RTSP URL
stream_uri = media_service.GetStreamUri({'StreamSetup': {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}}, 'ProfileToken': profiles[0].token})

# 打印 RTSP URL
print(f"RTSP Stream URI: {stream_uri.Uri}")
# # 使用 OpenCV 连接 RTSP 流
cap = cv2.VideoCapture(stream_uri.Uri)
if not cap.isOpened():
        print("Failed to open camera")
        exit()
else:
    print('Successfully open the camera')
ret, frame = cap.read()
print(ret, frame.shape)
cap.release()
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame.")
#         break

#     cv2.imshow("Camera Feed", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
