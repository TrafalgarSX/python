import codecs


def ReadFile(filePath, encoding=""):
    with codecs.open(filePath, "r", encoding) as f:
        return f.read()


def WriteFile(filePath, u, encoding=""):
    with codecs.open(filePath, "w", encoding) as f:
        # f.write(u.encode(encoding,errors="ignore"))
        f.write(u)


def UTF8_2_GBK(src, dst):
    content = ReadFile(src, encoding="utf-8")
    WriteFile(dst, content, encoding="gb18030")


def GBK_2_UTF8(src, dst):
    content = ReadFile(src, encoding="gb18030")
    WriteFile(dst, content, encoding="utf-8")


def main():
    print("*********Begin...**********")
    print("===========================")
    print("++++++++UTF8-2-gbk+++++++++")
    UTF8_2_GBK("test1.txt", "test2.txt")
    print("===========================")
    print("++++++++GBK-2-utf8+++++++++")
    GBK_2_UTF8("test2.txt", "test3.txt")
    print("===========================")
    print("*********End...************")


if __name__ == "__main__":
    main()
