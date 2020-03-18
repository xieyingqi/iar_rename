import re
import os
import shutil


def get_filename(type):
	for i in list:
		if os.path.splitext(i)[1] == type:  # [1]表示扩展名，[0]表示文件名
			return os.path.splitext(i)[0]


def change_text(type):
	filename = get_filename(type)
	if filename != None:
		file = open("./"+filename+type, 'r', encoding='UTF-8')
		lines = file.readlines()
		file.close()

		file = open("./"+filename+type, 'w+', encoding='UTF-8')
		for a in lines:
			new = re.sub(oldname, newname, a)
			file.write(new)
		file.close()
		os.rename(filename+type, newname+type)


def rm_dir(path):
	if os.path.exists(path):
		shutil.rmtree(path)


if __name__ == "__main__":
	newname = input("请输入新工程名：")  # 要替换的新的工程名

	list = os.listdir("./")  # 获取当前目录下文件名列表
	oldname = get_filename(".ewp")  # 原工程名
	change_text(".ewp")
	change_text(".ewd")
	change_text(".ewt")
	change_text(".dep")
	change_text(".eww")

	rm_dir(oldname)
	rm_dir("settings")
