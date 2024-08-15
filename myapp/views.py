from django.shortcuts import render

# Create your views here.


def print_ganjil(angka):
    list_angka = []
    for num in range(0, angka + 1):
        if num % 2 != 0:
            list_angka.append(num)
    list_angka_str = map(lambda x: str(x), list_angka)
    return " ".join(list_angka_str)


def print_prima(angka):
    list_angka = []
    for num in range(2, angka + 1):
        counter = 0
        for i in range(2, num):
            if num % i == 0:
                counter += 1
                break
        if counter == 0:
            list_angka.append(num)
    list_angka_str = map(lambda x: str(x), list_angka)
    return " ".join(list_angka_str)


def print_segitiga(angka):
    str_angka = str(angka)
    list_angka = []
    for i in range(len(str_angka)):
        new_str = str_angka[i]
        new_str += "0" * (i + 1)
        list_angka.append(new_str)
    return "\n".join(list_angka)


def index(request):
    if request.method == "POST":
        try:
            angka = int(request.POST["angka"])
            task = request.POST["task"]
            if angka < 0:
                return render(request, "index.html", {"error": "input angka kurang dari nol"})

            if task == "ganjil":
                data = print_ganjil(angka)
                return render(request, "index.html", {"result": data})
            elif task == "prima":
                data = print_prima(angka)
                return render(request, "index.html", {"result": data})
            elif task == "segitiga":
                data = print_segitiga(angka)
                return render(request, "index.html", {"result": data})
        except ValueError:
            return render(request, "index.html", {"error": "input bukan angka"})

    return render(request, "index.html")
