# **password-generator**

![GitHub License](https://img.shields.io/github/license/c1m50c/password-generator?color=blue&style=for-the-badge)
![Lines of Code](https://img.shields.io/tokei/lines/github/c1m50c/password-generator?style=for-the-badge)

Password Generator CLI written in Python. Some of the more useful features include the ability to define your own character set, password length, and if you would like to save the generated password as a text file or QR Code.


## **Installing Requirements**
```bash
$ cd password-generator
$ pip install -r ./requirements.txt
>> ...
```


## **Examples**
### **QR Code Generation**
```bash
$ cd password-generator
$ python3 src/main.py -qr ./output.bmp
>> >>> A4JYL,$23r;mt$F#
>> Saved generated password as a QR Code to './output.bmp'.
$ ./output.bmp
```
![Generated QRCode Example](qrc_example.bmp)



### **Finding Helpful Information**
```bash
$ cd password-generator
$ python3 src/main.py -h
>> Password Generator ~ Help
>> ...
```