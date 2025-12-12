# پروژه مهندسی نرم‌افزار ۱ – To-Do App Backend
 
## توضیح درباره برنامه و هدف آن
این پروژه یک بک‌اند کامل برای یک برنامه مدیریت وظایف (To-Do List) است که تمام عملیات **CRUD** را فراهم می‌کند:

- **Create** – ایجاد وظیفه جدید با عنوان و توضیحات (اختیاری)
- **Read** – نمایش لیست تمام وظایف
- **Update** – ویرایش عنوان، توضیحات و تغییر وضعیت وظیفه
- **Delete** – حذف وظیفه

وضعیت هر وظیفه می‌تواند یکی از موارد زیر باشد:
- `pending` (در حال انجام)
- `done` (انجام‌شده)
- `canceled` (کنسل‌شده)

ویژگی‌های اضافی:
- ثبت زمان ایجاد، به‌روزرسانی و تکمیل وظیفه (به وقت ایران)
- ویرایش فقط در حالت «در حال انجام» امکان‌پذیر است
- فرانت‌اند ریسپانسیو با HTML/CSS/JavaScript
- استفاده از Git با برنچ‌های feature و Pull Request
- استقرار با Docker (Dockerfile + docker-compose.yml)



## پیش‌نیازها
- Python 3.11 یا بالاتر
- Git
- Docker Desktop (اختیاری – فقط برای اجرای کانتینری)
- فایل .env در ریشه پروژه

## نصب پکیج‌ها و اجرای برنامه (قدم به قدم)

### روش ۱ – اجرای محلی (توصیه‌شده)
```bash
# ۱. کلون کردن ریپازیتوری
git clone https://github.com/USERNAME/ToDoList.git
cd ToDoList

# ۲. ساخت محیط مجازی (اختیاری ولی توصیه می‌شود)
python -m venv venv
venv\Scripts\activate        # در ویندوز
# یا: source venv/bin/activate   در لینوکس/macOS

# ۳. نصب وابستگی‌ها
pip install -r requirements.txt

# ۴. اجرای برنامه
python app.py
نمونه کد فایل .env :
#FLASK_APP=<main file name ex: main.py or app.py>
#FLASK_ENV=development
#SECRET_KEY=<Long String >
#DATABASE_URL=sqlite:///<path of ur sql lite DataBase>