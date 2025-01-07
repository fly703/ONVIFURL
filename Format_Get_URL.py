import cv2

camera_ip = '128.64.20.21'  # 摄像头IP地址
port = 554                   # 摄像头端口号
username = 'admin'          # 登录用户名
password = 'Admin123'       # 登录密码
def Hikvision_Get_URL(ip_address, username, password,cameara_port):
    '''
    应用于海康威视摄像机的URL获取函数
    '''
    url = f"rtsp://{username}:{password}@{ip_address}:{cameara_port}/Streaming/Channels/101"

    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("Failed to open camera")
        exit()
    
    print('Hik_Videos_URL:',url)
    cap.release()

def Dahua_Get_URL(ip_address, username, password,cameara_port):
    '''
    应用于大华摄像机的URL获取函数
    '''
    url = f"rtsp://{username}:{password}@{ip_address}:{cameara_port}/cam/realmonitor?channel=1&subtype=0"

    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("Failed to open camera")
        exit()
    
    print('Dahua_Videos_URL:',url)
    cap.release()

def main():
    # 测试海康威视摄像机
    Hikvision_Get_URL(camera_ip, username, password,port)

    # 测试大华摄像机
    # Dahua_Get_URL(camera_ip, username, password,port)

if __name__ == '__main__':
    main()