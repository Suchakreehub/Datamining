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
        self.geometry("840x720")

        self.configure(bg="white")

        # โหลดและปรับขนาดรูปภาพโลโก้
        logo_path = "C:/Users/lnwza/Downloads/Datamining/LogoF.png"
        logo_size = (200, 200)
        self.logo_image = self.load_and_resize_image(logo_path, logo_size)

        # แสดงรูปโลโก้ด้านบน
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.pack(pady=20)

        # โหลดและปรับขนาดรูปภาพของปุ่ม
        button_image_path = "C:/Users/lnwza/Downloads/Datamining/Start.png"
        button_image_size = (100, 40)
        self.button_image = self.load_and_resize_image(
            button_image_path, button_image_size
        )

        # สร้างปุ่ม "Start" ที่ตำแหน่งที่ถูกต้องบนรูป
        self.start_button = tk.Button(
            self,
            text="",
            command=self.open_next_page,
            bd=0,
            highlightthickness=0,
            image=self.button_image,
        )
        self.start_button.place(
            x=300, y=465, width=100, height=40
        )  # ปรับขนาดตามความต้องการ

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
        self.entry_gender = ttk.Combobox(
            self, values=self.gender_options, state="readonly"
        )
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
        self.entry_workout = ttk.Combobox(
            self, values=self.workout_options, state="readonly"
        )
        self.entry_workout.pack(pady=5)

        # ช่องกรอกสำหรับการสูบบุหรี่
        self.smoking_label = tk.Label(self, text="คุณสูบบุหรี่หรือไม่? (Yes / No):")
        self.smoking_label.pack(pady=5)
        self.smoking_options = ["Yes", "No"]
        self.entry_smoking = ttk.Combobox(
            self, values=self.smoking_options, state="readonly"
        )
        self.entry_smoking.pack(pady=5)

        self.random_label = tk.Label(self, text="กรุณาเลือกจำนวนการสุ่ม:")
        self.random_label.pack(pady=5)
        self.random_options = [i for i in range(1, 999)]  # 1 ถึง 999
        self.entry_random = ttk.Combobox(
            self, values=self.random_options, state="readonly"
        )
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
        chromosomes_1 = (gender, age, workout, smoking, per_heart_disease) 
        

        random_data_gene = random_population(gene) 
        random_data_gene.insert(0, chromosomes_1) 

        fawfa = display_min_fitness_chromosomes(random_data_gene) #เอาตัวchromosomeที่น้อยยสุดใส่ตัวแปร
        bwaba = single_point_crossover(fawfa) #เอาตัวลูกที่สับมาแล้วมาใส่ตัวแปร
        fmutant = mutant(bwaba)
        awaaw = calculate_fitness_after_crossover2(fmutant)

        
        print(f"asdasd: {awaaw[0]}, {awaaw[1]}")
        print(f"x: {fawfa[0],fawfa[1]}")  #แสดงค่าพ่อแม่ในterminal
        print(f"bwaba: {bwaba[0]}, {bwaba[1]}") #แสดงค่าลูกในterminal
        print(f"fmutant: {fmutant[0]}, {fmutant[1]}")

        # แสดงผลลัพธ์
        print(f"per_gen_age: {per_gen_age}")
        print(f"per_workout: {per_workout}")
        print(f"per_smoking: {per_smoking}")
        print(f"per_heart_disease: {per_heart_disease}")
        print("\n")
 
        # แสดงผลลัพธ์ใน ScrolledText widget
        result_message = (
            f"เพศ: {gender}\n"
            f"อายุ: {age}\n"
            f"เวลาออกกำลังกาย: {workout} นาที\n"
            f"การสูบบุหรี่: {smoking}\n"
            f"เปอร์เซ็นต์การเป็นโรคหัวใจ: {per_heart_disease}%\n"
            f"จำนวนที่สุ่มมา: \n"
            f""
            
        )
        # แสดงผลข้อมูลประชากรทั้งหมด
    #for i,generation in enumerate(, start=1):     
        for i, person in enumerate(random_data_gene, start=1):
            result_message += f"\nข้อมูลบุคคลที่ {i}:\n"
            result_message += f"เพศ: {person[0]}\nอายุ: {person[1]}\nเวลาออกกำลังกาย: {person[2]} นาที\nการสูบบุหรี่: {person[3]}\nเปอร์เซ็นต์การเป็นโรคหัวใจ: {person[4]}%\n"

        # แสดงผลว่า parent ที่ถูกเลือกคือตัวไหน
        for i, bestperson in enumerate(fawfa, start=1):
            result_message += f"\nparent {i}:\n"
            result_message += f"เพศ: {bestperson[0]}\nอายุ: {bestperson[1]}\nเวลาออกกำลังกาย: {bestperson[2]} นาที\nการสูบบุหรี่: {bestperson[3]}\nเปอร์เซ็นต์การเป็นโรคหัวใจ: {bestperson[4]}%\n"

        # แสดงผลลูกที่ผ่านการ crossover
        for i, crosschild in enumerate(bwaba, start=1):
            result_message += f"\nผล crossover ลูกคนที่ {i}:\n"
            result_message += f"เพศ: {crosschild[0]}\nอายุ: {crosschild[1]}\nเวลาออกกำลังกาย: {crosschild[2]} นาที\nการสูบบุหรี่: {crosschild[3]}\n"

        for i, mutantchild in enumerate(awaaw, start=1):
            result_message += f"\nผล mutant ลูกคนที่ {i}:\n"
            result_message += f"เพศ: {mutantchild[0]}\nอายุ: {mutantchild[1]}\nเวลาออกกำลังกาย: {mutantchild[2]} นาที\nการสูบบุหรี่: {mutantchild[3]}\nเปอร์เซ็นต์การเป็นโรคหัวใจ: {mutantchild[4]}%\n"

        
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
        return 0  # ถ้าไม่ตรงกับเงื่อนไขไหน ๆ ให้คืนค่าเป็น 0

    def percent_smoking(self, smoking):
        if smoking == "Yes":
            return 2
        elif smoking == "No":
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

