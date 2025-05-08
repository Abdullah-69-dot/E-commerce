# Django E-commerce

مشروع تجارة إلكترونية مبني بإطار عمل Django.

## المتطلبات
- Python 3.8 أو أحدث
- Django (يفضل استخدام requirements.txt)

## خطوات التشغيل
1. أنشئ بيئة افتراضية:
   ```bash
   python -m venv venv
   ```
2. فعّل البيئة الافتراضية:
   - على Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - على macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. ثبت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```
4. شغل السيرفر:
   ```bash
   python manage.py runserver
   ```

## ملاحظات
- تأكد من عدم رفع ملفات البيئة الافتراضية أو الملفات الحساسة إلى GitHub.
- عدّل الإعدادات حسب الحاجة في settings.py.
