"""
Дан текстовий файл f, елементами якого є символи. Записати в файл g ті компоненти файлу f, які є числами, а в файл
h - буквами.
"""
while True:
    f=open('f.txt', 'w')
    list=([input("Enter the item: ") for i in range(int(input("How many numbers do you want to enter? ")))])
    f.write(''.join(map(str,list)))
    f=open('f.txt', 'r')
    x=f.read()
    f.close()

    let=[]
    num=[]

    for i in x:
        if i.isalpha():
            let.append(i)
        if i.isnumeric():
            num.append(i)

    g=open('g.txt', 'w')
    g.write(' '.join(map(str,num)))
    g.close()

    h=open('h.txt', 'w')
    h.write(' '.join(map(str,let)))
    h.close()
   