import cv2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def pmath(path):
    text = pytesseract.image_to_string(Image.open(path))
    s1=''
    s2=''
    op=''
    for element in range(0,len(text)):
        if op=='' and text[element]!=' ' and (text[element]>='1' and text[element]<='9'):
            s1+=text[element]
        elif op!='' and text[element]!='':
            s2+=text[element]
        elif op=='' and text[element]!=' ':
            op+=text[element]
    print(text)
    if op=='+': print(int(s1)+int(s2))	
    elif op=='-': print(int(s1)-int(s2)) 
    elif op=='*' or op=='x': print(int(s1)*int(s2))
    elif op=='/': print(int(s1)/int(s2))
    else : print('nothing to do with!')

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        pmath(img_name)
        img_counter += 1


cam.release()
cv2.destroyAllWindows()
