from ultralytics import YOLO
import cv2
import utils
from flask import Flask, request, render_template, jsonify
import os
import mysql.connector

app = Flask(__name__)

# Set upload folder
UPLOAD_FOLDER = './static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Route for home page

@app.route('/')
def home():
    return render_template('upload.html')


# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            model = YOLO("D:\\project2\\number plate 1\\runs\\detect\\train5\\weights\\best.pt")
            # path = 'D:\\project2\\number plate 1\\testing_videos\\v1.mp4'

            path = f"./static/uploads/{file.filename}"  # path for the file upload


            cap = cv2.VideoCapture(path)

            # Check if the webcam opened successfully
            if not cap.isOpened():
                print("Error: Could not open webcam.")
                exit()

            while True:
                # Capture a frame from the webcam
                ret, frame = cap.read()
                if not ret:
                    print("Error: Could not read frame from webcam.")
                    break

                # Predict using YOLO model
                results = model.predict(source=frame, conf=0.5,
                                        show=True)  # show=True displays the frame with detections
                box = ''
                for result in results:
                    box = result.boxes.xyxy.tolist()
                if len(box) == 0:
                    pass
                else:
                    utils.crop(frame, box)
                    # utils.crop_and_filter(frame,box)

                # Press 'q' to exit the loop
                if cv2.waitKey(1) == ord('q'):
                    break

            # Release the webcam and close any OpenCV windows
            cap.release()
            cv2.destroyAllWindows()
            print(utils.numbers)
            # utils.numbers = {"AN01H0908", 'AN01H1689', 'AN01K9412'}
            print(utils.det_text)
            for i in utils.numbers:
                print(i)
            if len(utils.numbers) == 0:
                if utils.val_text == "valid":
                    return render_template("valid.html", number=utils.det_text)
                else:
                    return render_template("invalid.html", number=utils.det_text)
            else:

                mydb = mysql.connector.connect(host='localhost', user='root', passwd='1011',
                                               auth_plugin='mysql_native_password',
                                               database="license"
                                               )

                mycursor = mydb.cursor()

                mycursor.execute(
                    "select * from vehicle_registration v join driver_license d on v.license_plate=d.license_plate join violations vo on v.license_plate=vo.license_plate join emissions e on e.license_plate=v.license_plate join insurance i on i.license_plate=v.license_plate ")

                rows = mycursor.fetchall()

                for _ in rows:
                    all_list = [list(row) for row in rows]

                plates_data = []
                for number in utils.numbers:
                    for data_row in all_list:
                        if number == data_row[0]:
                            plates_data.append({
                                "license_plate": data_row[0],
                                "owner_name": data_row[1],
                                "date_reg": data_row[2],
                                "type_of_vehicle": data_row[3],
                                "license_no": data_row[4],
                                "dlname": data_row[5],
                                "add": data_row[6],
                                "vio_type": data_row[10],
                                "vio_date": data_row[11],
                                "amount": data_row[12],
                                "puc_expiry": data_row[15],
                                "policy_id": data_row[16],
                                "ins_exp": data_row[18],
                                "ins_comp": data_row[19],
                            })
                print(plates_data)

                print(plates_data)
                if len(plates_data) == 1:
                    return render_template("result.html", data=plates_data)
                else:
                    return render_template("video.html", data=plates_data)


if __name__ == '__main__':
    app.run(debug=True)
