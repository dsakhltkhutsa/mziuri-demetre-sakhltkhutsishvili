# 1. დაწერეთ პროგრამა, სადაც მომხარებელს შემოაყვანინებთ 2 რიცხვს. დაბეჭდეთ პირველი რიცხვის მეორეზე გაყოფის შედეგი.
# გაითვალისწინეთ შეცდომის მოხდენის შემთხვევები, თუ მომხარებელი არასწორ მონაცემებს შემოიყვანს, გამოუტანოს შესაბამისი შეტყობინება
# და ხელახლა მისცეს შესაძლებლობა რომ კიდევ შემოიტანოს რიცხვები. პროგრამა დასრულდეს მხოლოდ მაშინ, თუ მომხმარებელი ვალიდურ მონაცემებს შემოიტანს.
while True:
    try:
        a = int(input("shemoiyvanet pirveli ricxvi: "))
        b = int(input("shemoiyvanet meore ricxvi: "))
        res = a/b
        print(res)
        break
    except ValueError:
        print("monacemis tipi arasworia")
    except ZeroDivisionError:
        print("nulze gayofa ar sheizleba")

# 2. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა ორი რიცხვი. თუ პირველი რიცხვი იყოფა მეორეზე, ფუნქციამ დააბრუნოს განაყოფი.
# ხოლო თუ შეცდომა ფიქსირდება, ფუნქციამ დააბრუნოს შესაბამისი მნიშვნელობა. გამოიძახეთ ფუნქცია ნებისმიერი რიცხვებისთვის და შეამოწმეთ თქვენი პროგრამის სისწორე.
# მითითება: try..except ბლოკი უნდა ჩაწეროთ ფუნქციის აღწერაში.
def gayofa(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "Nulze gayofa sheudzlebelia"
    except Exception as e:
        return e
try:
    a = int(input("Shemoiyvanet pirveli ricxvi: "))
    b = int(input("Shemoiyvanet meore ricxvi: "))

    shedegi = gayofa(a, b)
    print(shedegi)

except ValueError:
    print("shemoiyvanet mteli ricxvi")
# 3.დაწერეთ პროგრამა, სადაც გაითვალისწინებთ IndexError შეცდომას.
numbers = [1,2,3]
try:
    print(numbers[10])
except IndexError:
    print("indeqsi arasworia")
#4. გახსენით myresult.txt ფაილი წაკითხვის რეჟიმში. თუ ფაილი არ არსებობს მოხდება შეცდომა. გაითვალისწინეთ შეცდომის სახელი და დაწერეთ შესაბამისი
# შეტყობინება შეცდომის შესახებ (try except-ის მეშვეობით).
try:
    with open("myresult.txt", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("myresult.txt faili ar arsebobs")
#5. შეიტანეთ ნებისმიერი a, b, c რიცხვები, რომლებიც წარმოადგენს კვადრატული განტოლების კოეფიციენტებს: ax2+bx+c=0 იპოვეთ კვადრატული განტოლების ფესვები.
# დააკვირდით რა სახის შეცდომები შესაძლოა მოხდეს და მოახდინეთ შესაძლო შეცდომების დაჭერა try... except ბლოკით.
import math  # მათემატიკური ფუნქციებისთვის (sqrt)

try:
    # კოეფიციენტების შეყვანა
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    # დისკრიმინანტის გამოთვლა: D = b² - 4ac
    D = b ** 2 - 4 * a * c

    # ფესვების გამოთვლა
    x1 = (-b + math.sqrt(D)) / (2 * a)  # (-b + √D) / 2a
    x2 = (-b - math.sqrt(D)) / (2 * a)  # (-b - √D) / 2a

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

except ValueError:
    # ხდება როცა: math.sqrt(D) და D < 0 (უარყოფითი რიცხვის ფესვი)
    # ან არასწორი შეყვანა (არა-რიცხვი)
    print("შეცდომა! უარყოფითი დისკრიმინანტი ან არასწორი შეყვანა")

except ZeroDivisionError:
    # ხდება როცა: a = 0 (გაყოფა ნულზე)
    print("შეცდომა! a არ უნდა იყოს 0")
#es jer ar gviswavlia shkolashi da claude damexmara
# 6. შეიყვანეთ 3 მთელი რიცხვი. თუ ეს რიცხვები აკმაყოფილებენ სამკუთხედის გვერდების სიგრძეების წესს
# (სამკუთხედის ნებისმიერი ორი გვერდის სიგრძის ჯამი მესამე გვერდის სიგრძეზე მეტია),
# მაშინ დაბეჭდეთ მათი საშუალო არითმეტიკული. წინააღმდეგ შემთხვევაში, გამოისროლეთ შეცდომა  (raise) შესაბამისი შეტყობინებით.
try:
    a = int(input("pirveli gverdi: "))
    b = int(input("meore gverdi: "))
    c = int(input("mesame gverdi: "))
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("ეს რიცხვები ვერ შექმნიან სამკუთხედს")
    average = (a + b + c) / 3
    print(average)
except ValueError:
    print("valueerori ari")




