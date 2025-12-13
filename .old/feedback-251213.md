## 【已完成】反馈体验 2025-12-12
总体上不错，但仍有许多待改进之处。

#### 你现在需要完善……
- 目前没有输出代码和可供复制的窗口的选项，我无法获取代码。你需要实现它，就像在grid.py中一样。
- 关于"允许生成的单位"和"允许搭载的单位"和"子单位配置"，同样需要链接数据库的Units数据库。
- 行为控制的"特殊状态"和状态切换的启用特殊状态重叠了，删除前者。
- 这个脚本需要实现实时切换语言，目前它需要重启应用才能切换，但重启后语言设置会丢失，所以实际上没法切换语言。
- 武器配置一栏中的大部分功能是错误的，我会在接下来为你提供详细的功能需求。
- 升级项一栏中的"简易升级项"功能是错误的，而"类型更变升级"是非必要的，可以删除。我会在接下来为你提供详细的功能需求。
- 基本信息的"科技引用"以及其他类似的地方需要连接Techs.csv


#### 更完善的功能需求和解释
武器配置中，你需要实现以下功能：
- 武器相关的输入框需要连接相应的csv。
- 需要分列两个表格，其一是配置，其二是武器。
在配置表格，包含配置名称输入框、默认启用复选框、全部武器可用时才启用复选框。当选中配置时，显示所选配置的武器内容。同时提供一个"无配置"”配置，它不允许被移动也不允许被删除。
在武器表格，包含武器名称输入框、武器数量输入框、发射数量输入框（无则留空）、发射时间输入框（无则留空）、自动交战复选框、显示备弹复选框、默认关闭复选框。


**武器配置最终应该是一个这样的结构：**

    Config “name” [Default] [OnlyFull]
        Weapon “missile_type” int_value [Launch int_value] [Time float_value] [AutoEngage] [Principal] [DefaultOff] 

如果只在默认配置下添加了武器，而没有添加其他配置，那么它应该直接输出武器的内容在根缩进下。

    Weapon “missile_type” int_value [Launch int_value] [Time float_value] [AutoEngage] [Principal] [DefaultOff] 


例如：我添加了"ALCM"&"Nuclear ALCM"两个配置，里面包含这些武器"ALCM"等武器

    Config "ALCM" Default OnlyFull
        Weapon "ALCM" 1 Launch 1 Time 150 Principal
	    Weapon "AAM" 2 Launch 1 Time 80 AutoEngage
	    Weapon "Plane Gun" 20000 Launch 1 Time 7 AutoEngage
    Config "Nuclear ALCM" OnlyFull
        Weapon "ALCM-N" 1 Launch 1 Time 150 Principal DefaultOff

这说明：
"ALCM"在"无配置"之外还存在配置的情况下，是默认使用的配置，并且当所有武器可用时，它才可用。
武器"ALCM"备弹1个，每次发射1枚，间隔时间刻150，显示备弹。
武器"AAM"备弹2个，每次发射1枚，间隔时间刻80，是自动交战武器。
武器"Plane Gun"备弹20000个，每次发射1枚，间隔时间刻7，是自动交战武器。

而"Nuclear ALCM"不是默认配置，所以它只能在游戏中被手动选择。当所有武器可用时，它才可用。
武器"ALCM-N"备弹1个，每次发射1枚，间隔时间刻150，显示备弹，默认关闭。

如果我在列表中的"无配置"配置中添加武器，那么它应该是：

    Weapon "Land Forces" 20000 Launch 1 Time 10 AutoEngage Principal
    Weapon "Small Arms" 20000 Launch 1 Time 10 AutoEngage DefaultOff
    Weapon "MANPAD" 20000 Launch 1 Time 75 AutoEngage DefaultOff
    Weapon "Nuclear Artillery" 20000 Launch 1 Time 150 AutoEngage
    Weapon "Fusion Artillery" 20000 Launch 1 Time 150 AutoEngage 
    Weapon "Chemical Artillery" 20000 Launch 1 Time 100 AutoEngage
    Weapon "Improved Chemical Artillery" 20000 Launch 1 Time 100 AutoEngage
    Weapon "Advanced Chemical Artillery" 20000 Launch 1 Time 100 AutoEngage

等等，就没有Config行了，而是直接输出在文本中。


升级配置中，你需要实现以下功能：
- 存在科技名称（引用数据库）输入框、修改（而非相乘当前值）复选框、增加（而非修改当前值）复选框、升级项输入框、修改值复选框。

它的语句是：

    ImprovedBy "Air_refuel" Range 1.5
    ImprovedBy "Powerful_Engine" Set Speed 65
    ImprovedBy "Advanced_Sonar" Add Range 100

ImprovedBy是固有的Headed，"Advanced_Sonar"等是科技名称的输入框，Set和Add是两个复选框，Range等是升级项、1.5等数值是修改值复选框

当我没有勾选"修改"时，他应该是这样：

    ImprovedBy "Electronic_Counters_Mk1" Size 0.99

如果勾选了"修改"时，他应该是这样：

    ImprovedBy "Powerful_Engine_Mk2" Set Speed 65

如果勾选了"增加"（并同时勾选"修改"）时，他应该以增加为准：

    ImprovedBy "Advanced_Sonar" Add Range 100


#### 你在完成上述后，仍然需要和我沟通，然后进一步完善……
- 页面缺乏灵活性，1024*768固定布局是我在没有熟悉掌握布局方法的时候做的，你需要让他在各个大小的窗口内保持良好的显示效果。
- 实现实时添加数据库的功能，并能指定添加的数据库属于哪一类别。