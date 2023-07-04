dictionary_fist = {"思维导图": "XMind 幕布 ProcessOn 知犀",
                   "问卷调查": "问卷星 麦客 调查派",
                   "H5工具": "易企秀 iH5 MAKA 人人秀",
                   "图文排版": "排版 135编辑器 秀米",
                   "在线作图:": "创客贴 稿定设计 Canva 图怪兽",
                   "词云生成": "易词云 图悦 WordArt",
                   "免费图库": "Pexels Unsiplash  Pixabay",
                   "PPT模板": "优品PPT 51PPPT 变色龙",
                   "专业剪辑": "Premiere Final Cut Pro  Vegas",
                   "视频格式转换": "格式工厂 迅捷视频转换器",
                   "PDF处理": "iLovePDF Smallpdf  PDF派",
                   "GIF录制": "GIFcam  SccreenToGif  SooGifLICEcap"}

keys = list(dictionary_fist.keys())
print("您可查询的工具类型有")
print(keys)
keyword = input("请输入想要查询的工具：")
if keyword in dictionary_fist:
    print("您查询的" + keyword + "工具有")
    print(dictionary_fist[keyword])
