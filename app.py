from browser import document, console, alert

input = document['input']
button = document['btn']
output0 = document['output0']
output1 = document['output1']
output2 = document['output2']
output3 = document['output3']
output4 = document['output4']
output5 = document['output5']
select = document['select']

def getNum(x):

    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan sebuah bilangan !!!')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

def formula(a, b):

    if a == 'Kilometer' :
        Hektometer = str (b * 10)
        Dekameter = str (b * 100)
        Meter = str (b * 1000)
        Desimeter = str (b * 10000)
        Centimeter = str (b * 100000)
        Milimeter = str (b * 1000000)
        
        return Hektometer, Dekameter, Meter, Desimeter, Centimeter, Milimeter

    elif a == 'Hektometer' :
        Kilometer = str (b / 10)
        Dekameter = str (b * 10)
        Meter = str (b * 100)
        Desimeter = str (b * 1000)
        Centimeter = str (b * 10000)
        Milimeter = str (b * 100000)
        
        return Kilometer, Dekameter, Meter, Desimeter, Centimeter, Milimeter

    elif a == 'Dekameter' :
        Kilometer = str (b / 100)
        Hektometer = str (b / 10)
        Meter = str (b * 10)
        Desimeter = str (b * 100)
        Centimeter = str (b * 1000)
        Milimeter = str (b * 10000)

        return Kilometer, Hektometer, Meter, Desimeter, Centimeter, Milimeter

    elif a == 'Meter' :
        Kilometer = str (b / 1000)
        Hektometer = str (b / 100)
        Dekameter = str (b / 10)
        Desimeter = str (b * 10)
        Centimeter = str (b * 100)
        Milimeter = str (b * 1000)

        return Kilometer, Hektometer, Dekameter, Desimeter, Centimeter, Milimeter

    elif a == 'Desimeter' :
        Kilometer = str (b / 10000)
        Hektometer = str (b / 1000)
        Dekameter = str (b / 100)
        Meter = str (b / 10)
        Centimeter = str (b * 10)
        Milimeter = str (b * 100)

        return Kilometer, Hektometer, Dekameter, Meter, Centimeter, Milimeter

    elif a == 'Centimeter' :
        Kilometer = str (b / 100000)
        Hektometer = str (b / 10000)
        Dekameter = str (b / 1000)
        Meter = str (b / 100)
        Desimeter = str (b / 10)
        Milimeter = str (b * 10)

        return Kilometer, Hektometer, Dekameter, Meter, Desimeter, Milimeter

    elif a == 'Milimeter' :
        Kilometer = str (b / 1000000)
        Hektometer = str (b / 100000)
        Dekameter = str (b / 10000)
        Meter = str (b / 1000)
        Desimeter = str (b / 100)
        Centimeter = str (b / 10)

        return Kilometer, Hektometer, Dekameter, Meter, Desimeter, Centimeter

    else :
        return 0
    
def main(ev):

    num = getNum(input.value)
    result = formula(select.value, num)
    output0.textContent = result[0]
    output1.textContent = result[1]
    output2.textContent = result[2]
    output3.textContent = result[3]
    output4.textContent = result[4]
    output5.textContent = result[5]

def keyEnter(ev):

    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

    button.bind('click', main)
    input.bind("keypress", keyEnter)
