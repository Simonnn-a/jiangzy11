from vip.guanjianzi驱动 import webuikeys

wk = webuikeys('Chrome')
wk.wait(10)
wk.visit('http://www.baidu.com')
wk.input('id','kw','测码学院')
wk.click('id','su')
wk.sleep(5)
wk.quit()











