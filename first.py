# ===============================
# شرح مفصل للقوائم (Lists) والداينمك ميثود في بايثون
# ===============================

# ========== الجزء 1: تعريف القوائم والوصول للعناصر ==========

# تعريف قائمة فارغة
empty_list = []                       # قائمة بدون أي عناصر
print(f"قائمة فارغة: {empty_list}")

# تعريف قائمة بأرقام
numbers = [1, 2, 3, 4, 5]            # قائمة تحتوي على أرقام
print(f"قائمة أرقام: {numbers}")

# تعريف قائمة بنصوص
fruits = ["تفاح", "موز", "برتقال"]    # قائمة تحتوي على نصوص
print(f"قائمة فواكه: {fruits}")

# تعريف قائمة مختلطة
mixed_list = [1, "تفاح", 3.14, True]  # قائمة يمكن أن تحتوي على أنواع مختلفة
print(f"قائمة مختلطة: {mixed_list}")

# الوصول للعناصر باستخدام الفهرس (Index)
print(f"العنصر الأول: {fruits[0]}")   # الفهرس 0 يعني أول عنصر
print(f"العنصر الثاني: {fruits[1]}")  # الفهرس 1 يعني ثاني عنصر
print(f"العنصر الأخير: {fruits[-1]}") # الفهرس -1 يعني آخر عنصر

# ========== الجزء 2: ميثود إضافة العناصر ==========

# append() - إضافة عنصر في نهاية القائمة
fruits.append("فراولة")               # إضافة "فراولة" لنهاية القائمة
print(f"بعد append: {fruits}")

# insert() - إضافة عنصر في موضع محدد
fruits.insert(1, "عنب")               # إضافة "عنب" في الموضع رقم 1
print(f"بعد insert: {fruits}")

# extend() - دمج قائمة بأخرى
more_fruits = ["مانجو", "أناناس"]     # قائمة جديدة
fruits.extend(more_fruits)            # دمج القائمتين
print(f"بعد extend: {fruits}")

# ========== الجزء 3: ميثود إزالة العناصر ==========

# remove() - إزالة أول occurrence لعنصر محدد
fruits.remove("موز")                  # إزالة أول ظهور لكلمة "موز"
print(f"بعد remove: {fruits}")

# pop() - إزالة عنصر من موضع محدد وإرجاع قيمته
removed_fruit = fruits.pop(2)         # إزالة العنصر في الفهرس 2
print(f"العنصر المُزال: {removed_fruit}")
print(f"بعد pop: {fruits}")

# pop() بدون index - يزيل آخر عنصر
last_fruit = fruits.pop()             # إزالة آخر عنصر
print(f"آخر عنصر مُزال: {last_fruit}")
print(f"بعد pop أخير: {fruits}")

# clear() - إفراغ القائمة بالكامل
temp_list = [1, 2, 3]                # قائمة مؤقتة
temp_list.clear()                     # إفراغ القائمة
print(f"بعد clear: {temp_list}")

# ========== الجزء 4: ميثود البحث والترتيب ==========

# index() - إيجاد index أول ظهور لعنصر
fruits_index = fruits.index("عنب")    # البحث عن index كلمة "عنب"
print(f"index العنب: {fruits_index}")

# count() - عد عدد مرات ظهور عنصر
numbers_list = [1, 2, 2, 3, 2, 4]    # قائمة بأرقام متكررة
twos_count = numbers_list.count(2)    # عدد مرات ظهور الرقم 2
print(f"عدد مرات ظهور 2: {twos_count}")

# sort() - ترتيب القائمة تصاعدياً
numbers_to_sort = [3, 1, 4, 1, 5, 9, 2]
numbers_to_sort.sort()                # ترتيب القائمة
print(f"بعد sort تصاعدي: {numbers_to_sort}")

# sort() تنازلياً
numbers_to_sort.sort(reverse=True)    # ترتيب القائمة تنازلياً
print(f"بعد sort تنازلي: {numbers_to_sort}")

# reverse() - عكس ترتيب القائمة
fruits.reverse()                      # عكس ترتيب العناصر
print(f"بعد reverse: {fruits}")

# ========== الجزء 5: ميثود النسخ والإنشاء ==========

