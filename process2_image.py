import cv2
import matplotlib.pyplot as plt
import numpy as np

image_name = 'pic1.png'   

img = cv2.imread(image_name)

if img is None:
    print("تصویر بارگذاری نشد. نام فایل را چک کنید!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # کرنل با وزن مرکزی ۵
    kernel5 = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]], dtype=np.float32)
    
    # کرنل با وزن مرکزی ۹
    kernel9 = np.array([[0, -1, 0],
                        [-1, 9, -1],
                        [0, -1, 0]], dtype=np.float32)
    
    sharpened5 = cv2.filter2D(gray, -1, kernel5)
    sharpened9 = cv2.filter2D(gray, -1, kernel9)
    
    # نمایش همه نتایج کنار هم
    plt.figure(figsize=(18, 10))
    plt.suptitle(f'تمرین ۲ - {image_name}', fontsize=16)
    
    plt.subplot(2, 4, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original RGB')
    plt.axis('off')
    
    plt.subplot(2, 4, 2)
    plt.imshow(gray, cmap='gray')
    plt.title('Grayscale')
    plt.axis('off')
    
    plt.subplot(2, 4, 3)
    plt.imshow(sharpened5, cmap='gray')
    plt.title('تیز شده (مرکز=۵)')
    plt.axis('off')
    
    plt.subplot(2, 4, 4)
    plt.imshow(sharpened9, cmap='gray')
    plt.title('تیز شده (مرکز=۹)')
    plt.axis('off')
    
    # هیستوگرام‌ها
    plt.subplot(2, 4, 5)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title('Histogram Grayscale')
    
    plt.subplot(2, 4, 6)
    plt.hist(sharpened5.ravel(), 256, [0, 256])
    plt.title('Histogram مرکز=۵')
    
    plt.subplot(2, 4, 7)
    plt.hist(sharpened9.ravel(), 256, [0, 256])
    plt.title('Histogram مرکز=۹')
    
    plt.tight_layout()
    plt.show()
    
    print(f" پردازش {image_name} انجام شد")
