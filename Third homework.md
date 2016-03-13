#Third homework第三次作业
##Problem题目
- 作业L1 在屏幕上用字符拼出自己姓名的英文
- 作业L2 在屏幕上用字符拼出任意次序的姓名
- 作业L3 在80*80点阵上用字符拼出你想画的东西，希望脑洞大开！（比如字符，火柴人，实现移动、旋转等等）

------
*注：这次作业的内容比较简单，摘要和背景介绍被省去。
##正文
   我是用矩阵表示了每个我需要表示的字母，这次作业遇到的一个重要问题就是**如果直接将数组输出的话，输出的结果带有中括号，逗号和引号**
为避免这一问题，一开始我采用了最笨的办法手动输入这个矩阵阵列的某一个元素，后来在敬雷同学的指导下，我用两个循环结构代替了冗长的输出，见我上传的文件，或下方。
比较自豪的一点是，由于充分利用数组list和矩阵，我用十分简洁的语句完成了作业L1,L2，并且这样的做法可以推广到26个字母，
缺点就是由于矩阵合并的困难，目前还没有能实每个字母做成单个模块，然后直接调用，后续将会改进。
- 作业L1[GUO.py](https://github.com/guoxiaowhu/computationalphysics_N2013301020099/blob/master/GUO.py)
输出结果截图![GUO.py](https://raw.githubusercontent.com/guoxiaowhu/computationalphysics_N2013301020099/master/GUO.png)
- 作业L2[OUG.py](https://github.com/guoxiaowhu/computationalphysics_N2013301020099/blob/master/OUG.py)
输出结果截图![OUG.py](https://raw.githubusercontent.com/guoxiaowhu/computationalphysics_N2013301020099/master/OUG.png)

等级3的作业，To be more romantically,I make an animation of a moving heart as following link:
- 作业L3[moving_heart.py](https://github.com/guoxiaowhu/computationalphysics_N2013301020099/blob/master/moving_heart.py)
- and it output file[moving_heart.txt](https://github.com/guoxiaowhu/computationalphysics_N2013301020099/blob/master/moving_heart.txt)
- and picture [moving_heart.py](https://raw.githubusercontent.com/guoxiaowhu/computationalphysics_N2013301020099/master/moving_heart.png)
##致谢
感谢敬雷同学提供了一个很好的思路，我的程序编写的大部分思路来源于他，此外，我还与许多同学进行讨论分析过，试图寻找较好的方法，感谢他们。
