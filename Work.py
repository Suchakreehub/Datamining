from PIL import Image, ImageTk
import tkinter as tk
import random
import numpy as np
from tkinter import scrolledtext
from tkinter import ttk

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Main Page")

        # กำหนดขนาดของหน้าต่าง
        # กำหนดขนาดของหน้าต่าง
        # กำหนดขนาดของหน้าต่าง
        # กำหนดขนาดของหน้าต่าง
        # กำหนดขนาดของหน้าต่าง
        # กำหนดขนาดของหน้าต่าง
        # กำหนดขนาดของหน้าต่าง
        # กำหนดขนาดของหน้าต่าง
        # กำหนดขนาดของหน้าต่าง
        # กำหนดขนาดของหน้าต่าง
        self.geometry("840x720")

        self.configure(bg="white")

        # โหลดและปรับขนาดรูปภาพโลโก้
        logo_path = "C:/Users/usEr/Desktop/New folder/LogoF.png"
        logo_size = (200, 200)
        self.logo_image = self.load_and_resize_image(logo_path, logo_size)

        # แสดงรูปโลโก้ด้านบน
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.pack(pady=20)

        # โหลดและปรับขนาดรูปภาพของปุ่ม
        button_image_path = "C:/Users/usEr/Desktop/New folder/Start.png"
        button_image_size = (100, 40)
        self.button_image = self.load_and_resize_image(button_image_path, button_image_size)

        # สร้างปุ่ม "Start" ที่ตำแหน่งที่ถูกต้องบนรูป
        self.start_button = tk.Button(self, text="", command=self.open_next_page, bd=0, highlightthickness=0, image=self.button_image)
        self.start_button.place(x=300, y=465, width=100, height=40)  # ปรับขนาดตามความต้องการ

    def load_and_resize_image(self, path, size):
        original_image = Image.open(path)
        resized_image = original_image.resize(size, Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(resized_image)
        return tk_image

    def open_next_page(self):
        # เรียกใช้หน้าต่างถัดไป
        self.destroy()  # ทำลายหน้าต่างปัจจุบัน
        next_page = NextPage()
        next_page.mainloop()

##ส่วนหน้า 2
        
class NextPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("หน้าถัดไป")
        self.geometry("840x720")

        label = tk.Label(self, text="นี่คือหน้าถัดไป")
        label.pack(pady=10)

        # ช่องกรอกสำหรับเพศ
        self.gender_label = tk.Label(self, text="คุณเป็นเพศอะไร? (Male / Female):")
        self.gender_label.pack(pady=5)
        self.gender_options = ["Male", "Female"]
        self.entry_gender = ttk.Combobox(self, values=self.gender_options, state="readonly")
        self.entry_gender.pack(pady=5)

        # Combobox สำหรับเลือกอายุ
        self.age_label = tk.Label(self, text="กรุณาเลือกอายุของคุณ:")
        self.age_label.pack(pady=5)
        self.age_options = [i for i in range(1, 101)]  # 1 ถึง 100 ปี
        self.entry_age = ttk.Combobox(self, values=self.age_options, state="readonly")
        self.entry_age.pack(pady=5)

        # ช่องกรอกสำหรับเวลาออกกำลังกาย
        self.workout_label = tk.Label(self, text="กรุณาเลือกเวลาออกกำลังกาย (นาที):")
        self.workout_label.pack(pady=5)
        self.workout_options = [i for i in range(1, 121)]  # 1 ถึง 120 นาที
        self.entry_workout = ttk.Combobox(self, values=self.workout_options, state="readonly")
        self.entry_workout.pack(pady=5)

        # ช่องกรอกสำหรับการสูบบุหรี่
        self.smoking_label = tk.Label(self, text="คุณสูบบุหรี่หรือไม่? (Yes / No):")
        self.smoking_label.pack(pady=5)
        self.smoking_options = ["Yes", "No"]
        self.entry_smoking = ttk.Combobox(self, values=self.smoking_options, state="readonly")
        self.entry_smoking.pack(pady=5)

        self.random_label = tk.Label(self, text="กรุณาเลือกจำนวนการสุ่ม:")
        self.random_label.pack(pady=5)
        self.random_options = [i for i in range(1, 999)]  # 1 ถึง 999 
        self.entry_random = ttk.Combobox(self, values=self.random_options, state="readonly")
        self.entry_random.pack(pady=5)

        # ปุ่มเพื่อแสดงผลลัพธ์
        input_button = tk.Button(self, text="แสดงผลลัพธ์", command=self.display_results)
        input_button.pack(pady=10)

        # ScrolledText widget สำหรับแสดงผลลัพธ์
        self.result_text = scrolledtext.ScrolledText(self, height=10, width=50)
        self.result_text.pack(pady=10)

    def display_results(self):
    # รับค่าจากช่องกรอก
     gender = self.entry_gender.get()
     age = int(self.entry_age.get())
     workout = int(self.entry_workout.get())
     smoking = self.entry_smoking.get()
     gene = int(self.entry_random.get())
     

    # คำนวณเปอร์เซ็นต์
     per_gen_age = self.percent_age_gender(gender, age)
     per_workout = self.percent_workout(workout)
     per_smoking = self.percent_smoking(smoking)
     per_heart_disease = self.percent_heart_disease(per_gen_age, per_workout, per_smoking)
     random_data_gene = random_population(gene)

     print(f"per_gen_age: {per_gen_age}")
     print(f"per_workout: {per_workout}")
     print(f"per_smoking: {per_smoking}")
     print(f"per_heart_disease: {per_heart_disease}")
     print(f"per_heart_disease: {random_data_gene}")
     print("\n")

    # ค้นหาเปอร์เซ็นต์ที่ต่ำที่สุดและข้อมูลที่เกี่ยวข้อง
     min_percentage = float('inf')  # กำหนดค่าเริ่มต้นเป็น Infinity
     min_percentage_data = None

     for i, person in enumerate(random_data_gene, start=1):
        if person[4] < min_percentage:
            min_percentage = person[4]
            min_percentage_data = person

    # แสดงผลลัพธ์ใน ScrolledText widget
     result_message = (
        f"เพศ: {gender}\n"
        f"อายุ: {age}\n"
        f"เวลาออกกำลังกาย: {workout} นาที\n"
        f"การสูบบุหรี่: {smoking}\n"
        f"เปอร์เซ็นต์การเป็นโรคหัวใจ: {per_heart_disease}%\n"
        f"จำนวนที่สุ่มมา: \n"  
    )
     for i, person in enumerate(random_data_gene, start=1):
        result_message += f"\nข้อมูลบุคคลที่ {i}:\n"
        result_message += f"เพศ: {person[0]}\nอายุ: {person[1]}\nเวลาออกกำลังกาย: {person[2]} นาที\nการสูบบุหรี่: {person[3]}\nเปอร์เซ็นต์การเป็นโรคหัวใจ: {person[4]}%\n"

     result_message += f"\n\nผลลัพธ์ที่มีเปอร์เซ็นต์ต่ำที่สุด:\n"
     result_message += f"เพศ: {min_percentage_data[0]}\nอายุ: {min_percentage_data[1]}\n"
     result_message += f"เวลาออกกำลังกาย: {min_percentage_data[2]} นาที\n"
     result_message += f"การสูบบุหรี่: {min_percentage_data[3]}\n"
     result_message += f"เปอร์เซ็นต์การเป็นโรคหัวใจ: {min_percentage_data[4]}%\n"

     self.result_text.delete(1.0, tk.END)  # ล้างเนื้อหาก่อนหน้า
     self.result_text.insert(tk.END, result_message)

    def percent_age_gender(self, gender, age):
     if gender == "Male":
        if age > 0 and age <= 39:
            return 0.03
        elif age >= 40 and age <= 59:
            return 0.1
        elif age >= 60:
            return 0.2
     elif gender == "Female":
        if age > 0 and age <= 39:
            return 0.02
        elif age >= 40 and age <= 59:
            return 0.08
        elif age >= 60:
            return 0.15
     return 0  # ถ้าไม่ตรงกับเงื่อนไขไหน ๆ ให้คืนค่าเป็น 0

    def percent_workout(self, workout):
        if workout < 30:
            return 0.15
        elif workout >= 30 and workout <= 60:
            return 0.1
        elif workout > 60:
            return 0.05
        return 0 # ถ้าไม่ตรงกับเงื่อนไขไหน ๆ ให้คืนค่าเป็น 0

    def percent_smoking(self, smoking):
        if(smoking == "Yes"):
         return 2
        elif(smoking == "No"):
         return 0.05

    def percent_heart_disease(self, per_gen_age, per_workout, per_smoking):
     print(f"per_gen_age: {per_gen_age}")
     print(f"per_workout: {per_workout}")
     print(f"per_smoking: {per_smoking}")

     if per_smoking == 2:  # ถ้าการสูบบุหรี่เป็น "Yes"
      result = int(((per_gen_age + per_workout + 0.05) * 100) * per_smoking)
      print(f"result (smoking): {result}")
      return result
     elif per_smoking == 0.05:  # ถ้าการสูบบุหรี่เป็น "No"
        result = int((per_gen_age + per_workout + per_smoking) * 100)
        print(f"result (no smoking): {result}")
        return result
     else:
        print("result (default)")
        return 0
     
def random_population(gene):
    data_gene = []
    for _ in range(gene):
        gender = random.choice(["Male", "Female"])
        age = random.randint(1, 100)
        workout = random.randint(0, 180)
        smoking = random.choice(["yes", "no"])

        per_gen_age = percent_age_gender(gender, age)
        per_workout = percent_workout(workout)
        per_heart_disease = percent_smoking(smoking, per_gen_age, per_workout)

        data_gene.append((gender, age, workout, smoking, per_heart_disease))
    return data_gene

def percent_age_gender(gender, age):
    if gender == "Male":
        if age > 0 and age <= 39:
            return 0.03
        elif age >= 40 and age <= 59:
            return 0.1
        elif age >= 60:
            return 0.2
    elif gender == "Female":
        if age > 0 and age <= 39:
            return 0.02
        elif age >= 40 and age <= 59:
            return 0.08
        elif age >= 60:
            return 0.15

def percent_workout(workout):
    if workout < 30:
        return 0.15
    elif workout >= 30 and workout <= 60:
        return 0.1
    elif workout > 60:
        return 0.05

def percent_smoking(smoking, per_gen_age, per_workout):
    if smoking.lower() == "yes":
        return int(((per_gen_age + per_workout + 0.05) * 100) * 2)
    elif smoking.lower() == "no":
        return int((per_gen_age + per_workout + 0.05) * 100)

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
