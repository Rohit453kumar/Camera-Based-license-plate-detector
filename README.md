This project is an AI-powered License Plate Detection System using YOLOv8 for plate detection and Tesseract OCR for character recognition. The system processes images or videos, extracts license plate numbers, and verifies them against a MySQL database to retrieve vehicle details. It is designed for traffic monitoring, toll collection, parking management, and law enforcement.

Features
✅ Automatic License Plate Detection using YOLOv8
✅ OCR-based Character Recognition using Tesseract
✅ Real-time Video Processing for continuous surveillance
✅ Vehicle Verification via MySQL database integration
✅ Web-based Interface using Flask for easy file uploads
✅ Role-based Access Control for secure data management

Technologies Used
Python
YOLOv8 (Ultralytics)
OpenCV
Tesseract OCR
Flask (Web Framework)
MySQL (Database Management)
HTML, CSS, JavaScript (Frontend UI)
Installation Instructions
1️⃣ Setup Environment
Ensure you have Python 3.7+ installed. Then, install the required dependencies:

bash
Copy
Edit
pip install ultralytics opencv-python flask mysql-connector-python pytesseract
2️⃣ Download YOLO Model
Place the trained YOLO model (best.pt) in your project directory.

3️⃣ Run the Flask App
bash
Copy
Edit
python main.py
Access the web interface at: http://127.0.0.1:5000/

Future Enhancements 🚀
🔹 AI-powered OCR models for higher accuracy
🔹 Integration with government traffic databases
🔹 Mobile app for on-the-go license plate verification
🔹 Cloud-based deployment for scalability
🔹 IoT-based real-time surveillance and fraud detection

Contributors
👤 Rohit kumar,Abhishek c margoor,J jaswasnt Reddy,Sandesh Shridhar Hegde, Harshit Raj

