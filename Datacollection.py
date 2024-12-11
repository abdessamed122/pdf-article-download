import bs4
from langchain.document_loaders import WebBaseLoader



# webpage extarct all text-----------------------------------------------------------
# Specify the URL
# url = "https://www.uaeu.ac.ae/en/cavm/doc/publication/ejfa/may2014.pdf#page=41"

# # Initialize the WebBaseLoader
# loader = WebBaseLoader(web_path=url)

# # Load the text asynchronously
# try:
#     documents = loader.load()
#     # Displaying the first 500 characters of the extracted text
#     extracted_text = "\n\n".join(doc.page_content for doc in documents)
#     print(extracted_text)  # Preview the first 500 characters
#     print("good ")
# except Exception as e:
#     print(f"An error occurred: {e}")
#     print("bad ")



# scholarly article ------------------------------------
# from scholarly import scholarly

# # Search for articles
# search_query = scholarly.search_pubs("algerian sahara")
# counter = 0  # تعريف العداد
# max_results = 20
# # Iterate through the results
# for result in search_query:
#     eprint_url = result.get('eprint_url')  # الحصول على eprint_url مباشرة
#     if eprint_url:  # إذا كانت موجودة
#         print(f"Title: {result['bib']['title']}")
#         print(f"eprint_url: {eprint_url}")
#         print("--" * 50)
#         counter += 1
#         if counter >= max_results:  # التوقف بعد الوصول إلى 20 نتيجة
#             break
    

# 777

# 1111111111111
# core.ac.uk article----------------------------------------
# import requests

# API_KEY = "BesL5yGuxoNYhwlQPvUKADSz7jnOc3dq"

# query = "react.js"  
# url = f"https://api.core.ac.uk/v3/search/works?apiKey={API_KEY}&q={query}"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     article_count = 0  
#     with open("output3.txt", "w", encoding="utf-8") as file:
#         for item in data['results']:
#             article_count += 1  # زيادة العداد
#             print("article_count:", article_count)
#             file.write(f"Title: {item['title']}\n")
#             file.write("-" * 50 + "\n")
#             file.write(f"Abstract: {item.get('abstract', 'No abstract available')}\n")
#             file.write("-" * 50 + "\n")
#             file.write(f"Full Text: {item.get('fullText', 'No full text available')}\n")
#             file.write("-" * 50 + "\n")
#             file.write(f"URL: {item.get('downloadUrl', 'No download URL available')}\n")
#             file.write("=" * 100 + "\n")
#     print("Data has been saved to 'output2.txt'")

# else:
#     print("Error:", response.status_code, response.text)


# 



# telcharge pdf article 
# import os
# import requests
# import time
# from scholarly import scholarly
# from PyPDF2 import PdfReader

# # إعدادات التحميل
# output_folder = "downloads"  # اسم المجلد للتنزيل
# os.makedirs(output_folder, exist_ok=True)  # إنشاء المجلد إذا لم يكن موجودًا

# # إعداد عداد النتائج
# counter = 0
# max_results = 10  # الحد الأقصى للنتائج
# keywords = ["JavaScript", "React.js"]  # الكلمات المفتاحية للتصفية

# # دالة للتحقق من صلاحية ملف PDF
# def is_valid_pdf(file_path):
#     try:
#         PdfReader(file_path)
#         return True
#     except:
#         return False

# # البحث عن المقالات
# search_query = scholarly.search_pubs("JavaScript React.js")

# # تنزيل الملفات
# for result in search_query:
#     # الحصول على البيانات الرئيسية
#     eprint_url = result.get('eprint_url')  # الحصول على رابط الملف
#     title = result.get('bib', {}).get('title', f"file_{counter + 1}")  # الحصول على عنوان المقال
#     abstract = result.get('bib', {}).get('abstract', "")  # ملخص المقال (قد لا يكون متوفرًا)

#     # تنظيف العنوان ليكون صالحًا كاسم ملف
#     valid_title = "".join(c if c.isalnum() or c in " _-" else "_" for c in title)
#     filename = os.path.join(output_folder, f"{valid_title}.pdf")  # استخدام العنوان كاسم الملف

#     # تصفية المقالات بناءً على الكلمات المفتاحية
#     if not any(keyword.lower() in (abstract.lower()) for keyword in keywords):
#         print(f"تم استبعاد المقال لأنه لا يحتوي على الكلمات المفتاحية: {title}")
#         continue

#     if eprint_url:
#         try:
#             # التحقق من الرابط قبل التنزيل
#             response = requests.head(eprint_url, timeout=10)
#             if response.status_code != 200:
#                 print(f"الرابط غير صالح أو محظور: {eprint_url}")
#                 continue