def display_min_fitness_chromosomes(random_data_gene):
    #เลือกตัวพ่อแม่จากที่น้อยที่สุด
    x = []
    y = []
    # เก็บค่า Fitness ของทุก Chromosomes
    fitness_values = [chromosome[4] for chromosome in random_data_gene]
    # เรียงลำดับค่า Fitness จากน้อยไปมาก
    sorted_fitness = sorted(fitness_values)
    # เลือกค่า Fitness ต่ำสุด 2 ค่า
    min_fitness_values = sorted_fitness[:2]        
    for chromosome in random_data_gene:
        if chromosome[4] in min_fitness_values:
            if not x:
                x = chromosome
            elif not y:
                y = chromosome
            else:
                break    
    return x, y

def single_point_crossover(fawfa):
    #crossover
    preA = fawfa[0] #เอาchromosome พ่อแม่ที่หามาใส่ในตัวแปรก่อน
    preB = fawfa[1] #เอาchromosome พ่อแม่ที่หามาใส่ในตัวแปรก่อน
    A = preA[:4] #เอาตัวแปรchromosome พ่อแม่ มาตัดเปอร์เซ็นความเสี่ยงก่อนที่จะสลับเพื่อที่จะได้เอาไปคำนวณหาค่าความเสี่ยง(fitnessfunction)อันใหม่ได้
    B = preB[:4] #เอาตัวแปรchromosome พ่อแม่ มาตัดเปอร์เซ็นความเสี่ยงก่อนที่จะสลับเพื่อที่จะได้เอาไปคำนวณหาค่าความเสี่ยง(fitnessfunction)อันใหม่ได้
    X = 2 #ตำแหน่งที่ต้องการสลับ(สลับหลังจากตำแหน่งเลขของตัวแปรนี้) 
    A_new = np.append(A[:X], B[X:]) 
    B_new = np.append(B[:X], A[X:])    
    return A_new, B_new

def mutant(bwaba):
    # สร้าง list ใหม่เพื่อสลับค่าตำแหน่ง 1 และ 2
    fitness_A_new_swapped = list(bwaba[0])
    fitness_A_new_swapped[1], fitness_A_new_swapped[2] = fitness_A_new_swapped[2], fitness_A_new_swapped[1]

    fitness_B_new_swapped = list(bwaba[1])
    fitness_B_new_swapped[1], fitness_B_new_swapped[2] = fitness_B_new_swapped[2], fitness_B_new_swapped[1]
    return fitness_A_new_swapped,fitness_B_new_swapped 

def calculate_fitness_after_crossover(fmutant):
    
    gender = fmutant[0]
    age = int(fmutant[1])
    workout = int(fmutant[2])
    smoking = fmutant[3]

    per_gen_age_new = percent_age_gender(gender, age)
    per_workout_new = percent_workout(workout)
    per_smoking_new = percent_smoking(smoking, per_gen_age_new, per_workout_new)
    per_heart_disease_new = (per_gen_age_new + per_workout_new + per_smoking_new) 
    return per_heart_disease_new

def calculate_fitness_after_crossover2(fmutant):
    per_heart_disease_new_A = calculate_fitness_after_crossover(fmutant[0])
    per_heart_disease_new_B = calculate_fitness_after_crossover(fmutant[1])
    fmutant[0].append(per_heart_disease_new_A)
    fmutant[1].append(per_heart_disease_new_B)
    return fmutant[0],fmutant[1]



if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
