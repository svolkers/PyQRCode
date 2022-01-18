import cv2

print("StartingApplication.....................")
img = cv2.imread(r"C:\Users\cgsvolke\Downloads\QRCode\myqr.png")
img = cv2.imread(r"C:\Users\cgsvolke\Downloads\QRCode\myqr-official.png")
img = cv2.imread(r"C:\Users\cgsvolke\Downloads\QRCode\UKQRCode.png")

detector = cv2.QRCodeDetector()

data, bbox, straight_qrcode = detector.detectAndDecode(img)
print(data)
#print(bbox)
#print(straight_qrcode)
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    print(bbox)
    n_lines = len(bbox)
    #for i in range(n_lines):
    #    # draw all lines
    #    point1 = tuple(bbox[i][0])
    #    point2 = tuple(bbox[(i+1) % n_lines][0])
    #    cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

        # display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()