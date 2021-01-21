import datetime
import requests
import urllib3
import json
import os


url = "https://oapi.dingtalk.com/robot/send?access_token="
headers = {'Content-Type': 'application/json'}
data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "咻咻咻杭州天气",
        "text": "#### 杭州天气 @150XXXXXXXX "
    },
    "at": {
        "isAtAll": False
    }
}
fpath = "/media/lame/0DD80F300DD80F30/document/工作安排.md"


def searchWorkMd(path, start, stop):
    fp = open(path)
    line = fp.readline()
    s = ""
    opens = False
    # http://10.0.130.209:9999/20210119.pdf
    # https://gitee.com/sevenclear/wordpush/raw/master/1.jpg
    print("搜索工作日志 path={0},时间 start={1} stop={2}".format(path, start, stop))
    while line:
        if line.strip() == start:
            s = s+line.strip()+"\n"
            opens = True
        else:
            if line.strip() == stop:
                break
            if(opens):
                x = line.strip()
                x = x.replace(" ---", " :---")
                x = x.replace("--- ", "--- ")
                s = s+"-    "+x+"\n"
        line = fp.readline()
    fp.close()
    print("日志搜索完成:")
    print(s)
    meta = "- 作者：郭修军 \n- 内容：工作日报 \n"
    s = meta+"\n"+s
    return s


def convertToPdf(fname, workMd):
    fp = open(fname+".md", 'w')
    fp.write(workMd)
    fp.close()
    os.system('pandoc -t latex --pdf-engine=xelatex -s -VCJKoptions=BoldFont="SimHei" -VCJKmainfont="SimHei" -o {0} {1}'.format(
        "../wordpush/" + fname+".pdf", fname+".md"))
    os.remove(fname+".md")


def convertToImage(fname):
    from wand.image import Image
    from PIL import Image as Pimage
    filename = "../wordpush/"+fname+".pdf"
    with(Image(filename=filename, resolution=120)) as source:
        images = source.sequence
        pages = len(images)
        for i in range(pages):
            n = i + 1
            newfilename = filename[:-4] + '.jpeg'
            Image(images[i]).save(filename=newfilename)
    os.remove("../wordpush/"+fname+".pdf")
    img = Pimage.open("../wordpush/"+fname+".jpeg")
    cropped = img.crop((100, 100, 900, 600))
    cropped.save("../wordpush/"+fname+".jpeg")


def gitpush(dir, fname):
    # os.chdir("../wordpush")
    os.chdir(dir)
    os.system("git add "+fname+".jpeg")
    os.system("git commit -a -m '"+fname+"'")
    os.system("git push origin master")


def pushdingtalk(work):
    print("当前时间:{0},发送工作日志...".format(ndatetime))
    data["markdown"]["title"] = "咻咻咻工作日志"
    data["markdown"]["text"] = "### 咻咻咻 {0} \n ".format(work)
    res = requests.post(url, json=data)
    print("信息已发送：返回值{0}".format(res.text))


if __name__ == "__main__":
    now = datetime.datetime.now()
    ydate = now - datetime.timedelta(days=2)
    tdate = now + datetime.timedelta(days=1)
    ndatetime = now.strftime("%Y%m%d")
    ydatetime = ydate.strftime("%Y%m%d")
    tdatetime = tdate.strftime("%Y%m%d")
    workmd = searchWorkMd(fpath, ndatetime, tdatetime)
    pushdingtalk(workmd)
