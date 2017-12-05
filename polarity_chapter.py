import pandas as pd
title = {'bubu':'步步惊心','changgexing':'长歌行','congcong':'匆匆那年',
         'dahan':'大汉情缘','disanzhong':'第三种爱情','fanyiguan':'翻译官',
         'fengqiuhuang':'凤求凰','fuyaohuanghou':'扶摇皇后','heyi':'何以笙箫默',
         'huaqiangu':'花千骨','huidaomingchao':'回到明朝当王爷','jinghuayuan':'镜花缘',
         'jingmen':'京门风月','jipinjiading':'极品家丁','jiuzhou':'九州缥缈录','langyabang':'琅琊榜',
         'luohun':'裸婚时代','miyuezhuan':'芈月传','qieshi':'且试天下','ruguowoniu':'如果蜗牛有爱情',
         'sansheng':'三生三世十里桃花','suiyue':'岁月是朵两生花','talaile':'他来了请闭眼',
         'weiwei':'微微一笑很倾城','wudong':'武动乾坤','wuxinfashi':'无心法师','zuoer':'左耳',
         'xiaohua':'校花贴身高手','xuanfeng':'旋风少女','xuezhong':'雪中悍刀行','zetian':'择天记',
         'zhifou':'知否知否应是绿肥红瘦','zhiwomen':'致我们单纯的小美好','zhuxian':'诛仙'}
f = []

for k,v in title.items():
    df = pd.read_table('%s.txt' % k)
    dfq = df[['章节','polarity']]
    dfm = dfq.groupby('章节').mean()
    f.append(dfm.rename(columns={'polarity':'%s' % v}).T)
po = pd.concat(f,axis = 0)
po.to_csv('po.txt',sep=',',encoding='utf-8')