#             # تنزيل الملف
#             response = requests.get(eprint_url, stream=True, timeout=30)
#             response.raise_for_status()

#             # التحقق من نوع المحتوى
#             content_type = response.headers.get("Content-Type", "")
#             if "application/pdf" not in content_type:
#                 print(f"الرابط لا يشير إلى ملف PDF: {eprint_url}")
#                 continue

#             # حفظ الملف
#             with open(filename, "wb") as file:
#                 for chunk in response.iter_content(chunk_size=1024):
#                     file.write(chunk)

#             # تحقق من صلاحية الملف
#             if not is_valid_pdf(filename):
#                 print(f"الملف غير صالح كملف PDF وتم حذفه: {filename}")
#                 os.remove(filename)
#                 continue

#             print(f"تم تحميل الملف بنجاح: {filename}")
#             counter += 1

#             # التوقف بعد تحميل العدد المطلوب
#             if counter >= max_results:
#                 break

#             # تأخير بين الطلبات لتجنب الحظر
#             time.sleep(5)

#         except requests.exceptions.RequestException as e:
#             print(f"فشل تحميل الرابط: {eprint_url}, الخطأ: {e}")
# 999999999999999999999999999
import os
import requests
import time
from scholarly import scholarly
from PyPDF2 import PdfReader
from difflib import SequenceMatcher

# إعدادات التحميل
output_folder = "downloads_1"  # اسم المجلد للتنزيل
os.makedirs(output_folder, exist_ok=True)  # إنشاء المجلد إذا لم يكن موجودًا

# إعداد عداد النتائج
counter = 0
max_results = 20  # الحد الأقصى للنتائج
keywords = ["JavaScript", "React.js"]  # الكلمات المفتاحية للتصفية

# دالة للتحقق من صلاحية ملف PDF
def is_valid_pdf(file_path):
    try:
        PdfReader(file_path)
        return True
    except:
        return False

# دالة لتقييم التشابه بين النص والكلمات المفتاحية
def similarity_score(text, keywords):
    score = 0
    for keyword in keywords:
        score += SequenceMatcher(None, text.lower(), keyword.lower()).ratio()
    return score / len(keywords)

# البحث عن المقالات
search_query = scholarly.search_pubs("JavaScript React.js")

# تنزيل الملفات
for result in search_query:
    # الحصول على البيانات الرئيسية
    eprint_url = result.get('eprint_url')  # الحصول على رابط الملف
    title = result.get('bib', {}).get('title', f"file_{counter + 1}")  # الحصول على عنوان المقال
    abstract = result.get('bib', {}).get('abstract', "")  # ملخص المقال (قد لا يكون متوفرًا)

    # تنظيف العنوان ليكون صالحًا كاسم ملف
    valid_title = "".join(c if c.isalnum() or c in " _-" else "_" for c in title)
    filename = os.path.join(output_folder, f"{valid_title}.pdf")  # استخدام العنوان كاسم الملف

    # تصفية المقالات بناءً على درجة التشابه
    score = similarity_score(title + " " + abstract, keywords)
    if score < 0.5:  # الحد الأدنى للدرجة المقبولة
        print(f"تم استبعاد المقال بناءً على التشابه: {title}")
        continue

    if eprint_url:
        try:
            # التحقق من الرابط قبل التنزيل
            response = requests.head(eprint_url, timeout=10)
            if response.status_code != 200:
                print(f"الرابط غير صالح أو محظور: {eprint_url}")
                continue

            # تنزيل الملف
            response = requests.get(eprint_url, stream=True, timeout=30)
            response.raise_for_status()

            # التحقق من نوع المحتوى
            content_type = response.headers.get("Content-Type", "")
            if "application/pdf" not in content_type:
                print(f"الرابط لا يشير إلى ملف PDF: {eprint_url}")
                continue

            # حفظ الملف
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)

            # تحقق من صلاحية الملف
            if not is_valid_pdf(filename):
                print(f"الملف غير صالح كملف PDF وتم حذفه: {filename}")
                os.remove(filename)
                continue

            print(f"تم تحميل الملف بنجاح: {filename}")
            counter += 1

            # التوقف بعد تحميل العدد المطلوب
            if counter >= max_results:
                break

            # تأخير بين الطلبات لتجنب الحظر
            time.sleep(5)

        except requests.exceptions.RequestException as e:
            print(f"فشل تحميل الرابط: {eprint_url}, الخطأ: {e}")
