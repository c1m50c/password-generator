# **password-generator**

![GitHub License](https://img.shields.io/github/license/c1m50c/password-generator?color=blue&style=for-the-badge)
![Lines of Code](https://img.shields.io/tokei/lines/github/c1m50c/password-generator?style=for-the-badge)

Password Generator CLI written in Python, has a lot of options to make the application as customizable as you would like. Some of the more useful features including the ability to define your own character set, password length, and if you would like to save it as a text file or QR Code.


## **Installing Requirements**
```bash
$ cd password-generator
$ pip install -r ./requirements.txt
>> ...
```


## **Examples**
```bash
$ cd password-generator
$ python3 src/main.py -c aAbBcC -f ./output.txt
>> BaBbCCbbAbbaCACb
$ cat ./output.txt
>> BaBbCCbbAbbaCACb
```

```bash
$ cd password-generator
$ python3 src/main.py
>> Password Generator ~ Help
>> ...
```