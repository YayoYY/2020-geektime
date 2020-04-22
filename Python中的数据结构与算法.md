# Python中的数据结构与算法

## list

Python的list数据结构是一个可变的线性表。实现的基本约束如下：

- 访问与更新的时间复杂度为O(1)。
- 允许任意加入元素，同时保证list变量的内存位置不变（id不变）。

由此可见，list属于分离式的线性表实现技术。



<div align='center'><img src='img/ole.png' width=500/></div>

各种操作的时间复杂度及其解释：

| 操作                       | 时间复杂度 | 解释                    |
| -------------------------- | ---------- | ----------------------- |
| lst[i]                     | O(1)       | 随机访问特性            |
| lst[i] = 1                 | O(1)       | 由其实现的基本约束可知  |
| len(lst)                   | O(1)       | 表中必须记录元素的个数  |
| lst.insert(len(lst), item) | O(1)       | 不用移动其他元素        |
| lst.append()               | O(1)       | 不用移动其他元素        |
| lst.pop()                  | O(1)       | 不用移动其他元素        |
| lst.sort()                 | O(nlogn)   | 蒂姆排序（归并 & 插排） |
| lst.extend(lst2)           | O(k)       | k为lst2的长度           |
| lst.insert(i, item)        | O(n)       | 需要移动其他元素        |
| lst.pop(i)                 | O(n)       | 需要移动其他元素        |
| lst.reverse()              | O(n)       | 遍历一遍                |
| max(lst), min(lst)         | O(n)       | 遍历一遍                |
| x in lst                   | O(n)       | 遍历一遍                |

## dict

dict和set的实现都是基于散列表的实现技术。

dict的key只能为不可变对象，value可以为可变对象和不可变对象。

set中的值也只能为不可变对象。

二者都利用内消解技术（开放寻址法）解决哈希冲突。

常见操作时间复杂度如下：

| 操作       | 时间复杂度 | 解释     |
| ---------- | ---------- | -------- |
| dic[i] = j | O(1)       | 哈希定位 |
| dic[i]     | O(1)       | 哈希定位 |
| dic.pop(i) | O(1)       | 哈希定位 |
| x in dic   | O(1)       | 哈希定位 |

ps. dic.keys实际上是一个list，所以查询的时候不要用x in dic.keys()，用x in dic。

## set

内部实现是dict。与list相比，能够更快速。

## Ref.

- [《数据结构与算法 Python语言描述》]()

- [【python】list，dict，set的时间复杂度](https://blog.csdn.net/acbattle/article/details/97012800)
- [查询set、dict、dict.keys()的速度对比](https://blog.csdn.net/juanjuan1314/article/details/78111860)