# copy() - إنشاء نسخة من القائمة
original = [1, 2, 3]                 # القائمة الأصلية
copied = original.copy()              # نسخ القائمة
copied.append(4)                      # إضافة عنصر للنسخة فقط
print(f"الأصل: {original}")           # الأصل لم يتغير
print(f"النسخة: {copied}")            # النسخة تحتوي على التغيير

# ========== الجزء 6: العمليات على القوائم ==========

# len() - معرفة طول القائمة
list_length = len(fruits)             # عدد العناصر في القائمة
print(f"طول القائمة: {list_length}")

# in - التحقق من وجود عنصر
has_apple = "تفاح" in fruits          # التحقق إذا كان "تفاح" موجود في القائمة
print(f"هل التفاح موجود؟ {has_apple}")

# + - دمج قائمتين
list1 = [1, 2, 3]                     # القائمة الأولى
list2 = [4, 5, 6]                     # القائمة الثانية
combined = list1 + list2              # دمج القائمتين
print(f"بعد الدمج: {combined}")

# * - تكرار القائمة
repeated = list1 * 3                  # تكرار القائمة 3 مرات
print(f"بعد التكرار: {repeated}")

# ========== الجزء 7: التقطيع (Slicing) ==========

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # قائمة طويلة

# [start:end] - من start إلى end-1
slice1 = numbers[2:6]                 # من الفهرس 2 إلى 5
print(f"من 2 إلى 5: {slice1}")

# [start:] - من start إلى النهاية
slice2 = numbers[5:]                  # من الفهرس 5 إلى النهاية
print(f"من 5 إلى النهاية: {slice2}")

# [:end] - من البداية إلى end-1
slice3 = numbers[:4]                  # من البداية إلى الفهرس 3
print(f"من البداية إلى 3: {slice3}")

# [start:end:step] - مع خطوة
slice4 = numbers[1:8:2]               # من 1 إلى 7 بخطوة 2
print(f"من 1 إلى 7 بخطوة 2: {slice4}")

# [::-1] - عكس القائمة
reversed_numbers = numbers[::-1]      # عكس القائمة كاملة
print(f"القائمة المعكوسة: {reversed_numbers}")

# ========== الجزء 8: List Comprehension ==========

# إنشاء قائمة جديدة من قائمة موجودة
squares = [x**2 for x in numbers]     # مربع كل عدد في القائمة
print(f"مربعات الأعداد: {squares}")

# List comprehension مع شرط
even_squares = [x**2 for x in numbers if x % 2 == 0]  # مربعات الأعداد الزوجية فقط
print(f"مربعات الأعداد الزوجية: {even_squares}")

# تحويل قائمة نصية
upper_fruits = [fruit.upper() for fruit in fruits]  # تحويل كل فاكهة لحروف كبيرة
print(f"الفواكه بحروف كبيرة: {upper_fruits}")

# ========== الجزء 9: أمثلة عملية شاملة ==========

def list_operations_demo():
    """عرض شامل لعمليات القوائم"""
    
    # إنشاء قائمة طلاب
    students = ["أحمد", "محمد", "فاطمة", "علي"]
    print(f"قائمة الطلاب الأصلية: {students}")
    
    # إضافة طلاب جدد
    students.append("حسن")
    students.insert(2, "زينب")
    print(f"بعد الإضافات: {students}")
    
    # ترتيب القائمة أبجدياً
    students.sort()
    print(f"بعد الترتيب الأبجدي: {students}")
    
    # البحث عن طالب
    if "أحمد" in students:
        position = students.index("أحمد") + 1
        print(f"أحمد موجود في المركز {position}")
    
    # إنشاء قائمة فرعية
    first_three = students[:3]
    print(f"الثلاثة الأوائل: {first_three}")
    
    # استخدام list comprehension
    students_upper = [name.upper() for name in students]
    print(f"الأسماء بحروف كبيرة: {students_upper}")
    
    return students

# تشغيل الدالة
final_list = list_operations_demo()

print("\n" + "="*50)
print("ملخص ميثود القوائم:")
print("الإضافة: append(), insert(), extend()")
print("الإزالة: remove(), pop(), clear()")
print("البحث: index(), count(), in")
print("الترتيب: sort(), reverse()")
print("النسخ: copy()")
print("المعلومات: len()")