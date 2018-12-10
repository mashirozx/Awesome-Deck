# Hearthstone Deck Embed Tool

TODO：

* 用django的template结构化一下 

后端流程：

```
输入卡组代码，传递给main.py
    |
    |
deck_code_decode.py 解码
    |
    |
dbfId_to_id.py 查询卡牌信息
    |
    |
html_generator.py 生成 hmtl

```